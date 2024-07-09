# Flask-APIs

Repository used for building and testing APIs based on Flask, integrated with Email Delivery with Mailtrap.

Some tecnologies used:

* Python(3.12.x);
* Flask(3.x);
* API Restful;
* SQL Alchemy;
* SQL(SQLite and PostgreSQL);
* Bootstrap(5.x);
* Html.

## Running the APIs

First, make sure your Pip is up to date and Python is the correct version, then create a Virtual Environment and install the dependencies. If sending emails is not working, the Mailtrap instance has possibly been deactivated.

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
```