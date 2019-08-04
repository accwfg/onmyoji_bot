**目前已开通项目网站，请访问[此地址](https://academicdog.github.io/onmyoji_bot/)获取最新信息。**

![avatar](https://raw.githubusercontent.com/AcademicDog/myresource/master/usage.png)

# 特别感谢
特别感谢society765在本项目中给与的启发，本项目在其[工作基础](https://github.com/society765/yys-auto-yuhun)上修改完成。

同时感谢sup817ch的图像识别思路，本项目game_ctl模块基于其[工作基础](https://github.com/sup817ch/AutoOnmyoji)。

# 使用说明

环境：python 3.7, 32 bit；yys PC端 默认分辨率 (1136x640)；win 10系统，屏幕(1920x1080)，显示设置100%。

1、该脚本可以用于阴阳师御魂、业原火、御灵、探索等单刷或双人组队，适用于PC端；

2、窗口现在可以完全后台，可以被遮挡，但是不能最小化，不能最小化，不能最小化；

3、玩家需要提前准备好战斗阵容，阵容需要锁定；

4、在战斗过程中，该脚本会自动拒绝所有悬赏封印的邀请；

5、本人只测试过魂十、探索，其他请自测；

6、如果60s程序没有任何操作，视为体力用光，为了保护加成，自动关闭YYS；

7、该脚本仅使用了画面找色，鼠标后台点击的函数，完全模拟人类玩家行为，没有使用任何内存读写函数。在敏感位置添加了均匀分布的随机时间漂移，和随机坐标漂移；


# 注意事项
1、点怪目前不可用，因为有的模型太大，挡住了点怪图标；

2、当使用 Windows 7 系统时，需要调整系统的画面设置：把主题调为最丑最挫的那个。在 Windows 10 系统中，不需要调整系统画面设置；

3、当使用高分辨率屏幕时，在阴阳师客户端程序兼容性选项里，不要勾选"替代高DPI缩放行为"，这个选项应该是默认不勾选的；

4、建议使用脚本时，去到人比较稀少的频道，以免点开路人对话框；

5、请关闭模型描边。

6、如果不想安装运行环境，可以访问下载最新已[编译](https://github.com/AcademicDog/onmyoji_bot/releases)版本，该版本有图形界面，同时注意.exe文件和/img文件夹应该放在同一目录后再运行。


# 更新说明
v1.0.0.0619--抛弃dll插件，用win32api，同时用图像识别替代简单找色。

v1.0.0.0621--修改了完成战斗后，等待时间重复计算的bug，同时移除了不必要的参数设置。

v1.0.0.06211--根据[#2](https://github.com/AcademicDog/onmyoji_bot/issues/2)，增加了对已编译文件使用的说明，同时将/img文件夹一起打包发布。

v1.0.0.0622--根据[#3](https://github.com/AcademicDog/onmyoji_bot/issues/3)，优化了乘客结算代码；将原先的灰度图像识别更改为彩色图像识别；在结算失败时，通过激活窗口来提醒玩家。

v1.0.0.0623--调整了结算时开蛋的点击，现在不会在主界面仍然无脑点击了，同时优化了司机结算代码，移除了激活窗口代码。

v1.0.0.0625--增加了UI，目前在ui分支中。

v1.0.0.0707--根据[#4](https://github.com/AcademicDog/onmyoji_bot/issues/4)，调整了UI设计。

v1.0.0.0710--增加了单人探索的代码。

v1.0.0.0711--根据[#5](https://github.com/AcademicDog/onmyoji_bot/issues/5)，调整了结算点击位置。

v1.0.0.0724--优化了探索代码。

v1.0.0.0728--根据[#6](https://github.com/AcademicDog/onmyoji_bot/issues/6)，优化了满级狗粮识别代码。

v1.0.0.0804--增加了探索完成后打BOSS的代码。

# 协议 (License)

该源代码使用了 [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) 开源协议。

This project is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) license.