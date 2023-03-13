from sympy import sympify, symbols, Function
x= symbols('x')

def biseccion(f, a, b, tol):
    """
    Implementación del método de bisección de Bolzano.

    :param f: Función a la que se le buscará la raíz.
    :param a: Extremo izquierdo del intervalo.
    :param b: Extremo derecho del intervalo.
    :param tol: Tolerancia deseada para el resultado.
    :return: Raíz de la función en el intervalo [a, b].
    """
    # Calcula el valor de la función en los extremos del intervalo
    fa = f.subs(x, a)
    fb = f.subs(x,b)

    # Verifica si los extremos del intervalo tienen signos opuestos
    if fa * fb >= 0:
        raise ValueError("Los extremos del intervalo deben tener signos opuestos.")

    # Ciclo principal
    while abs(b - a) > tol:
        # Calcula el punto medio
        c = (a + b) / 2

        # Calcula el valor de la función en el punto medio
        fc = f.subs(x,c)

        # Verifica en qué mitad del intervalo se encuentra la raíz
        if fc == 0:
            return c
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    # Retorna el valor del punto medio del intervalo final
    return (a + b) / 2

f = Function('f')(x)

F=input("digite la Ecuacion a Resolver\n")
f=sympify(F)
A=input("digite primer valor del intervalo\n")
a=int(A)
B=input("digite segundo valor del intervalo\n")
b=int(B)
raiz = biseccion(f, a, b, 1e-3)
print("La raíz de la función en el intervalo es:",raiz)
