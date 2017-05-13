##########################################################
# PSU ECE510 Post-silicon Validation Project 1
# --------------------------------------------------------
# Filename: tap_model.py
# --------------------------------------------------------
# Purpose: TAP Controller Class
##########################################################

class Tap_Model():
    """ class for TAP model """
    #TAP states 
    states = {
        'Test_Logic_Reset' : {'0':'Run_Test_Idle', '1':'Test_Logic_Reset'},
        'Run_Test_Idle'    : {'0':'Run_Test_Idle', '1':'Select_DR_Scan'},
        'Select_DR_Scan'   : {'0':'Capture_DR'   , '1':'Select_IR_Scan'},
        'Capture_DR'       : {'0':'Shift_DR'     , '1':'Exit1_DR'},
        'Shift_DR'         : {'0':'Shift_DR'     , '1':'Exit1_DR'},
        'Exit1_DR'         : {'0':'Pause_DR'     , '1':'Update_DR'},
        'Pause_DR'         : {'0':'Pause_DR'     , '1':'Exit2_DR'},
        'Exit2_DR'         : {'0':'Shift_DR'     , '1':'Update_DR'},
        'Update_DR'        : {'0':'Run_Test_Idle', '1':'Select_DR_Scan'},
        'Select_IR_Scan'   : {'0':'Capture_IR'   , '1':'Test_Logic_Reset'},
        'Capture_IR'       : {'0':'Shift_IR'     , '1':'Exit1_IR'},
        'Shift_IR'         : {'0':'Shift_IR'     , '1':'Exit1_IR'},
        'Exit1_IR'         : {'0':'Pause_IR'     , '1':'Update_IR'},
        'Pause_IR'         : {'0':'Pause_IR'     , '1':'Exit2_IR'},
        'Exit2_IR'         : {'0':'Shift_IR'     , '1':'Update_IR'},
        'Update_IR'        : {'0':'Run_Test_Idle', '1':'Select_DR_Scan'},
    } 

    max_length = 1000

    def __init__(self):
        """ set the cur_state to 'Test_Logic_Reset' """
        self.cur_state = 'Test_Logic_Reset' 

    def update_state(self,tms,tck):
        """ update the cur_state 
        
        :param tms: data for TMS pin
        :type tms: int (0/1)
        :param tck: data for TCK pin
        :type tck: int (0/1)
        :returns: str -- current state

        """
        if tck:
            self.cur_state = self.states[self.cur_state][str(tms)]   
        return self.cur_state

