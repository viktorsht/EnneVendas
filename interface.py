from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def validar_senha(self):
        pass
