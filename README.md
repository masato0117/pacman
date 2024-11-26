# Pacman Project

問題解決型実践演習の課題としてコマンドラインで動くパックマンゲームの作成

## Requirement
- Python 3.10.12


## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- メインプログラムを実行．
  - 出力されるマップ上のPlayerを動かhしたい方向に(W,A,S,Dキー)を入力する。
```shell
python main.py
```
- デフォルトのパラメータ設定をjson出力．
```shell
python config.py  # parameters.jsonというファイルが出力される．
```
- 以下のように，上記で生成されるjsonファイルの数値を書き換えて，実行時のパラメータを指定できます．
```shell
python main.py -p parameters.json
```
- 詳しいコマンドの使い方は以下のように確認できます．
```shell
python main.py -h
```


## Parameter Settings

- 指定できるパラメータは以下の通り．
```json
{
    "field_size": 10,    # 画面サイズの一辺
    "enemy_num": 20,     # エネミーの個数
    "item_num": 1        # アイテムの個数
}
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── config.py           # パラメータ定義
├── main.py             # 実行ファイル
├── game.py
├── item.py
├── player.py
├── enemy.py
├── food.py
├── weapon.py
├── block.py
├── wall.py
├── field.py
├── input_without_enter.py
├── parameters.json     # パラメータ指定用ファイル
├── result              # 結果出力ディレクトリ
│   └── 20211026_165841
└── utils.py            # 共有関数群
```
