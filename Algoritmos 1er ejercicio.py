# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# '
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

def cadena_valida(cadena):
    parentesis = {'(':')','[':']'}
    pila = []
    
    for c in cadena:
        if c in parentesis:
            pila.append(c)
        elif len(pila) == 0 or c != parentesis[pila.pop()]:
            return False
        
    return len(pila) == 0

print(cadena_valida('()'))
print(cadena_valida('()()()()()()()()()'))
print(cadena_valida('([])[]()'))

print(cadena_valida(')'))
print(cadena_valida('()['))
print(cadena_valida('(([))]'))
print(cadena_valida('(((((((((((((((((((((((((((((((((('))