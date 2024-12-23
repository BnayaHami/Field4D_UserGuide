# libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import base64
from streamlit_carousel import carousel

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
import plotly.graph_objects as go

# setting page conf
st.set_page_config(page_title="User Guide", page_icon = "🔧", layout="centered", initial_sidebar_state = 'expanded')

logo_url = "https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/f4d.png"

st.logo(logo_url)

st.sidebar.markdown("# Contact us")
st.sidebar.markdown('**IT Support Manager:** bnaya.hami@mail.huji.ac.il')
st.sidebar.markdown('**Customer relations manager:** gal.naftal@mail.huji.ac.il')
st.sidebar.markdown('**Systems Administrator:** nir.averbuch@mail.huji.ac.il')
st.sidebar.markdown('**CEO:** menachem.moshelion@mail.huji.ac.il')


st.title('Connect the system')

st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">This section explains how to connect all components of the system and initiate data collection</p>', unsafe_allow_html=True)
# st.info('This section explain how to conncet all the parts in the system and start collecting data')

st.markdown("""
To set up the system, follow these three stages:
<ol>
    <li style="font-size:18px;">Assign a Static IP to the Raspberry Pi</li>
    <li style="font-size:18px;">Activate the System and Configure Sensors</li>
    <li style="font-size:18px;">Position Sensors in the Measurement Area</li>
</ol>
""", unsafe_allow_html=True)

st.warning("**IMPORTANT:** All boards and sensors (Raspberry Pi, LaunchPad, SensorTag) contain electrical circuits sensitive to static electricity. Before handling, discharge any static voltage by touching a metallic object to prevent short circuits or potential fire hazards")

st.write('---')

st.header('1. Assign a Static IP to the Raspberry Pi')


st.markdown("""
To set up your experiment with a Raspberry Pi, follow these steps to ensure network connectivity and access to the device.
As part of the experiment setup, you need to assign a static IP address to your Raspberry Pi.
This will allow you to access it reliably from your computer.

""")

st.info("**Note:** It's important that both your computer and the Raspberry Pi are connected to the same network")



st.markdown('<p class="big-font">What is your workframe?</p>', unsafe_allow_html=True)

with st.expander("Within a Monitored Network (e.g., a University Network)"):
        st.markdown("""
        If you're working in a closed or monitored environment, such as a university, it's advisable to consult your IT department for assistance.
        They can help ensure network configuration and assign a static IP for the Pi.
        """)

with st.expander("Independent Setup with Ethernet"):
        st.markdown("""
        If you're working independently and have access to an Ethernet connection, connect both the Raspberry Pi and your computer to the
        same router using network cables.
        """)

with st.expander("Alternative Setup Using a SIM Router"):
        st.markdown("""
        If you don’t have a wired Ethernet connection, you can use a router that allows the insertion of a SIM card for wireless connectivity.
        A basic data package (around **5GB per month**) should be sufficient.
        Ensure the router has two network cable ports to connect both the Raspberry Pi and your computer.
        """)


st.markdown('<p class="big-font">Finding the Raspberry Pi IP Address</p>', unsafe_allow_html=True)


st.markdown("""
Once both your computer and the Raspberry Pi are connected to the same network, open the command line on your computer and type the
command `arp -a`. This will list devices connected to the network, showing two IP addresses: one for your computer and one for the Raspberry Pi.
One of them belongs to the Pi.

By following these steps, you’ll ensure a stable and accessible connection to your Raspberry Pi for your experiment.
""")

st.write('---')

st.header('2. Activate the System and Configure Sensors')


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
    st.write('The Raspberry Pi serves as the core of the system, responsible for collecting data from the sensors and transmitting it to the dashboard web app. The microSD card holds the operating system and necessary software for the system to function')
    st.image(f'Connect//sd_c.png')

