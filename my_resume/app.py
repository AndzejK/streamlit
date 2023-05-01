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
    "🏆 No. 1 - <Name 1>":"https://#",
    "🏆 No. 2 - <Name 2>":"https://#",
    "🏆 No. 3 - <Name 3>":"https://#",   
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
st.write("#")

# based on social media links we determine how manu cols we need
cols=st.columns(len(SOCIAL_MEDIA))

# loop through dictionary
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---- EXPERIENCE & QUALIFICATIONS ----
st.write("#")
st.subheader("Experience & Qualification")
# st.write("---")
st.write(
    """
- ✔️ I have strong communication skills
- ✔️ Experience using Python and a wide variety of its libraries
- ✔️ I possess good technical skills
- ✔️ Excellent team-player
    """
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL
- 🗄️ Databases: Postgres, MSSQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Application Support Engineer | alterDomus**")
st.write("05/2023 - Present")
st.write(
    """
- ► In progress...

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Customer Support Specialist | Revel Systems**")
st.write("08/2022 - 04/2023")
st.write(
    """
- ► Finding common ground between a user and me to set up a particular feature for Pont Of Sale (POS)
- ► Troubleshooting network, primarily LAN
- ► Guiding an end-user on how to set up different card readers (EFT) and troubleshoot them
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")

for project,link in PROJECTS.items():
    st.write(f"[{project}]({link})")