# https://pfpmaker.com/ - generate a nicer profile pic

from pathlib import Path
import streamlit as st
from PIL import Image # pip install streamlit pillow       

# ---- Path settings ----

# get current dir
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()

# other files based on the current dir
css_file=current_dir / "styles" / "main.css"
cv_file= current_dir / "files" / "CV.docx"
prof_pic= current_dir / "files" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Andzej Krupoves"
PAGE_ICON = ":wave:"
NAME = "Andzej Krupoves"
DESCRIPTION = """
Application Support Engineer.
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