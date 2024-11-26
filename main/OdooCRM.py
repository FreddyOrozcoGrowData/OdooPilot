import streamlit as st
import pandas as pd
import odoorpc

st.title("ODOO CRM")

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

#Consulta oportunidades
lead_ids = odoo.env['crm.lead'].search([])
leads = odoo.env['crm.lead'].read(lead_ids, ['name', 'email_from', 'phone', 'user_id', 'x_studio_linea', 'stage_id', 'team_id', 'x_studio_tipo_de_oportunidad', 'x_studio_edopreventa', 'x_studio_preventa', 'create_date', 'expected_revenue', 'x_studio_consultoria_cop', 'x_studio_datos_cop', 'x_studio_ti_cop', 'x_studio_alcance', 'x_studio_objeto', 'date_deadline', 'x_studio_fecha_efectiva_de_cierre', 'date_closed', 'write_date', 'x_studio_tipo_de_producto', 'x_studio_proyecto', 'won_status', 'write_date'])
 
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
    'Consultoría (COP$)': lead['x_studio_consultoria_cop'],
    'Datos (COP$)': lead['x_studio_datos_cop'],
    'TI (COP$)': lead['x_studio_ti_cop'],
    'Alcance': lead['x_studio_alcance'],
    'Objeto': lead['x_studio_objeto'],
    'Cierre Esperado': lead['date_deadline'],
    'Fecha Efectiva de Cierre': lead['x_studio_fecha_efectiva_de_cierre'],
    'Fecha de Cierre': lead['date_closed'],
    'Última Modificación el': lead['write_date'],
    'Tipo de Cliente': lead['x_studio_tipo_de_producto'],
    'Tipo de Venta': lead['x_studio_proyecto'],
    'Ganado': lead['won_status'],
    'Actualizado': lead['write_date']
    
} for lead in leads]


# Crear un DataFrame a partir de la lista
df_leads = pd.DataFrame(lead_data)
st.dataframe(df_leads)

df_leads['write_date_min'] = pd.to_datetime(df_leads['Actualizado'])

#df_leads['write_date_min'] = df_leads['Actualizado'] - pd.Timedelta(hours=5)

st.dataframe(df_leads)


