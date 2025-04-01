def balancear_combustion(fórmula):
    # Paso 1: Parsear la fórmula para extraer los valores de C (carbono) y H (hidrógeno)
    if 'C' in fórmula and 'H' in fórmula:
        # Extraer los números de C y H de la fórmula
        c_count = int(fórmula.split('C')[1].split('H')[0]) if 'C' in fórmula else 1
        h_count = int(fórmula.split('H')[1]) if 'H' in fórmula else 2
        
    # Si no está definida la fórmula, no se puede balancear.
    else:
        return "Fórmula no válida"

    # Paso 2: Balancear la reacción
    # La reacción general es: CₙH₂ₙ₊₂ + O₂ → CO₂ + H₂O
    # 1. Balancear los carbonos:
    #    El número de CO₂ debe ser igual al número de carbonos en el compuesto.
    co2_coef = c_count
    
    # 2. Balancear los hidrógenos:
    #    El número de H₂O debe ser igual a la mitad del número de hidrógenos en el compuesto.
    h2o_coef = h_count // 2
    
    # 3. Balancear el oxígeno:
    #    El número de átomos de oxígeno en los productos (CO₂ y H₂O) debe ser igual al número de átomos de oxígeno en O₂.
    #    Cada CO₂ aporta 2 oxígenos y cada H₂O aporta 1 oxígeno.
    o2_coef = (co2_coef * 2 + h2o_coef) / 2
    
    # Paso 3: Mostrar la ecuación balanceada
    return f"{fórmula} + {o2_coef}O₂ → {co2_coef}CO₂ + {h2o_coef}H₂O"

# Ejemplo de uso para un alcano (C₄H₁₀ - butano)
compuesto = "C4H10"
resultado = balancear_combustion(compuesto)
print(f"Reacción balanceada: {resultado}")

# Prueba con otro compuesto (C₂H₄ - eteno)
compuesto = "C2H4"
resultado = balancear_combustion(compuesto)
print(f"Reacción balanceada: {resultado}")
