import sched, time, board
from pymongo import MongoClient
from adafruit_bme280 import basic 

# setup for database
cluster = MongoClient("mongodb+srv://Senior:Senior2022@cluster0.o1ezz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Data"]
collection = db["02_16"]
# setup for scheduler
s = sched.scheduler(time.time, time.sleep)
# setup for bme280
i2c = board.I2C()
bme280 = basic.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

# celsius to fahrenheit conversion
def c_to_f(oldtemp):
    newtemp = (oldtemp * (9/5)) + 32
    return(newtemp)

# setup for sending data to database every minute
def data_upload(sc): 
    # grab latest time every callback
    seconds = time.time()
    local_time = time.ctime(seconds)
    hour = time.strftime("%I_%M_%S", time.localtime())

    # change celsius to fahrenheit
    bme280newtemp = c_to_f(bme280.temperature)

    # format document for mongodb
    bme280data = {
        hour: {
            "temp": bme280newtemp, 
            "humidity": bme280.relative_humidity, 
            "pressure": bme280.pressure,
            "altitude": bme280.altitude
        }
    }

    # add data to database
    collection.insert_one(bme280data)

    # console log to show updates
    print("\nUploaded data at... {0}".format(local_time))
    print("Temperature: {0} F".format(bme280newtemp))
    print("Humidity: {0} %%".format(bme280.relative_humidity))
    print("Pressure: {0} hPa".format(bme280.pressure))
    print("Altitude: {0} meters".format(bme280.altitude))
    s.enter(60, 2, data_upload, (s,))

# initiates data being sent to database
def run_data_upload():
    s.enter(0, 1, data_upload, (s,))
    s.run()

run_data_upload()