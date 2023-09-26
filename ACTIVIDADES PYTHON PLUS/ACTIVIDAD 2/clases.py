class Banda():
    
    generos = set()
        
    def __init__(self, nombre, genero="None"):
        self.nombre=nombre
        self.genero=genero
        self._integrantes=[]
        Banda.generos.add(genero)
    
    def agregar_integrante(self, integrantes):
                self._integrantes = integrantes
    
    def __str__(self):
        texto = f"La banda de {self.genero} {self.nombre} está integrada por: "
        for elem in self._integrantes:
            texto += f"\n\t\t{elem}"
        return texto



