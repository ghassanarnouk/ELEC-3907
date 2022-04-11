#!/bin/bash

cp -f /home/pi/Documents/ELEC-3907/Seth/integration/solar*.csv /home/pi/Documents/ELEC-3907/Ghassan/voltage/solar.csv

arara -l /home/pi/Documents/ELEC-3907/Ghassan/voltage/voltage.tex

xdg-open /home/pi/Documents/ELEC-3907/Ghassan/voltage/voltage.pdf
