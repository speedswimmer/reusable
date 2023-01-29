# simple script to use the BME280 sensor on a RaspberryPi to measure temperature, pressure and humidity
# RPi.bme280 library needs to be installed  (sudo pip install RPi.bme280)
# sudo apt-get install i2c-tools
# check that i2c kernel driver is enabled: $desg | grep i2c or $ lsmod | grep i2c
import smbus2
import bme280

SENSOR_ADDRESS = 0x76

try:
    # create a new instance of the BME280 sensor
    bus = smbus2.SMBus(1)
    # read chip ID of the sensor
    chip_id = bus.read_byte_data(SENSOR_ADDRESS, 0xD0)
    if chip_id == 0x60:
    # check if the sensor is present at the address
        bme280.load_calibration_params(bus, SENSOR_ADDRESS)
    # read data from the sensor
        data = bme280.sample(bus, SENSOR_ADDRESS)
    # print data using f-strings
        print(data.timestamp)
        print(f'Temperature: {data.temperature:0.1f}°C')
        print(f'Pressure: {data.pressure:0.1f} hPa')
        print(f'Humidity: {data.humidity:0.1f} %')
    else:
        raise ValueError(f'Sensor not found at address {SENSOR_ADDRESS:#x}')
    
except ValueError as e:
    print(f'Error: {e}')

except Exception as e:
    print(f'Error occured while reading sensor data: {e}')
