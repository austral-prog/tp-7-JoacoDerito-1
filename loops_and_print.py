def enumerate_list(lista: list[str]):
    resultado = []
    for i, elemento in enumerate(lista):
        if not elemento:
            continue
        resultado.append(f"{i}. {elemento}")
    return resultado

def enumerate_backwards(lista: list[str]):
    resultado = []
    for i, elemento in enumerate(lista):
        if not elemento:
            continue
        resultado.append(f"{i}. {elemento[::-1]}")
    return resultado
