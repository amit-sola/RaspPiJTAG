##########################################################
# PSU ECE510 Post-silicon Validation Project 1
# --------------------------------------------------------
# Filename: tap.py
# --------------------------------------------------------
# Purpose: TAP Controller Class
##########################################################

from tap.common.tap_gpio import *
from tap.log.logging_setup import *
import time

class Tap(Tap_GPIO):
    """ Class for JTAG TAP Controller"""

    def __init__(self,log_level=logging.INFO):
        """ initialize TAP """
        self.logger = get_logger(__file__,log_level)
        self.max_length = 1000

        #set up the RPi TAP pins
        Tap_GPIO.__init__(self)

    def toggle_tck(self, tms, tdi):
        """ toggle TCK for state transition 

        :param tms: data for TMS pin
        :type tms: int (0/1)
        :param tdi: data for TDI pin
        :type tdi: int (0/1)

        """
        self.set_io_data(tms, tdi, 1)
        self.set_io_data(tms, tdi, 0)



    def reset(self):
        """ set TAP state to Test_Logic_Reset """
        tms1 = 1
        tdi0 = 0
        # assert TMS for 5 TCKs in a row
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)

    def reset2ShiftIR(self):
        """ shift TAP state from reset to shiftIR """

        tms1 = 1
        tms0 = 0

        tdi0 = 0

        self.toggle_tck(tms0, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms0, tdi0)
        self.toggle_tck(tms0, tdi0)
        self.toggle_tck(tms0, tdi0)


    def exit1IR2ShiftDR(self):
        """ shift TAP state from exit1IR to shiftDR """
        tms1 = 1
        tms0 = 0

        tdi0 = 0

        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms0, tdi0)
        self.toggle_tck(tms0, tdi0)



    def exit1DR2ShiftIR(self):
        """ shift TAP state from exit1DR to shiftIR """
        tms1 = 1
        tms0 = 0

        tdi0 = 0

        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms1, tdi0)
        self.toggle_tck(tms0, tdi0)
        self.toggle_tck(tms0, tdi0)


    def shiftInData(self, tdi_str):
        """ shift in IR/DR data

        :param tdi_str: TDI data to shift in
        :type tdo_str: str

        """
        tms1 = 1
        tms0 = 0


        for data in range((len(tdi_str) - 1)):
            self.toggle_tck(tms0, int(tdi_str[data]))
            print (data, "shift in Data index ")

        self.toggle_tck(tms1, int(tdi_str[data+1]))



    def shiftOutData(self, length):
        """ get IR/DR data

        :param length: chain length        
        :type length: int
        :returns: int - TDO data

        """
        tms1 = 1
        tms0 = 0
        tdi0 = 0
        final_val = 0
        data = 0

        for data_index in range(length - 1):
            data = self.read_tdo_data()
            print("data out : ",data)
            self.toggle_tck(tms0,tdi0)
            final_val = (data << data_index) + final_val
            print (final_val, "final_val ")

        data = self.read_tdo_data()
        self.toggle_tck(tms1, tdi0)
        final_val = (data << (data_index+1)) + final_val

        return final_val



    def getChainLength(self):
        """ get chain length

        :returns: int -- chain length	

        """

        return 0
