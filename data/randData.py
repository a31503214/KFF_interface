#-*-coding:utf-8 -*-

import random
import string
import sys
from requests import sessions


# 存储大小写字母和数字特殊字符列表
STR = [chr(i) for i in range(65,91)]   #65-91对应字符A-Z
Str = [chr(i) for i in range(97,123)]   #a-z
number = [chr(i) for i in range(48,58)]  #0-9

#特殊字符串列表获取有点不同
initSpecial = string.punctuation      #这个函数获取到全部特殊字符结果为字符串形式
Special = []                          #定义一个空列表

#制作特殊符号列表
for i in initSpecial:
    Special.append(i)

# 中文千字文
Characters = \
"天地玄黄宇宙洪荒\
日月盈昃辰宿列张\
寒来暑往秋收冬藏\
闰余成岁律吕调阳\
云腾致雨露结为霜\
金生丽水玉出昆冈\
剑号巨阙珠称夜光\
果珍李柰菜重芥姜\
海咸河淡鳞潜羽翔\
龙师火帝鸟官人皇\
始制文字乃服衣裳\
推位让国有虞陶唐\
吊民伐罪周发殷汤\
坐朝问道垂拱平章\
爱育黎首臣伏戎羌\
遐迩一体率宾归王\
鸣凤在竹白驹食场\
化被草木赖及万方\
盖此身发四大五常\
恭惟鞠养岂敢毁伤\
女慕贞洁男效才良\
知过必改得能莫忘\
罔谈彼短靡恃己长\
信使可覆器欲难量\
墨悲丝染诗赞羔羊\
景行维贤克念作圣\
德建名立形端表正\
空谷传声虚堂习听\
祸因恶积福缘善庆\
尺璧非宝寸阴是竞\
资父事君曰严与敬\
孝当竭力忠则尽命\
临深履薄夙兴温凊\
似兰斯馨如松之盛\
川流不息渊澄取映\
容止若思言辞安定\
笃初诚美慎终宜令\
荣业所基籍甚无竟\
学优登仕摄职从政\
存以甘棠去而益咏\
乐殊贵贱礼别尊卑\
上和下睦夫唱妇随\
外受傅训入奉母仪\
诸姑伯叔犹子比儿\
孔怀兄弟同气连枝\
交友投分切磨箴规\
仁慈隐恻造次弗离\
节义廉退颠沛匪亏\
性静情逸心动神疲\
守真志满逐物意移\
坚持雅操好爵自縻\
都邑华夏东西二京\
背邙面洛浮渭据泾\
宫殿盘郁楼观飞惊\
图写禽兽画彩仙灵\
丙舍旁启甲帐对楹\
肆筵设席鼓瑟吹笙\
升阶纳陛弁转疑星\
右通广内左达承明\
既集坟典亦聚群英\
杜稿钟隶漆书壁经\
府罗将相路侠槐卿\
户封八县家给千兵\
高冠陪辇驱毂振缨\
世禄侈富车驾肥轻\
策功茂实勒碑刻铭\
盘溪伊尹佐时阿衡\
奄宅曲阜微旦孰营\
桓公匡合济弱扶倾\
绮回汉惠说感武丁\
俊义密勿多士实宁\
晋楚更霸赵魏困横\
假途灭虢践土会盟\
何遵约法韩弊烦刑\
起翦颇牧用军最精\
宣威沙漠驰誉丹青\
九州禹迹百郡秦并\
岳宗泰岱禅主云亭\
雁门紫塞鸡田赤诚\
昆池碣石钜野洞庭\
旷远绵邈岩岫杳冥\
治本于农务兹稼穑\
俶载南亩我艺黍稷\
税熟贡新劝赏黜陟\
孟轲敦素史鱼秉直\
庶几中庸劳谦谨敕\
聆音察理鉴貌辨色\
贻厥嘉猷勉其祗植\
省躬讥诫宠增抗极\
殆辱近耻林皋幸即\
两疏见机解组谁逼\
索居闲处沉默寂寥\
求古寻论散虑逍遥\
欣奏累遣戚谢欢招\
渠荷的历园莽抽条\
枇杷晚翠梧桐蚤凋\
陈根委翳落叶飘摇\
游鹍独运凌摩绛霄\
耽读玩市寓目囊箱\
易輶攸畏属耳垣墙\
具膳餐饭适口充肠\
饱饫烹宰饥厌糟糠\
亲戚故旧老少异粮\
妾御绩纺侍巾帷房\
纨扇圆洁银烛炜煌\
昼眠夕寐蓝笋象床\
弦歌酒宴接杯举殇\
矫手顿足悦豫且康\
嫡后嗣续祭祀烝尝\
稽颡再拜悚惧恐惶\
笺牒简要顾答审详\
骸垢想浴执热愿凉\
驴骡犊特骇跃超骧\
诛斩贼盗捕获叛亡\
布射僚丸嵇琴阮箫\
恬笔伦纸钧巧任钓\
释纷利俗并皆佳妙\
毛施淑姿工颦妍笑\
年矢每催曦晖朗曜\
璇玑悬斡晦魄环照\
指薪修祜永绥吉劭\
矩步引领俯仰廊庙\
束带矜庄徘徊瞻眺\
孤陋寡闻愚蒙等诮\
谓语助者焉哉乎也"

# -------------随机产生的的的字符--------------------------
"""        
:param Lth: 这是要求随机产生的字符的长度（位数）

:rtype: int 必须是正整数
"""


# 产生随机小写字母
def randLowercase(Lth=0):
    lowercases = random.sample(Str*Lth,Lth)
    lowercase = randChars(Lth,lowercases)
    return  lowercase


# 产生随机小写字母
def randUpperercase(Lth=0):
    upperercases = random.sample(STR*Lth,Lth)
    upperercase = randChars(Lth, upperercases)
    return  upperercase


# 产生随机特殊字符
def randPunctuation(Lth=0):
    punctuations = random.sample(Special*Lth,Lth)
    punctuation = randChars(Lth,punctuations)

    return  punctuation


# 产生随机数字
def randnumber(Lth=0):
    digs = random.sample(number*Lth,Lth)
    dig = randChars(Lth,digs)

    return  dig

# 产生随机汉字
def randCharacters(Lth=0):

    characters = random.sample(Characters*Lth,Lth)
    character = randChars(Lth,characters)

    return  character

# 将随机产生的字符列表转化为字符串
def randChars(Lth,name):
    STRING = ""
    for i in range(Lth):
        STRING += name[i]
    return STRING



if __name__ == '__main__':
    print(randCharacters(100))



































# ---------------------------- 华丽的分割线 ---------------------------------------------
# total = STR + Str + number + Special
# print total

'''
def Randompassword(your_choice):
    if your_choice in total:
        passwordli = random.sample(total,int(your_choice))
        passwordst = ''.join(passwordli)
        print "" + your_choice + "" + passwordst

    else:
        print ""
'''

'''
if __name__ == '__main__':
    while True:
        choice = raw_input("")
        if choice != 'q':
            Randompassword(choice)
        else:
            break

'''
