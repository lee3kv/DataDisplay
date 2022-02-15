import cv2
import sched, time#, board
from adafruit_bme280 import basic as adafruit_bme280

s = sched.scheduler(time.time, time.sleep)
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25



def upload_data(sc): 
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Uploaded data at... {0}".format(local_time))
    print("\nTemperature: {0} C".format(bme280.temperature))
    print("Humidity: {0} %%".format(bme280.relative_humidity))
    print("Pressure: {0} hPa".format(bme280.pressure))
    print("Altitude = {0} meters".format(bme280.altitude))
    s.enter(60, 1, upload_data, (sc,))

s.enter(1, 1, upload_data, (s,))
s.run()