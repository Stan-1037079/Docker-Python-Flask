import xml.etree.ElementTree as ET

def tag_to_html(tag_name, text):
    if tag_name.lower() in ["title", "header"]:
        return f"<h2>{text}</h2>\n"
    else:
        return f"<p>{tag_name}: {text}</p>\n"

# Parse XML into Element Tree
tree = ET.parse('productcatalogus.xml')
root = tree.getroot()

with open('output.html', 'w', encoding='utf-8') as html_file:
    
    html_file.write("<html>\n<head>\n<title>XML to HTML</title>\n</head>\n<body>\n")
    
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
            
                html_content = tag_to_html(subsubchild.tag, subsubchild.text)
                html_file.write(html_content)
    
    
    html_file.write("</body>\n</html>")

print("Conversion to HTML completed.")