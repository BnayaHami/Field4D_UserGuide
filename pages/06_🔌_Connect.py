# libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import plotly.express as px
import plotly.graph_objects as go
import base64

# setting page conf
st.set_page_config(page_title="User Guide", page_icon = "🔧", layout="centered")

st.sidebar.markdown("# Contact us")
st.sidebar.markdown('**IT Support Manager:** bnaya.hami@mail.huji.ac.il')
st.sidebar.markdown('**Systems Administrator:** nir.averbuch@mail.huji.ac.il')
st.sidebar.markdown('**CEO:** menachem.moshelion@mail.huji.ac.il')


st.title('Connect the system')

st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">This section explain how to conncet all the parts in the system and start collecting data </p>', unsafe_allow_html=True)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:25px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10= st.tabs(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

with tab1:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Insert the microSD card into its slot <b></p>', unsafe_allow_html=True)
    st.image(f'Connect\\sd_c.PNG')

with tab2:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the LaunchPad (to any of the USB ports)<b></p>', unsafe_allow_html=True)
    st.image(f'Connect\\lp.PNG')

with tab3:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the Network cable<b></p>', unsafe_allow_html=True)
    st.image(f'Connect\\network.PNG')

with tab4:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the power supply<b></p>', unsafe_allow_html=True)
    st.image(f'Connect\\power_c.PNG')

with tab5:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>That is how it should look like<b></p>', unsafe_allow_html=True)    
    st.image(f'Connect\\system.PNG')

with tab6:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>On your browser, open the dashboard webapp<b></p>', unsafe_allow_html=True)  
    st.markdown("<style> .big-fontsh {font-size:18px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fontsh">Here you can control your sensors, start/end experiments, and see your data</p>',unsafe_allow_html=True)
    st.markdown('<p class="big-fontsh">A quick tutorial for the webapp is on the next slide</p>',unsafe_allow_html=True)
    with st.expander("How to get into the dashboard webapp?"):
        st.write("""The dashboard webapp whould be your Raspberry PI's IP with the port 3000
                 \n For example: 127.0.0.1:3000
                 \n Pay attention that the computer you are working from should be using is on the same network as your Raspberry PI """)
    with st.expander("How to get your Pi's IP?"):
        st.write("""You should assign a static IP to your Raspberry Pi.
                    If you are working within a university setting, It's advisable to seek assistance from your university's
                    IT department for this process.""")
    # future: Open the website
    st.image(f'Connect\\dashboard.PNG')


with tab7:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Tutorial for the dashboard website<b></p>', unsafe_allow_html=True) 
    tab71, tab72, tab73, tab74, tab75, tab76, tab77, tab78, tab79, tab80, tab81, tab82 = st.tabs(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    with tab71:
        st.image(f'Connect\\dashboard_1.PNG')
    with tab72:
        st.image(f'Connect\\dashboard_2.PNG')
    with tab73:
        st.image(f'Connect\\dashboard_3.PNG')
    with tab74:
        st.image(f'Connect\\dashboard_4.PNG')
        st.markdown('<p class="big-fonts"><b>Note: Ping button is shown on the following section<b></p>', unsafe_allow_html=True)
    with tab75:
        st.image(f'Connect\\dashboard_5.PNG')
    with tab76:
        st.image(f'Connect\\dashboard_6.PNG')
    with tab77:
        st.image(f'Connect\\dashboard_7.PNG')
    with tab78:
        st.image(f'Connect\\dashboard_8.PNG')
    with tab79:
        st.image(f'Connect\\dashboard_9.PNG')
    with tab80:
        st.image(f'Connect\\dashboard_10.PNG')
    with tab81:
        st.image(f'Connect\\dashboard_11.PNG')
    with tab82:
        st.image(f'Connect\\dashboard_12.PNG')


with tab8:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>While the dashboard webapp is open, Connect the batteries to the SensorTag<b></p>', unsafe_allow_html=True)    
    st.image(f'Connect\\con_bat.PNG')

with tab9:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Press the right bottom to send a ping<b></p>', unsafe_allow_html=True)
    st.markdown('<p class="big-fontsh">Note: It usually takes about 1-2 minutes for the sensor to be recognized by the system and be able to send a ping. we recommend to insert the batteries to all of the sensors and then start sending pings</p>', unsafe_allow_html=True) 
    st.image(f'Connect\\ping.PNG')


with tab10:
    st.markdown('<p class="big-fonts">Begin defining your sensors and experiment information as outlined in the tutorial</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-fonts">You are ready to begin your experiment! Once you start, ensure that you position your sensors according to their allocated locations and begin data collection</p>', unsafe_allow_html=True) 
    st.markdown('<p class="big-fonts">Check out the section below for our recommendations on positioning the sensors to achieve the most accurate measurements</p>', unsafe_allow_html=True)



st.write('---')

st.header('Setup')

st.write("""**Note**: this is our suggestion for placing the sensors in a greenhouse:  \nTwo sensors are assigned for each plant,
one of them is in the height of the canopy (gradually raised up during the plant's growth),
and the second one at a high place above the plant.  \nWe do that in order to measure meteorological data in the plant's
close environment and the layer above that affects it. We are using clamps and metal poles to place the sensors, as will be shown below""")

tab14, tab15, tab16, tab17, tab18, tab19 = st.tabs(['1', '2', '3', '4', '5', '6'])

with tab14:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>All the parts for placing a sensor<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect\\equipment.PNG')

with tab15:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the clamp to the poles<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect\\clamp.PNG')

with tab16:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Place the sensor into its holder<b></p>', unsafe_allow_html=True)
    st.write("""
    1. Place the sensor into its cover (black)
    \n2. This is the orientation in which the sensor should go into the holder
    \n3. Make sure the light sensor is placed under the hole and exposed to light
    \n4. Connect the sensor to the batteries case using a zip tie
    """)
    st.image(f'Connect\\sp_place.PNG')

with tab17:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the sensor to the pole<b></p>', unsafe_allow_html=True)
    st.write("""
    1. Make a hole in the pole, and pass a metal string through the holes of the holder and the pole to tie them together
    \n2. That's how it should look like
    \n3. Insert a cover (cardboard or plastic) to the holder's slot. This is done to prevent the temperature sensor from heating and give a wrong reading
    \n**Note:** Make sure you place the sensor so the arrow on the holder points north, to enable illumination of the light sensor and cover the other sensors
    """)
    st.image(f'Connect\\holder.PNG')

with tab18:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Example in the greenhouse<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect\\sp_green.PNG')   

with tab19:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Two heights sensors<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect\\two_h.PNG')   










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