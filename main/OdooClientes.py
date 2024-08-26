import streamlit as st
import pandas as pd
import odoorpc

st.title("ODOO CLIENTES")

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

# Buscar los IDs de los partners
partner_ids = odoo.env['res.partner'].search([])

# Leer los datos de los partners
partners = odoo.env['res.partner'].read(partner_ids, [
    'name', 'email', 'phone', 'mobile', 'user_id', 'company_type', 
    'country_id', 'city', 'street', 'vat', 'create_date'
])

# Crear una lista de diccionarios con los datos de los partners
partner_data = [{
    'ID': partner['id'],
    'Nombre': partner['name'],
    'Correo': partner['email'],
    'Teléfono': partner['phone'],
    'Móvil': partner['mobile'],
    'Comercial': partner['user_id'][1] if partner['user_id'] else '',
    'Tipo de Compañía': partner['company_type'],
    'País': partner['country_id'][1] if partner['country_id'] else '',
    'Ciudad': partner['city'],
    'Dirección': partner['street'],
    'NIF/CIF': partner['vat'],
    'Fecha de Creación': partner['create_date'],
} for partner in partners]

# Crear un DataFrame a partir de la lista
df_partners = pd.DataFrame(partner_data)

# Mostrar el DataFrame en Streamlit
st.dataframe(df_partners)
