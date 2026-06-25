#!/usr/bin/env python3
# ============================================================================
#  飞 机 大 战  —— 手把手注释版
#  运  行：python plane_war.py
#  操  作：WASD / 方向键 = 移动    空格 = 开始     q = 退出
#  说  明：这份代码加了很多大白话注释，
#          没学过编程的人也能看懂每一行在干什么。
# ============================================================================

# ── 第一步：导入工具包 ──
#   下面这几行是「import」，相当于去工具箱里拿工具。
#   curses     = 终端画画工具（在命令行窗口里画图形）
#   time       = 时间工具（让程序能等一会儿、能算时间）
#   random     = 随机工具（让敌机随机出现）
#   math       = 数学工具（这里其实没用到，但不碍事）
import curses
import time
import random
import math


# ══════════════════════════════════════════════════════════════════════════
#  第二部分：飞机长什么样（造型数据）
# ══════════════════════════════════════════════════════════════════════════
#
#  游戏里的飞机不是图片，而是用键盘上的字符拼出来的。
#  下面这几行就是在设计飞机的样子。
#  每架飞机由好几行字符串组成，一行一行叠起来就是完整的飞机。
#

# ── 玩家的飞机 ──
#   用 3 行字符串拼成一架小飞机：
#     第1行: "  ^  "    → 机头（尖尖的箭头）
#     第2行: " /|\\ "   → 机身（斜杠是机翼，竖杠是机身）
#     第3行: "/ | \\"   → 机尾（更宽的机翼）
#   注意：字符串里的反斜杠 \ 在 Python 里要写成 \\ 才行。
P_ARTS = [
    "  ^  ",
    " /|\\ ",
    "/ | \\"
]
PW, PH = 5, 3   # 飞机宽5个字符，高3行

# ── 小敌机 ──
#   第1行: "\|/"    → 一个倒着的人形，像小鸟
#   第2行: " | "    → 机身
ES_ARTS = ["\\|/", " | "]
ESW, ESH = 3, 2    # 宽3字符，高2行

# ── 大敌机（更耐打） ──
#   比小敌机多了一行，更大更威武
EB_ARTS = ["\\|/", " | ", "/|\\"]
EBW, EBH = 3, 3    # 宽3字符，高3行

# ── 爆炸效果 ──
#   飞机被打爆时显示的图案（3行 x 3列的火花）
BOOM = [
    ["+", "|", "+"],
    ["*", "*", "*"],
    ["+", "|", "+"],
]


# ══════════════════════════════════════════════════════════════════════════
#  第三部分：游戏里的"东西"（类）
# ══════════════════════════════════════════════════════════════════════════
#
#  编程里的「class（类）」就像一张设计图纸。
#  图纸画好了，就能照着它做出好多份实体的「东西（对象）」。
#  比如 Player 类就是「玩家飞机图纸」，
#  用这张图纸可以造出一架具体的飞机放在游戏里。
#
#  每个类里都有：
#    - __init__  → 构造函数，就是"造东西时怎么造"的说明书
#    - 各种方法  → 这个东西能干什么
#


# ──────── 玩家飞机 ────────
class Player:
    """玩家的飞机
    
    属性（这架飞机有什么）：
      x, y  → 飞机在屏幕上的位置（左上角坐标）
      inv   → 无敌时间（被撞后有几帧画面是无敌的，数值越大无敌越久）
      cd    → 射击冷却（射完一发自冷却几帧才能再射）
    """
    def __init__(self, x, y):
        """造一架新飞机，摆到 (x, y) 位置"""
        self.x = x       # 飞机左上角在第几列
        self.y = y       # 飞机左上角在第几行
        self.inv = 0     # 无敌帧数（0 = 不无敌）
        self.cd = 0      # 射击冷却（0 = 可以射）

    def reset(self, x, y):
        """重置飞机，重新放到 (x, y) 位置"""
        self.x = x
        self.y = y
        self.inv = 0
        self.cd = 0


