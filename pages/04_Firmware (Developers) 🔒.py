# libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import base64

PASSWORD = st.secrets["FIRMWARE_PASSWORD"]  # For Firmware page

# Initialize session state for password
if "authenticated_firmware" not in st.session_state:
    st.session_state.authenticated_firmware = False

# Password protection logic
if not st.session_state.authenticated_firmware:
    st.title("Restricted Access")
    st.warning("This page is limited to developers only, Access is restricted")
    st.markdown("This section is not necessary for the installation, and refers to some guides and commands for developers")
    password_input = st.text_input("Enter the password to access this page:", type="password")
    if st.button("Submit"):
        if password_input == PASSWORD:
            st.session_state.authenticated_firmware = True
            st.success("Access Granted!")
            st.rerun()  # Use st.rerun instead of experimental_rerun
        else:
            st.error("Incorrect password. Please try again.")
    st.stop()

# setting page conf
st.set_page_config(page_title="User Guide", page_icon = "🔧", layout="centered", initial_sidebar_state = 'expanded')

logo_url = "https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/f4d.png"

st.logo(logo_url)


st.sidebar.markdown("# Contact us")
st.sidebar.markdown('f4d_support@field4d.com')


st.title('Firmware')

st.markdown("<style> .big-fontl {font-size:22px !important; color:red} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-fontl">✱ <b>for developers<b> </p>', unsafe_allow_html=True)

st.markdown("<style> .big-fontt {font-size:18px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-fontt">This section explain how to manage the OS system of the RaspberryPi and the firmwares of the LaunchPad and the sensors</p>', unsafe_allow_html=True)

st.warning("**IMPORTANT:** All boards and sensors (Raspberry Pi, LaunchPad, SensorTag) contain electrical circuits/drives sensitive to static electricity. Therefore, before any operation, discharge any possible static voltage by touching something metallic to prevent short circuits or fires")

st.write('---')

st.subheader('1. Install Raspberry Pi Operation system (OS) to a microSD card')
st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">Step 1 </p>', unsafe_allow_html=True)
st.write('**Download Raspberry Pi imager**')
st.write('Link: https://www.raspberrypi.com/software/')
st.write('Follow the instructions')
st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">Step 2 </p>', unsafe_allow_html=True)
st.write('**Install the OS, as described below**')

font_css = """
<style>
button[data-baseweb="tab"] {
  font-size: 22px;
}
</style>
"""

st.write(font_css, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab34, tab35, tab36, tab37, tab38, tab39, tab40, tab41 = st.tabs([' 1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'])

with tab1:
    st.write('**Open the Raspberry Pi Imager**')
    st.info("**Note:** If you have something written on your card, you might would need to reset it before writing the IMG")
    st.image(f'Firmware/firm1.png')

with tab2:
     st.write('**Insert the card reader with the MicroSD card**')
     st.image(f'Firmware/IMG.png')

with tab3:
    st.write('**Click on “Choose device”**')
    st.image(f'Firmware/firm2.png')

with tab4:
    st.write('**Choose Raspberry pi 5**')
    st.image(f'Firmware/firm3.png')

with tab5:
    st.write('**Click on “Choose OS”**')
    st.image(f'Firmware/firm4.png')

with tab6:
    st.write('**Choose “Use custom”**')
    st.image(f'Firmware/firm5.png')

with tab7:
    st.write('**Choose the IMG**')
    st.info('**Note:** The relevant IMG is detailed in the email sent to you and might have a different name')
    st.image(f'Firmware/firm6.png')

with tab8:
    st.write('**Click on “Chosse storage”**')
    st.image(f'Firmware/firm7.png') 

with tab9:
    st.write('**Click on the available SD card**')
    st.image(f'Firmware/firm8.png') 

with tab10:
    st.write('**Click on “Next”**')
    st.image(f'Firmware/firm9.png')  

with tab11:
    st.write('**Click on “Edit settings”**')
    st.image(f'Firmware/firm10.png')

with tab34:
    st.write('**Fill in the hostname and password. make sure the Username is "pi"**')
    st.image(f'Firmware/firm11.png')   

with tab35:
    st.write('**Proceed to "Services", and make sure the SSH is enabled, and the option is set to "Use password authentication**')
    st.image(f'Firmware/firm12.png')

with tab36:
    st.write('**Proceed to "Options", making sure to check these rubrics, and press "Save"**')
    st.image(f'Firmware/firm13.png')

with tab37:
    st.write('**Click on “yes”**')
    st.image(f'Firmware/firm14.png')

with tab38:
    st.write('**Click on “yes”**')
    st.image(f'Firmware/firm15.png')

with tab39:
    st.write('**Wait for the installation to complete**')
    st.image(f'Firmware/firm16.png')

with tab40:
    st.write('**Click on “Continue”**')
    st.image(f'Firmware/firm17.png')

with tab41:
     st.subheader("Your'e all set!")           

st.write('---')

# Install the launchpad and the sensortag hardwares

st.subheader('')
st.subheader('2. Flash the LaunchPad and the SensorTag firmwares')


st.write('**Download UniFlash software**')
st.write('Link: https://www.ti.com/tool/UNIFLASH')
st.write('If you are struggling with downloading, check the FAQ for more information')
st.page_link("pages/07_FAQ.py", label="Press here to go to FAQ")

st.info('**Note:** You should get the LaunchPad and SensorTag firmwares from your provider')

st.warning("**IMPORTANT:** Make sure that the LaunchPad and the Debugger aren't connected to the computer simultaneously")

st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">Flash LaunchPad firmware </p>', unsafe_allow_html=True)

font_css2 = """
<style>
button[data-baseweb="tab"] {
  font-size: 22px;
}
</style>
"""

st.write(font_css2, unsafe_allow_html=True)



tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20 = st.tabs([' 1', '2', '3', '4', '5', '6', '7', '8', '9'])

with tab12:
     st.write('**Open UniFlash**')
     st.image(f'Firmware/gw1.png')

with tab13:
     st.write('**Connect the LaunchPad**')
     st.image(f'Firmware/gw_c.png')

with tab14:
     st.write('**The LaunchPad should appear**')
     st.image(f'Firmware/gw2.png')     

with tab15:
     st.write('**Press "Start"**')
     st.image(f'Firmware/gw3.png')   

with tab16:
     st.write('**Press "Browse"**')
     st.image(f'Firmware/gw4.png')  

with tab17:
     st.warning('**IMPORTANT:** Choose the "gw" file. Ensure that you select the "gw" file associated with the LaunchPad, not the "sp" file, which belongs to the SensorTag')
     st.image(f'Firmware/gw5.png')   

with tab18:
     st.write('**Press "Load Image"**')
     st.image(f'Firmware/gw6.png')

with tab19:
     st.write('**Make sure the program loaded successfully**')
     st.image(f'Firmware/gw7.png')

with tab20:
     st.subheader("Your'e all set!")           

st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">Flash SensorTag firmware </p>', unsafe_allow_html=True)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:25px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

tab21, tab22, tab23, tab24, tab25, tab26, tab27, tab28, tab29, tab30, tab31, tab32, tab33 = st.tabs([' 1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])

with tab21:
     st.write('**Open UniFlash (Or start a new session)**')
     st.image(f'Firmware//sp1.png')

with tab22:
     st.write('**Connect the debugger**')
     st.info("**Note**: The debugger doesn't come with a cable, but it uses a standard micro USB cable. You can use the one that comes with the LaunchPad or any other micro USB cable you have.")
     st.image(f'Firmware//debugger1.png')

with tab23:
    st.write('**The debugger should appear**')
    st.image(f'Firmware/sp2.png')     

with tab24:
    st.markdown("<style> .big-fonts {font-size:18px !important; color:red} </style>", unsafe_allow_html=True)
    st.write('**Conncet a sensor to the debugger (video below)**')
    st.markdown('<p class="big-fonts"><b>Warning: do not connect the debugger to a sensor when the the batteries are in<b></p>', unsafe_allow_html=True)
    st.image(f'Firmware/debugger2_edit.png')
    st.subheader('How to connect a sensor to the debugger:') 
    if st.button('open video'):
        debugger = open(f'Firmware/debugger.mp4', 'rb')
        video_bytes = debugger.read() 
        st.video(video_bytes)     

with tab25:
     st.write('**In this tab insert the following: "cc2650"**')
     st.image(f'Firmware/sp3.png')  

with tab26:
     st.write('**Choose the sencod one**')
     st.image(f'Firmware/sp4.png')   

with tab27:
     st.write('**Scroll down and press "Start"**')
     st.image(f'Firmware/sp5.png')

with tab28:
     st.write('**Press "Browse"**')
     st.image(f'Firmware/sp6.png')

with tab29:
     st.warning('**IMPORTANT:** Choose the "sp" file. Ensure that you select the "sp" file associated with the SensorTag, not the "gw" file, which belongs to the LaunchPad')
     st.image(f'Firmware/sp7.png')

with tab30:
     st.write('**Press "Load Image"**')
     st.image(f'Firmware/sp8.png')

with tab31:
     st.write('**Make sure the program loaded successfully**')
     st.info("**Note:** From this point, you don't have to start the whole proccess again, you can simply connect another sensor to the debugger and press 'Load Image'")
     st.image(f'Firmware/sp9.png')

with tab32:
    st.write('**Disconnect the sensor from the debugger**')
    st.write('At this point, all the sensors should be written with the firmware. In the next sections, you will learn how to configure sensor settings and start an experiment')
    debugger2 = open(f'Firmware/debugger2.mp4', 'rb')
    video_bytes2 = debugger2.read() 
    st.video(video_bytes2)     

with tab33:
    st.subheader("Your'e all set!")


st.write('---')
st.info('**Note:** Check out the Software section for additional information if needed')
st.page_link("pages/06_Connect.py", label="Continue to Connect")

     

















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
