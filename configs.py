import os
from os.path import join
import sys

IMG_DIR = 'crop_img'
RECOG_TEXTFILE = 'rec_res.txt'

IMG_IDS = os.listdir(IMG_DIR)
IMG_IDS.sort()
IMG_PATHS = [join(IMG_DIR, img_id) for img_id in IMG_IDS]

print(f'Found {len(IMG_PATHS)} cropped images!\n')

with open(RECOG_TEXTFILE, 'r') as f:
    CONTENT = [line.strip().split('\t') for line in f.readlines()]
    CONTENT = sorted(CONTENT, key=lambda entry: entry[0])

img_ids_in_content = [entry[0].split('/')[-1] for entry in CONTENT]
for i, img_path in enumerate(IMG_PATHS):
    img_id = img_path.split('/')[-1]
    if img_id not in img_ids_in_content:
        CONTENT.insert(i, [join(IMG_DIR, img_id), ' '])

print('\n'.join(map(str, IMG_PATHS[:7])))
print()
print('\n'.join(map(str, CONTENT[:7])))