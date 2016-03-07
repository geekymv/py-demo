import xml.etree.ElementTree as ET

def parseXml():
	tree = ET.parse('test.xml')
	root = tree.getroot()
	if (root.tag == 'xml'):
		for child in root:
			print child.tag, ' ----> ', child.text
	else:
		print 'none...'
		
if __name__ == '__main__':
	parseXml()

