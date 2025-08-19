# libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import base64


# setting page conf
st.set_page_config(page_title="User Guide", page_icon = "🔧", layout="centered", initial_sidebar_state = 'expanded')

logo_url = "https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/f4d.png"

st.logo(logo_url)

st.sidebar.markdown("# Contact us")
st.sidebar.markdown('f4d_support@field4d.com')


st.header('The first step')

st.markdown("<style> .big-fontl {font-size:20px !important; color:red} </style>", unsafe_allow_html=True)

st.write('The first step is to sign in to our website. the url is https://field4d.com', unsafe_allow_html=True)

st.image(f'FirstStep/login_f4d.png', width=600)

st.write('We will send you an email with your username and password after your payment has been confirmed. If you have not received it, please contact us. On the website, you will be able to track your experiments, analyze them, and download the data collected by the system. For now, you can already view two demo experiments on the website to help you understand how the system works.')
st.info('Please note that this website is only for viewing and analyzing collected data. To set up the system and manage experiments, you will find the instructions in the next sections of this user guide')

# st.markdown("<style> .big-fonts {font-size:20px !important;} </style>", unsafe_allow_html=True)
# st.markdown('<p class="big-fonts">here is the link to the website:</p>', unsafe_allow_html=True)

st.markdown("<style> .big-fontshl {font-size:21px !important} </style>", unsafe_allow_html=True)
st.markdown("<style> .big-fontshls {font-size:21px !important; color: grey !important;} </style>", unsafe_allow_html=True)

st.markdown("<style> .big-fontshy {font-size:17px !important; color: grey !important;} </style>", unsafe_allow_html=True)

st.write('---')

st.markdown("<style> .big-fonts {font-size:20px !important;} </style>", unsafe_allow_html=True)
st.markdown("""<p class="big-fonts">On the sidebar, you will find all the necessary steps for setting up the system, as follows:</p>""", unsafe_allow_html=True)

st.markdown("""<p class="big-fontshl"><b>Hardware:<b></p>""", unsafe_allow_html=True)
st.markdown("""<p class="big-fontsh">Lists all the equipment required for the system</p>""", unsafe_allow_html=True)

st.markdown("""<p class="big-fontshls"><b>Firmware:<b></p>""", unsafe_allow_html=True)
st.markdown("""<p class="big-fontshy">Manage the OS of the Raspberry Pi and the firmware of the LaunchPad and sensors (relevant primarily for developers). If you are a developer, this is a required part of the installation</p>""", unsafe_allow_html=True)

st.markdown("""<p class="big-fontshls"><b>Software:<b></p>""", unsafe_allow_html=True)
st.markdown("""<p class="big-fontshy">Provides guides and useful tools for managing the software (relevant primarily for developers), this part is not required for the installation</p>""", unsafe_allow_html=True)

st.markdown("""<p class="big-fontshl"><b>Connect:<b></p>""", unsafe_allow_html=True)
st.markdown("""<p class="big-fontsh">Explains how to conncet all the parts in the system and start collecting data</p>""", unsafe_allow_html=True)

st.markdown("""<p class="big-fontshl"><b>FAQ:<b></p>""", unsafe_allow_html=True)
st.markdown("""<p class="big-fontsh">Addresses common questions and provides additional information</p>""", unsafe_allow_html=True)

st.write('---')
st.page_link("pages/03_Hardware.py", label="Continue to Hardware")




# st.image(f"images\\ping.PNG")






















# footer

# import htbuilder
# from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
# from htbuilder.units import percent, px
# from htbuilder.funcs import rgba, rgb


# def image(src_as_string, **style):
#     return img(src=src_as_string, style=styles(**style))

# def link(link, text, **style):
#     return a(_href=link, _target="_blank", style=styles(**style))(text)

# def layout(*args):

#     style = """
#     <style>
#       # MainMenu {visibility: hidden;}
#       footer {visibility: hidden;}
#     </style>
#     """

#     style_div = styles(
#         left=0,
#         bottom=0,
#         margin=px(0, 0, 0, 0),
#         width=percent(100),
#         text_align="center",
#         height="0px",
#         opacity=0.8
#     )

#     style_hr = styles(
#     )

#     body = p()
#     foot = div(style=style_div)(hr(style=style_hr), body)

#     st.markdown(style, unsafe_allow_html=True)

#     for arg in args:
#         if isinstance(arg, str):
#             body(arg)
#         elif isinstance(arg, HtmlElement):
#             body(arg)

#     st.markdown(str(foot), unsafe_allow_html=True)

# def footer():
#     myargs = [
#         "<b> GitHub <b>",
#         link("https://github.com/", image('https://i.pinimg.com/736x/b1/5e/ed/b15eedbdafbbdbca3249e3942f4faf3b.jpg',
#         	width=px(30), height=px(30), margin= "0em")),
#         " Our Website ",
#         link("https://streamlit.io/", image('https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX1523002.jpg',
#         	width=px(30), height=px(30), margin= "0em")),
#         br(),
#     ]
#     layout(*myargs)

# if __name__ == "__main__":
#     footer()
