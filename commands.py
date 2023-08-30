import os

def execute_mkdisk(tokens):
    size = None
    path = None
    fit = None
    unit = None
    
    for token in tokens:
        if token.type == 'SIZE':
            size = token.value
        elif token.type == 'PATH':
            path = token.value
        elif token.type == 'FIT':
            fit = token.value
        elif token.type == 'UNIT':
            unit = token.value
    
    if size is None:
        print("El tamaño es obligatorio en el comando mkdisk.")
        return
    
    if path is None:
        print("El path es obligatorio en el comando mkdisk.")
        return
    
    # Extraer el nombre del archivo del path
    file_name = os.path.basename(path)
    file_name = os.path.splitext(file_name)[0]  # Remover la extensión .dsk
    
    # Calcular el tamaño en bytes según la unidad especificada
    if unit == 'K':
        size_in_bytes = size * 1000  # Kilobytes a bytes
    else:
        size_in_bytes = size * 1000 * 1000  # Megabytes a bytes
    
    # Crear el archivo binario con el tamaño especificado
    with open(file_name + ".dsk", "wb") as file:
        block_size = 1024 if unit == 'K' else 1024 * 1024
        num_blocks = size_in_bytes // block_size
        remaining_bytes = size_in_bytes % block_size

        for _ in range(num_blocks):
            file.write(b'\x00' * block_size)
        
        if remaining_bytes:
            file.write(b'\x00' * remaining_bytes)

    print("Ejecutando comando mkdisk:")
    print("Tamaño:", size)
    print("Ruta:", path)
    print("Nombre de archivo:", file_name)
    print("Fit:", fit)
    print("Unit:", unit)
    print(f"Se ha creado el archivo {file_name}.dsk de tamaño {size} {unit}")