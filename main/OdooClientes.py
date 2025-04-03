#!/usr/bin/env python
# coding: utf-8

# ## Odoo_Clientes
# 
# New notebook

# # Clientes desde Odoo

# # Importar Librerias

# In[1]:


#get_ipython().system('pip install odoorpc')
import pandas as pd
import odoorpc
import csv


# # Configurar Conexión

# In[2]:


# Configurar la conexión
url = 'grow-data.odoo.com'
port = 443
db = 'odoo-ps-psus-grow-data-production-4404155'
username = 'freddy.orozco@growdata.com.co'
password = 'd56172461f273e1cde7c202a1ecc248dccd4317d'


# # Crear Instancia

# In[3]:


# Crear una instancia del cliente Odoo
odoo = odoorpc.ODOO(url, port=port, protocol='jsonrpc+ssl')
# Conectarse a la base de datos
odoo.login(db, username, password)
# Verificar la conexión obteniendo el usuario actual
user = odoo.env.user


# # Busqueda de los IDs parthers

# In[4]:


# Buscar los IDs de los partners
partner_ids = odoo.env['res.partner'].search([])
 
# Leer los datos de los partners
partners = odoo.env['res.partner'].read(partner_ids, [
    'display_name', 'email', 'phone', 'company_type', 
    'country_id', 'city', 'vat', 'write_date'
])
 
# Crear una lista de diccionarios con los datos de los partners
partner_data = [{
    'ID': partner['id'],
    'Nombre Público': partner['display_name'],
    'Correo': partner['email'],
    'Teléfono': partner['phone'],
    'Tipo de Compañía': partner['company_type'],
    'País': partner['country_id'][1] if partner['country_id'] else '',
    'Ciudad': partner['city'],
    'NIT': partner['vat'],
    'Actualizado_Original': partner['write_date']
} for partner in partners]
 
# Crear un DataFrame a partir de la lista
df_partners = pd.DataFrame(partner_data)

#Ajuste (GMT-5)
df_partners['Actualizado_Original'] = pd.to_datetime(df_partners['Actualizado_Original'], errors='coerce')
df_partners['Actualizado'] = df_partners['Actualizado_Original'] - pd.Timedelta(hours=5)
# st.dataframe(df_partners)


# Mostrar el DataFrame
print(df_partners)

# Crear un archivo CSV apartir del dataframe

df_partners.to_csv("abfss://GrowData_Gestion@onelake.dfs.fabric.microsoft.com/Odoo.Lakehouse/Files/ClientesOdoo.csv")

# leer un archivo CSV apartir del dataframe

#df_partners = spark.read.csv("abfss://GrowData_Gestion@onelake.dfs.fabric.microsoft.com/Odoo.Lakehouse/Files/ClientesOdoo.csv")

# Reemplazar datos

#df_partners.write.mode("overwrite").format("delta").saveAsTable("ClientesOdoo")

