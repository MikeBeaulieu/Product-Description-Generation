import xml.etree.cElementTree as ET
import requests
import time
from bs4 import BeautifulSoup
from xml.dom import minidom
import lxml.etree as etree
import urllib.request
from urllib.request import urlopen
from urllib.parse import urljoin

''' Function to Pass the url of each product on the page to get all relevant info like Title, Features and Description'''

def passUrlToGetInfo(url,n):
    try:
        html = urlopen(url)
        webcodestr = BeautifulSoup(html,"html.parser")

        root = ET.Element("T-Shirt")
        doc1 = ET.SubElement(root, "Link")
        doc2 = ET.SubElement(root,"Details")

        ''' To store the Page url and Image Url in the xml '''
        ET.SubElement(doc1,"PageUrl").text = "\n"+url
        try:
            imgurl = webcodestr.find_all("meta", {"name":"twitter:image"})
            imgurlfnd = imgurl[0].attrs['content']
            ET.SubElement(doc1,"ImgUrl").text = "\n"+imgurlfnd
        except:
            print(None)

        ''' To store the title in the xml '''
        try:
            title = webcodestr.find_all("span", {"class":"brand"})
            titlefnd = title[0].text.strip()
            title2 = webcodestr.find_all("span", {"class":"product-title"})
            titlefnd2 = title2[0].text.strip()
            ET.SubElement(doc2,"Title").text = "\n"+titlefnd+" "+titlefnd2
        except:
            print(None)

        ''' To store the description in the xml '''

        try:
            desc = webcodestr.find_all("div", {"class":"detail"})
            descfnd = desc[0].text.strip()
            ET.SubElement(doc2,"Description").text = "\n"+descfnd
        except:
            print(None)

        ''' To create the XML Tree and create the xml document '''
        tree = ET.ElementTree(root)
        tree.write("Files\kurtas\ filename"+str(n)+".xml")

    except urllib.error.HTTPError as err:
        print(None)


''' Main Function '''
for i in range(1,1000000):
    n = i
    x= 52*(i-1)+1
    while n != (i+1):
        main = "https://www.jabong.com/women/clothing/kurtas-suit-sets/?sort=popularity&dir=desc&source=topnav_&men@limit=1015&page="+str(n)
        getlink = requests.get("https://www.jabong.com/women/clothing/kurtas-suit-sets/?sort=popularity&dir=desc&source=topnav_&men@limit=1015&page="+str(n))
        getpage = getlink.content
        eachpage = BeautifulSoup(getpage,"lxml")
        eachpagedivsecond = eachpage.find_all(class_ = "tile-cta")
        for all in eachpagedivsecond:
            url = urljoin(main, all["href"])
            print(x)
            passUrlToGetInfo(url,x)
            x = x + 1
        n = n+1
