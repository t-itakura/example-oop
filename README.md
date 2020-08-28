# example-oop

## Abstract Factory Pattern
```
関連する一連のインスタンスを状況に応じて、適切に生成する方法を提供する。
インスタンスの生成を専門に行うクラスを用意する。
Abstract Factoryパターンは、テーマの共通な個別のファクトリーのグループをカプセル化
する手段を提供する。このとき、ファクトリーの具体的なクラスを指定しない。
インスタンス生成クラスをFactoryクラスにまとめることでアプリケーションから
独立する。このことによってアプリケーションを変更することなくインスタンス生成を変更することができる。
```

***例題***
ピザを作る
- ピザは生地、ソースからできます
- 工場Aでは、生地に小麦、ソースにトマトを使用
- 工場Bでは、生地に米粉、ソースにバジルを使用

```
Factory: 工場
Factoryクラスが持つコンポーネント: 生地, ソース
各工場は各生地、ソースクラスを持つhas-aの関係
```

## Factory Method Pattern
```
オブジェクト生成と具体的な処理を分離し、柔軟にオブジェクトを利用することができる。
インスタンスの生成はスーパークラスで決め、具体的な実装はサブクラス側で行う。
FactoryごとにどのProductを生成するかオブジェクト作成時に作成するオブジェクトのクラスを
サブクラスに選ばせる
```

***例題***
動物の鳴き声をチェック
- 牛,もしくは豚、鶏を作る工場
- 動物を作ったら鳴き声でどの動物かチェックする

```
Creater(Factory): 工場
Product: 牛、豚、鶏
```


## 参考
[Python命名規則一覧](https://qiita.com/naomi7325/items/4eb1d2a40277361e898b)  
[Factory Methodパターン](https://pydp.info/GoF_dp/creation/03_Factory_Method/index.html)  
[沈思黙考：デザインパターン(Abstract Factory パターン)](https://qiita.com/morimotof/items/67a9e2a8d7e15ea321d2)  
[Factory Method パターン](http://www.ie.u-ryukyu.ac.jp/~e085739/java.it.1.html)  
