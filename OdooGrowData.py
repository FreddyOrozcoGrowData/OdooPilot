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
navigation_tree = {
    "Odoo Grow Data": [
        st.Page("main/OdooCRM.py", title="Odoo CRM"),   
        st.Page("main/OdooClientes.py", title="Odoo Clientes")]
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

# Crear una instancia del cliente Odoo /Jau das the Generative AI solution integrit with oder túls and platforms wi currently yus?/
odoo = odoorpc.ODOO(url, port=port, protocol='jsonrpc+ssl')
# Conectarse a la base de datos
odoo.login(db, username, password)
# Verificar la conexión obteniendo el usuario actual
user = odoo.env.user
Username = user.name
ID = str(user.id)
st.write("USERNAME: "+user.name+"")
st.write(ID)
