#!/usr/bin/python3

##########################################################
# PSU ECE510 Post-silicon Validation Projects
# --------------------------------------------------------
# Filename: regression.py
# --------------------------------------------------------
# Purpose: TAP Controller Regression Script
##########################################################

import argparse
import time
import sys
import glob
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../..')))
from tap.log import logging_setup
import logging

def create_test_suite():
    test_files = glob.glob('tests/*.py')
    modules = ['tests.'+str[6:len(str)-3] for str in test_files]
    suites = unittest.defaultTestLoader.loadTestsFromNames(modules) 
    testSuite = unittest.TestSuite(suites)
    return testSuite

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "TAP Controller Regression Run")
    parser.add_argument('-rs', '--regressionseed', help='seed to reproduce regression', type=int, default=None)
    parser.add_argument('-s', '--sim', help='Simulation mode', action='store_true', default=False)
    parser.add_argument('-v', '--verbosity', help='Debug message verbosity level', choices=['debug', 'info','warning','critical'], default='info')
    
    #if len(sys.argv) == 1:
    #    parser.print_help()
    #    sys.exit(1)
    args = parser.parse_args()

    #if (args.regressionseed is not None) and (args.regressionseed < 0):
    #    parser.error("regressionseed can't be a negative integer")
    
    if args.verbosity.upper() == "DEBUG":
        logging_setup.set_log_level(logging.DEBUG)
    elif args.verbosity.upper() == "INFO":
        logging_setup.set_log_level(logging.INFO)
    elif args.verbosity.upper() == "WARNING":
        logging_setup.set_log_level(logging.WARNING)
    elif args.verbosity.upper() == "CRITICAL":
        logging_setup.set_log_level(logging.CRITICAL)

    logging_setup.setup_logging()

    testSuite = create_test_suite()
    testRunner = unittest.TextTestRunner(verbosity=1)
    testRunner.run(testSuite)
    