with tab2:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the LaunchPad<b></p>', unsafe_allow_html=True)
    st.info('Make sure to connect the LaunchPad to one of the grey USB ports of the Raspberry Pi, not the blue ones')
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
        st.write("The SensorTag is a wireless device, and the ping button is used to send a signal to the Raspberry Pi. This signal helps identify the sensor and connect it to the system. Pressing the ping button enables the sensor to appear in the dashboard app, where you can assign it a name, location, label, and other identifiers.")
    st.info('It usually takes about 1-2 minutes for the sensor to be recognized by the system and able to send a ping. We recommend inserting the batteries into all sensors before starting to send pings') 
    st.image(f'Connect//ping.png')
    st.warning('**IMPORTANT:** There are two buttons, one on each side of the sensor. Ensure you press the correct button, located on the right side when the sensor is facing up. The other button resets the sensor, causing a delay of a few minutes before the system recognizes it again') 


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
    # with st.expander("How to get your Pi's IP?"):
    #     st.write("""You should assign a static IP to your Raspberry Pi. If you are working within a university or any closed or monitored network, it is advisable to seek assistance from the IT department for this process.""")
    st.image(f'Connect//dashboard.png')


with tab9:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Tutorial for the dashboard website<b></p>', unsafe_allow_html=True)
    st.info('Note: Due to a temporary compatibility issue, the pictures are a bit blurry, we recommend zooming in for a more comfortable viewing experience ')
    # tab71, tab72, tab73, tab74, tab75, tab76, tab77, tab78, tab79, tab80, tab81, tab82 = st.tabs(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    # with tab71:
    #     st.image(f'Connect//dashboard_1.png')
    # with tab72:
    #     st.image(f'Connect//dashboard_2.png')
    # with tab73:
    #     st.image(f'Connect//dashboard_3.png')
    # with tab74:
    #     st.image(f'Connect//dashboard_4.png')
    # with tab75:
    #     st.image(f'Connect//dashboard_5.png')
    # with tab76:
    #     st.image(f'Connect//dashboard_6.png')
    # with tab77:
    #     st.image(f'Connect//dashboard_7.png')
    # with tab78:
    #     st.image(f'Connect//dashboard_8.png')
    #     st.write('When you add a label or experiment info, it becomes available for selection with each sensor. This action updates the list of available options for you to choose from')
    # with tab79:
    #     st.image(f'Connect//dashboard_9.png')
    # with tab80:
    #     st.image(f'Connect//dashboard_10.png')
    # with tab81:
    #     st.image(f'Connect//dashboard_11.png')
    # with tab82:
    #     st.image(f'Connect//dashboard_12.png')
    test_items = [
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_1.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_2.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_3.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_4.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_5.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_6.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_7.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_8.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_9.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_10.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_11.png"
        ),
        dict(
            title='',
            text='',
            img="https://raw.githubusercontent.com/BnayaHami/Field4D_UserGuide/main/Connect/dashboard_12.png"
        )
    ]

    carousel(items=test_items, interval=99999, container_height=320, width=1.0)

