################################################################################
################################################################################
#
# FILE NAME:
#  commonLIB.py
#
# AUTHOR:
#  Jeffrey Wang
#
# PURPOSE:
#  Library file for test scripts
#
################################################################################
################################################################################

#Python imports
import json
import time
import logging

##################################################
#
# Class: CommonLib
#
# Description: class for common functions 
#
##################################################
class CommonLib:

    #*******************************************************
    #
    # Function: logger
    #
    # Description: Custom logging function for Python 2
    #
    # Return:  log output
    #
    #*******************************************************
    
    def logger(self,output):
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')
        time.sleep(0.75)
        return logging.info(output)

    #*******************************************************
    #
    # Function: logger
    #
    # Description: Custom logging function for Python 3
    #
    # Return:  log output
    #
    #*******************************************************

