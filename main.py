from multiprocessing.spawn import import_main_path
import streamlit as st 
import seaborn as sns 
import pandas as pd
import os.path
import pathlib

st.title("Cotiza tu Patrimonio")

add_input_mail = st.sidebar.text_input("Email:",type="default")

st.text("Conoce el valor de tu patrimonio")

tab1, tab2= st.tabs(["Individual","Conjunto"])

with tab1:
    col_form,col_result = st.columns(2)
    with col_form.container():
        with st.form(key="registro-inmueble"):
            fecha = st.date_input("Fecha")
            option_tipo_via = st.selectbox('Tipo de via',["Calle","Jiron","Avenidas","Pasaje","Carretera","Manzana","Lote","Parcela","Fundo", "Sin Via"])
            option_piso = st.selectbox('Piso',["Primero","Segundo",])
            numero_estacionamiento = st.select_slider("Numero de Estacionamientos", options=[0,1,2,3,4,6,7],)
            numero_depositos = st.select_slider("Numero de Depositos", options=[0,1,2,3,4,6,7],)
            #numero_estacionamiento = st.select_slider("Numero de Estacionamientos", options=[0,1,2,3,4,6,7],)
            categoria = st.selectbox('Categoria del Bien',["Departamento","Vivienda Familiar","Local Comercial","Terreno Urbano","Edificación en Construcción","Edificio Comercial","Vehículo","Almacén/Taller","Terreno Rústico", "Oficina","Maquinaria y/o Equipo","Centro Comercial","Muebles y Enseres","Industria","Fundo Agrícola","Estacionamiento/depósito","Emarbacación"])
            numero_frentes = st.select_slider("Número de frentes", options=[1,2,3,4],)
            edad = st.text_input("Edad inmueble")
            elevador = genre = st.radio("Elevador",('Si', 'No',))
            estado_conservacion = st.selectbox('Estado Conservación',["Buen Estado","Regular",])
            metodo_representado = st.selectbox('Método Representado',["Costo o Reposición","Comparación Mercado","Renta o Capitalización"])
            moneda_calculos = st.selectbox('Moneda de la Tasacion',["USD","Soles",])
            area_terreno = st.text_input("Tamaño del Terreno")
            area_edificacion = st.text_input("Tamaño de la edificación")
            st.form_submit_button("Cotizar")
with tab2:
    uploaded_file = st.file_uploader("Seleccionar archivo csv",type=['csv'])
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        data = uploaded_file.getvalue().decode('utf-8').splitlines()         
        st.session_state["preview"] = ''    
        for i in range(0, min(5, len(data))):
            st.session_state["preview"] += data[i]
        df = pd.read_csv(uploaded_file)
        df.to_csv("data/demo.csv")
        st.write(df)
    #preview = st.text_area("CSV Preview", "", height=150, key="preview")
    #upload_state = st.text_area("Upload State", "", key="upload_state")



def upload():
    if uploaded_file is None:
        st.session_state["upload_state"] = "Upload a file first!"
    else:
        data = uploaded_file.getvalue().decode('utf-8')
        parent_path = pathlib.Path(__file__).parent.parent.resolve()           
        save_path = os.path.join(parent_path, "data")
        complete_name = os.path.join(save_path, uploaded_file.name)
        destination_file = open(complete_name, "w")
        destination_file.write(data)
        destination_file.close()
        st.session_state["upload_state"] = "Saved " + complete_name + " successfully!"
        st.button("Upload file to Sandbox", on_click=upload)