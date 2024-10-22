class Field:
    """Fieldクラス
    Fieldクラスではゲームフィールドを生成し表示するクラスである．
    プレイヤー，敵，物体の位置を更新し，フィールド上に表示する機能を持つ．
    位置を更新する際に衝突判定をする．

    Attributes:
        players (list[Player]): プレイヤー情報
        enemies (list[Enemy]): 敵の情報
        foods (list[Food]): アイテム情報
        blocks (list[Block]): アイテムのリスト
        fields (list[list[str]]): フィールド情報
        field_size (int): フィールドサイズ
    """

    def __init__(
        self,
        players: list[Player],
        enemies: list[Enemy],
        foods: list[Food],
        blocks: list[Block],
        field_size: int = 8) -> None:

        """
        Fieldクラスの初期化をする関数

        Args:
            players (list[Player]): プレイヤー情報
            enemies (list[Enemy]): 敵の情報
            foods (list[Food]): アイテム情報
            blocks (list[Block]): ブロックのリスト
            field_size (int): フィールドサイズ
        """
        pass

    def update_field(self) -> list[list[str]]:
        """
        プレイヤー，敵，物体の位置を参照して，フィールドを更新する関数

        Returns:
            list[list[str]]: 更新されたフィールド

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> e1 = Enemy(2, 0)
            >>> e1.icon = "e1"
            >>> e2 = Enemy(1, 1)
            >>> e2.icon = "e2"
            >>> e = [e1, e2]
            >>> f = [Food(0, 1)]
            >>> f[0].icon = "f1"
            >>> b1 = Block(0, 2)
            >>> b1.icon = "b1"
            >>> b2 = Enemy(1, 2)
            >>> b2.icon = "b2"
            >>> b = [b1, b2]
            >>> field = Field(p, e, f, b, 3)
            >>> field.update_field()[0]
            ['\\u3000', 'p1', 'e1']
            >>> field.update_field()[1]
            ['f1', 'e2', '\\u3000']
            >>> field.update_field()[2]
            ['b1', 'b2', '\\u3000']
        """

        pass

    def display_field(self) -> None:
        """
        フィールドを表示する関数

        Example:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> e1 = Enemy(2, 0)
            >>> e1.icon = "e1"
            >>> e2 = Enemy(1, 1)
            >>> e2.icon = "e2"
            >>> e = [e1, e2]
            >>> f = [food(0, 1)]
            >>> f[0].icon = "f1"
            >>> b1 = Block(0, 2)
            >>> b1.icon = "b1"
            >>> b2 = Enemy(1, 2)
            >>> b2.icon = "b2"
            >>> b = [b1, b2]
            >>> field = Field(p, e, f, b, 3)
            >>> field.display_field()
            w: 上に移動
            a: 左に移動
            s: 下に移動
            d: 右に移動
              p1e1
            f1e2 
            b1b2
        """

        pass

    def collision_detection(
            self,
            target:Item,
            items:list[Item]) -> Item | None:
        """
        プレイヤー，敵，物体の位置が重なっているか判定する関数
        
        Args:
            target (Item): アイテム1
            items (list[Item]): アイテム2

        Returns:
            Item | None: 重なっているアイテムがあればそのアイテム，なければNone

        Examples:
            >>> p = Item(0, 0)
            >>> e = Item(1, 1)
            >>> field = Field([p], [e], [], [])
            >>> p.next_x = 1
            >>> r = field.collision_detection(p, [e])
            >>> r is None
            True
            >>> p.next_y = 1
            >>> r = field.collision_detection(p, [e])
            >>> r is e
            Ture
        """

        pass 
    
    if __name__ == "__main__":
        import doctest
        doctest.testmod()