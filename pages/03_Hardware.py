# libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import base64

from streamlit_extras.stodo import to_do

# setting page conf
st.set_page_config(page_title="User Guide", page_icon = "🔧", layout="centered", initial_sidebar_state = 'expanded')

logo_url = "https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/f4d.png"

st.logo(logo_url)

st.sidebar.markdown("# Contact us")
st.sidebar.markdown('**Support:** f4d_support@field4d.com')
st.sidebar.markdown('**Customer relations manager:** gal.naftal@mail.huji.ac.il')

# titles
st.title('Hardware')
st.markdown("<style> .big-font {font-size:20px !important;color:black} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font"><b>Here is all the equipment you need to power up the system<b></p>', unsafe_allow_html=True)

st.markdown(
    """
<style>
div[data-testid="stExpander"] details summary p{
    font-size: 18px;
    font-weight: bold;
}
</style>
""" ,unsafe_allow_html=True,)

st.subheader('Provided equipment:')

expander1 = st.expander('RaspberryPi')
expander1.image(f'Hardware/pi.png', width=200)
expander1.write('**Note: use only RaspberyPi 5**')
expander1.write('Suggestions for online purchace:')
expander1.write('https://www.raspberrypi.com/products/raspberry-pi-5/')
expander1.write('https://piitel.co.il/shop/raspberry-pi-5/')

expander2 = st.expander('RaspberryPi power supply')
expander2.image(f'Hardware//power.png', width=200)
expander2.write('Suggestion for online purchase:')
expander2.write('https://piitel.co.il/shop/27w-usb-c-psu/')

expander3 = st.expander('Micro-USB cable')
expander3.image(f'Hardware//cable.png', width=200)

expander7 = st.expander('LaunchPad CC2650')
expander7.image(f'Hardware//gw.png', width=200)

expander8 = st.expander('Sensortag cc2650stk')
expander8.image(f'Hardware//sp.png', width=200)

expander9 = st.expander('MicroSD')
expander9.image(f'Hardware//sd.png', width=200)
expander9.write('Including the Raspberry Pi Operating system')

expander10 = st.expander('Debugger (optional)')
expander10.image(f'Hardware//debug.png', width=200)
expander10.write('Relevant for developers')

expander6 = st.expander('Card Reader/Writer (optional)')
expander6.image(f'Hardware//card.png', width=200)
expander6.write('Relevant for developers')

st.subheader('Self-purchase:')



expander4 = st.expander('Network cable')
expander4.image(f'Hardware//n-cable.png', width=200)

expander5 = st.expander('AA batteries')
expander5.image(f'Hardware//battery.png', width=150)

st.write('---')

st.subheader('Appendices')

st.markdown('<p class="big-font"><b>For your convenience, here is an equipment list<b></p>', unsafe_allow_html=True)

expander12 = st.expander('Equipment list')
with expander12:
    to_do(
        [(st.write, "**RaspberryPi**")],
        "Pi",
    )
    to_do(
        [(st.write, "**RaspberryPi power supply**")],
        "Pi_supply",
    )
    to_do(
        [(st.write, "**Micro-USB cable**")],
        "USB",
    )
    to_do(
        [(st.write, "**Network cable**")],
        "network",
    )
    to_do(
        [(st.write, "**AA batteries**")],
        "AA",
    )
    to_do(
        [(st.write, "**LaunchPad CC2650**")],
        "gw",
    )
    to_do(
        [(st.write, "**Sensortag cc2650stk**")],
        "sp",
    )
    to_do(
        [(st.write, "**MicroSD**")],
        "sd",
    )
    to_do(
        [(st.write, "**Card Reader/Writer (optional)**")],
        "card",
    )
    to_do(
        [(st.write, "**Debugger (optional)**")],
        "deb",
    )


st.markdown('<p class="big-font"><b>Texas Instruments CC2650stk SensorTag component Overview:<b></p>', unsafe_allow_html=True)
expander11 = st.expander('Click here to see')
expander11.image(f'Hardware//sensortag.png')

st.write('---')

st.markdown('<p class="big-font"><b>A basic Illustration of the system<b></p>', unsafe_allow_html=True)
st.image(f'Hardware//schema.png')

st.write('---')
st.page_link("pages/04_Firmware (Developers) 🔒.py", label="For developers - continue to Firmware")
st.page_link("pages/06_Connect.py", label="For regular users - continue to Connect")



# st.markdown("<style> .big-font {font-size:20px !important;color:black} </style>", unsafe_allow_html=True)
# st.markdown('<p class="big-font"><b>For your convenient, here is a "to do list" for the equipment<b></p>', unsafe_allow_html=True)

# import streamlit_extras
# from streamlit_extras.stodo import to_do

# expander10 = st.expander('Equipment list')
# with expander10:
#     to_do(
#         [(st.write, "**RaspberryPi**")],
#         "Pi",
#     )
#     to_do(
#         [(st.write, "**RaspberryPi power supply**")],
#         "Pi_supply",
#     )
#     to_do(
#         [(st.write, "**Micro-USB cable**")],
#         "USB",
#     )
#     to_do(
#         [(st.write, "**Network cable**")],
#         "network",
#     )
#     to_do(
#         [(st.write, "**AA batteries**")],
#         "AA",
#     )
#     to_do(
#         [(st.write, "**Card Reader/Writer (optional)**")],
#         "card",
#     )
#     to_do(
#         [(st.write, "**LaunchPad CC2650**")],
#         "gw",
#     )
#     to_do(
#         [(st.write, "**Sensortag cc2650stk**")],
#         "sp",
#     )
#     to_do(
#         [(st.write, "**MicroSD**")],
#         "sd",
#     )















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
    
