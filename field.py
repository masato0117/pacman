

class Field:
    """Fieldクラス
    Fieldクラスではゲームフィールドを生成し表示するクラスである．
    プレイヤー，敵，物体の位置を更新し，フィールド上に表示する機能を持つ．
    位置を更新する際に衝突判定をする．

    Attributes:
        players (list[Player]): プレイヤー情報
        enemies (list[Enemy]): 敵の情報
        objects (list[Object]): アイテム情報
        fields (list[list[str]]): フィールド情報
        field_size (int): フィールドサイズ
    """

    def __init__(
        self,
        players: list[Player],
        enemies: list[Enemy],
        objects: list[Object],
        field_size: int 8) -> None:
        """
        Fieldクラスの初期化をする関数

        Args:
            players (list[Player]): プレイヤー情報
            enemies (list[Enemy]): 敵の情報
            objects (list[Object]): アイテム情報
            fields (list[list[str]]): フィールド情報
            field_size (int): フィールドサイズ
        """
        pass
