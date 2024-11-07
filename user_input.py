from input_without_enter import InputWithoutEnter


"""ユーザからの入力を受け取る

"""


class UserInput:
    """ユーザの入力を受け取るクラス"""

    @staticmethod
    def get_user_input() -> tuple[int, int]:
        """ユーザの入力を受け取り、x, y座標の差分を返す
        Returns:
           tuple[int, int]:x, y座標の差分（例:（1, 0）、(-1, 0)、(0, 1)、(0, -1)など）
        """
        # キー入力
        key = InputWithoutEnter.input_without_eneter()
        # 入力されたキーに対応する座標差分を返す
        if key == "w":
            return (0, 1)
        elif key == "a":
            return (-1, 0)
        elif key == "s":
            return (0, -1)
        elif key == "d":
            return (1, 0)
        else:
            return (0, 0)
