import streamlit as st
from streamlit_option_menu import option_menu
import classifier
import home
import contact


st.write('### Mechanical Parts Classifier')
st.write('##### This page created by [Abi Sugiri](https://github.com/abisugiri)')
st.markdown('---')


selected = option_menu(None, ["Home", "Classifier","Contact"], 
    icons=['house', 'gear-fill', 'envelope-at-fill'], 
    menu_icon="cast", default_index=0, orientation="vertical",
    styles={
        "icon": {"color": "yellow", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"1px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "grey"},
    }
)
    
selected
    

if selected == 'Classifier':
    classifier.run()

elif selected == 'Home':
    home.run()
else:
    contact.run()