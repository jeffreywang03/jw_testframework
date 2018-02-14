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
    def fnTestBool(self, testcase):
        if testcase:
            print "TEST INFO     Test Pass"
        else:
            print "TEST INFO     Test FAIL"        
