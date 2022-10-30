from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy as db
import json

with open("secrets.json", "r") as s:
    secrets = json.load(s)

def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "vernal-tracer-367015:us-central1:uranium-twitter-test", 
            "pg8000",
            user="postgres",
            password=secrets["gcp_pass"],
            db="uranium-twitter-test",
            ip_type= IPTypes.PUBLIC 
        )
        return conn

engine = db.create_engine(
    "postgresql+pg8000://",
    creator=getconn())

metadata = db.MetaData()

profile = db.Table(
    'test_table',
    metadata,
    db.Column('col1', db.String, primary_key=True),
    db.Column('Col2', db.Integer))

metadata.create_all(engine)


    