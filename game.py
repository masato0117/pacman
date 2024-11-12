import time
from player import Player
from field import Field
from user_input import UserInput
from config import Parameters
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
        self.setup(params)  # ゲームの初期設定
        self.start()  # ゲームのメインループ

    def setup(self, params: Parameters) -> None:
        """Gameの初期設定
        ゲームの初期設定を行うメソッド.

        Args:
           Params (Parameters): configのパラメータのインスタンス
        """
        f_size = params.field_size  # フィールドのサイズ
        # フィールドの初期化
        self.players = [Player(1, 1)]
        self.field = Field(
            self.players,
            f_size)

    def start(self) -> str:
        """ゲームのメインループ
        ゲームのメインループを実行するメソッド
        キー入力を受け取る、プレイヤーと敵の移動、フィールド更新
        ゲーム終了条件を満たした場合は終了

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
                key = UserInput.get_user_input()
                player.get_next_pos(key)
                # filedの更新
                self.field.update_field()

                # 一定の間隔で処理を繰り返す
                # 0.3秒待つ
                time.sleep(0.3)

                # 終了時のチェック
