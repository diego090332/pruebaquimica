import streamlit as st

def balancear_combustion(fórmula):
    # Parsear la fórmula para extraer los valores de C (carbono) y H (hidrógeno)
    if 'C' in fórmula and 'H' in fórmula:
        # Extraer los números de C y H de la fórmula
        c_count = int(fórmula.split('C')[1].split('H')[0]) if 'C' in fórmula else 1
        h_count = int(fórmula.split('H')[1]) if 'H' in fórmula else 2
    else:
        return "Fórmula no válida"

    # Balanceo de la reacción
    # 1. Balancear los carbonos:
    co2_coef = c_count
    
    # 2. Balancear los hidrógenos:
    h2o_coef = h_count // 2
    
    # 3. Balancear el oxígeno:
    o2_coef = (co2_coef * 2 + h2o_coef) / 2
    
    # Formato de la ecuación balanceada
    return f"{fórmula} + {o2_coef}O₂ → {co2_coef}CO₂ + {h2o_coef}H₂O"

# Título de la aplicación
st.title("Balanceador de Reacción de Combustión de Hidrocarburos")

# Ingreso de la fórmula del compuesto
fórmula = st.text_input("Ingresa la fórmula química (ejemplo: C4H10):")

if fórmula:
    resultado = balancear_combustion(fórmula)
    st.write(f"Ecuación balanceada: {resultado}")
else:
    st.write("Ingresa una fórmula para balancear la reacción.")
