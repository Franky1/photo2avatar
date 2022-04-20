# just for local testing purposes
import os

path = './checkpoint/temp.zip'

if not os.path.exists(path):
    decoder_url = 'wget --no-verbose -O ./checkpoint/temp.zip https://www.dropbox.com/sh/63xqqqef0jtevmg/AADN7izdFHxueUbTSRBZrpffa?dl=0'
    os.system(decoder_url)
