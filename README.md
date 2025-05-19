# metrics-visualizer

A lightweight telemetry stack for device metrics using InfluxDB and Grafana.

## Project Overview

This project provides a simple framework for collecting, storing, and visualizing device metrics. It includes:

- A Python-based metrics emitter that simulates device telemetry (e.g., temperature readings) and sends data to InfluxDB.
- An InfluxDB instance for time-series data storage.
- A Grafana instance for visualizing the collected metrics in real time.

The stack is containerized using Docker for easy setup and deployment.

## Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.8+ recommended)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/)

## Setup

```bash
docker-compose up --build
```

- Grafana: http://localhost:3000
- InfluxDB: http://localhost:8086