import threading
from time import sleep
from random import randint

class gatito(threading.Thread): ##Herencia de threading.Thread Para la independencia de cada gato

    ##Constructor de la clase gatito
    def __init__(self, nombre, tipo, plato):
        threading.Thread.__init__(self) ##llama a la clase para que garantixce el ser un hilo
        self.nombre=nombre ##Por que cada gato tiene un nombre
        self.tipo=tipo     ##Si es hembra, macho o invasor
        self.estado = "hambriento" ##Define el estado que tendra el gato
        self.porciones = 0  ##cuantas porciones ha comido el gato
        self.plato = plato  ##en que plato esta llevando la accion, para el considerarlo en el semaphoro
    """INTRODUCIR ATRIBUTOS PARA QUE LA CLASE PUEDA INTERACTUAR CON LA INTERFA<"""        
    ##funcion para que el hilo trabaje
    def run(self):
        ##cilo para que se repita esta acción
        while True:
            self.comer() ##llamado a comer
            sleep(randint(1,19))     ##Tiempo de reposo, al ser un gato, podriamos decir que duerme o hace cualquier otra cosa de gatos
    
    ##funcion para que el gato coma
    def comer(self):
        ##asignando las porciones que come cada tipo de gato
        if self.tipo.upper() == "MACHO" :
            porciones = 2
        elif self.tipo.upper() == "HEMBRA":
            porciones = 1 
        else:
            porciones = randint(1,3) ##puesto que no se sabe cuando va a comer


        #accesos al plato, donde se verificara que no este lleno y asi 
        if self.plato.semaforo.acquire(blocking=True): #SI el metodo dice que si hay suficiente comida en el plato comera
            self.estado="comiendo" 
            sleep(randint(1,3))     #tiempo que se tarda en comer
            self.estado="satisfecho"
        else:
            self.estado="hambriento"
        
        self.plato.semaforo.realease() #libera el semaforo 
        
"""INTRODUCIR METODOS PARA LA INTERFAZ GRAFICA"""        
"""INTRODUCIR ACTUALIZACION EN LOS METODOS PARA LA INTERFAZ GRAFICA """    

