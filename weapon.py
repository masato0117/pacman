from item import Item


class Weapon(Item):
    """
    Weaponクラス
    アイテムの位置とアイコンを管理するクラス

    Attributes:
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        status (bool): アイテムの状態
        icon (str): 表示アイコン

    Examples:
        >>> weapon = Weapon(4, 5)
        >>> weapon.now_x
        4
        >>> weapon.now_y
        5
        >>> weapon.icon
        '🍒'
        >>> weapon.status
        True
        >>> isinstance(weapon, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "🍒"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
