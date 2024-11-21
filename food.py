from item import Item


class Food(Item):
    """
    Foodクラス
    回復アイテムの位置とアイコンを管理するクラス

    Attributes:
        x (int): x座標
        y (int): y座標
        icon (str): 表示アイコン

    Examples:
        >>> food = Food(3, 3)
        >>> food.now_x
        3
        >>> food.now_y
        3
        >>> food.icon
        '🍒'
        >>> isinstance(food, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "🍒"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
