# Import library elements
from gpiozero import MCP3008 # Using MCP3008 ADC
from gpiozero import Servo
from gpiozero import Button, LED
from time import sleep #provides time for servo to adjust
from signal import pause

# Setup

# ADC channels for potentiometer and LDRs
pot = MCP3008(channel=0,differential=False,max_voltage=3.3)
LDR_NW = MCP3008(channel=2,differential=False,max_voltage=3.3) # LDR in north west position
LDR_SW = MCP3008(channel=3,differential=False,max_voltage=3.3) # LDR in south west position
LDR_NE = MCP3008(channel=4,differential=False,max_voltage=3.3) # LDR in north east position
LDR_SE = MCP3008(channel=5,differential=False,max_voltage=3.3) # LDR in south east position

# Servo

# Servo PWM:
# 1ms = -90 degrees
# 2ms = +90 degrees

# Servo was not achieving full -90 and + 90 range of motion when using GPIOZERO, so
# had to add correction factor to lower and upper range.  This was acheived
# using trial and error until the servo moved the full 180 degrees.  0.46
# was the maximum that could be used before the servo started acting
# erraticaly.

# Servo PWM:
# -90 degrees = 1ms - corrrection
# +90 degrees = 2 ms + correction

# SERVO 1
# -------------------------------------------------------------------------------------
MinPW_NS = 0.001
MaxPW_NS = 0.0025
# Create servo object using corrected pulse width
#Uses GPIO18 (pin 12 on Pi)
servo_NS = Servo("GPIO18", min_pulse_width= MinPW_NS, max_pulse_width = MaxPW_NS)
servo_NS.value = None

# SERVO 2
# -------------------------------------------------------------------------------------
MinPW_EW = 0.001
MaxPW_EW = 0.0025
# Create servo object using corrected pulse width
# Uses GPIO4 (pin 7 on Pi)
servo_EW = Servo("GPIO17", min_pulse_width = MinPW_EW , max_pulse_width = MaxPW_EW)
servo_EW.value = None

# Setup manual adjust button interrupts and manual adjust LED
btn_Auto = Button("GPIO23",pull_up = True)
btn_LeftRight = Button("GPIO25",pull_up = True)
btn_UpDown = Button("GPIO21",pull_up = True)
LEDManAdjust = LED("GPIO24")

# Program global variables
LDR_Diff = 0.3 #Allows a 0.3 difference
state = 0

# Functions

def LeftRight():
   
    LEDManAdjust.on()
   
    while True:
       
        print(pot.voltage)
        #The range of voltage values from the pot is between 0 and 3.3V.
        #Convert this to a percentage of the full servo range (2).
        #Subtract by 1 to get into the servo range (-1 to 1).
        ServoValue = (pot.voltage / 3.3) - 1
        #Assign value to servo
        servo_EW.value = ServoValue
       
        if btn_Auto.is_pressed:
            return 0
       
        if btn_UpDown.is_pressed:
            return 2

    return

def UpDown():
   
    LEDManAdjust.blink(on_time = 0.5,off_time = 0.5)
   
    while True:
        print(pot.voltage)
        #The range of voltage values from the pot is between 0 and 3.3V.
        #Convert this to a percentage of the full servo range (2).
        #Subtract by 1 to get into the servo range (-1 to 1).
        ServoValue = (pot.voltage / 3.3) - 1
        #Assign value to servo
        servo_NS.value = ServoValue       

        if btn_Auto.is_pressed:
            return 0
       
        if btn_LeftRight.is_pressed:
            return 1

    return

# Main code
# -------------------------------------------------------------------
LEDManAdjust.off()


#print("test servo EW")

#print("clockwise")
#servo_NS.value = -0.9
#sleep(2)

#print("stop")
#servo_NS.value = None
#sleep(2)

#print("Counter-clockwise")
#servo_NS.value = 0.8
#sleep(2)

#print("stop")
#servo_NS.value = None
#sleep(2)


while True:
    if state == 0:
        LEDManAdjust.off()
        # Automatic adjustment code block
        LDR_North = (LDR_NE.voltage + LDR_NW.voltage) / 2
        LDR_South = (LDR_SE.voltage + LDR_SW.voltage) / 2
        LDR_East = (LDR_NE.voltage + LDR_SE.voltage) / 2
        LDR_West = (LDR_NW.voltage + LDR_SW.voltage) / 2
       
        print(f'LDR_North: {LDR_North:.4f} LDR_South: {LDR_South:.4f} Difference: {(LDR_North - LDR_South):.4f} LDR_East: {LDR_East:.4f} LDR_West: {LDR_West:.4f} Difference: {(LDR_East - LDR_West):.4f}')           

        # Adjust North South Servo   
           
        if ((LDR_North - LDR_South) > LDR_Diff):
            servo_NS.value = -0.9
           
        elif ((LDR_North - LDR_South) < (-1 * LDR_Diff)):
            servo_NS.value = 0.9
       
        else:
            servo_NS.value = None
           
        #Adjust East West Servo   
           
        if ((LDR_East - LDR_West) > LDR_Diff):
            servo_EW.value = -0.9
           
        elif ((LDR_East - LDR_West) < (-1 * LDR_Diff)):
            servo_EW.value = 0.9
       
        else:
            servo_EW.value = None



        if btn_UpDown.is_pressed:
            state = UpDown()
           
        if btn_LeftRight.is_pressed:
            state = LeftRight
           
    elif state == 1:
        state = LeftRight()
       
    else:
        state = UpDown()