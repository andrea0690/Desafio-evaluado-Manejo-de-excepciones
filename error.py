class Error(Exception):
    pass

class DimensionError(Error):
    
    def __init__(self, mensaje: str, dimension: int, maximo: int):
        
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self) -> str:
        if self.dimension == None and self.maximo == None:
            return super().__str__()
        else:
            ret =f"{self.mensaje}."
            if self.dimension != None:
                ret += f"Propiedad ingresada: {self.dimension}."
            if self.maximo != None:
                ret += f" Máximo {self.maximo} valor permitido."
            return ret