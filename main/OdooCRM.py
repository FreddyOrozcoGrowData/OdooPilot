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
#lead_ids = odoo.env['crm.lead'].search([])
lead_ids = odoo.env['crm.lead'].with_context(active_test=False).search([])

#st.write(lead_ids)
leads = odoo.env['crm.lead'].read(lead_ids, ['active', 'name', 'email_from', 'phone', 'partner_id', 'user_id', 'x_studio_linea', 'stage_id', 'team_id', 'x_studio_tipo_de_oportunidad', 'x_studio_edopreventa', 'x_studio_preventa', 'create_date', 'expected_revenue', 'x_studio_consultoria_cop', 'x_studio_datos_cop', 'x_studio_ti_cop', 'x_studio_alcance', 'x_studio_objeto', 'date_deadline', 'x_studio_fecha_efectiva_de_cierre', 'date_closed', 'write_date', 'x_studio_tipo_de_producto', 'x_studio_proyecto', 'won_status', 'write_date'])


lead_data = [{
 'ID': lead['id'],
 'Activo': lead['active'],
 'Nombre': lead['name'],
 'Correo': lead['email_from'],
 'Teléfono': lead['phone'],
 'Cliente': lead['partner_id'][1] if lead['partner_id'] else '',
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

#Ajuste (GMT-5)
df_leads['Actualizado'] = pd.to_datetime(df_leads['Actualizado'], errors='coerce')
df_leads['write_date_min'] = df_leads['Actualizado'] - pd.Timedelta(hours=5)

filtop01, filtop02, filtop03, filtop04, filtop05, filtop06 = st.columns(6)
with filtop01:
 ListComercial = df_leads['Comercial'].drop_duplicates().tolist()
 ListComercial.insert(0, "ALL")
 FilterComercialSel = st.selectbox('Comercial:', ListComercial)
 df_leads_bk = df_leads
 if FilterComercialSel == 'ALL':
  df_leads = df_leads_bk
 else:
  df_leads = df_leads[df_leads['Comercial'] == FilterComercialSel].reset_index(drop=True)
  
with filtop02:
 ListLinea = df_leads['Línea'].drop_duplicates().tolist()
 ListLinea.insert(0, "ALL")
 FilterLineaSel = st.selectbox('Línea:', ListLinea)
 df_leads_bk2 = df_leads
 if FilterLineaSel == 'ALL':
  df_leads = df_leads_bk2
 else:
  df_leads = df_leads[df_leads['Línea'] == FilterLineaSel].reset_index(drop=True)
 
with filtop03:
 ListTipoOport = df_leads['Tipo Oportunidad'].drop_duplicates().tolist()
 ListTipoOport.insert(0, "ALL")
 FilterTipoOportSel = st.selectbox('Oportunidad:', ListTipoOport)
 df_leads_bk3 = df_leads
 if FilterTipoOportSel == 'ALL':
  df_leads = df_leads_bk3
 else:
  df_leads = df_leads[df_leads['Tipo Oportunidad'] == FilterTipoOportSel].reset_index(drop=True)

with filtop04:
 ListEquipoVenta = df_leads['Equipo de Ventas'].drop_duplicates().tolist()
 ListEquipoVenta.insert(0, 'ALL')
 FilterEquipoVentaSel = st.selectbox('Equipo Ventas:', ListEquipoVenta)
 df_leads_bk4 = df_leads
 if FilterEquipoVentaSel == 'ALL':
  df_leads = df_leads_bk4
 else:
  df_leads = df_leads[df_leads['Equipo de Ventas'] == FilterEquipoVentaSel].reset_index(drop=True)

with filtop05:
 ListPreventa = df_leads['Preventa Asignado'].drop_duplicates().tolist()
 ListPreventa.insert(0, 'ALL')
 FilterPreventaSel = st.selectbox('Preventa:', ListPreventa)
 df_leads_bk5 = df_leads
 if FilterPreventaSel == 'ALL':
  df_leads = df_leads_bk5
 else:
  df_leads = df_leads[df_leads['Preventa Asignado'] == FilterPreventaSel].reset_index(drop=True)

with filtop06:
 ListActive = df_leads['Activo'].drop_duplicates().tolist()
 ListActive.insert(0, 'ALL')
 FilterActiveSel = st.selectbox('Activo:', ListActive)
 df_leads_bk6 = df_leads
 if FilterActiveSel == 'ALL':
  df_leads = df_leads_bk6
 else:
  df_leads = df_leads[df_leads['Activo'] == FilterActiveSel].reset_index(drop=True)

st.dataframe(df_leads)

dfT = len(df_leads)
dfLU = df_leads['Actualizado'].max()
# Convertir a string legible
#dfLU = dfLU.strftime('%Y-%m-%d %H:%M:%S')
dfLU = dfLU.strftime('%Y-%m-%d')
dfIE = sum(df_leads['Ingresos Esperados'])


metricop01, metricop02, metricop03, metricop04, metricop05 = st.columns(5)

with metricop01:
 st.metric("LAST UPDATE", dfLU)
with metricop02:
 st.metric("LEADS", dfT)
#with metricop03:
 #st.metric("INGRESOS", dfIE)


st.divider()

df_leads_fil = df_leads.iloc[0, :]

st.dataframe(df_leads_fil)

X = df_leads_fil['Nombre']
st.write(X)

if '\n' in X:
    st.write("Contiene salto de línea")
