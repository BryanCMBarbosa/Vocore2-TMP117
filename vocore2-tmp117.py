import smbus
import time

class tmp117():
    def __init__(self, address = 0x48):
        self.bus = smbus.SMBus(0)
        self.device.address = address
        self.r = [0x0220]

    def read_raw_data(self):
        self.bus.write_i2c_block_data(0x48, 0x01, self.r)
        time.sleep(0.5)
        response = self.bus.read_i2c_block_data(0x48, 0x00, 2)
        return response

    def read_converted_data(self):
        reading = self.read_raw_data()
        converted_reading = (reading[0]<<8 | reading[1])
        return converted_reading

    def read_celsius_temp(self):
        return self.read_converted_data() * 0.0078125

    def read_fahrenheit_temp(self):
        return ((self.read_converted_data() * 0.0078125) * 1.8) + 32

    def read_kelvin_temp(self):
        return (self.read_converted_data() * 0.0078125) + 273.15