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

st.sidebar.markdown("# Contact us")
st.sidebar.markdown('**IT Support Manager:** bnaya.hami@mail.huji.ac.il')
st.sidebar.markdown('**Systems Administrator:** nir.averbuch@mail.huji.ac.il')
st.sidebar.markdown('**CEO:** menachem.moshelion@mail.huji.ac.il')


st.title('Connect the system')

st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">This section explain how to conncet all the parts in the system and start collecting data </p>', unsafe_allow_html=True)

st.write("**IMPORTANT:** All boards and sensors (Raspberry Pi, LaunchPad, SensorTag) contain electrical circuits/drives sensitive to static electricity. Therefore, before any operation, discharge any possible static voltage by touching something metallic to prevent short circuits or fires")


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
    st.markdown('<p class="big-fonts"><b>Insert the microSD card into its slot in the Raspberry Pi<b></p>', unsafe_allow_html=True)
    st.write('The Raspberry Pi constitutes the core of the system and is responsible for collecting data from the sensors and sending it to the dashboard webapp. The microSD card contains the operating system and the software required for the system to function.')
    st.image(f'Connect//sd_c.png')

with tab2:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the LaunchPad (to any of the USB ports)<b></p>', unsafe_allow_html=True)
    st.image(f'Connect//lp.png')

with tab3:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the Network cable<b></p>', unsafe_allow_html=True)
    st.image(f'Connect//network.png')

with tab4:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the power supply<b></p>', unsafe_allow_html=True)
    st.image(f'Connect//power_c.png')

with tab5:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>That is how it should look like<b></p>', unsafe_allow_html=True)    
    st.image(f'Connect//system.png')

with tab6:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the batteries to the SensorTag<b></p>', unsafe_allow_html=True)    
    st.image(f'Connect//con_bat.png')

with tab7:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Press the right bottom to send a ping<b></p>', unsafe_allow_html=True)
    with st.expander("How this works?"):
        st.write("The SensorTag is a wireless device, and the ping button is used to send a signal to the Raspberry Pi. This signal is used to identify the sensor and connect it to the system. Next, you will be able to assign the sensor a Name/Location/Label etc.")
    st.markdown('**Note:** It usually takes about 1-2 minutes for the sensor to be recognized by the system and be able to send a ping. we recommend to insert the batteries to all of the sensors and then start sending pings') 
    st.markdown('**IMPORTANT:** There are two buttons, one on each side of the sensor. Ensure you press the correct button, which is located on the right side of the sensor when it is facing up. The other button resets the sensor and will cause a delay of a few minutes before the sensor is recognized by the system again') 
    st.image(f'Connect//ping.png')

with tab8:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>On your browser, open the dashboard webapp<b></p>', unsafe_allow_html=True)  
    st.markdown("<style> .big-fontsh {font-size:18px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fontsh">Here you can control your sensors, start/end experiments, and see your data</p>',unsafe_allow_html=True)
    st.markdown('<p class="big-fontsh">A quick tutorial for the webapp is on the next slide</p>',unsafe_allow_html=True)
    with st.expander("How to get into the dashboard webapp?"):
        st.write("The dashboard webapp would be your Raspberry PI's IP with the port 3000")
        st.write("For example: 127.0.0.1:3000")
        st.write("Pay attention that the computer you are working from should be using is on the same network as your Raspberry PI")
    with st.expander("How to get your Pi's IP?"):
        st.write("""You should assign a static IP to your Raspberry Pi. If you are working within a university or any closed or monitored network, it is advisable to seek assistance from the IT department for this process.""")
    st.image(f'Connect//dashboard.png')


with tab9:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Tutorial for the dashboard website<b></p>', unsafe_allow_html=True) 
    tab71, tab72, tab73, tab74, tab75, tab76, tab77, tab78, tab79, tab80, tab81, tab82 = st.tabs(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    with tab71:
        st.image(f'Connect//dashboard_1.png')
    with tab72:
        st.image(f'Connect//dashboard_2.png')
    with tab73:
        st.image(f'Connect//dashboard_3.png')
    with tab74:
        st.image(f'Connect//dashboard_4.png')
        st.markdown('<p class="big-fonts"><b>Note: Ping button is shown on the following section<b></p>', unsafe_allow_html=True)
    with tab75:
        st.image(f'Connect//dashboard_5.png')
    with tab76:
        st.image(f'Connect//dashboard_6.png')
    with tab77:
        st.image(f'Connect//dashboard_7.png')
    with tab78:
        st.image(f'Connect//dashboard_8.png')
        st.write('When you add a Label/Experiment Info, you will be able to select it for each sensor. This action will update the list of available options from which you can choose')
    with tab79:
        st.image(f'Connect//dashboard_9.png')
    with tab80:
        st.image(f'Connect//dashboard_10.png')
    with tab81:
        st.image(f'Connect//dashboard_11.png')
    with tab82:
        st.image(f'Connect//dashboard_12.png')

with tab10:
    st.markdown('<p class="big-fonts">Begin defining your sensors and experiment information as outlined in the tutorial</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-fonts">You are ready to begin your experiment! Once you start, ensure that you position your sensors according to their allocated locations and begin data collection</p>', unsafe_allow_html=True) 
    st.markdown('<p class="big-fonts">Check out the section below for our recommendations on positioning the sensors to achieve the most accurate measurements</p>', unsafe_allow_html=True)

st.write('---')

st.header('Setup')

st.write("**Note**: this is our suggestion for placing the sensors in a greenhouse:")
st.write("Two sensors are assigned for each plant, one of them is in the height of the canopy (gradually raised up during the plant's growth), and the second one at a high place above the plant")
st.write("We do that in order to measure meteorological data in the plant's close environment and the layer above that affects it. We are using clamps and metal poles to place the sensors, as will be shown below")

tab14, tab15, tab16, tab17, tab18, tab19 = st.tabs(['1', '2', '3', '4', '5', '6'])

with tab14:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>All the parts for placing a sensor<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect//equipment.png')

with tab15:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the clamp to the poles<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect//clamp.png')

with tab16:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Place the sensor into its holder<b></p>', unsafe_allow_html=True)
    st.write("Soon, the STL file of this holder will be available for download")
    st.write("1. Place the sensor into its cover (black)")
    st.write("2. This is the orientation in which the sensor should go into the holder")
    st.write("3. Make sure the light sensor is placed under the hole and exposed to light")
    st.write("4. Connect the sensor to the batteries case using a zip tie")
    st.image(f'Connect//sp_place.png')

with tab17:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the sensor to the pole<b></p>', unsafe_allow_html=True)
    st.write("1. Make a hole in the pole, and pass a metal string through the holes of the holder and the pole to tie them together")
    st.write("2. That's how it should look like")
    st.write("3. Insert a cover (cardboard or plastic) to the holder's slot. This is done to prevent the temperature sensor from heating and give a wrong reading")
    st.write("**Note:** Make sure you place the sensor so the arrow on the holder points north, to enable illumination of the light sensor and cover the other sensors")
    st.image(f'Connect//holder.png')

with tab18:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Example in the greenhouse<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect//sp_green.png')   

with tab19:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Two heights sensors<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect//two_h.png')   










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
