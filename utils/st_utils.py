import os.path
from pathlib import Path
import inspect

import streamlit as st
from st_pages import add_page_title


def initialize_st_page(title: str, icon: str, layout="wide", initial_sidebar_state="collapsed"):
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout=layout,
        initial_sidebar_state=initial_sidebar_state
    )
    caller_frame = inspect.currentframe().f_back

    add_page_title(layout=layout, initial_sidebar_state=initial_sidebar_state)

    current_directory = Path(os.path.dirname(inspect.getframeinfo(caller_frame).filename))
    readme_path = current_directory / "README.md"
    with st.expander("About This Page"):
        st.write(readme_path.read_text())
