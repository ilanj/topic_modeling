import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import json
import os

path = 'dataset/bbc/'
class_text = pd.DataFrame()
class_text
i = 1
list_of_dirs = os.listdir(path)
for label in list_of_dirs:
    current_label_dir_path = os.path.join(path, label)
    if os.path.isdir(os.path.join(current_label_dir_path)):
        list_of_images = os.listdir(current_label_dir_path)

        for image in list_of_images:
            try:
                if image not in ['Thumbs.db', 'README.TXT']:
                    current_image_path = os.path.join(current_label_dir_path, image)
                    #                 print(current_image_path)

                    file = open(current_image_path, "r")
                    file_text = file.read()
                    s2 = pd.Series([i, current_image_path, label, file_text, image])
                    class_text = class_text.append(s2, ignore_index=True)
                    i = i + 1
            except Exception as e:
                print(current_image_path)
                print(e)
    #                 print(current_image_path)

class_text.columns = ['id', 'file_path', 'document_page_type', 'text', 'file_name']
class_text.to_csv("dataset" + '/' + "class_text.csv")