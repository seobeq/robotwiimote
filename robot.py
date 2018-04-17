# New robot control with wiimote.
# 30 March 18

import RPi.GPIO as GPIO
import time
import cwiid
#from movement import*

def forwards():
  GPIO.output(5,True)
  GPIO.output(6,True)

  GPIO.output(10,True)
  GPIO.output(9,False)
  GPIO.output(11,True)
  GPIO.output(0,False)

def backwards():
  GPIO.output(5,True)
  GPIO.output(6,True)

  GPIO.output(10, False)
  GPIO.output(9,True)
  GPIO.output(11,False)
  GPIO.output(0, True)

def left():
  GPIO.output(5,True)
  GPIO.output(6,True)

  GPIO.output(10,False)
  GPIO.output(9,True)
  GPIO.output(11,True)
  GPIO.output(0,False)

def right():
  GPIO.output(5,True)
  GPIO.output(6,True)

  GPIO.output(10,True)
  GPIO.output(9,False)
  GPIO.output(11,False)
  GPIO.output(0,True)

def stop():
  GPIO.output(10,False)
  GPIO.output(9,False)
  GPIO.output(11,False)
  GPIO.output(0,False)

button_delay = 0.1

GPIO.setmode(GPIO.BCM)

GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(0,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

# main
print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Try to connect to the Wiimote & quit if not found
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Can't connect to Wiimote"
  quit()

print 'Wiimote connected'
wii.rpt_mode = cwiid.RPT_BTN
try:
  while True:
    buttons = wii.state['buttons']
    if (buttons & cwiid.BTN_UP):
      # Forwards
      time.sleep(button_delay)    
      forwards()
   
    elif (buttons & cwiid.BTN_DOWN):
      # backwards
      time.sleep(button_delay)  
      backwards()
  
    elif (buttons & cwiid.BTN_LEFT):
      # left
      time.sleep(button_delay)         
      left()
   
    elif(buttons & cwiid.BTN_RIGHT):
      # right
      time.sleep(button_delay)          
      right()
  
    else:
      # stop
      stop()


      #press button A to stop all motors
    if (buttons & cwiid.BTN_A):
      time.sleep(button_delay)              
      stop()
      quit()
    
except KeyboardInterrupt:
  print '\n Exited with ctrl+c'

finally:
  GPIO.cleanup()


