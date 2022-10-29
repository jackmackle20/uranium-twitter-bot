from google.cloud.sql.connector import Connector, IPTypes

def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "vernal-tracer-367015:us-central1:uranium-twitter-test", 
            "pg8000",
            user="postgres",
            password=".FfHpiC*S30oefI+",
            db="uranium-twitter-test",
            ip_type= IPTypes.PUBLIC 
        )
        return conn
    
getconn()