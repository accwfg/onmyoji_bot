from gameLib.game_ctl import GameControl
from mitama.fighter_driver import DriverFighter
from mitama.fighter_passenger import FighterPassenger
from tools.logsystem import WriteLog

import logging
import threading
import win32gui

hwndlist = []


def get_all_hwnd(hwnd, mouse):
    '''
    获取所有阴阳师窗口
    '''
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        if win32gui.GetWindowText(hwnd) == u'阴阳师-网易游戏':
            hwndlist.append(hwnd)


def get_game_hwnd():
    win32gui.EnumWindows(get_all_hwnd, 0)


class ThreePerson():
    def __init__(self,needMark=False):
        # 初始化窗口信息
        try:
            get_game_hwnd()
            self.hwndlist = hwndlist
            # 检测窗口信息是否正确
            num = len(self.hwndlist)
            if num == 3:
                logging.info('检测到三个窗口，窗口信息正常')
            else:
                logging.info('检测到' + str(num) + '个窗口，窗口信息异常！脚本停止')
                hwndlist.clear()
                return None


            # 初始化司机和打手
            for hwnd in hwndlist:
                yys = GameControl(hwnd)
                if yys.find_game_img('img\\KAI-SHI-ZHAN-DOU.png'):
                    self.driver = DriverFighter(hwnd=hwnd, needMark=needMark, passengerNum=3)
                    hwndlist.remove(hwnd)
                    logging.info('发现司机')
            self.passengerOne = FighterPassenger(hwnd=hwndlist[0])
            self.passengerTwo = FighterPassenger(hwnd=hwndlist[1])
            logging.info('发现两个乘客')
        except IndexError :
            logging.info('游戏窗体检测出现异常')


    def start(self):
        try:
            task1 = threading.Thread(target=self.driver.start)
            task2 = threading.Thread(target=self.passengerOne.start)
            task3 = threading.Thread(target=self.passengerThree.start)
            task1.start()
            task2.start()
            task3.start()
            # task1.join()
            # task2.join()
        except AttributeError:
            logging.error('游戏异常,请检查游戏是否运行')

    def deactivate(self):
        # 停止脚本后需要移除所有获取的窗体句柄
        hwndlist.clear()
        self.driver.deactivate()
        self.passenger.deactivate()
