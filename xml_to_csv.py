import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

if not os.path.exists('./data'):
    os.makedirs('./data')


def load_files(files):
    xml_list = []
    for xml_file in files:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


    return xml_df

def xml_to_csv(path):
    files = list(glob.glob(path + '/*.xml'))
    length = len(files)
    cutoff = int(.8 * length)

    xml_df_train = load_files(files[:cutoff])
    xml_df_test = load_files(files[cutoff:])
    return xml_df_train, xml_df_test


def main():
    image_path = os.path.join(os.getcwd(), 'annotations')
    xml_df_train, xml_df_test = xml_to_csv(image_path)
    
    xml_df_train.to_csv('./data/train_labels.csv', index=None)
    xml_df_test.to_csv('./data/test_labels.csv', index=None)
    print('Successfully converted xml to csv.')


main()
