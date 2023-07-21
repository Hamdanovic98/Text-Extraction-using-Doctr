FROM python:3.8-slim-buster

WORKDIR /app

# Update package lists and install system dependencies
RUN apt-get update && apt-get install -y sudo dbus git libgl1-mesa-glx libglib2.0-0 libpango1.0-dev poppler-utils

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Clone and install doctr
RUN git clone https://github.com/mindee/doctr.git
RUN pip3 install -e doctr/.[tf]  # Include TensorFlow dependency

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD streamlit run app.py --server.enableCORS false

