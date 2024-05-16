# libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import base64
import webbrowser

# setting page conf
st.set_page_config(page_title="User Guide", page_icon = "🔧", layout="centered")

st.sidebar.markdown("# Contact us")
st.sidebar.markdown('**IT Support Manager:** bnaya.hami@mail.huji.ac.il')
st.sidebar.markdown('**Systems Administrator:** nir.averbuch@mail.huji.ac.il')
st.sidebar.markdown('**CEO:** menachem.moshelion@mail.huji.ac.il')

st.title('Software')

st.markdown("<style> .big-font {font-size:22px !important; color:red} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-font">✱ <b>for developers<b></p>', unsafe_allow_html=True)
st.markdown('**Note:** This section is not required for the installation, and is refers to some guides and commands useful for developers')


st.markdown("""
<style>
.stButton>button:first-child { 
    background-color: rgb(255, 255, 255) !important;
    font-size: 20px !important; 
    font-weight: bold !important;
    height: 8em !important;
    width: 11em !important;
    border-radius: 10px 10px 10px 10px !important;
} 
</style>""",
unsafe_allow_html=True)

col1, col2, col3 = st.columns(spec = 3)

with col1:
    ssh = st.button("SSH connection")
    daemon = st.button('Daemon')

if ssh:
    st.subheader('SSH connection')
    st.write('**How to connect to your RaspberryPi through SSH:**')
    st.write('Connection to your RaspberryPi is possible through the terminal or an open source based platform like Visual Studio Code')
    st.write('**Note**: If you are using VS code or simillar platform make sure to install SSH extention')
    st.write("""To connect to your RaspberryPi, type: "ssh pi@######" with the RaspberryPi's IP and insert the password if needed""")
    st.write("""**Note**: To get the RaspberryPi's IP, you should connect it to a screen and a keyboard, and type in the terminal: "ifconfig" """)

daemon_code = """
[Unit]
Description= FieldArr@y IPv6 to IPv4


[Service]
WorkingDirectory=/home/pi/6to4/build
ExecStart=/usr/local/bin/node from6to4.js
Restart=on-failure
User=pi

[Install]
WantedBy=multi-user.target
"""

if daemon:
    st.subheader('Daemon')
    st.write('**This section explain the basics of creating a daemon and include an example for a daemon that returns the 6to4 service if case of an electrical failure**')
    st.write('Link To Service Example : https://github.com/moshelionlab/hisai/blob/main/Idan/cannabis_experiment/gw.service#L11')
    st.markdown("<style> .big-fontsh {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-fontsh"><b>Step 1<b></p>', unsafe_allow_html=True)
    st.write('**a.** Copy this code to the following path in your Pi:  \n"pi\\6to4\Deamon\\" ')
    st.code(daemon_code, language=None)
    st.write('**b.** Call the file "6to4.service"')
    st.markdown('<p class="big-fontsh"><b>Step 2<b></p>', unsafe_allow_html=True)
    st.write('**Open the terminal and follow the next commands:**')
    st.write('Copy the service to the following location')
    st.code('sudo cp ../Deamon/6to4.service /etc/systemd/system', language=None)
    # st.markdown('<p class="big-fontsh"><b>Step 3<b></p>', unsafe_allow_html=True)
    st.write('Enable the Service')
    st.code('sudo systemctl enable 6to4.service', language=None)
    # st.markdown('<p class="big-fontsh"><b>Step 4<b></p>', unsafe_allow_html=True)
    st.write('Start the service')
    st.code('sudo systemctl start 6to4.service', language=None)
    # st.markdown('<p class="big-fontsh"><b>Step 5<b></p>', unsafe_allow_html=True)
    st.write('Refresh the Deamon services')
    st.code('sudo systemctl daemon-reload', language=None)
    # st.markdown('<p class="big-fontsh"><b>Step 6<b></p>', unsafe_allow_html=True)
    st.write('Check Deamon Service Status')
    st.code('sudo systemctl status 6to4.service', language=None)
    # st.markdown('<p class="big-fontsh"><b>Step 7<b></p>', unsafe_allow_html=True)
    st.write('Check the Journal to see if service is running')
    st.code('journalctl -b -ef -u 6to4.service', language=None)






with col2:
    backend = st.button("Useful backend commands")

if backend:
    st.subheader('Useful backend commands')
    st.write('**Note**: The following commands are relevant for linux environment')

    st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Screen commands </p>', unsafe_allow_html=True)

    st.write('Working with screen recommended to facilitate the ability for launching and using more than one shell session through an individual ssh session')

    st.write("**1. Create a screen:**")
    st.code("Screen -S '6to4'", language=None)

    st.write("**2. Check for existed screens:**")
    st.code("Screen -ls", language=None)

    st.write("**3. Connect to a screen:**")
    st.code("Screen -rx #####/'6to4'", language=None)


    st.markdown("<style> .big-font {font-size:22px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-font">npm commands </p>', unsafe_allow_html=True)

    st.write("**1. Compile the '6to4' application:**")
    st.code("cd '6to4'\nsudo npm run-script build", language=None)

    st.write("**2. Run the '6to4' application:**")
    st.code("cd '6to4'\nsudo npm start", language=None)

    st.write("**3. Stop the '6to4' service:**")
    st.code('sudo systemctl stop 6to4 service', language=None)

    st.write("**4. shows service history status:**")
    st.code('journalctl -b-fu 6to4.service', language=None)

    st.write("**5. close a service:**")
    st.code('pgrep node → shows number\nsudo kill -a ######', language=None)


with col3:
    query = st.button("Basic queries using Python")

influx_query = """

# imports
import pandas as pd
import numpy as np
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import warnings
from influxdb_client.client.warnings import MissingPivotFunction
from influxdb_client import InfluxDBClient
warnings.simplefilter("ignore", MissingPivotFunction)

def Influx_Pull(T):
    bucket = "Insert_your_bucket"
    my_org = "Insert_your_org"
    my_token = "Insert_your_token"
    # Store the URL of your InfluxDB instance
    url= "Insert_your_url"

    # Set the timeframe and the filter parameters for the query
    query = f'from(bucket: "bucket")\\
    |> range(start: -{T}h)\\
    |> filter(fn: (r) => r["Insert_filter"] == "Insert_filter")\\
    |> aggregateWindow(every: 3m, fn: mean, createEmpty: false)'

    client = InfluxDBClient(url=url, token=my_token, org=my_org)
    # Create a dataframe from the pulled data
    df  = client.query_api().query_data_frame(org=my_org, query=query)")

    return df"""

mongo_query_local = """
import pymongo
myclient_local = pymongo.MongoClient("mongodb://localhost:27017/")
mydb_local = myclient_local["Insert_your_DB"]
mycol_local = mydb_local["Insert_your_col"])
"""

mongo_query_global = """
import pymongo
myclient_global = pymongo.MongoClient("Insert_your_global_client")
mydb_global = myclient_global["Insert_your_DB"]
mycol_global = mydb_global["Insert_your_col"]
"""


if query:
    st.markdown("<style> .big-fonts {font-size:23px !important;} </style>", unsafe_allow_html=True)
    st.subheader('Basic queries from InfluxDB and MongoDB')
    st.markdown('<p class="big-fonts">InfluxDB query</p>', unsafe_allow_html=True)

    st.code(influx_query,language="python")
    
    st.write('Check out this link for more information:  \nhttps://www.influxdata.com/')

    st.markdown('<p class="big-fonts">MongoDB query</p>', unsafe_allow_html=True)

    st.write('**Query from local DB**')

    st.code(mongo_query_local, language="python")

    st.write('**Query from global DB**')
    
    st.code(mongo_query_global, language="python")

    st.write('Check out this link for more information: \nhttps://www.w3schools.com/python/python_mongodb_getstarted.asp')















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
