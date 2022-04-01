from time import sleep
from datetime import datetime
from ina219 import INA219
import pandas as pd
from pathlib import Path

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
        current_time = current_time.replace(':', '')
        current_time = current_time[0:4]
        dict['Time'].append(current_time)
        dict['Voltage'].append(v)
        dict['Current'].append(i)
        dict['Power'].append(p)
        current_date = now.strftime("%Y:%m:%d")
        current_date = current_date.replace(':', '')
        title = 'solar' + current_date + '.csv'
        df = pd.DataFrame(data = dict)
        print(title)
        if (current_time == '2359'):
            Path('/home/pi/Documents/ELEC-3907/Alex/' + title).rename('/home/pi/Documents/ELEC-3907/Alex/Database/' + title)
            print('FILE MOVED')
        df.to_csv(title, index = False) 
        sleep(1)
        
           


except KeyboardInterrupt:
    print("\n exiting")

