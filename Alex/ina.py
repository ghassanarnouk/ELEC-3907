from time import sleep
from datetime import datetime
from ina219 import INA219
import pandas as pd

ina = INA219(shunt_ohms = 0.1, max_expected_amps = 0.6, address = 0x40, busnum = 1)

ina.configure(voltage_range = ina.RANGE_16V, gain = ina.GAIN_AUTO, bus_adc = ina.ADC_128SAMP, shunt_adc = ina.ADC_128SAMP)

dict = {'Time': [],
        'Voltage':[],
        'Current':[],
        'Power':[],
        }

try:
    while 1:
        v = ina.voltage()
        i = ina.current()
        p = ina.power()
        print("\n POWER: %f \n CURRENT: %f \n VOLTAGE: %f" %(p, i, v))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dict['Time'].append(current_time)
        dict['Voltage'].append(v)
        dict['Current'].append(i)
        dict['Power'].append(p)
        df = pd.DataFrame(data = dict)
        df.to_csv('solar.csv', index = False)
        sleep(30)

except KeyboardInterrupt:
    print("\n exiting")

