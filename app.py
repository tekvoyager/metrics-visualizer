import os
import time
import random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = os.getenv("INFLUXDB_BUCKET")
org = os.getenv("INFLUXDB_ORG")
token = os.getenv("INFLUXDB_TOKEN")
url = os.getenv("INFLUXDB_URL")

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

def emit_metrics():
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        point = Point("device_metrics") \
            .tag("device", "sensor_001") \
            .field("temperature", temperature) \
            .time(time.time_ns(), WritePrecision.NS)
        write_api.write(bucket=bucket, org=org, record=point)
        print(f"[EMIT] temperature={temperature}")
        time.sleep(5)

if __name__ == "__main__":
    emit_metrics()