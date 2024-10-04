# Airgradient Grafana Dashboard
Display data from the [AirGradient DIY Pro](https://www.airgradient.com/documentation/diy-pro-presoldered-v42/) on a dashboard using [Grafana](https://grafana.com/) and [InfluxDB](https://www.influxdata.com).

## About
[AirGradient](https://www.airgradient.com/) creates air quality monitors that can measure PM1, PM2.5, PM10, CO2, TVOC, NOX, temperature and humidity. We will use InfluxDB to store and track periodic AirGradient data and Grafana to create a dashboard to create visuals and alerts in response to the current and trending air quality.

## Getting Started
Create an account with InfluxDB Cloud and Grafana Cloud. 
Get the tokens from InfluxDB and set up Grafana Cloud dashboard.
Install Arduino IDE.
Edit the Arduino code.
Open up the AirGradient.
Upload the arduino code onto the AirGradient's ESP8266.
(or once I figure it out, run a python file with esptool.py to upload onto the ESP8266 instead)

### Create an account w/ InfluxDB Cloud

### Create an account w/ Grafana Cloud

## Installation and Configuration


### Configuring the AirGradient Code
Do you have the Arduino IDE installed?? If not, install it [here](https://www.arduino.cc/en/software).

Get a USB to USB-C cable. Unscrew the back of the AirGradient DIY Pro. You can see the mini processor with it's own usb-c port. Connect that to your computer's usb port. Open up the Arduino IDE. 

Next, locate the .ino file in the arduino folder and change lines __. Not necessary, but you can turn off the connection to the AirGradient's built in API by setting that bool to false on line __. Next upload.



## Contact
