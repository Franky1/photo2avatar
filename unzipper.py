# just for local testing purposes
import os
import zipfile

path = './checkpoint/temp.zip'

with zipfile.ZipFile(path, 'r') as archive:
    # archive.printdir()
    archive.extractall('./checkpoint/')

os.rename('./checkpoint/UGATIT_selfie2anime_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing',
        './checkpoint/UGATIT_sample_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing')
