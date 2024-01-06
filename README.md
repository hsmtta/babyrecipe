## 概要
離乳食のレシピを作成するツールです。タンパク質1種類、野菜をN種類、味付けを1種類をランダムに選択します。選択される素材はコードを参照してください。

## 使い方
```bash
$ python recipe.py -h
usage: recipe.py [-h] [-v N] [-n N]

options:
  -h, --help           show this help message and exit
  -v N, --vegetable N  # of vegetable to use
  -n N, --number N     # of recipe to generate
```

```bash
$ python recipe.py -v 3 -n 5
ぶりと トマトさといも人参の 鰹風味
牛肉と ズッキーニまいたけピーマンの 鰹風味
豆腐と マッシュルーム玉ねぎブロッコリーの 鰹風味
牛肉と ピーマンさといもズッキーニの 鰹風味
卵と えのき白菜まいたけの 野菜風味
```
