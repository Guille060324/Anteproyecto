import random
import string

def generar_contraseña(longitud, caracteres, excluir_similares=False, requisitos_personalizados=None):
    if excluir_similares:
        caracteres = caracteres.translate(str.maketrans('', '', 'Il1O0'))
    
    if requisitos_personalizados:
        caracteres += ''.join(requisitos_personalizados)
    
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def evaluar_fortaleza(contraseña):
    puntuacion = 0
    if len(contraseña) >= 8:
        puntuacion += 1
    if any(c.isdigit() for c in contraseña):
        puntuacion += 1
    if any(c.islower() for c in contraseña):
        puntuacion += 1
    if any(c.isupper() for c in contraseña):
        puntuacion += 1
    if any(c in string.punctuation for c in contraseña):
        puntuacion += 1
    
    return puntuacion
