from item import Item
from player import Player
from wall import Wall
from block import Block
from enemy import Enemy
from food import Food


class Field:
    """Fieldクラス
    Fieldクラスではゲームフィールドを生成し表示するクラスである．
    プレイヤー，敵，物体の位置を更新し，フィールド上に表示する機能を持つ．
    位置を更新する際に衝突判定をする．

    Attributes:
        players (list[Player]): プレイヤー情報
        blocks (list[Block]): アイテムのリスト
        enemies (list[Enemy]): 敵の情報
        weapons (list[Weapon]): 武器情報
        fields (list[list[str]]): フィールド情報
        field_size (int): フィールドサイズ
    """

    # フィールドを生成する関数
    def __init__(
            self,
            players: list[Player],
            walls: list[Wall],
            blocks: list[Block],
            enemies: list[Enemy],
            foods: list[Food],
            f_size: int = 6):

        """
        Fieldクラスの初期化をする関数

        Args:
            players (list[Player]): プレイヤー情報
            walls (list[Wall]): 壁のリスト
            blocks (list[Block]): 障害物のリスト
            enemies (list[Enemy]): 敵の情報
            weapons (list[weapon]): 武器情報
            field_size (int): フィールドサイズ
        """

        self.f_size = f_size
        self.field = [[" " for _ in range(f_size)] for _ in range(f_size)]
        self.players = players
        self.walls = walls
        self.blocks = blocks
        self.enemies = enemies
        self.foods = foods

        # それぞれのアイテムの位置をFieldに更新する関数
        self.update_field()

    def update_field(self) -> list[list[str]]:

        """
        プレイヤー，敵，物体の位置を参照して，フィールドを更新する関数

        Returns:
            list[list[str]]: 更新されたフィールド

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> w = [Wall(0, 0)]
            >>> w[0].icon = "w1"
            >>> b1 = Block(0, 2)
            >>> b1.icon = "b1"
            >>> b2 = Block(1, 2)
            >>> b2.icon = "b2"
            >>> b = [b1, b2]
            >>> e1 = Enemy(2, 0)
            >>> e1.icon = "e1"
            >>> e2 = Enemy(1, 1)
            >>> e2.icon = "e2"
            >>> e = [e1, e2]
            >>> f = [Food(0, 1)]
            >>> f[0].icon = "f1"
            >>> field = Field(p, w, b, e, f, 3)
            >>> field.update_field()[0]
            ['w1', 'p1', 'e1']
            >>> field.update_field()[1]
            ['f1', 'e2', '\\u3000']
            >>> field.update_field()[2]
            ['b1', 'b2', '\\u3000']
        """

        # フィールドの最大サイズを保存
        max_size = len(self.field)
        # フィールドを全て空白にする
        for i in range(max_size):
            for j in range(max_size):
                self.field[i][j] = "　"
        # フィールドを更新する処理を記述
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        for wall in self.walls:
            if wall.status:
                self.field[wall.now_y][wall.now_x] = wall.icon
        for block in self.blocks:
            if block.status:
                self.field[block.now_y][block.now_x] = block.icon
        for enemy in self.enemies:
            if enemy.status:
                self.field[enemy.now_y][enemy.now_x] = enemy.icon
        for food in self.foods:
            if food.status:
                self.field[food.now_y][food.now_x] = food.icon
        return self.field

    # フィールドを表示する関数
    def display_field(self) -> None:

        """
        フィールドを表示する関数

        Example:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> w = [Wall(0, 0)]
            >>> w[0].icon = "w1"
            >>> b1 = Block(0, 2)
            >>> b1.icon = "b1"
            >>> b2 = Block(1, 2)
            >>> b2.icon = "b2"
            >>> b = [b1, b2]
            >>> e1 = Enemy(2, 0)
            >>> e1.icon = "e1"
            >>> e2 = Enemy(1, 1)
            >>> e2.icon = "e2"
            >>> e = [e1, e2]
            >>> f = [Food(0, 1)]
            >>> f[0].icon = "f1"
            >>> field = Field(p, w, b, e, f, 3)
            >>> field.display_field()
            w: 1マス上に移動
            a: 1マス左に移動
            s: 1マス下に移動
            d: 1マス右に移動
            w1p1e1
            f1e2　
            b1b2　
        """

        # 動き方を表示
        print("w: 1マス上に移動")
        print("a: 1マス左に移動")
        print("s: 1マス下に移動")
        print("d: 1マス右に移動")

        # self.fieldを表示する処理を記述
        max_width = max(len(row) for row in self.field)

        for row in self.field:
            # 各行の文字列を作成し，不足部分を空白で埋める
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)

    # 衝突判定をする関数
    def collision(
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
            >>> field = Field([p], [], [], [e], [])
            >>> p.next_x = 1
            >>> r = field.collision(p, [e])
            >>> r is None
            True
            >>> p.next_y = 1
            >>> r = field.collision(p, [e])
            >>> r is e
            True
        """

        # 衝突判定をする処理を記述
        for item in items:
            if item.next_x == target.next_x and item.next_y == target.next_y:
                return item
        return None

    # 特別な衝突処理をする関数
    def post_collision_processing(
            self,
            items: list[Item],
            kind: int = 1,
            collision_count: int = 0) -> None:
        """
        プレイヤー，敵，物体の位置が重なっているか判定する関数
            Args:
            items (list[Item]): アイテム
            kind (int = 1): プレイヤーか敵のどちらが呼び出されたかを判別
            collision_count (int = 0): この関数が呼び出された回数

        Returns:
            None

        Examples:
            >>> p = Player(1, 1)
            >>> e = Enemy(1, 2)
            >>> w1 = Wall(0, 1)
            >>> w2 = Wall(0, 2)
            >>> w = [w1, w2]
            >>> b1 = Block(2, 1)
            >>> b2 = Block(2, 2)
            >>> b = [b1, b2]
            >>> field = Field([p], w, b, [e], [], 6)
            >>> p.next_x = 2
            >>> field.post_collision_processing([p], 1)
            >>> p.now_x == 1
            True
            >>> p.next_x = 0
            >>> field.post_collision_processing([p], 1)
            >>> p.now_x == 4
            True
            >>> e.next_x = 0
            >>> field.post_collision_processing([e], 2)
            >>> e.next_x == 1
            True
            >>> e.next_x = 2
            >>> field.post_collision_processing([e], 2)
            >>> e.next_x == 3
            True
        """

        for item in items:
            # 障害物，壁との衝突判定
            collided_block = self.collision(item, list(self.blocks))
            collided_wall = self.collision(item, list(self.walls))
            # プレイヤーが壁に衝突した場合
            if collided_wall and kind == 1:
                item.update_special_pos(int(len(self.field)), kind)
                self.post_collision_processing(list(items), kind)
            # 敵が障害物に衝突した場合
            elif collided_block and kind == 2:
                # 複数回衝突した場合
                if collision_count > 0:
                    item.update_pos(stuck=True)
                # 初めて障害物に衝突した場合
                else:
                    collision_count = collision_count + 1
                    item.update_special_pos(int(len(self.field)), kind)
                    self.post_collision_processing(list(items),
                                                   kind,
                                                   collision_count)
            # プレイヤーが障害物に，敵が壁に衝突した場合
            elif collided_wall and kind == 2 or collided_block and kind == 1:
                item.update_pos(stuck=True)
            # どれにも当てはまらない場合，位置を更新
            else:
                item.update_pos()
        return None

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
