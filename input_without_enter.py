import sys
import termios


class InputWithoutEnter:
    """ユーザの入力を受け取るクラス"""

    @staticmethod
    def get_user_input() -> tuple[int, int]:
        """ユーザの入力を受け取り、x, y座標の差分を返す
        Returns:
           tuple[int, int]:x, y座標の差分（例:（1, 0）、(-1, 0)、(0, 1)、(0, -1)など）
        """
        # キー入力
        key = InputWithoutEnter.input_without_enter()
        # 入力されたキーに対応する座標差分を返す
        if key == "w":
            return (0, -1)
        elif key == "a":
            return (-1, 0)
        elif key == "s":
            return (0, 1)
        elif key == "d":
            return (1, 0)
        else:
            return (0, 0)

    @staticmethod
    def input_without_enter():
        '''エンターキーを押さずに入力を受け取る
        Returns:
           str: 入力された文字
        '''

        # 標準入力のファイルディスクリプタを取得
        fd = sys.stdin.fileno()

        # fdの端末属性をゲットする
        # oldとnewには同じものが入る
        # newに変更を加えて適応する
        # oldは後で元に戻すため
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)

        # new[3]はlflags
        # ICANON(カノニカルモードのフラグ)を外す
        new[3] &= ~termios.ICANON
        # ECHO(入力された文字を表示する否かのフラグ)を外す
        new[3] &= ~termios.ECHO

        try:
            # 書き換えたnewをfdに適応する
            termios.tcsetattr(fd, termios.TCSANOW, new)
            # キーボードから入力を受ける
            # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
            ch = sys.stdin.read(1)

        finally:
            # fdの属性を元に戻す
            # 具体的にはICANONとECHOが元に戻る
            termios.tcsetattr(fd, termios.TCSANOW, old)

        return ch
