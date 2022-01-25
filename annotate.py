import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def createXML(indexID):
    root = minidom.Document()

    annot = root.createElement("annotation")
    root.appendChild(annot)
    
    xml_path = str("C:/Users/Sophia/Desktop/LitterBotCleanTests/Annotations/")+str(indexID)+".xml"
    path = root.createElement("path")
    annot.appendChild(path)

    size = root.createElement("size")
    annot.appendChild(size)

    width = root.createElement("width")
    height = root.createElement("height")
    depth = root.createElement("depth")
    size.appendChild(width)
    size.appendChild(height)
    size.appendChild(depth)

    xml_content = root.toprettyxml(indent='\t')
    
    with open(xml_path, "w") as f:
        f.write(xml_content)

def fillXML(indexID, h, w, d):
    xml_path = str("C:/Users/Sophia/Desktop/LitterBotCleanTests/Annotations/")+str(indexID)+".xml"
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for path in root.iter('path'):
        path.text = xml_path
    for width in root.iter('width'):
        width.text = str(w)
    for height in root.iter('height'):
        height.text = str(h)
    for depth in root.iter('depth'):
        depth.text = str(d)
    tree.write(xml_path)

def drawRect(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coords.append([x,y])
        if not len(coords)%2:
            cv2.rectangle(img, coords[len(coords)-2], coords[len(coords)-1], color=(0,255,0))  
            cv2.waitKey(1)
            cv2.imshow("sample",img)


def addCoords(indexID, bnd_coords, j):
    xml_path = str("C:/Users/Sophia/Desktop/LitterBotCleanTests/Annotations/")+str(indexID)+".xml"
    tree = ET.parse(xml_path)
    root = tree.getroot()

    obj = ET.SubElement(root, 'object{}'.format(str(j)))
    label = ET.SubElement(obj, 'label{}'.format(str(j)))
    bndbox = ET.SubElement(obj, 'bndbox{}'.format(str(j)))
    xmin = ET.SubElement(bndbox, 'xmin{}'.format(str(j)))
    ymin = ET.SubElement(bndbox, 'ymin{}'.format(str(j)))
    xmax = ET.SubElement(bndbox, 'xmax{}'.format(str(j)))
    ymax = ET.SubElement(bndbox, 'ymax{}'.format(str(j)))

    for label in root.iter('label{}'.format(str(j))):
        label.text = str('1')

    for xmin in root.iter('xmin{}'.format(str(j))):
        xmin.text = str(bnd_coords[0][0])
    for ymin in root.iter('ymin{}'.format(str(j))):
        ymin.text = str(bnd_coords[0][1])
    for xmax in root.iter('xmax{}'.format(str(j))):
        xmax.text = str(bnd_coords[1][0])
    for ymax in root.iter('ymax{}'.format(str(j))):
        ymax.text = str(bnd_coords[1][1])


    tree.write(xml_path)


for i in range(32, len(os.listdir("Photos"))):

    coords = []
    indexID = '0'*(4-len(str(i)))+str(i)

    createXML(indexID)
    img_path = "C:/Users/Sophia/Desktop/LitterBotCleanTests/Photos/"+str(indexID)+".jpg"
    img = cv2.imread(img_path)
    h, w, d = img.shape
    fillXML(indexID, h, w, d)
    cv2.imshow("sample",img)

    cv2.setMouseCallback('sample', drawRect)
    cv2.waitKey(0)

    k=0
    for j in range(len(coords)//2):
            j = 2*j
            addCoords(indexID, coords[j:j+2], k)
            k+=1