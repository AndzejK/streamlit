# https://pfpmaker.com/ - generate a nicer profile pic

from pathlib import Path
import streamlit as st
from PIL import Image # pip install streamlit pillow       

# ---- Path settings ----

# get current dir
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()

# other files based on the current dir
css_file=current_dir / "styles" / "main.css"
cv_file= current_dir / "files" / "cv_krupoves.pdf"
prof_pic= current_dir / "files" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | A. Krupoves"
PAGE_ICON = ":mango:"
NAME = "Andzej Krupoves"
DESCRIPTION = """
Application Support Engineer 💽
"""
EMAIL = "andzejkrupoves@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/krupoves/",
    "GitHub": "https://github.com/AndzejK",
}
PROJECTS = {
    "🏆 Sales Dashboard - ",
    "🏆 Income and Expense Tracker -",
    "🏆 Desktop Application - ",   
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

# ----- LOAD CSS, PDF & Profil PIC -----
with open(css_file) as file: #my_resume/styles/main.css
    st.markdown("<style>{}</style>".format(file.read()),unsafe_allow_html=True)
with open(cv_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
prof_pic=Image.open(prof_pic) 

# ----- Hero section -----
col1,col2=st.columns(2,gap="small")

with col1:
    st.image(prof_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="🌐 Download CV!",
        data=PDFbyte,
        file_name=cv_file.name,
        mime="application/octet-stream"
    )
    st.write(EMAIL)

# ---- Social Links ----