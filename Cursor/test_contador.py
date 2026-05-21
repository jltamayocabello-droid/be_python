from contador import contar_palabras


def test_contar_palabras_cadena_simple():
    assert contar_palabras("Hola hola mundo") == 3


def test_contar_palabras_cadena_vacia():
    assert contar_palabras("") == 0


def test_contar_palabras_ignora_mayusculas_y_puntuacion():
    assert contar_palabras("Hola, mundo! Python.") == 3


def test_contar_palabras_una_sola_palabra():
    assert contar_palabras("texto") == 1
