import sys
sys.path.append("../lib")
from commonlib import *
cLib = CommonLib()

f = open('logs\helloworld.html','w')

jwLogo = 'C:\Users\Jeffrey\Desktop\jw_testframework\lib\LogHelper\minilogo.png'


header = """




<!-- CSS Styling -->
<style>
    header {
        margin-left: auto;
        text-align: center;
        margin-right: auto; 
    }
    header #text1 {
        font-family: Verdana, Arial;
        font-weight: bolder;
        color: #0066CC;
        margin-left: auto;
        text-align: center;
        margin-right: 40px;
        margin-top: 2px;
    }
    h1, h2{
        font-family: Verdana, Arial;
    }
    h2 {
        text-align: left;
    }
    table {
        font-family: Verdana, Arial;
        border-collapse: collapse;
    }
    td, th {
        border: 0.5px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    th {
        background-color: #99CCFF;
    }


    /*tr:nth-child(even) {
        background-color: #dddddd;
    }*/

</style>




<!-- HTML Page Header -->
<header>
    <img src='%s'>
    <ul id="text1">JW TEST FRAMEWORK Ver.1.0</ul>
    <h1>Post-Analysis Report</h1>
<header>
<br><br>





<!-- Test Environment Table -->
<table style="width:25%%">
  <tr>
    <th>Test Environment</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Test Script</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Test Description</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>PCIP</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Test Script Duration</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Test Start Time</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Test End Time</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Tests Executed</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Test Passed</th>
    <td>asdf</td>
  </tr>
  <tr>
    <th>Test Failed</th>
    <td>asdfasdfasdfasdfasdf</td>
  </tr>      
</table>
<br><br><br>



<!-- Test Results Table -->
<h2>Test Results</h2>
<table style="width:50%%">
  <tr>
    <th>TCID</th>
    <th>Test Case</th>
    <th>Test Description</th>
    <th>Test Result</th>
  </tr>
  <tr>
    <td>01_01</td>
    <td>HTML Report</td>
    <td>HTML Report For Post Analysis</td>
    <td>PASS</td>    
  </tr>
  <tr>
    <td>01_02</td>
    <td>HTML Report2</td>
    <td>HTML Report For Post Analysis2</td>
    <td>FAIL</td>    
  </tr>  
</table>
""" % jwLogo

testResult = """
<!-- Test Results Table -->
<h2>Test Results</h2>
<table>
  <tr>
    <th>TCID</th>
    <th>Test Case</th>
    <th>Test Description</th>
    <th>Test Result</th>
  </tr>
  <tr>
    <td>01_01</td>
    <td>HTML Report</td>
    <td>HTML Report For Post Analysis</td>
    <td>PASS</td>    
  </tr>
  <tr>
    <td>01_02</td>
    <td>HTML Report2</td>
    <td>HTML Report For Post Analysis2</td>
    <td>FAIL</td>    
  </tr>  
</table>
"""

cLib.logger("Test executed...")

f.write(header)
f.write(testResult)
f.close()
