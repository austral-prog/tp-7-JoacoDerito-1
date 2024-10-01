def find_from_index(word: str, lista: list[str], index: int):
    for idx, el in enumerate(lista):
        if idx >= index and el == word:
            return idx
    return -1

def index_of_empty(lista: list[str]):
    for idx, el in enumerate(lista):
        if el == "":
            return idx
    return -1

def index_of(word: str, lista: list[str]):
    for idx, el in enumerate(lista):
        if el == word:
            return idx
    return -1

def poner(palabra: str, lista: list[str]):
    for idx, el in enumerate(lista):
        if el == "":
            lista[idx] = palabra
            return idx
    return -1

def eliminar(palabra: str, lista: list[str]):
    contador = 0
    for idx, el in enumerate(lista):
        if el == palabra:
            lista[idx] = ""
            contador += 1
    return contador