# ──────── 子弹 ────────
class Bullet:
    """一颗向上的子弹
    
    属性：
      x, y    → 子弹位置
      alive   → 是否还活着（True=还在飞，False=该消失了）
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True   # 刚射出来，当然是活着的


# ──────── 敌机 ────────
class Enemy:
    """一架敌机
    
    属性：
      x, y    → 敌机位置
      big     → 是否是大敌机（True=大，False=小）
      hp      → 血量（要打几下才爆）
      alive   → 是否还活着
    """
    def __init__(self, x, y, big):
        self.x = x
        self.y = y
        self.big = big              # 大小标志
        # 大敌机血多（2~3点），小敌机血少（1点）
        # random.randint(0,1) 随机出 0 或 1
        self.hp = 2 + random.randint(0, 1) if big else 1
        self.max_hp = self.hp       # 记录满血值（以后可能用来显示血条）
        self.alive = True


# ──────── 爆炸 ────────
class Explosion:
    """一团爆炸效果
    
    属性：
      x, y        → 爆炸中心位置
      frame       → 当前是第几帧（第几张画面）
      max_frame   → 总共显示几帧后消失
      alive       → 是否还在显示
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0          # 从第0帧开始
        self.max_frame = 8      # 一共显示8帧后消失
        self.alive = True

    def update(self):
        """每帧调用一次，让爆炸变老，到时间就消失"""
        self.frame += 1
        if self.frame >= self.max_frame:
            self.alive = False  # 到时间了，熄灭


