# -*- coding: utf-8 -*-
"""
Created on Mon Jul  29 16:30:41 2024
@author: Freddy J. Orozco R.
@Powered: Grow Data SAS
"""

import streamlit as st
import pandas as pd
import odoorpc

st.set_page_config(layout="wide")

st.logo("Resources/Img/growdata_logo-removebg-preview.png")

navigation_tree = {
    "Odoo Data": [
        st.Page("main/OdooCRM.py", title="Odoo CRM", icon=":material/quick_reference_all:"),   
        st.Page("main/OdooClientes.py", title="Odoo Clientes", icon=":material/group:"),
        st.Page("main/OdooFields.py", title="Odoo Fields", icon=":material/data_check:")]
}

nav = st.navigation(navigation_tree, position="sidebar")
nav.run()

st.sidebar.title("GROWDATA")

# Configurar la conexión
url = 'grow-data.odoo.com'
port = 443
db = 'odoo-ps-psus-grow-data-production-4404155'
username = 'freddy.orozco@growdata.com.co'
password = 'd56172461f273e1cde7c202a1ecc248dccd4317d'

# Crear una instancia del cliente Odoo /
odoo = odoorpc.ODOO(url, port=port, protocol='jsonrpc+ssl')
# Conectarse a la base de datos
odoo.login(db, username, password)
# Verificar la conexión obteniendo el usuario actual
user = odoo.env.user
USERNAME = user.name
ID = str(user.id)
st.sidebar.write("USER: "+USERNAME+"")
st.sidebar.write("ID: "+ID+"")
