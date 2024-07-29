# -*- coding: utf-8 -*-
"""
Created on Mon Jul  29 16:30:41 2024

@author: Freddy J. Orozco R.
@Powered: Grow Data SAS
"""

import streamlit as st
st.set_page_config(layout="wide")
navigation_tree = {
    "Main": [
        st.Page("main/OdooCRM.py", title="Odoo CRM"),   
        st.Page("main/OdooClientes.py", title="Odoo Clientes")]
}

nav = st.navigation(navigation_tree, position="sidebar")
nav.run()

with sidebar:
    st.title("GROW DATA")
