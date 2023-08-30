from ply import lex
import re
# Definir tokens
tokens = ['MKDISK', 'SIZE', 'PATH', 'FIT', 'UNIT']

def t_MKDISK(t):
    r'mkdisk'
    return t

def t_SIZE(t):
    r'\s*-size=\s*(\d+)\s*'  # Cambiar la expresión regular para capturar el valor numérico sin espacios
    match = re.search(r'\d+', t.value)  # Buscar la coincidencia numérica en la cadena
    if match:
        t.value = int(match.group())  # Extraer el valor numérico capturado
    else:
        t.value = 0  # Valor por defecto en caso de no encontrar un número
    return t

def t_PATH(t):
    r'\s*-path=[a-zA-Z0-9_\/]+\.dsk'  # Cambiar la expresión regular para permitir espacios antes de '-path='
    t.value = t.value.strip()[6:]  # Asegurarse de eliminar espacios y luego extraer la ruta
    return t

def t_FIT(t):
    r'-fit=(BF|FF|WF)'
    t.value = t.value[5:]  # Extraer el valor después de '-fit='
    return t

def t_UNIT(t):
    r'-unit=(K|M)'
    t.value = t.value[6:]  # Extraer el valor después de '-unit='
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Carácter inesperado:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()