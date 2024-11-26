"""親クラス
block,player,enemy,weaponの親クラス
"""


class Item:
    """block,player,enemy,weaponの親クラス

    Attributes:
       now_x(int) : 現在のx座標
       now_y(int) : 現在のy座標
       next_x(int) : 次の時刻でのx座標
       next_y(int) : 次の時刻でのy座標
       status(bool) : アイテムの状態(True>存在,False>存在しない・消滅した)
       icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(self, x, y) -> None:
        """
        Itemクラスのコンストラクタ
        引数にx座標とy座標を受け取り、それぞれの座標を初期化する

        Args:
            x(int): x座標
            y(int): y座標

        Returns:
            None

        Examples:
            >>> item = Item(2, 3)
            >>> item.now_x
            2
            >>> item.now_y
            3
            >>> item.next_x
            2
            >>> item.next_y
            3
            >>> item.icon
            ''
            >>> item.status
            True
        """
        self.now_x = x   # 現在のx座標
        self.now_y = y   # 現在のy座標
        self.next_x = x   # 次の時刻でのx座標
        self.next_y = y   # 次の時刻でのy座標
        self.status = True   # アイテムの状態(True>存在,False>存在しない・消滅した)
        self.icon = ""   # 表示されるアイテムのアイコン

    def get_next_pos(self) -> tuple[int, int]:
        """
        次の時刻の座標を取得するメソッド
        デフォルトでは現在の座標を返すため，子クラスでオーバーライドすることを想定している．

        Returns:
            tuple[int, int]: 現在の座標

        Examples:
            >>> item = Item(2, 3)
            >>> item.get_next_pos()
            (2, 3)
        """
        return (self.now_x, self.now_y)

    def get_pos(self) -> tuple[int, int]:
        """
        次の時刻の座標を取得するメソッド
        デフォルトでは現在の座標を返すため，子クラスでオーバーライドすることを想定している．

        Returns:
            tuple[int, int]: 現在の座標

        Examples:
            >>> item = Item(2, 3)
            >>> item.get_pos()
            (2, 3)
        """
        return (self.now_x, self.now_y)

    def update_pos(self, stuck: bool = False) -> None:
        """
        座標を更新するメソッド
        引数に次に移動したい座標をとり,その座標にプレイヤーの現在座標を更新する.

        Args:
            stuck (bool): そのターンに動けない場合にTrueを渡す (default: False)

        Returns:
            None

        Examples:
            >>> item = Item(2, 3)
            >>> item.next_x = 3
            >>> item.next_y = 4
            >>> item.get_pos()
            (2, 3)
            >>> item.update_pos()
            >>> item.get_pos()
            (2, 3)

        """
        if stuck:
            self.next_x = self.now_x
            self.next_y = self.now_y
            return

        self.now_x = self.next_x
        self.now_y = self.next_y

    def update_teleportate_pos(
            self,
            max_size: int = 6) -> None:
        """
        壁に衝突したら右端と左端,上端と下端を繋げて移動する

        Args:
            max_size: 座標最大値

        Returns:
            None

        Examples:
            >>>self.next_x = 0
            >>>self.now_x = 1
            >>>self.next_y = 1
            >>>self.now = 1
            >>>Item.update_pos()
            (18, 1)
        """

        horizontal_parameter: int = self.next_x - self.now_x
        vertical_parameter: int = self.next_y - self.now_y
        if horizontal_parameter > 0:
            self.next_x = 1
            self.next_y = self.now_y
        elif horizontal_parameter < 0:
            self.next_x = max_size - 2
            self.next_y = self.now_y
        elif vertical_parameter > 0:
            self.next_x = self.now_x
            self.next_y = 1
        else:
            self.next_x = self.now_x
            self.next_y = max_size - 2
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
