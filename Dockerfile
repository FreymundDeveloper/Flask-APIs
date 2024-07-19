FROM python:3.9.17-bookworm

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Set the working directory in the container
ENV APP_HOME /back-end
WORKDIR $APP_HOME

# Set the Python path to include the Basic_Hotel_API directory
ENV PYTHONPATH $APP_HOME/Basic_Hotel_API

# Copy local code to the container image
COPY . ./

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 Basic_Hotel_API.app:app
