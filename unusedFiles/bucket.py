import os, time, datetime
from datetime import timezone
from influxdb_client_3 import InfluxDBClient3
import server


def write(host, org, database, token):
    with InfluxDBClient3(host=host, org=org,
                         token=token) as client:
        while True:
            dt = datetime.datetime.now(timezone.utc)
            points = {
                "measurement": "air",
                "tags": {},
                "fields": server.get_data("192.168.0.3", 4000),
                "time": dt,
            }
            client.write(database=database, record=points, write_precision="s")
            time.sleep(120)

if __name__ == "__main__":
    write("https://us-east-1-1.aws.cloud2.influxdata.com",
          "airgradient", "monitor", os.environ.get("INFLUXDB_TOKEN"))
