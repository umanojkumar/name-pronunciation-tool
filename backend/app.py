import os
import streamlit as st
import numpy as np
from PIL import  Image

from multipage import MultiPage
from pages import your_profile, search_user


app = MultiPage()

app.add_page("Your Profile", your_profile.app)
app.add_page("Search User", search_user.app)

app.run()
