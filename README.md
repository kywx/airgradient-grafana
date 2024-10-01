# Airgradient Grafana Dashboard
Display data from the [AirGradient DIY Pro](https://www.airgradient.com/documentation/diy-pro-presoldered-v42/) on a dashboard utilizing [Grafana](https://grafana.com/) and [InfluxDB](https://www.influxdata.com).

## About
[AirGradient](https://www.airgradient.com/) creates air quality monitors that can measure PM1, PM2, PM2.5, PM10, CO2, TVOCs, NOX, temperature and humidity levels. We will use InfluxDB to store periodic AirGradient data and Grafana to create a dashboard to create clear visuals and alerts in response to the current and trending air quality.



## Installation
First, download the git repo. 

### Configuring the AirGradient
Do you have the Arduino IDE installed?? If not, install it [here](https://www.arduino.cc/en/software).

Ensure that a USB to USB-C cable is on hand. Unscrew the back of the AirGradient. You can see the mini processor with it's own usb-c port. Connect that to your computer's usb port. Open up the Arduino IDE. 

Next, locate the .ino file in the arduino folder and change lines __. Not necessary, but you can turn off the connection to the AirGradient's built in API by setting that bool to false on line __. Next upload.



## Getting Started
Create an account with InfluxDB Cloud and Grafana Cloud.

## Contact
