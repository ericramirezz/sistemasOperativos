from Gato import Gato, TipoGato
from Plato import Plato 
from Dispensador import Dispensador
from threading import Lock

#creando par de platos
plato1 = Plato(1)
plato2 = Plato(2)
listaPlatos = [plato1, plato2]
#instanciando el dispensador con los platos
dispensador = Dispensador(listaPlatos)