import time
from player import Player
from wall import Wall
from block import Block
from enemy import Enemy
from food import Food
from field import Field
from input_without_enter import InputWithoutEnter as Input
from config import Parameters
from random import randint as random
import logging
import os


logger = logging.getLogger(__name__)


class Game():
    """ゲームの進行をするクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス.

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (Field): フィールドのインスタンス
    """

    def __init__(self, params: Parameters) -> None:

        """Gameクラスの初期化をする関数

        Args:
           params (Parameters): configのパラメータのインスタンス
        """
        self.players: list[Player] = []
        self.walls: list[Wall] = []
        self.blocks: list[Block] = []
        self.enemies: list[Enemy] = []
        self.foods: list[Food] = []
        self.field = Field([], [], [], [], [], 0)
        self.clear_count = 0    # ステージクリア数
        self.setup(params)  # ゲームの初期設定
        self.start(params)  # ゲームのメインループ

    def setup(self, params: Parameters) -> None:
        """Gameの初期設定
        ゲームの初期設定を行うメソッド.

        Args:
           Params (Parameters): configのパラメータのインスタンス
        """
        f_size = params.field_size  # フィールドのサイズ
        e_num = params.enemy_num  # 敵の数
        f_num = params.food_num  # 食べ物の数
        item_space = []  # アイテムがある場所
        # フィールドの初期化
        self.players = [
            Player(random(1, f_size - 2), random(1, f_size - 2))
            for _ in range(1)]
        # 敵をフィールド内に生成する
        self.enemies = [
            Enemy(random(1, f_size - 2), random(1, f_size - 2))
            for _ in range(e_num)]
        # 食べ物をフィールド内に生成する
        self.foods = [
            Food(random(1, f_size - 2), random(1, f_size - 2))
            for _ in range(f_num)]
        # フィールドの周りを壁とするwallインスタンスを生成
        if f_size < 4:
            raise ValueError("field_size must be greater than 4")
        self.walls = [
            Wall(x, y)
            for x in range(f_size)
            for y in range(f_size)
            if x == 0 or x == f_size - 1 or y == 0 or y == f_size - 1
        ]
        # 障害物をフィールド内に生成する
        self.blocks = [
            Block(x, y)
            for x in range(1, f_size - 2)
            for y in range(1, f_size - 2)
            if x == random(1, f_size - 2) or y == random(1, f_size - 2)
        ]
        # アイテムの位置が重複している場合，新たな座標を付与
        for item in self.players + self.enemies + self.foods + self.blocks:
            if item.now_x * item.now_y not in item_space:
                item_space.append(item.now_x * item.now_y)
            else:
                while True:
                    item.now_x = random(1, f_size - 2)
                    item.now_y = random(1, f_size - 2)
                    if item.now_x * item.now_y not in item_space:
                        item_space.append(item.now_x * item.now_y)
                        item.next_x = item.now_x
                        item.next_y = item.now_y
                        break

        self.field = Field(
            self.players,
            self.walls,
            self.blocks,
            self.enemies,
            self.foods,
            f_size)

    def start(self, params: Parameters) -> str:
        """ゲームのメインループ
        ゲームのメインループを実行するメソッド
        キー入力を受け取る、プレイヤーと敵の移動、フィールド更新
        アイテムを取るとステージクリア
        敵と接触するとゲームオーバー、スコア表示（ゲーム終了条件）

        Returns:
            str: ゲームの終了時のメッセージ (例: "Game Over!", "Game Clear!")
        """
        # ゲームのメインループ
        while True:
            #  フィールドの表示
            os.system("cls" if os.name == "nt" else "clear")  # ターミナルのクリア
            self.field.display_field()

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = Input.get_user_input()
                player.get_next_pos(key)

            # 敵の移動を決定
            for enemy in self.enemies:
                enemy.get_next_pos()

            # プレイヤーと敵の移動
            self.field.post_collision_processing(list(self.players), 1)
            self.field.post_collision_processing(list(self.enemies), 2)

            for player in self.players:
                # 敵との衝突判定
                if self.field.collision(player, list(self.enemies)):
                    player.change_face_bad()
                    self.field.update_field()
                    os.system("cls" if os.name == "nt" else "clear")
                    # ターミナルをクリア
                    self.field.display_field()
                    logger.info("Game Over!")
                    print("Clear Stage:", self.clear_count)
                    return "Game Over!"

                # 食べ物との衝突判定
                collided_item = self.field.collision(player, list(self.foods))
                if collided_item is not None:
                    collided_item.status = False
                    if all([not food.status for food in self.foods]):
                        player.change_face_good()
                        self.field.update_field()
                        os.system("cls" if os.name == "nt" else "clear")
                        # ターミナルをクリア
                        self.field.display_field()
                        logger.info("Next stage")
                        # 新しいステージの生成
                        self.clear_count = self.clear_count + 1
                        self.next_setup(params)
                        self.next_game(params)
                        return "Next stage"

            # filedの更新
            self.field.update_field()

            # 一定の間隔で処理を繰り返す
            # 0.3秒待つ
            time.sleep(0.3)

            # 終了時のチェック

    def next_setup(self, params: Parameters) -> None:
        """Gameの再初期設定
        ゲームの設定変更を行うメソッド.

        Args:
           Params (Parameters): configのパラメータのインスタンス
        """
        f_size = params.field_size  # フィールドのサイズ
        e_num = params.enemy_num + self.clear_count  # 敵の数
        f_num = params.food_num  # 食べ物の数
        item_space = []  # 空白ではない数
        # フィールドの初期化
        self.players = [
            Player(random(1, f_size - 2), random(1, f_size - 2))
            for _ in range(1)]
        # 敵をフィールド内に生成する
        self.enemies = [
            Enemy(random(1, f_size - 2), random(1, f_size - 2))
            for _ in range(e_num)]
        # 食べ物をフィールド内に生成する
        self.foods = [
            Food(random(1, f_size - 2), random(1, f_size - 2))
            for _ in range(f_num)]
        # フィールドの周りを壁とするwallインスタンスを生成
        if f_size < 4:
            raise ValueError("field_size must be greater than 4")
        self.walls = [
            Wall(x, y)
            for x in range(f_size)
            for y in range(f_size)
            if x == 0 or x == f_size - 1 or y == 0 or y == f_size - 1
        ]
        # 障害物をフィールド内に生成する
        self.blocks = [
            Block(x, y)
            for x in range(1, f_size - 2)
            for y in range(1, f_size - 2)
            if x == random(1, f_size - 2) or y == random(1, f_size - 2)
        ]
        # 空白の位置とアイテムがある位置の識別
        for item in self.players + self.enemies + self.foods + self.blocks:
            print(item)
            if item not in item_space:
                item_space.append(item)
            else:
                while True:
                    item = (random(1, f_size - 2), random(1, f_size - 2))
                    if item not in item_space:
                        item_space.append(item)
                        break

        self.field = Field(
            self.players,
            self.walls,
            self.blocks,
            self.enemies,
            self.foods,
            f_size)

    def next_game(self, params) -> None:
        """次のゲームの開始
            次のゲームを開始する
        """
        self.start(params)
