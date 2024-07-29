import streamlit as st
import pandas as pd
import odoorpc

st.title("ODOO MODEL FIELDS")

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

#Crear filtro
menuopt01, menuopt02, menuopt03 = st.columns(3)
with menuopt01:
    ModelOptions = ['CRM', 'Partner']
    ModelSel = st.selectbox("Seleccionar modelo:", ModelOptions)
with menuopt02:
    DataTypeOptions = ['datetime', 'boolean', 'many2one', 'date', 'selection', 'char', 'float', 'integer', 'html', 'many2many', 'monetary', 'one2many', 'text']
    DataTypeSel = st.selectbox("Seleccionar tipo de datos:", DataTypeOptions)
    
if ModelSel == 'CRM':

    # Obtener todos los campos del modelo crm.lead
    fields = odoo.env['crm.lead'].fields_get()
    # Crear una lista para almacenar la información de los campos
    field_info = []
    # Iterar sobre los campos y extraer toda la información
    for field_name, field_data in fields.items():
        field_info.append({
            'Nombre': field_name,
            **field_data  # Esto incluirá todos los atributos del campo
        })
    # Crear un DataFrame con la información de los campos
    df_fields = pd.DataFrame(field_info)
    # Ordenar el DataFrame por el nombre del campo
    df_fields = df_fields.sort_values('Nombre')
    # Mostrar el DataFrame
    df_fields = df_fields[df_fields['type'] == DataTypeSel].reset_index(drop=True)
    st.dataframe(df_fields)
    
elif ModelSel == 'Partner':

    # Obtener todos los campos del modelo res.partner
    fields = odoo.env['res.partner'].fields_get()
    
    # Crear una lista para almacenar la información de los campos
    field_info = []
    
    # Iterar sobre los campos y extraer información relevante
    for field_name, field_data in fields.items():
        field_info.append({
            'Nombre': field_name,
            'Tipo': field_data.get('type'),
            'String': field_data.get('string'),
            'Ayuda': field_data.get('help'),
            'Requerido': field_data.get('required', False),
            'Readonly': field_data.get('readonly', False),
        })
    
    # Crear un DataFrame con la información de los campos
    df_fields = pd.DataFrame(field_info)
    
    # Ordenar el DataFrame por el nombre del campo
    df_fields = df_fields.sort_values('Nombre')
    
    # Mostrar el DataFrame usando Streamlit
    st.dataframe(df_fields)
    
