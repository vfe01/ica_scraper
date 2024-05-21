# Start from the official Python slim image
FROM python:3.9-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    firefox-esr \
    wget \
    ca-certificates \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Install GeckoDriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.30.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.30.0-linux64.

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY scraper.py .

ENTRYPOINT [ "python", "./scraper.py" ]