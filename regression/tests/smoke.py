##########################################################
# PSU ECE510 Post-silicon Validation Projects
# --------------------------------------------------------
# Filename: smoke.py
# --------------------------------------------------------
# Purpose: TAP Controller Smoke Tests
##########################################################

import os, sys
from tap.common.loopback import *
from tap.common.tap import *
import unittest

class smoke(unittest.TestCase):
    """ smoke/power on tests, hopefully won't produce actual smoke """
    
    def setUp(self):
        """ fires before each test
        Setting up for the test
    
        """
        log_level = LOG_LEVEL 
        self.logger = get_logger(self.id(), log_level)
        log(self.logger, 'info', '{}Running {}'.format(color_map['highlight'],self.id()))

        self.tap = Tap(log_level=log_level)
        self.loopback_monitor = LoopBack(log_level=log_level)
        self.loopback_monitor.set_monitor()
    
    def tearDown(self):
        """ fires after each test
        Cleaning up after the test
    
        """
        self.loopback_monitor.remove_monitor()
        self.tap.clean_up()
        log(self.logger, 'info', '{}Done with {}\n'.format(color_map['highlight'],self.id()))    
    
    def testReset(self):
        self.tap.reset()
        self.assertEqual("Test_Logic_Reset",self.loopback_monitor.cur_state)


    def testReset2ShiftIR(self):
        self.tap.reset()
        self.tap.reset2ShiftIR()
        self.assertEqual("Shift_IR", self.loopback_monitor.cur_state)


    def testExit1IR2ShiftDR(self):

        tms1 = 1
        tdi0 = 0
        self.tap.reset()
        self.tap.reset2ShiftIR()
        self.tap.toggle_tck(tms1, tdi0)

        self.tap.exit1IR2ShiftDR()
        self.assertEqual("Shift_DR", self.loopback_monitor.cur_state)


    def testReadDeviceCode(self):
        self.tap.reset()
        self.tap.reset2ShiftIR()

        self.tap.shiftInData("100100")


        self.tap.exit1IR2ShiftDR()

        result = self.tap.shiftOutData(32)
        print (result, " IDCODE result")