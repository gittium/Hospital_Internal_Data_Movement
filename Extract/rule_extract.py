from abc import ABC , abstractmethod

class RuleExtract(ABC):  #ABC set rule to child class
    
    @abstractmethod
    def extract(self):
        pass