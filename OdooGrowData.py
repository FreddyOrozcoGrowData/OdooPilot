import streamlit as st
import pandas as pd
import odoorpc

st.set_page_config(layout='wide')
st.title("ODOO GW")

# Configurar la conexión
url = 'grow-data.odoo.com'
port = 443
db = 'odoo-ps-psus-grow-data-production-4404155'
username = 'freddy.orozco@growdata.com.co'
password = 'd56172461f273e1cde7c202a1ecc248dccd4317d'

# Crear una instancia del cliente Odoo
odoo = odoorpc.ODOO(url, port=port, protocol='jsonrpc+ssl')

# Conectarse a la base de datos
odoo.login(db, username, password)

# Verificar la conexión obteniendo el usuario actual
user = odoo.env.user
#print(f'Conectado como: {user.name} (ID: {user.id})')

st.write("USERNAME: "+user.name+"")
st.write("USERNAME: "+user.id+"")

#st.write("Conectado como: {user.name} (ID: {user.id})")
