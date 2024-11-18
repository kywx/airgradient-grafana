# Airgradient Grafana Dashboard
Display data gathered by an [AirGradient DIY Pro](https://www.airgradient.com/documentation/diy-pro-presoldered-v42/) on a dashboard using [Grafana](https://grafana.com/) and [InfluxDB](https://www.influxdata.com).

## About
[AirGradient](https://www.airgradient.com/) creates air quality monitors, like the AirGradient DIY Pro, that can measure PM1, PM2.5, PM10, CO2, TVOC index, NOX index, temperature, and humidity levels. We will use InfluxDB to store and track periodic data gathered from the air quality monitor and then give Grafana access to that data in order to make a dashboard to create visuals and alerts in response to the current and trending air quality.


### Examples
Insert photo + alt description + description

## Getting Started (Summary)
- *Create an account* with InfluxDB Cloud.
- **Save** the tokens from InfluxDB.

- **Install** Arduino IDE.
- **Edit** the Arduino code to include your tokens.
- **Upload** the arduino code onto the AirGradient's ESP8266.

- *Create an account* with Grafana Cloud.
- **Set up** the Grafana Cloud Dashboard.

## Create an account w/ InfluxDB Cloud
Note: InfluxDB will only store up to 30 days of data for free. If you want to keep your data, consider buying their product or using another database(that is compatiable with Grafana).


**Start here** : [https://cloud2.influxdata.com/signup](https://cloud2.influxdata.com/signup)
- Verify your account
- Workspace details don't matter that much
- Save/Remember your organization name
- Storage Provider of your choice

### List of Important Variables to Note
- Organization name
- Bucket name
- API Token

### Create your bucket
Once you have verified your account, you should be in the Resource Center. Of the 4 dropdown options, expand the one that says "Manage Databases & Security". Then, click on the "GO TO BUCKETS" button. It should be the first one. Here, you will see two "system buckets". We will ignore them. Click on the "+ CREATE BUCKET" button. Name your bucket. Click "Create". Now you should see the bucket you just created above the two system buckets.

### Generate your API Token
Now, look at the navbar to the left. We are currently on "Buckets". We want to move to "API Tokens". Here, we will create an API Token to access our bucket. Click on "+ GENERATE API TOKEN". From the dropdown, choose "Custom API Token". Select the bucket you just create and check off both read and write access. Then click "GENERATE". **Make sure to copy the token**.



## Arduino Installation and Configuration

### Downloading the Arduino IDE
If you do not already have the Arduino IDE installed, you can install it [here](https://www.arduino.cc/en/software).

### Installing Dependencies
- Go to Tools > Manage Libraries (or CTRL+SHIFT+I)
- Install the "ESP8266 Influxdb" library (if the lastest version doesn't work, install the 3.13.2 version)
- Install the 2.14.15 version "AirGradient Air Quality Sensor" library
- Also install the following libraries : "WifiManager", "U8g2", "Sensirion I2C SGP41", "Sensirion Gas Index Algorithm", and "Arduino-SHT"

### Select Board and Port
1. First, we need to select the board in the AirGradient. Go to Tools > Board:- > esp8266 > LOLIN(WEMOS) D1 mini(clone).

2. Then, we need to select the port. In order to do this, we must connect the AirGradient's ESP8266 to a PC through a USB-C to USB cable. In order to access the ESP8266, we must unscrew and open up the back of the AirGradient. Then, you should see a USB-C port attached to the ESP8266. Attach the USB side to your PC. Now, in the Arduino IDE, you should be able to go to Tools > Port > COM[some number].

### Configuring the AirGradient ESP8266
1. Download the arduino folder in the repository. Now open the .ino file in the Arduino IDE(File > Open).

2. Change lines 58-61
- line 58: your influxdb url (you can check in your browser)
- line 59: your api token
- line 60: your organization name
- line 61: your bucket name

3. (Optional) Change lines 62-65
- line 62: The name of the point variable
- line 63: how often the AirGradient will send data to InfluxDB(in minutes)
- line 64: Set false if you don't want the data to be sent to InfluxDB
- line 65: Set false if you don't want your air quality data to be sent to AirGradient's API

4. Upload the file onto the ESP8266
- It's the button with the arrow(->)


## Create an account w/ Grafana Cloud
**Start here** : [https://grafana.com/auth/sign-up/create-user?pg=hp&plcmt=cloud-promo&cta=create-free-account](https://grafana.com/auth/sign-up/create-user?pg=hp&plcmt=cloud-promo&cta=create-free-account)

1. Set up the Grafana Stack in any deployment region.

2. Launch Grafana Cloud.

3. Go to Home > Connections > Add new connection

4. Search for InfluxDB as a data source (not as an integration). Click "Add new data source".

5. Change the name to whatever you'd like. Toggle on the Default option. Change Query Language to "SQL" using the dropdown menu. Under HTTP, insert your URL(same as the one in the arduino code). Under Auth, turn on "Basic auth". Under InfluxDB details, insert your bucket name next to Database then insert your API token next to Token.

6. Click "Save & Test". If it shows a green message saying "OK", you have succesfully connected to your database. If it is red, please ensure that the data you entered is correct.

7. Now that you have the Data Source configured, you can finally create the dashboard. Go to Home > Dashboards.

8. Click New > Import. If you want to create your own dashboard setup, you can go to New > New dashboard and figure it out yourself.

9. Upload the grafana_template.json file from the repository. Change the name to whatever you want. Change the uid to anything but the original. Then click Import.

10. You will see lots of errors. That is because the data source is not read properly yet. We need to let Grafana connect to each panel. Click the Edit button to enter edit mode. 

11. Hover over the CO2 box. Click the 3 dots that appear on the top right of the box and click edit.

12. Now you can click either "Back to dashboard" or "Refresh" to see your data show up. If there is still an error, your table name might be different from the preset one. In this case, you would have to go build your own SQL queries. You can go "Back to dashboard" and see the change on your dashboard. At the top, you can set the time from "Last 6 hours" to anything else.

13. Make sure to click the "Save Dashboard" button after you make changes.

14. This is a simple dashboard setup where you can monitor the progression of your air quality levels.

15. Alerts?? Well... not yet.

16. Troubleshooting? :


## Contact
For any inquiries about AirGradient, please email m.walter@uci.edu.

For any inquiries about source code/Arduino/Grafana Cloud, please email kylieh2@uci.edu.

For any inquiries about InfluxDB Cloud, please email smsam@uci.edu.


## See any room for improvement?
a kind pull request
