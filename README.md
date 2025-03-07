**Objective**

These Python scripts allow to extract records from the DineConnect API and post them to a Mongo database.

**Requirements**

* Python installed on the machine running this application.
* Credentials for accessing the DineConnect API - you need to request to DineConnect for your credentials.
* Credentials for writing to a MongDB database - this database will be used for storing the data extracted from the DineConnect API.

**How to run this application**

* Copy the file `config-sample.py` to `config.py`.
* Edit `config.py` with your credentials and defaults.
* To extract the tickets records from the DineConnect API and post them to the Mongo database, run `python3 extract_tickets.py` and follow the instructions of the script.

