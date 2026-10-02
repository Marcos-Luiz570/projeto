def mover_discos(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        print(f"Mover o disco 1 de {origem} para {destino}")
    else:
        mover_discos(num_discos - 1, origem, auxiliar, destino)
        print(f"Mover o disco {num_discos} de {origem} para {destino}")
        mover_discos(num_discos - 1, auxiliar, destino, origem)

mover_discos(4, 'Torre 1', 'Torre 3', 'Torre 2')