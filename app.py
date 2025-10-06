import cv2
import os
import xml.etree.ElementTree as ET

# Load your XML annotation file
def load_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    boxes = []

    for member in root.findall('object'):
        box = member.find('bndbox')
        boxes.append((
            int(box.find('xmin').text),
            int(box.find('ymin').text),
            int(box.find('xmax').text),
            int(box.find('ymax').text),
            member.find('name').text
        ))
    return boxes

# Visualize Image with Annotations
def visualize_image_with_annotations(img_path, boxes):
    img = cv2.imread(img_path)
    
    for box in boxes:
        x_min, y_min, x_max, y_max, class_name = box
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
        cv2.putText(img, class_name, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow("Annotated Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example Usage
xml_file = 'animals.xml'
image_file = 'animals.jpg'

boxes = load_annotation(xml_file)
visualize_image_with_annotations(image_file, boxes)