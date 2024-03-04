import xml.etree.ElementTree as ET

#Parse XML into Element Tree    
tree = ET.parse('productcatalogus.xml')

root = tree.getroot()
for child in root:
    for subchild in child:
        for subsubchild in subchild:
            print(subsubchild.tag, subsubchild.text)
        #print(subchild.tag, subchild.text)
    #print(child.tag, child.attrib)

#Root
#print(root.tag)
#print(len(root))

#Access Root Child
#print(root[22].tag)
#print(len(root[22]))

#for child in root:  
 #   print(child[1].tag, child[1].text)

#from bs4 import BeautifulSoup

#with open('productcatalogus.xml', 'r', encoding='utf-8') as file:  
 #   xml_content = file.read()

#soup = BeautifulSoup(xml_content, 'xml')  

#html_contents = soup.find_all('html_content')  

#for html_content in html_contents:
 #   print(html_content)