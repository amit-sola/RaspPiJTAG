##########################################################
# PSU ECE510 Post-silicon Validation Project 1
# --------------------------------------------------------
# Filename: tap_gpio.py
# --------------------------------------------------------
# Purpose: TAP Controller GPIO Pins Setup
##########################################################

import RPi.GPIO as GPIO
import time

#GPIO port addresses
TMS = 5
TDO = 6
TDI = 13
TCK = 19

class Tap_GPIO():
    """ class for Raspberry Pi GPIO"""
    
    def __init__(self):
        """ set initial states for GPIO pins """
        self.setup_time = 0.1
    
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # TMS: RPi ---> TAP
        GPIO.setup(TMS, GPIO.OUT)    
        # TDI: RPi ---> TAP
        GPIO.setup(TDI, GPIO.OUT)    
        # TCK: RPi ---> TAP
        GPIO.setup(TCK, GPIO.OUT)
        # TDO: RPi <--- TA
        GPIO.setup(TDO, GPIO.IN, pull_up_down=GPIO.PUD_UP)    

        #set the initial data on IO pins
        GPIO.output(TMS, 0)        
        GPIO.output(TDI, 0)        
        GPIO.output(TCK, 0)        
       
    def set_io_data(self, tms, tdi, tck):
        """ set GPIO pin data

        :param tms: data for TMS pin
        :type tms: int (0/1)
        :param tdi: data for TDI pin
        :type tdi: int (0/1)
        :param tck: data for TCK pin
        :type tck: int (0/1)

        """
        GPIO.output(TMS, tms)          
        GPIO.output(TDI, tdi)          
        self.delay(self.setup_time)
        GPIO.output(TCK, tck)
       
    def read_tdo_data(self):
        """ read TDO data

        :returns: int -- the TDO data	

	"""
        rslt = GPIO.input(TDO)
        #time.sleep(self.setup_time)
        return rslt
       
    def delay(self, delay = 0):
        """ set artificial delay for setup, hold etc.

        :param delay (Optional): time in seconds
        :type delay: float       

        """
        time.sleep(delay)   

    def clean_up(self):
        """ reset used ports back to input mode """
        GPIO.cleanup()

