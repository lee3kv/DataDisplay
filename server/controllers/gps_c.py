from pymongo import MongoClient
import time

# create collections based on the day
day = time.strftime("%m_%d", time.localtime())

# setup for database
cluster = MongoClient("mongodb+srv://Senior:Senior2022@cluster0.o1ezz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Data"]
collection = db["BME"]

# bme data schema
bme280data = {
    day: {
        hour: {
            "temp": bme280newtemp, 
            "humidity": bme280.relative_humidity, 
            "pressure": bme280.pressure,
            "altitude": bme280.altitude
        }
    }
}

# updates data with the latest values
update = {'$push': {bme280data}}

