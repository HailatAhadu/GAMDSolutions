import xml.etree.ElementTree
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

url = "http://www.erca.gov.et:8008/wserca/index.jsf?tin="
timeout = 5
tin = "00"
arry1 = []
totaltext = ""
try:
    req = requests.get(url + tin).text
    data1 = BeautifulSoup(req, 'lxml')
    body = data1.body.text
    body = body.strip()

    try:
        myroot = ET.fromstring(body)
        mytree = list(myroot)
        z = 0

        for y in mytree:
            totaltext += y.tag + " " + y.text + "\n"
            # print(y.tag + " " + y.text)
            z = z + 1
        print(totaltext)



    except xml.etree.ElementTree.ParseError as err:
       print("Input Error", "The TIN Number you input is not find")

except (requests.ConnectionError, requests.Timeout):
    print("Input Error", "Please check the Internet Connection")
















