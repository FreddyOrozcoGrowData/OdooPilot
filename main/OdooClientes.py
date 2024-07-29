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

# Crear una instancia del cliente Odoo /Jau das the Generative AI solution integrit with oder túls and platforms wi currently yus?/
odoo = odoorpc.ODOO(url, port=port, protocol='jsonrpc+ssl')
# Conectarse a la base de datos
odoo.login(db, username, password)
# Verificar la conexión obteniendo el usuario actual
user = odoo.env.user
Username = user.name
st.write("USERNAME: "+user.name+"")
st.write(user.id)

lead_ids = odoo.env['crm.lead'].search([])
leads = odoo.env['crm.lead'].read(lead_ids, ['name', 'email_from', 'phone', 'user_id', 'x_studio_linea', 'stage_id', 'team_id', 'x_studio_tipo_de_oportunidad', 'x_studio_edopreventa', 'x_studio_preventa', 'create_date', 'expected_revenue'])

lead_data = [{
    'ID': lead['id'],
    'Nombre': lead['name'],
    'Correo': lead['email_from'],
    'Teléfono': lead['phone'],
    'Comercial': lead['user_id'][1] if lead['user_id'] else '',
    'Línea': lead['x_studio_linea'],
    'Etapa': lead['stage_id'][1] if lead['stage_id'] else '',
    'Equipo de Ventas': lead['team_id'][1] if lead['team_id'] else '',
    'Tipo Oportunidad': lead['x_studio_tipo_de_oportunidad'],
    'Etapa Preventa': lead['x_studio_edopreventa'],
    'Preventa Asignado': lead['x_studio_preventa'][1] if lead['x_studio_preventa'] else '',
    'Fecha de Creación': lead['create_date'],
    'Ingresos Esperados': lead['expected_revenue'],
} for lead in leads]

# Crear un DataFrame a partir de la lista
df_leads = pd.DataFrame(lead_data)
st.dataframe(df_leads)
