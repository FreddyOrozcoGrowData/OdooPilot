# -*- coding: utf-8 -*-
"""
Created on Mon Jul  29 16:30:41 2024

@author: Freddy J. Orozco R.
@Powered: Grow Data SAS
"""

import streamlit as st
st.set_page_config(layout="wide")
navigation_tree = {
    "Odoo Grow Data": [
        st.Page("main/OdooCRM.py", title="Odoo CRM"),   
        st.Page("main/OdooClientes.py", title="Odoo Clientes")]
}

nav = st.navigation(navigation_tree, position="sidebar")
nav.run()

st.sidebar.title("GROWDATA")
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
