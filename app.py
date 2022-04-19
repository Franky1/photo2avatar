import os
import subprocess
import sys
import zipfile

import cv2
import numpy as np
import PIL
import streamlit as st
from PIL import Image

import UGATIT
from preprocessing import preprocess

st.header("Photo to Avatar")
st.write("Choose any image and get corresponding avatar:")

uploaded_file = st.file_uploader("Choose an image...")

# newImg.save(out_f)

@st.cache
def download_checkpoint():
    path = './checkpoint/temp'
    if not os.path.exists(path):
        decoder_url = 'wget -O ./checkpoint/temp https://www.dropbox.com/sh/63xqqqef0jtevmg/AADN7izdFHxueUbTSRBZrpffa?dl=0'

        with st.spinner('downloading pretrained model...'):
            os.system(decoder_url)

        with zipfile.ZipFile(path, 'r') as zip_ref:
          zip_ref.extractall('./checkpoint')

        os.rename('./checkpoint/UGATIT_selfie2anime_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing','./checkpoint/UGATIT_sample_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing')

if uploaded_file is not None:
    download_checkpoint()
    img = PIL.Image.open(uploaded_file).convert("RGB")
    img = np.array(img)
    pre = preprocess.Preprocess()
    # face alignment and segmentation
    face_rgba = pre.process(img)
    face = face_rgba[:,:,:3].copy()
    mask = face_rgba[:,:,3].copy()[:,:,np.newaxis]/255.
    face_white_bg = (face*mask + (1-mask)*255).astype(np.uint8)
    cv2.imwrite('./dataset/sample/testA/0000.png', cv2.cvtColor(face_white_bg, cv2.COLOR_RGB2BGR))

    with st.spinner('Wait for modeling...'):
      subprocess.run([f"{sys.executable}", "main.py"])

    img_uploaded = Image(uploaded_file)
    img_processed = Image(filename="./dataset/sample/testA/0000.png")
    output = Image(filename="./results/UGATIT_sample_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing/0000.png")

    st.image(img_uploaded, caption='Input Image', use_column_width=True)
    st.image(img_processed, caption='Processed Image', use_column_width=True)
    st.image(output, caption='Avatar', use_column_width=True)
