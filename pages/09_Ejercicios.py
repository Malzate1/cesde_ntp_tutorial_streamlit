import streamlit as st
import random

st.subheader("Ejercicio 1: Saludo Simple")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"¡Bienvenido, {nombre}!")

st.divider()

st.subheader("Ejercicio 2: Calculadora de Producto")

num1=st.number_input("Ingresa un número:" , step=None)
num2=st.number_input("Ingresa otro número:", step=None)

resultado= num1*num2
st.write(f"El resultado de la multiplicacion de los dos números es **{resultado}**")

if num1>100 or num2>100:
    st.warning("Números grandes")

st.divider()

st.subheader("Ejercicio 3: Convertidor de Temperatura (Radio Buttons)")

conversion= st.radio("Qué tipo de conversión quieres?",
                     ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
temp= st.number_input("Ingresa la temperatura: ", step=None)

if conversion == "Celsius a Fahrenheit":
    resultado = (temp * 9/5) + 32
    st.write(f"{temp}°C equivale a **{resultado}°F**")
else:
    resultado = (temp - 32) * 5/9
    st.write(f"{temp}°F equivale a **{resultado}°C**")

st.divider()

st.subheader("Ejercicio 4: Galerí­a de Mascotas (Tabs)")

tab1,tab2,tab3=st.tabs(["🐱 Gatos", "🐶 Perros", "🐦 Aves"])

with tab1:
    st.image("https://www.zooplus.es/magazine/wp-content/uploads/2020/12/Gato-ex%C3%B3tico-2.webp",
             caption="Un gatito coqueto", width=300)
    if st.button("Me gusta 🐱"):
        st.toast("Te gusta esta mascota")

with tab2:
    st.image("https://content.elmueble.com/medio/2024/05/17/grifon-de-bruselas_fd0e0b64_240517193611_1000x750.jpg",
             caption="Perrito gruñon",width=300)
    if st.button("Me gusta 🐶"):
        st.toast("Te gusta esta mascota")

with tab3:
    st.image("https://i0.wp.com/birdscolombia.com/wp-content/uploads/2016/03/rupicola-peruvianus.jpg?fit=919%2C1200&ssl=1",
             caption="Impajaritable de mirar un gallito de roca",width=300)
    if st.button("Me gusta 🐦"):
        st.toast("Te gusta esta mascota")

st.divider()

st.subheader("Ejercicio 5: Caja de Comentarios (Formulario)")

with st.form("Formulario con comentarios"):
    asunto=st.text_input("Asunto:")
    mensaje=st.text_area("Mensaje:")
    envio=st.form_submit_button("Enviar")

if envio:
    if mensaje == "":
        st.error("El mensaje no puede estar vacío")
    else:
        st.success("¡Formulario enviado!")
        st.json({
            "Asunto": asunto,
            "Mensaje": mensaje
        })

st.divider()

st.subheader("Ejercicio 6: Login Simulado (Session State)")

if "logueado" not in st.session_state:
    st.session_state.logueado= False

if st.session_state.logueado:
    st.success("Bienvenido admin!")
    if st.button("Cerrar sesión."):
        st.session_state.logueado= False
        st.rerun()

else:
    usuario = st.text_input("Usuario")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if usuario == "admin" and contrasena == "1234":
            st.session_state.logueado=True
            st.rerun()
        else:
            st.error("Credenciales incorrectas")

st.divider()

st.subheader("Ejercicio 7:Lista de Compras (Session State)")

if "producto" not in st.session_state:
    st.session_state.producto=[]

nuevo_producto = st.text_input("Nuevo producto", key="input_producto")

if st.button("Agregar producto") and nuevo_producto:
    st.session_state.producto.append(nuevo_producto)
    st.success(f"Producto '*{nuevo_producto}*' agregado!")

st.write("### Tus productos:")
for i, producto in enumerate(st.session_state.producto):
    st.write(f"{i + 1}. {producto}")

if st.button("Limpiar lista"):
    st.session_state.producto = []
    st.rerun()

st.divider()

st.subheader("Ejercicio 8: Gráfico Interactivo")

N= st.slider("Cantidad de números", min_value=10 , max_value=100 , value= 50)

datos = [random.randint(1, 100) for _ in range(N)]

st.line_chart(datos)

if st.button("Regenerar"):
    st.rerun()






