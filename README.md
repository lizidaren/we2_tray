# we2_tray：《流浪地球2》风格 倒计日壁纸生成
内含托盘小工具 (Python)

## 如何使用？
1.安装依赖库（PIL和pystray)  
`pip install pillow pystray`

2.准备字体文件  
你需要准备 *"字魂59号-创粗黑.ttf"* 和 *"Alte_DIN_1451_Mittelschrift_gepraegt_Regular.ttf"*  
可以在[这里](https://www.bilibili.com/read/cv21439547/ "论2023年电影《流浪地球2》中使用的字体（附ttf）")找到  
下载后请和源代码放在一起

3.运行we2_tray.py，然后通过任务栏中的图标对其进行控制即可

4.可以使用托盘菜单或直接编辑配置文件以修改文字内容  
（“距离xx”那一段文字越长，图片效果越好）

## 代码说明
- we2_timer.py 用于生成图片(使用PIL)
- we2_tray.py 提供托盘服务
- we2_cfg.txt 是配置文件，英文中的@符号将被自动替换为数字
- 其他请参阅注释

## 已知的问题
- 当十位数字为1时，排版出现偏差
- 退出不能保存配置

## Q&A: 为什么要手动点击才能更改数字？
因为这个项目最初设计是在无网边缘设备上运行，所以设备时间可能不正确，因此程序不自动更新数字。可以通过自行修改we2_tray.py加入该功能。
