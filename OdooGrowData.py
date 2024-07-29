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

Username = user.name


st.write("USERNAME: "+user.name+"")
st.write(user.id)

#st.write("Conectado como: {user.name} (ID: {user.id})")



# Crear una lista vacía para almacenar los datos de los leads
lead_data = []

# Buscar todos los leads
leads = odoo.env['crm.lead'].search([])

# Iterar sobre los leads y agregar los datos a la lista
for lead_id in leads:
    lead = odoo.env['crm.lead'].browse(lead_id)
    lead_data.append({
        'ID': lead.id,
        'Nombre': lead.name,
        'Correo': lead.email_from,
        'Teléfono': lead.phone,
        'Etapa': lead.stage_id.name if lead.stage_id else '',
        'Equipo de Ventas': lead.team_id.name if lead.team_id else '',
        'Fecha de Creación': lead.create_date,
        'Ingresos Esperados': lead.expected_revenue,
    })

# Crear un DataFrame a partir de la lista
df_leads = pd.DataFrame(lead_data)
st.dataframe(df_leads)
