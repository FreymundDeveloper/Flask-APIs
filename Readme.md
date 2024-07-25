# Flask-APIs

Repository used for building and testing APIs based on Flask, integrated with Email Delivery with Mailtrap and hosted on a PythonAnywhere and Google Cloud(disabled due to timeout issues) servers.

Some tecnologies used:

* Python(3.12.x);
* Flask(3.x);
* API Restful;
* SQL Alchemy;
* SQL(SQLite and PostgreSQL);
* Bootstrap(5.x);
* Html;
* Docker;
* Google Cloud.

## Running the APIs

First of all, create a ".env" file in the root of the application (based on the ".env.example" model). Now, make sure that your Pip is updated and that Python is the correct version, then Create a Virtual Environment and install dependencies. If sending emails is not working, the Mailtrap instance has possibly been disabled.

```bash
# Build a Virtual Ambience
$ python -m venv <AmbienceName>

# Installation
$ pip install -r requirements.txt

# Start Virtual Ambience
$ .\<AmbienceName>\Scripts\activate
# Or
$ .\<AmbienceName>\Scripts\activate.bat

# Stop Virtual Ambience
$ deactivate

# Update Pip Version(if necessary)
$ python.exe -m pip install --upgrade pip
```

## Deploy/Running on Cloud

Make sure you have an instance running on the Google Cloud platform and also have the Shell SDK installed. After that, replace the content of “app.py” with the content of “gcloud_app.txt” and execute the commands and their settings below:

**Obs**: Have a Virtual Ambient ready and running before running the commands below.

```bash
# Start Shell SDK
$ gcloud init

# Execute the Deploy to server
$ gcloud run deploy --source . 
```