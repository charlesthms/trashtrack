# Use a base image with Python 3.8
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY app/backend/ /app/backend/

# Copy the frontend code (Streamlit) into the container
COPY app/frontend/ /app/frontend/

# Expose ports for both FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Default command to run FastAPI (Backend)
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

