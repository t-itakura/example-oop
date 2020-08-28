import abc

def main():
    cow_factory = CowFactory()
    cow_factory.factory_method()
    cow.check_animal()

    chiken = ChichenFactory()
    chiken.check_animal()

# 抽象クラスCreater
class Factory:
    def __init__(self):
        # 動物の種類はここで決定
        self.animal = self.factory_method()
    
    def create(self, breed):
        # 動物(品種)を決める
        self.animal = create_breed(breed)

        return self.animal
    
    @abc.abstractmethod
    def factory_method(self):
        pass

    @abc.abstractclassmethod
    def create_breed(self, breed):
        pass

# Creater
class CowFactory(Factory):
    def factory_method(self):
        return Cow()
    
    def 


# Product
class Animal:
    def __init__(self, breed):
        self.breed = breed

    @abc.abstractclassmethod
    def call(self):
        pass

class Cow(Animal):
    def call(self):
        print("mow")

