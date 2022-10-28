from pickle import FALSE


def leer_puntuacion(nombre_clase):
    #ui_bubble_rating bubble_50 → 5
    #ui_bubble_rating bubble_45 → 4.5
    #ui_bubble_rating bubble_40 → 4
    condicion = True
    bubble=50
    while condicion:

        if (nombre_clase == f'ui_bubble_rating bubble_{bubble}'):
            puntuacion = bubble/10
            condicion = False
        else:
            bubble=bubble-5
        
        if (bubble<0):
            condicion = False

    return puntuacion     
