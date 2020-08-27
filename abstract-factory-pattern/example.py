# Factory抽象クラス, 
class AbstractPizzaFactory:
    def __init__(self):
        pass

    def add_dough(self):
        pass

    def add_source(self):
        pass

# ConcreateFactory, 抽象クラスAbstractPizzaFactoryを実装した,Factory具象クラス
# Factory具象クラスからコンポーネント(生地, ソース)を生成する
class PizzaFactoryA(AbstractPizzaFactory):
    def __init__(self):
        pass
    
    def add_dough(self):
        return WheatDough()
    
    def add_source(self):
        return TomatoSource()

class PizzaFactoryB(AbstractPizzaFactory):
    def __init__(self):
        pass
    
    def add_dough(self):
        return RiceFlourDough()
    
    def add_source(self):
        return BasilSource()

# コンポーネント(生地)
class Dough:
    def __init__(self):
        pass
    
    def check(self):
        pass

class WheatDough(Dough):
    def check(slef):
        print("生地は小麦")

class RiceFlourDough(Dough):
    def check(self):
        print("生地は米粉")

# コンポーネント(ソース)
class Source:
    def __init__(self):
        pass

    def check(self):
        pass

class TomatoSource(Source):
    def check(self):
        print("ソースはトマト")

class BasilSource(Source):
    def check(self):
        print("ソースはバジル")


if __name__ == "__main__":
    # Factoryを呼び出すアプリ側の処理
    # 生成するFactoryクラスを決める
    pizza_flg = 1
    
    f = PizzaFactoryA() if pizza_flg == 1 else PizzaFactoryB()
    
    # ファクトリーから生成するコンポーネントの具象クラスを意識する必要がない
    f.add_dough().check()
    f.add_source().check()