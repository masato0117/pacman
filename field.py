from item import Item
from player import Player


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

    # フィールドを生成する関数
    def __init__(
            self,
            players: list[Player],
            f_size: int = 6) -> None:

        """
        Fieldクラスの初期化をする関数

        Args:
            players (list[Player]): プレイヤー情報
            enemies (list[Enemy]): 敵の情報
            foods (list[Food]): アイテム情報
            blocks (list[Block]): ブロックのリスト
            field_size (int): フィールドサイズ
        """

        self.field_size = f_size
        self.field = [[" " for _ in range(f_size)] for _ in range(f_size)]
        self.players = players

        # それぞれのアイテムの位置をFieldに更新する関数
        self.update_field(self)

        pass

    def update_field(self) -> list[list[str]]:

        """
        プレイヤー，敵，物体の位置を参照して，フィールドを更新する関数

        Returns:
            list[list[str]]: 更新されたフィールド

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p, 3)
            >>> field.update_field()[0]
            ['\\u3000', 'p1', '\\u3000']
        """

        # フィールドを全て空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                self.field[i][j] = " "

        # フィールドを更新する処理を記述
        for player in self.players:
            self.field[player.now_y][player.now_x] = player.icon
        return self.field

    # フィールドを表示する関数
    def display_field(self) -> None:

        """
        フィールドを表示する関数

        Example:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> field = Field(p, 3)
            >>> field.display_field()
            w: 1マス上に移動
            a: 1マス左に移動
            s: 1マス下に移動
            d: 1マス右に移動
        """

        # 動き方を表示
        print("w: 1マス上に移動")
        print("a: 1マス左に移動")
        print("s: 1マス下に移動")
        print("d: 1マス右に移動")

        # self.fieldを表示する処理を記述
        max_width = max(len(row) for row in self.field)

        for row in self.field:
            # 各行の文字列を作成し，不足部分を空白で埋める．
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)

    # 衝突判定をする関数
    def collision_detection(
            self,
            target: Item,
            items: list[Item]) -> Item | None:

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
            >>> p.next_x = 1
            >>> p.next_y = 1
        """

        # 衝突判定をする処理を記述
        for item in items:
            if item.next_x == target.next_x and item.next_y == target.next_y:
                return item
        return None

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
