FROM python:3.11-alpine

# Set workdir
WORKDIR /app

# Copy only dependency files first (for better caching)
COPY pyproject.toml ./

# Install system dependencies needed for Poetry and build tools
RUN apk update && apk add --no-cache \
    curl \
    gcc \
    g++ \
    libffi-dev \
    musl-dev \
    openssl-dev \
    python3-dev \
    build-base

# Install Poetry manually
ENV POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    PATH="${POETRY_HOME}/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    /opt/poetry/bin/poetry config virtualenvs.create false


# Install Python dependencies
RUN export PATH="/opt/poetry/bin:$PATH" && poetry install --no-root
# Now copy the app source
COPY . /app

# Expose app port
EXPOSE 8000

# Command to run the app
CMD ["/opt/poetry/bin/poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
