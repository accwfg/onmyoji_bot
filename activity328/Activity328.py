import random
import threading

import tools.utilities as ut
from gameLib.fighter import Fighter
from gameLib.game_ctl import GameControl


class Activity328(Fighter):
    def __init__(self, done=1, emyc=0):
        # 初始化
        Fighter.__init__(self, '', emyc)

    def start(self):
        '''单人战斗主循环'''
        while self.run:
            self.log.writeinfo(self.name + '开始寻找是否有车')
            # 等待一个小时
            self.yys.wait_game_img(r'img/MIJING.png',
                                              60 * 60)

            position = self.yys.wait_game_img(r'img/JIN-RU.png',
                                              10)
            self.log.writeinfo(self.name + '找到车了')
            self.yys.mouse_click_bg(position)
            threading.sleep(random.randint(100, 200))
