# 球2 倒计时图片生成
# author: lizidaren
from PIL import Image, ImageDraw, ImageFont

FONTS = {
	"zh59"   : "字魂59号-创粗黑.ttf",
	"DIN1451": "Alte_DIN_1451_Mittelschrift_gepraegt_Regular.ttf"
}

def generate(maintext="距离xx", prompt="还剩", number="7", unit="天", english="@ days till xxx", bg="./bg.jpg", path="./tmp.jpg"):
	# 图片生成函数
	
	# 针对英文单词复数的优化
	if 'DAYS' in english:
		if int(number) <= 1:
			english = english.replace('DAYS', 'DAY')
	number = str(number)
	
	# 英文中的@符号自动替换为数字
	if '@' in english:
		english = english.replace('@', number)
	
	img = Image.open(bg)
	
	# 计算字体大小
	font_size = img.size[0] // 35
	
	font_cn  = ImageFont.truetype(FONTS["zh59"]   , font_size)
	font_num = ImageFont.truetype(FONTS["DIN1451"], int(font_size*2.3))
	font_en  = ImageFont.truetype(FONTS["zh59"]   , int(font_size // 2))
	
	# 绘制
	draw = ImageDraw.Draw(img)
	base_x = img.size[0]*0.65
	base_y = img.size[1]*0.7
	draw.text((base_x, base_y),maintext,(255,255,255),font=font_cn)
	draw.text((base_x+(len(maintext)-len(prompt))*font_size, base_y+font_size),prompt,  (255,255,255),font=font_cn)
	draw.text((base_x+((len(maintext)+0.2)*font_size), base_y-0.35*font_size),number,(255,0,0),font=font_num)
	draw.text((base_x+((len(maintext)+0.2)*font_size)+(len(number)*font_size*(2.3-1)), base_y+font_size),unit,(255,255,255),font=font_cn)
	draw.text((base_x+(len(maintext)-len(prompt))*font_size+0.1*font_size, base_y+font_size*2.1),english,(255,255,255),font=font_en)
	
	ox, oy = base_x+(len(maintext)-len(prompt))*font_size-0.35*font_size, base_y + font_size*1.2
	draw.rectangle((ox, oy, ox+font_size//5, oy+font_size*2), fill=(255,0,0))
	
	img.save(path)

if __name__ == "__main__":
	# 测试用
	print("=====流浪地球2 倒计时图片生成=====")
	print("直接回车以使用括号中的默认值")
	# or后为默认值
	generate(input("主提示词(距离比赛)> ")         or "距离比赛",
			input("副提示词(还有)> ")              or "还有",
			input("数字(7)> ")                     or "7",
			input("单位(天)> ")                    or "天",
			input("英文(@ days till the match)> ") or "@ days till the match",
			input("背景原图(./bg.jpg)> ")          or "./bg.jpg"
	)
	print("图片已经保存为tmp.jpg")