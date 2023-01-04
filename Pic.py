# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import module
import streamlit as st
from PIL import Image
# Display Images
img = Image.open("Karina3.png")
st.image(img, width=500)
