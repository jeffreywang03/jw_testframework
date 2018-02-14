################################################################################
################################################################################
#
# FILE NAME:
#  test_CPUstatus.py
#
# AUTHOR:
#  Jeffrey Wang
#
# PURPOSE:
#  Test script used to verify CPU status of the test PC
#  Recommended to run this script before executing any test suites
#
################################################################################
################################################################################

import sys
sys.path.append("../lib")
from commonlib import *
from TestController import *
import xml.etree.ElementTree as ET
import re
import time
#Custom Test libraries
cLib = CommonLib()
testcontrol = TestController()


################################################################################
#                     Parse the Command Line Arguments
################################################################################
import argparse



def fnTestModule_1():
	cLib.logger("----------------------------------------------------------------------")
	cLib.logger("Module 1: Basic Functionality - Frequency Shift & Negative Load       ")
	cLib.logger("----------------------------------------------------------------------")


	a = 10
	b = 20

	if a+b == 30:
		result = True
		testcontrol.fnTestBool(result)
	else:
		result = False		
		testcontrol.fnTestBool(result)



fnTestModule_1()