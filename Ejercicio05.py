#Laboratorio N° 21 - Ejercicio 05
#Autor: Andrea Camargo
#Colaboro: 
#Tiempo: 20 minutos

class OperadorInvalidoError(Exception):
    pass

def calcular(operacion_str):
    operadores = ['+', '-', '*', '/']
    try:
        operador_encontrado = None
        for op in operadores:
            if op in operacion_str:
                operador_encontrado = op
                break 
            
        if not operador_encontrado:
            raise OperadorInvalidoError("Operador no reconocido o formato inválido.")

        partes = operacion_str.split(operador_encontrado)
        
        if len(partes) != 2:
            return "Error: Formato debe ser 'numero operador numero'"

        n1 = float(partes[0].strip())
        n2 = float(partes[1].strip())
        
        if operador_encontrado == '+': return n1 + n2
        if operador_encontrado == '-': return n1 - n2
        if operador_encontrado == '*': return n1 * n2
        if operador_encontrado == '/':
            if n2 == 0: raise ZeroDivisionError
            return n1 / n2

    except ValueError:
        return "Error: Los valores deben ser números válidos."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."
    except OperadorInvalidoError as e:
        return f"Error: {e}"
    except IndexError:
        return "Error: Formato incompleto."

print(f"Resultado: {calcular('10 / 2')}")   
print(f"Resultado: {calcular('10 / 0')}")   
print(f"Resultado: {calcular('hola + 5')}") 
print(f"Resultado: {calcular('10 % 2')}")   