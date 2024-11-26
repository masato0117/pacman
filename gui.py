from tkinter import Tk, Frame


class Gui:
    """Guiクラス
    Guiクラスではゲームに関する情報をGUIとして別ウィンドウに表示する．
    """

    def display_gui(self):
        root = Tk()  # この下に画面構成を記述
        # ----------- ①Window作成 ----------- #
        root.title('tkinterの使い方')   # 画面タイトル設定
        root.geometry('360x360')        # 画面サイズ設定

        i = 0
        frame_list = []
        for x in range(13):
            for y in range(13):
                frame = Frame(root, width=30, height=30, bg='Gray')
                frame.num = i
                frame_list.append(frame)
                frame.grid(row=x, column=y)
                i += 1
        root.mainloop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
