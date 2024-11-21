from item import Item


class Wall(Item):
    """
    Wallクラス
    壁の位置とアイコンを管理するクラス

    Attributes:
        x (int): x座標
        y (int): y座標
        icon (str): 表示アイコン

    Examples:
        >>> wall = Wall(3, 3)
        >>> wall.now_x
        3
        >>> wall.now_y
        3
        >>> wall.icon
        '⚪'
        >>> isinstance(wall, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "⚪"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
