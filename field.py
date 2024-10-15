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

    def field_update(self) -> list[list[str]]:
        """
        プレイヤー，敵，物体の位置を参照して，フィールドを更新する関数

        Returns:
            list[list[str]]: 更新されたフィールド

        Examples:
        
        """

        pass

    def field_display(self):
        """
        フィールドを表示する関数

        Example:

        """

        pass

    def collision_detection(self):
        """
        プレイヤー，敵，物体の位置が重なっているか判定する関数
        
        Args:
            target (Item): アイテム1
            items (list[Item]): アイテム2

        Returns:
            Item | None: 重なっているアイテムがあればそのアイテム，なければNone

        Examples:

        """

        pass 

>>>>>>> field
