FROM python:3.12-slim

WORKDIR /exercises

# Install system dependencies for playwright
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install bun for task running
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="$PATH:/root/.bun/bin"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install playwright browsers (only needed for testing)
RUN playwright install chromium --with-deps
