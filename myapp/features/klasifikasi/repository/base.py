from abc import ABC, abstractmethod

class ModelRepositoryBase(ABC):
    @abstractmethod
    def save(self, model):
        raise NotImplementedError
    
    @abstractmethod
    def load(self):
        raise NotImplementedError