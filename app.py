import streamlit as st
import random

# Datos de los elementos de la tabla periódica con su grupo y familia
elementos = {
    'Hidrógeno': {'grupo': 1, 'familia': 'No metales'},
    'Helio': {'grupo': 18, 'familia': 'Gases nobles'},
    'Litio': {'grupo': 1, 'familia': 'Metales alcalinos'},
    'Berilio': {'grupo': 2, 'familia': 'Metales alcalinotérreos'},
    'Boro': {'grupo': 13, 'familia': 'Metales del grupo 13'},
    'Carbono': {'grupo': 14, 'familia': 'No metales'},
    'Nitrógeno': {'grupo': 15, 'familia': 'No metales'},
    'Oxígeno': {'grupo': 16, 'familia': 'No metales'},
    'Flúor': {'grupo': 17, 'familia': 'Halógenos'},
    'Neón': {'grupo': 18, 'familia': 'Gases nobles'},
    # Agregar más elementos según se desee
}

# Función para seleccionar un nuevo ejercicio
def nuevo_ejercicio():
    elemento = random.choice(list(elementos.keys()))
    info_elemento = elementos[elemento]
    return elemento, info_elemento

# Función para mostrar el quiz
def quiz():
    st.title("Quiz sobre la Tabla Periódica")
    st.write("Responde las preguntas sobre el grupo y familia de los elementos de la tabla periódica.")
    
    # Generar un nuevo ejercicio al inicio o al hacer clic en el botón
    if 'elemento_actual' not in st.session_state:
        st.session_state.elemento_actual, st.session_state.info_elemento = nuevo_ejercicio()

    # Preguntar al usuario sobre el grupo y la familia del elemento actual
    st.write(f"**Elemento:** {st.session_state.elemento_actual}")
    
    respuesta_grupo = st.text_input(f"¿A qué grupo pertenece {st.session_state.elemento_actual}?")
    respuesta_familia = st.text_input(f"¿A qué familia pertenece {st.session_state.elemento_actual}?")

    if st.button("Verificar respuesta"):
        # Verificar las respuestas
        correcto_grupo = str(st.session_state.info_elemento['grupo']) == respuesta_grupo
        correcto_familia = st.session_state.info_elemento['familia'].lower() == respuesta_familia.lower()

        if correcto_grupo and correcto_familia:
            st.success("¡Respuesta correcta!")
        else:
            if not correcto_grupo:
                st.error(f"Grupo incorrecto. El grupo correcto es {st.session_state.info_elemento['grupo']}.")
            if not correcto_familia:
                st.error(f"Familia incorrecta. La familia correcta es {st.session_state.info_elemento['familia']}.")

    if st.button("Generar nuevo ejercicio"):
        st.session_state.elemento_actual, st.session_state.info_elemento = nuevo_ejercicio()

# Llamar a la función para iniciar el quiz
quiz()
