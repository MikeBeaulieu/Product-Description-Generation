import xml.etree.cElementTree as ET
from secrets import randbelow
from random import randint

f = open("kurtas.txt", "w", encoding='utf-8')
j = 1
x = 1
for i in range(1,11982):
        try:
            tree = ET.parse("Files\kurtas\ filename"+str(i)+".xml")
            det = tree.find('Details')
            title = det.find('Title')
            fin_title = ' '.join(title.text.split())
            description = det.find('Description')
            fin_desc = ' '.join(description.text.split())
            f.write(fin_title+": "+fin_desc+"\n")
            f.write("\n\n\n")
            print(i)
        except:
            print(None)
            x = x+1
            continue
print (x)
