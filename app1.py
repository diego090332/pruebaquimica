import sympy as sp

def balancear_combustion(fórmula):
    # Analizar los compuestos en la fórmula de entrada
    if fórmula.lower().startswith("c") and 'h' in fórmula.lower():
        # Obtener los valores de C y H en la fórmula (asumiendo que es un alcano, alqueno o alquino)
        # Alcanos: CnH2n+2, Alquenos: CnH2n, Alquinos: CnH2n-2
        
        # Extract number of Carbon (C) and Hydrogen (H)
        c_count = int(fórmula.split('C')[1].split('H')[0]) if 'C' in fórmula else 1
        h_count = int(fórmula.split('H')[1]) if 'H' in fórmula else 2
        
        # Definir los incógnitas para el balanceo de la ecuación
        a, b, c = sp.symbols('a b c')  # a es el coeficiente del compuesto orgánico, b el de O2, y c el de CO2

        # Balanceo de la ecuación de combustión
        # Fórmula general: CxHy + O2 -> CO2 + H2O
        ecuaciones = [
            a * c_count - c,  # Balance de Carbono
            a * h_count - 2 * b,  # Balance de Hidrógeno
            2 * b - 2 * c  # Balance de Oxígeno
        ]

        # Resolver el sistema de ecuaciones
        soluciones = sp.linsolve(ecuaciones, a, b, c)

        return soluciones

# Ejemplo de uso para un alcano (C₄H₁₀)
compuesto = "C4H10"
resultados = balancear_combustion(compuesto)

print(f"Resultado del balanceo: {resultados}")
