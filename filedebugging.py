# just for debugging
import os
import glob
import streamlit as st


def get_local_files():
    local_files = []

    for p in glob.glob(pathname="./checkpoint/**", recursive=True):
        if os.path.isfile(p):
            local_files.append(p)

    for p in glob.glob(pathname="./dataset/**", recursive=True):
        if os.path.isfile(p):
            local_files.append(p)

    for p in glob.glob(pathname="./results/**", recursive=True):
        if os.path.isfile(p):
            local_files.append(p)

    return local_files


st.write("Show all local ML related files:")
st.table(get_local_files())
