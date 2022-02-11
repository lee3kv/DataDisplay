import sched, time
from adafruit_circuitpython_bme280 import basic as adafruit_bme280

s = sched.scheduler(time.time, time.sleep)
bme280 = adafruit_bme280.Adafruit_BME280_I2C()

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

# while True:
#     print("\nTemperature: %0.1f C" % bme280.temperature)
#     print("Humidity: %0.1f %%" % bme280.relative_humidity)
#     print("Pressure: %0.1f hPa" % bme280.pressure)
#     print("Altitude = %0.2f meters" % bme280.altitude)
#     time.sleep(2)

def upload_data(sc): 
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Uploaded data at..." % local_time)
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    s.enter(60, 1, upload_data, (sc,))

s.enter(1, 1, upload_data, (s,))
s.run()