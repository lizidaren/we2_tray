import threading
from tkinter import Tk
from tkinter import simpledialog as sd
from tkinter import filedialog as fd

import pystray
from PIL import Image
from pystray import MenuItem, Menu
import os
from ctypes import windll

from we2_timer import generate

APP_NAME = "倒计时壁纸"
APP_VERSION = 1.0

# 读入配置
first_start = False
config = []
if os.path.exists("./we2_cfg.txt"):
	with open("./we2_cfg.txt", encoding="utf-8") as f:
		content = f.read().split("\n")
	if len(content) != 6:
		# 配置文件错误，视为重新配置
		first_start = True
	else:
		config = content[:]
		config[2] = int(config[2])
else:
	first_start = True

# 设置壁纸
# 注意这里设置的壁纸重启后失效
def set_wallpaper(path):
	windll.user32.SystemParametersInfoW(20,0,path,0)

# 更新壁纸（托盘点击）
def update_wallpaper(*args):
	generate(*config)
	set_wallpaper(os.getcwd()+os.sep+"tmp.jpg")

# 写配置文件
def write_config():
	with open("./we2_cfg.txt", "w", encoding="utf-8") as f:
		f.write("\n".join([str(i) for i in config]))

# 退出
def quit_window(icon: pystray.Icon):
	write_config()
	icon.stop()
	win.destroy()

# 设置文字
def set_text(*args):
	maintext = sd.askstring(APP_NAME, "设置倒计时标题 (距离某事件)")
	prompt   = sd.askstring(APP_NAME, "设置倒计时提示 (还剩)")
	number   = sd.askinteger(APP_NAME,"设置倒计时数字 (7)")
	unit     = sd.askstring(APP_NAME, "设置倒计时单位 (天)")
	english  = sd.askstring(APP_NAME, "设置倒计时英文 (@ DAYS TILL XX EVENT)").upper()
	bg       = fd.askopenfilename()
	global config
	config = [maintext, prompt, number, unit, english, bg]
	write_config()
	update_wallpaper()

# 数字+1
def add_num(*args):
	global config
	config[2] = config[2] + 1
	update_wallpaper()

# 数字-1
def sub_num(*args):
	global config
	if config[2] == 0:
		icon.notify("数字已经为零！", APP_NAME)
		return ;
	config[2] = config[2] - 1
	update_wallpaper()

# 设置托盘菜单
menu = (
	MenuItem('设置文字内容', set_text),
	MenuItem('数字 +1', add_num),
	MenuItem('数字 -1', sub_num, default=True),
	MenuItem('刷新', update_wallpaper),
	Menu.SEPARATOR,
	MenuItem('退出', quit_window)
)

# 设置托盘图标
image = Image.open("icon64.png")
icon = pystray.Icon("icon", image, APP_NAME, menu)

# 开一个似有似无的Tk窗口
win = Tk()
win.geometry("1x1+9999+9999")
win.overrideredirect(True)

# 用一个
threading.Thread(target=icon.run, daemon=True).start()

# 开始运行的提示
win.after(100, lambda :icon.notify("By Lizidaren", APP_NAME+" 已开始运行"))

# 初次运行判定
if first_start:
	win.after(1000, set_text)
else:
	update_wallpaper()

win.mainloop()