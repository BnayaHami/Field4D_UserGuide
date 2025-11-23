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
st.sidebar.markdown('f4d_support@field4d.com')


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
expander1.write('Optional: Raspberry Pi case')
expander1.image('Hardware//pi_cover.png', width=150)

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

st.markdown('<p class="big-font"><b>CC2650stk SensorTag maintenance guide<b></p>', unsafe_allow_html=True)
expander11 = st.expander('Click here to see')
expander11.image(f'https://lucid.app/lucidchart/784465cf-0a03-4a48-8277-246ab823b96d/edit?viewport_loc=-401%2C756%2C3508%2C1471%2C0_0&invitationId=inv_e8557cd7-15f1-42a3-9ec2-51cbf389e78f')

st.write('---')

st.markdown('<p class="big-font"><b>A basic Illustration of the system<b></p>', unsafe_allow_html=True)
st.image(f'Hardware//schema.png')

st.write('---')
st.page_link("pages/04_Firmware (Developers) 🔒.py", label="For developers - continue to Firmware")
st.page_link("pages/06_Connect.py", label="For regular users - continue to Connect")