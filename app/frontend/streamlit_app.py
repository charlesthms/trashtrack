import requests
import streamlit as st


# Define the backend FastAPI URL
backend_url = "http://backend:8000/api/v1" # 'backend' is the name of the backend service in docker-compose.yml

# Fetch data from the FastAPI backend (GET request)
def fetch_backend_data():
    try:
        response = requests.get(f"{backend_url}/trashes")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Display data from the backend
st.title("Streamlit Frontend")
st.write("This data is fetched from the FastAPI backend:")

backend_data = fetch_backend_data()
st.json(backend_data)

