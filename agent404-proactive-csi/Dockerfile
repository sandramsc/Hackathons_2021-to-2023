# Dockerfile for ProActive CSI Agent 404
# Multi-agent AI system for IBM watsonx Orchestrate

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install IBM watsonx Orchestrate CLI
RUN pip install --no-cache-dir watsonx-orchestrate-cli

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p logs data/output

# Set permissions
RUN chmod +x scripts/*.sh scripts/deployment/*.sh scripts/testing/*.sh 2>/dev/null || true

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Default command - run Streamlit demo
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]

