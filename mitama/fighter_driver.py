from gameLib.fighter import Fighter
from tools.game_pos import CommonPos, YuhunPos
import tools.utilities as ut

import logging
import time


class DriverFighter(Fighter):
    """
    御魂战斗司机程序，参数mode, emyc
    """

    def __init__(self, emyc=0, hwnd=0, needMark=False, passengerNum=2):
        # 初始化
        Fighter.__init__(self, 'Driver: ', emyc, hwnd)
        self.needMark = needMark
        self.passengerNum = passengerNum
        # 第一次点击挑战
        self.firstClickTiaoZhan = True

    def start(self):
        '''单人御魂司机'''
        # 设定点击疲劳度
        mood1 = ut.Mood()
        mood2 = ut.Mood()
        mood3 = ut.Mood(3)

        # 战斗主循环
        self.yys.wait_game_img('img\\KAI-SHI-ZHAN-DOU.png',
                               self.max_win_time)
        while self.run:
            # 司机点击开始战斗，需要锁定御魂阵容
            mood1.moodsleep()
            if self.passengerNum == 2:
                self.log.writeinfo('Driver: 等待1位乘客上车')
                self.click_until('开始战斗按钮', 'img\\ZI-DONG.png', *
                YuhunPos.TiaoZhanBtn, mood2.get1mood() / 1000)
                self.log.writeinfo('Driver: 已进入战斗')
            elif self.passengerNum == 3:
                self.log.writeinfo('Driver: 等待2位乘客上车')
                # if self.firstClickTiaoZhan is True:
                #     print('第一次挑战')
                #     time.sleep(1)
                #     self.firstClickTiaoZhan = False
                #     self.yys.mouse_click_bg(*YuhunPos.TiaoZhanBtn)
                # else:
                self.yys.wait_game_img('img\\JIA-CHENG.png')
                # print('加成按钮已经出现')
                self.yys.mouse_click_bg(*YuhunPos.TiaoZhanBtn)
                # self.click_until('开始战斗按钮', 'img\\DUI-YOU-JIA-HAO.png', *
                # YuhunPos.TiaoZhanBtn, mood2.get1mood() / 1000, appear=False)
                # print('点击挑战按钮成功')

            # logging.info('御魂司机的needmark为{}'.format(self.needMark))

            if self.needMark is True:
                # todo 点击大舅妈
                logging.info('等待点击大舅妈,坐标{}'.format(self.ShiShenPos))
                self.log.writeinfo('Driver: 等待点击式神')
                # self.click_once_if_appear('点击式神','img\\YI-HUI-MU.png',
                # *YuhunPos.大舅妈位置,mood2.get1mood() / 1000)
                self.yys.wait_game_img('img\\YI-HUI-MU.png')
                self.click_once_if_appear('式神','img\\YI-HUI-MU.png',self.ShiShenPos,None,1,True)
                # self.click_until('式神', 'img\\ZHUN-BEI.png',
                #                           self.ShiShenPos, pos_end=None, step_time=mood2.get1mood() / 1000,appear=False)
            # 检测是否打完
            self.check_end()
            mood2.moodsleep()

            # 在战斗结算页面
            self.click_until('结算', 'img/JIN-BI.png',
                             *CommonPos.second_position, mood3.get1mood() / 1000)
            self.click_until('结算', 'img/JIN-BI.png',
                             *CommonPos.second_position, mood3.get1mood() / 1000, False)

            # 等待下一轮
            logging.info('Driver: 等待下一轮')
            start_time = time.time()
            while time.time() - start_time <= 20 and self.run:
                if (self.yys.wait_game_img('img\\KAI-SHI-ZHAN-DOU.png', 1, False)):
                    self.log.writeinfo('Driver: 进入队伍')
                    break

                # 点击默认邀请
                if self.yys.find_game_img('img\\ZI-DONG-YAO-QING.png'):
                    self.yys.mouse_click_bg((497, 319))
                    time.sleep(0.2)
                    self.yys.mouse_click_bg((674, 384))
                    self.log.writeinfo('Driver: 自动邀请')
