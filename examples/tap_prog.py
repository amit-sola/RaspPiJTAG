#!/usr/bin/python3

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from tap.common.tap import *
from tap.log import logging_setup

logging_setup.setup_logging()

t = Tap(log_level=logging.DEBUG)
t.reset()
t.reset2ShiftIR()

# select IDCODE register
t.shiftInData("100100")

# go to DR
t.exit1IR2ShiftDR()

# find IDCODE register length
#length = t.getChainLength()
#print("scan chain length is: %s"%length)

rslt = t.shiftOutData(32)
print("Device IDCODE is: %#x"%rslt)

# select EXTEST register
#t.shiftInData("111100")
#t.exit1IR2ShiftDR()
#print("chain is %s"%t.getChainLength())
#rslt = t.shiftOutData(744)
#print("Device IDCODE is: {0:#0746b}".format(rslt))