# Define custom CSS styles for the text
st.markdown("""
    <style>
        .big-fontsss {
            font-size: 18px;
            font-weight: bold;
            color: #4A4A4A; /* A soft dark gray */
            background-color: #F0F0F5; /* Light gray background */
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

with tab10:
    st.markdown('<p class="big-fontsss">1. Begin defining your sensors and experiment information as outlined in the tutorial</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-fontsss">2. You are ready to begin your experiment! Once you start, ensure that you position your sensors according to their allocated locations and begin data collection</p>', unsafe_allow_html=True) 
    st.markdown('<p class="big-fontsss">3. Move on to the section below for instructions on positioning the sensors</p>', unsafe_allow_html=True)

st.write('---')

st.header('3. Position Sensors in the Measurement Area')

st.info("**Note:** This is our recommended sensor placement for the greenhouse. We strongly advise following it closely to ensure optimal results")
st.write("Two sensors are assigned for each plant, one of them is in the height of the canopy (gradually raised up during the plant's growth), and the second one at a high place above the plant. We do that in order to measure meteorological data in the plant's close environment and the layer above that affects it")

tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22 = st.tabs(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

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
    st.write("STL files of this holder are available for download (below)")
    st.write("1. Place the sensor into its little black cover")
    st.write("2. This is the orientation in which the sensor should go into the holder")
    st.write("3. Make sure the light sensor is placed under the hole and exposed to light")
    st.write("4. Connect the sensor to the batteries case using a hot glue gun")
    st.image(f'Connect//old_cover.png')

with tab17:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Connect the sensor to the pole<b></p>', unsafe_allow_html=True)
    st.write("That's how it should look like")
    st.info("**Note:** Make sure you place the sensor so the arrow on the holder points north, to enable illumination of the light sensor and cover the other sensors")
    st.image(f'Connect//holder.png')

with tab18:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Example in the greenhouse<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect//sp_green.png')   

with tab19:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Two heights sensors<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect//two_h.png')

with tab20:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>All the parts for placing a sensor<b></p>', unsafe_allow_html=True)
    st.info('Suggested here another cover version')
    st.image(f'Connect//equipment_2.png')

with tab21:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Place the sensor into its holder<b></p>', unsafe_allow_html=True)
    st.write("STL files of this holder are available for download (below)")
    st.info('Note that in this version, the sensor should be placed in the cover with both the black and the transparent parts')
    st.write("1. insert the sensor into the the cover")
    st.write("2. insert the second part of the cover, it should get in with a click. Make sure the light sensor is placed under the hole and exposed to light")
    st.write("3. Example usage")
    st.image(f'Connect//new_cover.png')

with tab22:
    st.markdown("<style> .big-fonts {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fonts"><b>Example in the greenhouse<b></p>', unsafe_allow_html=True)  
    st.image(f'Connect//sp_green2.png') 

st.write('---')


## Title of the Streamlit app
st.subheader("Appendix - STL Files for 3D Printing")

# Paths to the predefined STL files
stl_file_path_1 = os.path.join(os.path.dirname(__file__), 'Base_With_Cover.stl')
stl_file_path_2 = os.path.join(os.path.dirname(__file__), 'SP_assaf.stl')

# Load the STL files
mesh1 = mesh.Mesh.from_file(stl_file_path_1)
mesh2 = mesh.Mesh.from_file(stl_file_path_2)

# Extract the vertices and  faces for the first STL file
vertices1 = mesh1.points.reshape(-1, 3)
faces1 = np.arange(len(vertices1)).reshape(-1, 3)

# Extract the vertices and faces for the second STL file
vertices2 = mesh2.points.reshape(-1, 3)
faces2 = np.arange(len(vertices2)).reshape(-1, 3)

# Create Plotly figures
fig1 = go.Figure(data=[go.Mesh3d(
    x=vertices1[:, 0],
    y=vertices1[:, 1],
    z=vertices1[:, 2],
    i=faces1[:, 0],
    j=faces1[:, 1],
    k=faces1[:, 2],
    color='grey',
    opacity=1,
    showscale=False,
    name='Base_With_Cover'
)])

fig2 = go.Figure(data=[go.Mesh3d(
    x=vertices2[:, 0],
    y=vertices2[:, 1],
    z=vertices2[:, 2],
    i=faces2[:, 0],
    j=faces2[:, 1],
    k=faces2[:, 2],
    color='grey',
    opacity=1,
    showscale=False,
    name='SP_assaf'
)])

# Update the layout for better visualization and aspect ratio
for fig in [fig1, fig2]:
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='data'
        ),
        margin=dict(r=0, l=0, b=0, t=0)
    )

# Create tabs for navigation
tab101, tab102 = st.tabs(["Ver1", "Ver2"])

with tab101:
    st.write('First version')
    st.plotly_chart(fig1)
    with open(stl_file_path_1, "rb") as file1:
        st.download_button(
            label="Download STL file",
            data=file1,
            file_name="Base_With_Cover.stl",
            mime="application/octet-stream"
        )

with tab102:
    st.write('Second version')
    st.plotly_chart(fig2)
    with open(stl_file_path_2, "rb") as file2:
        st.download_button(
            label="Download STL file",
            data=file2,
            file_name="SP_assaf.stl",
            mime="application/octet-stream"
        )

# Update the layout for better visualization and aspect ratio
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode='data'
    ),
    margin=dict(r=0, l=0, b=0, t=0)
)