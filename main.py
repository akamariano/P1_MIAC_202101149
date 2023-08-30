from lexer_parser import lexer
from commands import execute_mkdisk

while True:
    try:
        command = input("Ingresa un comando: ")
        if not command:
            continue
        
        lexer.input(command)  # Configurar la entrada del lexer
        tokens = list(lexer)   # Convertir los tokens en una lista
        
        print("Comandos y atributos reconocidos:")
        for token in tokens:
            print("Leyendo",token.type, token.value)  # Imprimir los tokens reconocidos
            
        # Llamar a la función correspondiente al comando
        if tokens and tokens[0].type == 'MKDISK':
            execute_mkdisk(tokens)
        else:
            print("Comando no reconocido.")
    except EOFError:
        break
