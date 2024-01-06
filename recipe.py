#
# (c) 2024 Takahiro Hashimoto
#
import random
import argparse

protein = ["鶏肉", "豚肉", "牛肉", "魚", "卵", "豆腐"]
fishes = ["さば", "あじ", "いわし", "さけ", "まぐろ", "かつお", "たい", "たら", "ぶり", "かれい"]
vegetables = ["人参", "玉ねぎ", "ほうれん草", "かぼちゃ", "大根", "キャベツ", "ブロッコリー", "トマト",
              "ピーマン", "なす", "かぶ", "れんこん", "さつまいも", "ごぼう", "しいたけ", "しめじ",
              "えのき", "まいたけ", "マッシュルーム", "パプリカ", "ズッキーニ", "白菜", "さといも", "ネギ"]
soup = ["鰹", "野菜"]

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--vegetable", type=int, metavar="N", default=3, help="# of vegetable to use")
parser.add_argument("-n", "--number", type=int, metavar="N", default=1, help="# of recipe to generate")
args = parser.parse_args()

for _ in range(args.number):
    veg_choices = random.sample(vegetables, args.vegetable)
    pro_choice = random.choice(protein)
    soup_choice = random.choice(soup)

    if pro_choice == "魚":
        pro_choice = random.choice(fishes)

    print(f"{pro_choice}と {''.join(veg_choices)}の {soup_choice}風味")
