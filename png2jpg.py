import os
from glob import glob                                                           
import cv2 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--dir', required=True, type=str)
args = vars(ap.parse_args())

path = os.path.join(args['dir'], '*.png')

pngs = glob(path)
for j in pngs:
    img = cv2.imread(j)
    path = './' + j[:-3] + 'jpg'
    print path
    cv2.imwrite(path, img)