# ══════════════════════════════════════════════════════════════════════════
#  第四部分：游戏主控中心（Game 类）
# ══════════════════════════════════════════════════════════════════════════
#
#  Game 类是整场游戏的"总导演"。
#  它管理着：
#    1. 游戏窗口画多大
#    2. 玩家、子弹、敌机、爆炸这些演员
#    3. 分数、生命、等级这些数据
#    4. 什么时候该更新画面、什么时候该检查碰撞
#    5. 游戏现在是"标题画面"还是"正在玩"还是"游戏结束"
#
class Game:
    # ── 初始化：布置舞台 ──
    def __init__(self, stdscr):
        """布置游戏舞台
        
        参数 stdscr 是 curses 给的"屏幕画板"，
        所有画图操作都是在这块画板上进行的。
        """
        self.scr = stdscr                # 保存画板
        self.h, self.w = stdscr.getmaxyx()  # 获取终端窗口的高(h)和宽(w)

        # ── 游戏区域 ──
        #   我们不在整个终端上画，只在中间画一个方框。
        #   方框的大小由 gw（宽）和 gh（高）决定。
        self.gw = min(34, self.w - 2)    # 游戏区宽度（最多34格）
        self.gh = min(22, self.h - 4)    # 游戏区高度（最多22行）
        self.gx = (self.w - self.gw) // 2  # 方框左上角的列坐标（居中）
        self.gy = 2                        # 方框左上角的行坐标

        # ── 游戏状态 ──
        #   state 有三个可能的值：
        #     "title"  → 标题画面（等待按空格开始）
        #     "play"   → 游戏中
        #     "over"   → 游戏结束（显示分数）
        self.state = "title"
        self.score = 0      # 得分
        self.lives = 3      # 生命数（3条命）
        self.level = 1      # 关卡等级（越高敌机越多越快）
        self.pause_timer = 0  # （暂时没用，留着以后做暂停用）

        # ── 创建演员 ──
        #   生成玩家飞机，放在游戏区底部中间
        self.player = Player(self.gw // 2, self.gh - 4)
        self.bullets = []      # 子弹列表（一开始没有子弹）
        self.enemies = []      # 敌机列表（一开始没有敌机）
        self.explosions = []   # 爆炸列表（一开始没有爆炸）
        self.fire_rate = 8     # 射击速度（每隔8帧射一次）

        # ── 按键状态 ──
        #   记录玩家按了哪些键。
        #   L=左, R=右, U=上, D=下, F=射击
        #   1 = 按着，0 = 没按
        self.keys = {"L": 0, "R": 0, "U": 0, "D": 0, "F": 0}
        self.move_cd = 0   # 移动冷却（控制飞机移动速度，值越大越慢）

    # ── 重置游戏 ──
    def reset(self):
        """重新开始一局（生命、分数、等级都归零）"""
        self.score = 0
        self.lives = 3
        self.level = 1
        self.player.reset(self.gw // 2, self.gh - 4)  # 飞机放回中间
        self.bullets.clear()       # 清空所有子弹
        self.enemies.clear()       # 清空所有敌机
        self.explosions.clear()    # 清空所有爆炸
        self.move_cd = 0           # 移动冷却归零
        self.state = "play"        # 切换到"游戏中"状态

    # ════════════════════════════════════════════════════════════════════
    #  生成函数（造子弹、造敌机、造爆炸）
    # ════════════════════════════════════════════════════════════════════

    # ── 开火（射子弹） ──
    def fire(self):
        """射出一轮子弹（三发散弹：左、中、右各一颗）"""
        if self.player.cd > 0:
            return  # 冷却中，不能射
        # 三颗子弹的位置：
        #   左：飞机最左边   →  self.player.x
        #   中：飞机正中间   →  self.player.x + 2
        #   右：飞机最右边   →  self.player.x + 4
        #   都从飞机头顶往上一格射出
        self.bullets.append(Bullet(self.player.x,     self.player.y - 1))
        self.bullets.append(Bullet(self.player.x + 2, self.player.y - 1))
        self.bullets.append(Bullet(self.player.x + 4, self.player.y - 1))
        self.player.cd = self.fire_rate  # 重置冷却，等几帧后才能再射

    # ── 生成敌机 ──
    def spawn_enemy(self):
        """随机生出一架敌机（可能是大的也可能是小的）"""
        # 判断是出大敌机还是小敌机
        # 等级越高，出大敌机的概率越大
        # 0.12 + level * 0.03  → 等级1时15%，等级10时42%
        big = random.random() < 0.12 + self.level * 0.03

        w = EBW if big else ESW   # 看是大的宽还是小的宽
        # 随机选一个水平位置（不让敌机贴着两边边框）
        x = random.randint(1, self.gw - w - 1)
        # 起始位置在屏幕上方外面（y为负数），这样敌机是"飞进来"的
        y = -ESH if not big else -EBH

        self.enemies.append(Enemy(x, y, big))

    # ── 生成爆炸 ──
    def spawn_explosion(self, x, y):
        """在 (x, y) 位置放一团爆炸特效"""
        self.explosions.append(Explosion(x, y))

    # ════════════════════════════════════════════════════════════════════
    #  碰撞检测（判断两个东西有没有撞到一起）
    # ════════════════════════════════════════════════════════════════════
    #
    #  碰撞检测的原理很简单：
    #    每个东西都有一个"包围盒"（就是它占的矩形区域）。
    #    两个矩形如果重叠了，就是撞上了。
    #
    #  参数说明：
    #    ax, ay = A物体的左上角坐标
    #    aw, ah = A物体的宽和高
    #    bx, by = B物体的左上角坐标
    #    bw, bh = B物体的宽和高
    #
    @staticmethod
    def hit(ax, ay, aw, ah, bx, by, bw, bh):
        """判断矩形A和矩形B是否重叠（即是否相撞）"""
        # 判断逻辑：
        #   A的右边 > B的左边  AND  A的左边 < B的右边  → 水平方向重叠
        #   AND
        #   A的下边 > B的上边  AND  A的上边 < B的下边  → 垂直方向重叠
        # 两个方向都重叠 = 撞上了！
        return (ax < bx + bw and ax + aw > bx and
                ay < by + bh and ay + ah > by)

    # ════════════════════════════════════════════════════════════════════
    #  更新逻辑（每帧都跑一遍，让游戏世界前进一步）
    # ════════════════════════════════════════════════════════════════════
    #
    #  游戏不是一直往前跑的，而是一帧一帧地"跳"。
    #  就像动画片一样，每秒钟显示好多张静止的画面，
    #  每张画面之间只变化一点点，看起来就是连贯的。
    #
    #  update() 函数就是负责计算"每一帧之间发生了什么变化"：
    #    1. 玩家有没有按方向键？→ 移动飞机
    #    2. 冷却时间有没有减少？→ 减少冷却
    #    3. 子弹是不是该往上走了？→ 移动子弹
    #    4. 是不是该出新敌机了？→ 生成敌机
    #    5. 敌机往下走了没？→ 移动敌机
    #    6. 子弹打中敌机了没？→ 扣血/打爆
    #    7. 敌机撞到玩家了没？→ 扣命/游戏结束
    #    8. 爆炸效果是不是该消失了？→ 清除爆炸
    #
    def update(self):
        """更新一帧：让所有东西动一步"""
        # 如果不是"游戏中"状态，啥也不做
        if self.state != "play":
            return

        # ── 1. 冷却倒计时 ──
        #    射击冷却和无敌时间，每帧减少1
        if self.player.cd > 0:
            self.player.cd -= 1    # 射击冷却减1
        if self.player.inv > 0:
            self.player.inv -= 1   # 无敌时间减1

        # ── 2. 移动玩家飞机 ──
        #    为了不让飞机跑太快，我们加了一个"移动冷却"（move_cd）。
        #    只有 move_cd 到 0 时才能移动，移动后把 move_cd 设成 8，
        #    这样飞机会每9帧才能动一格，非常缓慢。
        if self.move_cd > 0:
            self.move_cd -= 1       # 移动冷却减1
        else:
            moved = False           # 记录有没有移动过
            # 按左键 且 飞机没贴左边墙 → 往左移一格
            if self.keys["L"] and self.player.x > 1:
                self.player.x -= 1; moved = True
            # 按右键 且 飞机没贴右边墙 → 往右移一格
            if self.keys["R"] and self.player.x < self.gw - PW - 1:
                self.player.x += 1; moved = True
            # 按上键 且 飞机没贴顶 → 往上移一格
            if self.keys["U"] and self.player.y > 2:
                self.player.y -= 1; moved = True
            # 按下键 且 飞机没贴底 → 往下移一格
            if self.keys["D"] and self.player.y < self.gh - PH - 1:
                self.player.y += 1; moved = True
            # 如果确实移动了，就重置移动冷却，下次要等8帧才能再动
            if moved:
                self.move_cd = 8

        # ── 3. 自动射击 ──
        #    只要冷却结束了就自动开火，不用玩家按空格
        if self.player.cd == 0:
            self.fire()

        # ── 4. 子弹往上飞 ──
        for b in self.bullets:
            b.y -= 1                # 子弹向上移一格（y越小越靠上）
            if b.y < 0:
                b.alive = False     # 超出屏幕上方，子弹消失
        # 只保留还活着的子弹（死掉的子弹从列表中移除）
        self.bullets = [b for b in self.bullets if b.alive]

        # ── 5. 随机生成敌机 ──
        #    rate 控制敌机出现的频率：
        #      等级1 → rate=11，每12帧（约1.2秒）可能出一架
        #      等级10 → rate=2，每3帧（约0.3秒）可能出一架
        #    等级越高，敌机出现越频繁！
        rate = max(2, 12 - self.level)
        if random.randint(0, rate) == 0:
            self.spawn_enemy()

        # ── 6. 敌机往下飞 ──
        for e in self.enemies:
            # 敌机下落速度：
            #   小敌机：1 + level//5  （等级高会变快）
            #   大敌机：1 + level//8  （大敌机稍微慢一点）
            sp = 1 + self.level // 8 if e.big else 1 + self.level // 5
            e.y += sp                # 敌机向下移
            if e.y > self.gh + 2:
                e.alive = False      # 飞出屏幕底部，消失
        self.enemies = [e for e in self.enemies if e.alive]

        # ── 7. 子弹打中敌机了吗？ ──
        #    双重循环：每颗子弹 vs 每架敌机
        for b in self.bullets:
            if not b.alive:
                continue              # 子弹死了，跳过
            for e in self.enemies:
                if not e.alive:
                    continue          # 敌机死了，跳过
                w, h = (EBW, EBH) if e.big else (ESW, ESH)
                # 调用碰撞检测函数
                if self.hit(b.x, b.y, 1, 1, e.x, e.y, w, h):
                    b.alive = False   # 子弹消失（打中了）
                    e.hp -= 1         # 敌机扣血
                    if e.hp <= 0:     # 血扣完了 → 敌机爆炸
                        e.alive = False
                        # 在敌机中央放爆炸特效
                        self.spawn_explosion(e.x + w // 2, e.y + h // 2)
                        # 加分：大敌机30分，小敌机10分
                        self.score += 30 if e.big else 10
                        # 升级：每60分升一级
                        nl = self.score // 60 + 1
                        if nl > self.level:
                            self.level = nl
                    break             # 一颗子弹只打中一架敌机
        # 清理死掉的子弹和敌机
        self.bullets = [b for b in self.bullets if b.alive]
        self.enemies = [e for e in self.enemies if e.alive]

        # ── 8. 敌机撞到玩家了吗？ ──
        #    只有不在无敌状态时才判断
        if self.player.inv == 0:
            for e in self.enemies:
                if not e.alive:
                    continue
                w, h = (EBW, EBH) if e.big else (ESW, ESH)
                if self.hit(self.player.x, self.player.y, PW, PH,
                            e.x, e.y, w, h):
                    e.alive = False   # 敌机消失
                    # 玩家位置爆炸
                    self.spawn_explosion(self.player.x + 2, self.player.y + 1)
                    self.lives -= 1   # 扣一条命
                    self.player.inv = 40  # 40帧无敌（约4秒）
                    if self.lives <= 0:
                        self.state = "over"  # 没命了，游戏结束
                        self.spawn_explosion(self.player.x + 2, self.player.y + 1)
                    break
        self.enemies = [e for e in self.enemies if e.alive]

        # ── 9. 爆炸效果更新 ──
        #    让每团爆炸往前走一帧，到时间了就熄灭
        for ex in self.explosions:
            ex.update()
        self.explosions = [e for e in self.explosions if e.alive]

    # ════════════════════════════════════════════════════════════════════
    #  绘制画面（在终端上画出游戏画面）
    # ════════════════════════════════════════════════════════════════════
    #
    #  render() 就像一位画家，每帧都把整个画面重画一遍：
    #    1. 先清空画板
    #    2. 画边框（方框）
    #    3. 画顶部的分数/生命/等级
    #    4. 画子弹（竖线 | ）
    #    5. 画敌机（用 ASCII 字符拼）
    #    6. 画爆炸（火花特效）
    #    7. 画玩家飞机
    #    8. 画底部的提示文字
    #
    def render(self):
        """绘制一帧画面"""
        self.scr.clear()   # 1. 清空画板，从头画起

        # 计算游戏区在屏幕上的实际位置
        ox, oy = self.gx, self.gy   # 偏移量

        # ── 画边框 ──
        #    四角用 "+"，横线用 "-"，竖线用 "|"
        border_style = curses.A_NORMAL
        self.scr.addch(oy, ox, '+', border_style)                         # 左上角
        self.scr.addch(oy, ox + self.gw - 1, '+', border_style)           # 右上角
        self.scr.addch(oy + self.gh - 1, ox, '+', border_style)           # 左下角
        self.scr.addch(oy + self.gh - 1, ox + self.gw - 1, '+', border_style)  # 右下角
        for x in range(1, self.gw - 1):
            self.scr.addch(oy, ox + x, '-', border_style)              # 上横线
            self.scr.addch(oy + self.gh - 1, ox + x, '-', border_style)  # 下横线
        for y in range(1, self.gh - 1):
            self.scr.addch(oy + y, ox, '|', border_style)              # 左竖线
            self.scr.addch(oy + y, ox + self.gw - 1, '|', border_style)  # 右竖线

        # ── 画顶部信息栏 ──
        #    显示：SCORE:分数  LV:等级  ♥♥♥（红心表示生命）
        info = " SCORE:%05d  LV:%d " % (self.score, self.level)
        hearts = "♥" * self.lives + "♡" * (3 - self.lives)  # 实心心+空心心
        info += hearts
        for i, c in enumerate(info):
            if i + 1 < self.gw - 1:
                try:
                    self.scr.addch(oy, ox + i + 1, c)
                except:
                    pass  # 怕出界，画不进去就算了

        # ── 画子弹 ──
        #    子弹用竖线 "|" 表示
        for b in self.bullets:
            if 0 <= b.y < self.gh - 1 and 1 <= b.x < self.gw - 1:
                try:
                    self.scr.addch(oy + b.y + 1, ox + b.x + 1, '|')
                except:
                    pass

        # ── 画敌机 ──
        #    按敌机的造型数组，一个字符一个字符地画
        for e in self.enemies:
            w, h = (EBW, EBH) if e.big else (ESW, ESH)
            arts = EB_ARTS if e.big else ES_ARTS
            for dy in range(h):          # 遍历每一行
                for dx in range(w):      # 遍历每一列
                    ch = arts[dy][dx]
                    if ch != ' ':        # 空格不画（透明部分）
                        sx = ox + e.x + dx + 1
                        sy = oy + e.y + dy + 1
                        if 0 < e.y + dy < self.gh - 1 and 0 < e.x + dx < self.gw - 1:
                            try:
                                if e.big:
                                    # 大敌机用粗体显示（更显眼）
                                    self.scr.addch(sy, sx, ch, curses.A_BOLD)
                                else:
                                    self.scr.addch(sy, sx, ch)
                            except:
                                pass

        # ── 画爆炸 ──
        #    爆炸每2帧换一个字符：* → + → o → . 循环
        for ex in self.explosions:
            r = ex.frame // 2
            chars = ["*", "+", "o", "."]
            ch = chars[r % 4] if r < len(chars) else '.'
            # 3x3 的爆炸范围
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    sx = ox + ex.x + dx + 1
                    sy = oy + ex.y + dy + 1
                    if 0 < ex.y + dy < self.gh - 1 and 0 < ex.x + dx < self.gw - 1:
                        try:
                            self.scr.addch(sy, sx, ch)
                        except:
                            pass

        # ── 画玩家飞机 ──
        if self.state == "play":
            # 无敌时闪烁：每隔3帧切换显/隐
            show = not (self.player.inv > 0 and (self.player.inv // 3) % 2 == 0)
            if show:
                for dy in range(PH):
                    for dx in range(PW):
                        ch = P_ARTS[dy][dx]
                        if ch != ' ':
                            sx = ox + self.player.x + dx + 1
                            sy = oy + self.player.y + dy + 1
                            if 0 < self.player.y + dy < self.gh - 1 and 0 < self.player.x + dx < self.gw - 1:
                                try:
                                    # 玩家飞机用粗体，更醒目
                                    self.scr.addch(sy, sx, ch, curses.A_BOLD)
                                except:
                                    pass

        # ── 画底部提示文字 ──
        bottom = oy + self.gh   # 游戏框的下一行

        if self.state == "title":
            # 标题画面：显示游戏名和操作说明
            title = "  P L A N E   W A R  "
            tx = (self.w - len(title)) // 2
            try:
                self.scr.addstr(bottom, tx, title, curses.A_BOLD)
            except:
                pass
            sub = "Space to Start  |  q to Quit"
            sx2 = (self.w - len(sub)) // 2
            try:
                self.scr.addstr(bottom + 1, sx2, sub)
            except:
                pass
            sub2 = "WASD/Arrows Move  Auto Fire"
            sx3 = (self.w - len(sub2)) // 2
            try:
                self.scr.addstr(bottom + 2, sx3, sub2)
            except:
                pass

        elif self.state == "over":
            # 游戏结束画面：显示 Game Over 和分数
            msg = "  GAME OVER  "
            mx = (self.w - len(msg)) // 2
            try:
                self.scr.addstr(bottom, mx, msg, curses.A_BOLD)
            except:
                pass
            sc = "Score: %d" % self.score
            sx2 = (self.w - len(sc)) // 2
            try:
                self.scr.addstr(bottom + 1, sx2, sc)
            except:
                pass
            again = "Space to Restart  |  q to Quit"
            ax = (self.w - len(again)) // 2
            try:
                self.scr.addstr(bottom + 2, ax, again)
            except:
                pass

        elif self.state == "play":
            # 游戏中：底部显示简单提示
            hint = "Arrows/WASD move  Space fire"
            hx = (self.w - len(hint)) // 2
            try:
                self.scr.addstr(bottom, hx, hint)
            except:
                pass

        # 把画好的内容真正显示到屏幕上
        self.scr.refresh()

    # ════════════════════════════════════════════════════════════════════
    #  输入处理（读取玩家的按键）
    # ════════════════════════════════════════════════════════════════════
    #
    #  每帧开始前，程序会问终端："玩家有没有按键？按了哪些？"
    #  然后把按下的键记录下来，供 update() 使用。
    #
    #  poll_input 的意思是"轮询输入"，
    #  就像快递员一直问"有没有我的快递？"一样。
    #
    def poll_input(self):
        """轮询所有待处理的按键，更新按键状态表"""
        # 先把所有键设为"没按"，然后根据实际按键再设为"按了"
        self.keys = {"L": 0, "R": 0, "U": 0, "D": 0, "F": 0}

        # 循环读取所有待处理的按键（可能同时按了多个）
        while True:
            key = self.scr.getch()    # 问终端：有按键吗？
            if key == -1:
                break                 # -1 表示没有按键，退出循环

            # q 键 → 退出游戏
            if key == ord('q'):
                return False

            # 空格键 → 开始游戏 / 重新开始 / 手动射一发
            if key == ord(' '):
                if self.state == "title":
                    self.reset()            # 标题画面 → 开始游戏
                elif self.state == "over":
                    self.reset()            # 游戏结束 → 重新开始
                elif self.state == "play":
                    self.fire()             # 游戏中 → 额外射一发
            if key == ord(' '):
                self.keys["F"] = 1          # 标记"射击键被按了"

            # 方向键 / WASD → 移动
            if key == curses.KEY_LEFT or key == ord('a'):
                self.keys["L"] = 1
            if key == curses.KEY_RIGHT or key == ord('d'):
                self.keys["R"] = 1
            if key == curses.KEY_UP or key == ord('w'):
                self.keys["U"] = 1
            if key == curses.KEY_DOWN or key == ord('s'):
                self.keys["D"] = 1

        return True  # 继续游戏（返回 False 就退出）

    # ════════════════════════════════════════════════════════════════════
    #  主循环（游戏引擎的"心脏"）
    # ════════════════════════════════════════════════════════════════════
    #
    #  游戏就像一台永动机，一直在重复做三件事：
    #    1. 读按键（你按了什么？）
    #    2. 更新逻辑（飞机移动、子弹飞行、碰撞检查...）
    #    3. 渲染画面（把最新状态画到屏幕上）
    #
    #  然后休息一小会儿（sleep），再重复下一轮。
    #  这个"读键→更新→画图→等待"的循环就叫「游戏主循环」。
    #
    #  每秒钟循环的次数叫 FPS（帧率）。
    #  这里我们每帧等 0.1 秒，所以一秒大约跑 10 帧。
    #
    def run(self):
        """游戏主循环：永不停歇，直到玩家按 q 退出"""
        while True:
            # 第一步：读按键
            if not self.poll_input():
                break        # poll_input 返回 False = 按了 q，退出

            # 第二步：更新游戏逻辑
            self.update()

            # 第三步：绘制画面
            self.render()

            # 休息 0.1 秒（控制游戏速度，太快了人反应不过来）
            time.sleep(0.1)


# ══════════════════════════════════════════════════════════════════════════
#  第五部分：启动游戏（入口函数）
# ══════════════════════════════════════════════════════════════════════════
#
#  main() 是游戏的"大门"。
#  当你在终端里输入 python plane_war.py 时，
#  程序就从这个函数开始执行。
#
#  curses.wrapper(main) 是 curses 提供的一个"保姆"，
#  它会帮我们：
#    1. 进入"全屏模式"（隐藏光标、禁用回显）
#    2. 运行 main() 函数
#    3. 退出时自动恢复终端原样（光标显示、回显恢复）
#  这样就算游戏崩溃了，终端也不会被搞乱。
#
def main(stdscr):
    """游戏入口：设置终端环境，启动游戏"""
    # 隐藏光标（不让那个闪烁的小方块碍眼）
    curses.curs_set(0)
    # 设置非阻塞模式（getch() 如果没有按键，立即返回 -1，不等）
    stdscr.nodelay(1)

    # 创建游戏对象（搭好舞台）
    game = Game(stdscr)
    # 先画一帧（显示标题画面）
    game.render()

    # 运行游戏（进入主循环）
    try:
        game.run()
    except KeyboardInterrupt:
        pass  # Ctrl+C 也能退出，不会报错


# ── 最后一行：程序的真正入口 ──
#   这句话的意思是：
#     如果这个文件是被直接运行的（python plane_war.py），
#     就执行 curses.wrapper(main) 启动游戏。
#     如果这个文件是被别的程序"导入"的，就不自动运行。
if __name__ == "__main__":
    curses.wrapper(main)
