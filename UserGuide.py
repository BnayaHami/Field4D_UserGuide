# libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import webbrowser
import base64

###titles and basic design

# setting page conf
st.set_page_config(page_title="User Guide", page_icon = "🔧", layout="centered", initial_sidebar_state = 'expanded')

st.sidebar.markdown("# Contact us")
st.sidebar.markdown('**IT Support Manager:** bnaya.hami@mail.huji.ac.il')
st.sidebar.markdown('**Systems Administrator:** nir.averbuch@mail.huji.ac.il')
st.sidebar.markdown('**CEO:** menachem.moshelion@mail.huji.ac.il')

st.image('fieldarray.PNG', width  = 250)

st.markdown('---')

# st.subheader('Welcome to the user guide of Field4D!')

st.markdown("<style> .big-font {font-size:38px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font"><b>Welcome to the user guide of Field4D<b></p>', unsafe_allow_html=True)

st.image('moris.jpg')

st.markdown("<style> .big-fonts {font-size:20px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-fonts">Here you have all the information you need to start up the system and start collecting data. On the sidebar you will find different sections about everything you will need for your system</p>', unsafe_allow_html=True)

st.subheader("Let's get started")


# footer

import htbuilder
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
    </style>
    """

    style_div = styles(
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        text_align="center",
        height="0px",
        opacity=0.8
    )

    style_hr = styles(
    )

    body = p()
    foot = div(style=style_div)(hr(style=style_hr), body)

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "<b> GitHub <b>",
        link("https://github.com/", image('https://i.pinimg.com/736x/b1/5e/ed/b15eedbdafbbdbca3249e3942f4faf3b.jpg',
        	width=px(30), height=px(30), margin= "0em")),
        " Our Website ",
        link("https://streamlit.io/", image('https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX1523002.jpg',
        	width=px(30), height=px(30), margin= "0em")),
        br(),
    ]
    layout(*myargs)

if __name__ == "__main__":
    footer()
