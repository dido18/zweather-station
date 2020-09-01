################################################################################
# Zerynth Device Manager
#
# Created by Zerynth Team 2020 CC
# Authors: E.Neri, D.Neri
###############################################################################

from bsp.drivers import wifi
import streams
from zdm import zdm
from bosch.bme280 import bme280
import mcu


def pub_temp_hum():
    tag = 'weather'
    temp, hum, pres = bme.get_values()
    print("Temperature:", temp, "C")
    print("Humidity:", hum, "%")
    print("Pressure:", pres, "Pa")
    payload = {'temp': temp, 'hum': hum, "pres": pres}
    device.publish(payload, tag)
    print('Published: ', payload)


streams.serial()

try:
    bme = bme280.BME280(I2C0)
    print("Bme Ready!")
    for i in range(0,5):
        wifi.init()
        print("Connecting to wifi...")
        interface = wifi.interface()
        #interface.link("Mio", interface.WIFI_WPA2, "avvertenza")
        interface.link("CasaNeSa", interface.WIFI_WPA2, "3UBJU8U7L3TTTYCT")
        
        print("Connect wifi done")
        break

    # Create a ZDM Device
    device = zdm.Device()
    # connect the device to the ZDM
    print("Connecting....")
    device.connect()
    print("Connected.")

    while True:
        try:
            pub_temp_hum()
            sleep(180000)
        except Exception as e:
            print("Publish error", e)
            mcu.reset()
            

except Exception as e:
    print("main", e)