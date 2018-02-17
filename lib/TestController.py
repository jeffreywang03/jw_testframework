################################################################################
################################################################################
#
# FILE NAME:
#  TestController.py
#
# AUTHOR:
#  Jeffrey Wang
#
# PURPOSE:
#  File with various test/qa post-analysis functions
#
################################################################################
################################################################################

#Python imports
import logging


##################################################
#
# Class: CommonLib
#
# Description: class for common functions 
#
##################################################
class TestController(object):

    #*******************************************************
    #
    # Function: fnTestBool
    #
    # Description: Function to output boolean test results
    #
    # Return:  PASS or FAIL or NotTested
    #
    #*******************************************************
    def fnTestBool(self,TCID,testcase):
        """
        if testcase:
            print "TEST INFO     Test Pass"
        else:
            print "TEST INFO     Test FAIL"        
        """
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("Testing Test Case: %s" % TCID)
        if testcase:
            return logging.info("Test Pass")
        else:
            return logging.error("Test FAIL")
       