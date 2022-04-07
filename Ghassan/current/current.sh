#!/bin/bash

cp -f /home/pi/Documents/ELEC-3907/Alex/solar*.csv /home/pi/Documents/ELEC-3907/Ghassan/current/solar.csv

arara -l /home/pi/Documents/ELEC-3907/Ghassan/current/current.tex

xdg-open current.pdf
