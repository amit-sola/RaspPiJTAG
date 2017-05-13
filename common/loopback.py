##########################################################
# PSU ECE510 Post-silicon Validation Project 1
# --------------------------------------------------------
# Filename: loopback.py
# --------------------------------------------------------
# Purpose: TAP Controller Loopback Monitor
##########################################################

import RPi.GPIO as GPIO
from tap.model.tap_model import *
from tap.log.logging_setup import *

TMS_LOOPBACK = 20
TCK_LOOPBACK = 21

class LoopBack(Tap_Model):
    """ loopback monitor class """
    def __init__(self, log_level=logging.INFO):
        """ initialize GPIO loopback pins """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TMS_LOOPBACK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(TCK_LOOPBACK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self.logger = get_logger(__file__,log_level)
        #initialize tap_model
        Tap_Model.__init__(self)

    def set_monitor(self):
        """ set up interrupt based event detection for loopback pins """ 
        GPIO.add_event_detect(TCK_LOOPBACK, GPIO.RISING, callback=self.tck_callback,bouncetime=10)

    def remove_monitor(self):
        """ remove interrupt based event detection for loopback pins """ 
        GPIO.remove_event_detect(TCK_LOOPBACK)

    def tck_callback(self, pin):
        """ call back routine for TCK loopback pin interrupt """
        message = "TMS: {}, TCK: {}".format(GPIO.input(TMS_LOOPBACK), GPIO.input(TCK_LOOPBACK))
        log(self.logger, 'debug', message) 
        if GPIO.input(TCK_LOOPBACK) == 1:
            state = self.update_state(GPIO.input(TMS_LOOPBACK),GPIO.input(TCK_LOOPBACK))
            log(self.logger, 'info', state) 

