import abc

def main():
    # 牛
    cow_factory = CowFactory()
    cow_factory.create_animal().call()
    # 豚
    pig_factory = PigFactory()
    pig_factory.create_animal().call()
    # 鶏
    chicken_factory = ChickenFactory()
    chicken_factory.create_animal().call()

# 抽象クラスCreater
class Factory:
    def create(self, kind):
        # 動物を決める
        animal = create_animal()
        return animal
    
    @abc.abstractclassmethod
    def create_animal(self):
        pass

# Createrの具象クラス
class CowFactory(Factory):
    def create_animal(self):
        return Cow()

class PigFactory(Factory):
    def create_animal(self):
        return Pig()

class ChickenFactory(Factory):
    def create_animal(self):
        return Chicken()

# Product
class Animal:
    @abc.abstractclassmethod
    def call(self):
        pass

class Cow(Animal):
    def call(self):
        print("mow")

class Pig(Animal):
    def call(self):
        print("boo")

class Chicken(Animal):
    def call(self):
        print("coak")

if __name__ == "__main__":
    main()