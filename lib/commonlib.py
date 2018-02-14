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
    	header = "LOG INFO      "
    	if type(output) == float or type(output) == int:
    		_output = str(output)
    		print header + _output
    	else:
    		print header + output
    	#logger timer
    	time.sleep(0.25)

    #*******************************************************
    #
    # Function: logger
    #
    # Description: Custom logging function for Python 3
    #
    # Return:  log output
    #
    #*******************************************************
    def logger(self,output):
        header = "LOG INFO      "
        if type(output) == float or type(output) == int:
            _output = str(output)
            print(header + _output)
        else:
            print(header + output)
        #logger timer
        time.sleep(0.25)

    #*******************************************************
    #
    # Function: logger
    #
    # Description: Custom logging function
    #
    # Return:  log output
    #
    #*******************************************************
