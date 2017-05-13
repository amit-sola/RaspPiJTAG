##########################################################
# PSU ECE510 Post-silicon Validation Project 1
# --------------------------------------------------------
# Filename: logging_setup.py
# --------------------------------------------------------
# Purpose: logging configuration routines
##########################################################

import os
import json
import logging.config
import colorama

colorama.init()

LOG_LEVEL = logging.DEBUG

def set_log_level(level):
    global LOG_LEVEL
    LOG_LEVEL = level

def setup_logging():
    """ read the logging configure file & configure logging """
    path = os.path.join(os.path.dirname(__file__),'logging.json')

    #exception handling for Sphinx
    #try: 
    with open(path, 'rt') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    #except:
    #    print("exception with logging.json file")

#logging color scheme
color_map = {
    'debug'     : colorama.Fore.RESET + colorama.Style.RESET_ALL,
    'info'      : colorama.Fore.RESET + colorama.Style.RESET_ALL,
    'warning'   : colorama.Fore.YELLOW + colorama.Style.BRIGHT,
    'error'     : colorama.Fore.RED + colorama.Style.BRIGHT,
    'critical'  : colorama.Fore.RED + colorama.Style.BRIGHT,
    'reset'     : colorama.Fore.RESET + colorama.Style.RESET_ALL,
    'highlight' : colorama.Fore.CYAN + colorama.Style.BRIGHT,
}

def get_logger(name, level):
    """ return a logger

    :param name: name to use for the logger
    :type name: str
    :param level: severity of the log
    :type level: str
    :returns: logging.Logger 

    """
    logger = logging.getLogger(name) 
    logger.setLevel(level)
    return logger

def log(logger,level,*args,**kwargs):
    """ log routine for TAP

    :param logger: logger to use
    :type logger: logging.Logger
    :param level: severity of the logged message
    :type level: str
    :param args: variable length argument list
    :type args: tuple
    :param kwargs: keyworded variable length argument list
    :type kwargs: dict

    """

    kwargs['extra'] = {}
    #kwargs['extra']['level'] = level.upper()
    kwargs['extra']['COLOR'] = color_map[level]
    kwargs['extra']['COLORRESET'] = color_map['reset']

    getattr(logger,level)(*args, **kwargs)
