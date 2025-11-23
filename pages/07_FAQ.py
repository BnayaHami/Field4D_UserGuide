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


st.title('Frequently asked questions')

st.markdown("<style> .big-fonts {font-size:18spx !important;} </style>", unsafe_allow_html=True)
st.markdown('<p class="big-fonts">Note: if you cannot see the pictures you can open them in a new tab</p>', unsafe_allow_html=True)

st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: 30px;
    font-weight:bold;
}
</style>
""" ,unsafe_allow_html=True,)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:25px;
    }
</style>
'''

st.write(css, unsafe_allow_html=True)


with st.expander('Downloading Uniflash software'):
    st.markdown("<style> .big-font {font-size:19px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Here are the steps for downloading and installing Uniflash</p>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['1', '2', '3', '4', '5'])
    with tab1:
        st.markdown("<style> .big-font {font-size:19px !important;} </style>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Open the following link:</p>', unsafe_allow_html=True)
        st.write('https://www.ti.com/tool/UNIFLASH')
    with tab2:
        st.markdown("<style> .big-font {font-size:19px !important;} </style>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Press on "Downloads"</p>', unsafe_allow_html=True)
        st.image(f'FAQ//ti1.png')
    with tab3:
        st.markdown("<style> .big-font {font-size:19px !important;} </style>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Press on "Download options"</p>', unsafe_allow_html=True)
        st.image(f'FAQ//ti2.png')
    with tab4:
        st.markdown("<style> .big-font {font-size:19px !important;} </style>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Choose the option suitable for you</p>', unsafe_allow_html=True)
        st.image(f'FAQ//ti3.png')
    with tab5:
        st.markdown('<p class="big-font">Follow the wizard instructions for the installation</p>', unsafe_allow_html=True)



with st.expander('Writing error on Uniflash'):
    st.markdown("<style> .big-font {font-size:19px !important;} </style>", unsafe_allow_html=True)
    st.markdown('<p class="big-font">if you are getting the following error while writing the SensorTag/LaunchPad:</p>', unsafe_allow_html=True)
    st.image(f'FAQ//debug.png')
    st.markdown('<p class="big-font">Press "Update"</p>', unsafe_allow_html=True)

st.subheader('Field4D Scheme')
st.image(f'FAQ//Scheme.png', width=800)

st.markdown('<p class="big-font"><b>CC2650stk SensorTag maintenance guide</b></p>', unsafe_allow_html=True)

expander12 = st.expander('Click here to see')
expander12.write("[Open diagram](https://lucid.app/lucidchart/784465cf-0a03-4a48-8277-246ab823b96d/edit?viewport_loc=-401%2C756%2C3508%2C1471%2C0_0&invitationId=inv_e8557cd7-15f1-42a3-9ec2-51cbf389e78f)")

expander13 = st.expander("Click here to see")
expander13.markdown(
    """
    <a href="https://lucid.app/lucidchart/784465cf-0a03-4a48-8277-246ab823b96d/edit?invitationId=inv_e8557cd7-15f1-42a3-9ec2-51cbf389e78f"
       target="_blank"
       style="font-size:18px;">
       Open diagram (new tab)
    </a>
    """,
    unsafe_allow_html=True
)

expander14 = st.expander("Click here to see")
expander14.markdown(
    """
    <a href="https://lucid.app/lucidchart/784465cf-0a03-4a48-8277-246ab823b96d/edit?invitationId=inv_e8557cd7-15f1-42a3-9ec2-51cbf389e78f&page=0_0"
       target="_blank"
       style="font-size:18px; color:#1f77b4;">
       Open diagram (new tab)
    </a>
    """,
    unsafe_allow_html=True,
)

# expander1 = st.expander('Downloading Uniflash')
# expander1.tab1.write('Downloading Uniflash')


# from streamlit_image_select import image_select
# img = image_select(label = "Tutorial",
#                    images = 
#                    ["fieldarray.png",
#                     "fieldarray.png",
#                     "fieldarray.png","fieldarray.png",
#                     "fieldarray.png",
#                     "fieldarray.png"],
#                     use_container_width=False)
# st.image(img)

# pip install streamlit-carousel

# from streamlit_carousel import carousel

# test_items = [
#     dict(
#         title="Slide 1",
#         text="A tree in the savannah",
#         interval=None,
#         img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
#     ),
#     dict(
#         title="Slide 2",
#         text="A wooden bridge in a forest in Autumn",
#         img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
#     ),
#     dict(
#         title="Slide 3",
#         text="A distant mountain chain preceded by a sea",
#         img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
#     ),
# ]

# carousel(items=test_items, width=1)














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
