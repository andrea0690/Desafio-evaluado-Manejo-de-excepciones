from error import DimensionError


class Foto():
    MAX = 2500
    MIN = 1

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < self.MIN or ancho > self.MAX:
            raise DimensionError('Ancho no permitido', ancho, self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto < self.MIN or alto > self.MAX:
            raise DimensionError('Alto no permitido', alto, self.MAX)
        self.__alto = alto
        
foto1 = Foto(2000, 2000, 'Andrea')

foto1.ancho = 3000
