FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (so Docker caches it)
COPY requirements.txt .

# Upgrade pip + install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy your app code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
