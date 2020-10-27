
import datetime

def totalmes(fechainicio, fechafinal):
    num_months = (fechafinal.year - fechainicio.year) * 12 + (fechafinal.month - fechainicio.month)
    return(int(num_months) + 1)
