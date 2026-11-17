
def sumar(a, b): 
    """
        Suma dos numeros y devuelve la suma de ambos
        :param int a: Numero 1
        :param int b: Numero 2
        :return suma de las variables a y b
        :rtype int de la suma de las variables a y b
        :raises ValueError si algún parametro no es un numero entero
    """
    return a + b

def restar(a, b): 
    """
        Resta dos numeros y devuelve el total de ambos
        :param int a: Numero 1
        :param int b: Numero 2
        :return resta de las variables a y b
        :rtype int devuelve la resta de las variables a y b
        :raises ValueError si algún parametro no es un numero entero
    """
    return a - b

def multiplicar(a, b): 
    """
        Multiplica dos numeros y devuelve el total de ambos
        :param int a: Numero1
        :param int b: Numero2
        :return int de la multiplicacion de las variables a y b
        :raises ValueError si algún parametro no es un numero entero
    """    
    return a * b

def dividir(a, b):
    """
        Divide dos numeros y devuelve el cociente de ambos
        :param int a: Numero 1
        :param int b: Numero 2
        :return int de las variables a y b
        :rtype int del cociente de las variables a y b
        :raises ValueError si algún parametro no es un numero entero
    """
    if b == 0: raise ValueError("No se puede dividir entre cero")
    return a / b