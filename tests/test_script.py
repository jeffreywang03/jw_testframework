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

tree = ET.parse('food_menu.xml')
root = tree.getroot()
result = False
#print root[0][1].text
#print root[0][2].text

cLib.logger("#####################################################")
cLib.logger("")
cLib.logger("Test Case 1: Verify menu item costs more than $4.00")
cLib.logger("")
cLib.logger("#####################################################")

for food in root.findall('food'):
	name = food.find('name').text
	price = food.find('price').text
	cLib.logger("Food: %s" % name)
	cLib.logger("Price: %s" % price)
	#Use regex to remove $ from price for test
	regex = r"\$"
	float_price = float(re.sub(regex, "", price))	#re.sub([regex character], [sub], [original])
	if float_price >= 5.0:
		result = True
		testcontrol.fnTestBool(result)
	else:
		result = False		
		testcontrol.fnTestBool(result)
	cLib.logger("")

cLib.logger("##############################################################")
cLib.logger("")
cLib.logger("Test Case 2: Verify there are no Strawberries in the food")
cLib.logger("")
cLib.logger("##############################################################")

for food in root.findall('food'):
	name = food.find('name').text
	price = food.find('price').text
	cLib.logger("Food: %s" % name)
	cLib.logger("Price: %s" % price)
	#Use regex to remove $ from price for test
	regex = r"Strawberry"
	if re.match(regex, name):
		result = False
		cLib.logger("Food item may contain Strawberries!")		
		testcontrol.fnTestBool(result)
	else:
		result = True
		testcontrol.fnTestBool(result)
	cLib.logger("")


"""
regex = r"\$"
price = '$505'
if re.match(regex, price):
	print 'match'
else:
	print 'no match'
print "*"*20

no =  re.sub(regex, "", price)
print no
"""


