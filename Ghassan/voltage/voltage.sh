#!/bin/bash

cp -f /home/pi/Documents/ELEC-3907/Alex/solar*.csv /home/pi/Documents/ELEC-3907/Ghassan/voltage/solar.csv

arara -l /home/pi/Documents/ELEC-3907/Ghassan/voltage/voltage.tex
