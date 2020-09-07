print('#####################################')
print('###########欢迎来到英雄无敌##########')
print('##############载入中...##############')
print('##########正在加载请耐心等待#########')

use = str(input('请输入用户名:'))
pw1 = str(input('请输入密码:'))
pw2 = str(input('请再次输入密码:'))
while True:
    if pw1 == pw2:
        print('用户名为:',use)
        print('密码为:',pw1)
        break
    else:
        print('两次密码不同 请重新输入:')
        pw1 = str(input('请输入密码:'))
        pw2 = str(input('请再次输入密码:'))
print('######################################')
name = str(input('请输入英雄的名字:'))
while not name == '':
    print('英雄的名字:',name)
    break
else :
    print('系统默认生成名字为 玩家一')
a = str(input('请选择您的职业[1.法师/2.弓箭/3.坦克/4.刺客/5.奶妈]:'))
hp1 ='HP=1000 初始攻击力: 法术300 物理0'
hp2 ='HP=1000 初始攻击力：法术0 物理300'
hp3 ='HP=3000 初始攻击力：法术0 物理100'
hp4 ='HP=1200 初始攻击力：法术0 物理200'
hp5 ='HP=800  初始攻击力：法术200 物理0'
while True:
      if a =='1':
         print('您的职业为法师',hp1)
         break
      if a =='2':
         print('您的职业为弓箭',hp2)
         break
      if a =='3':
         print('您的职业为坦克',hp3)
         break
      if a =='4':
         print('您的职业为刺客',hp4)
         break
      if a =='5':
         print('您的职业为奶妈',hp5)
         break
      else:
         print('输入职业不存在请重新输入:')
         a = str(input('请选择您的职业[1.法师/2.弓箭/3.坦克/4.刺客/5.奶妈]:'))
print('#############################')
print('进入游戏 地图###')
map =[['#','#','#'],['#','#','#'],['#','#','#',]]
for i in "123":
    pass
for i in map:
    print(i)
for x,y,z in map:
    print(x)

A = str(input('A键向左走'))
while True:
    if A == 'A' :
        print('向左移动←##')
        break
    if A =='a':
        print('向左移动←##')
        break
    else:
        print('移动失败 请重新输入:')
        A = str(input(''))


D = str(input('D键向右走'))
while True:
    if D == 'D' :
        print('向右移动→##')
        break
    if D =='d':
        print('向右移动→##')
        break
    else:
        print('移动失败 请重新输入:')
        D = str(input(''))

W = str(input('W键向前走'))
while True:
    if W == 'W' :
        print('向前移动↑##')
        break
    if W =='w':
        print('向前移动↑##')
        break
    else:
        print('移动失败 请重新输入:')
        W = str(input(''))

S = str(input('S键向后走'))
while True:
    if S == 'S' :
        print('向后移动↓##')
        break
    if S =='s':
        print('向后移动↓##')
        break
    else:
        print('移动失败 请重新输入:')
        S = str(input(''))

print('####################################')
introduce = str(input('输入【help】可查看技能介绍:'))
while True:
    if introduce =='help':
       print('Q，W可探头 数字键盘为技能键盘 空格为跳跃 C键下蹲 Z键趴下 shift加速 鼠标控制视角 左右键控制人物')
       break
    else:
        print('')
        break
print('######################')
free = str(input('输入free 开启自动模式 自动寻找任务:'))
while True:
    if free =='free':
       print('自动模式已开启')
       break
    else:
       print('关闭自动模式')
       

import turtle
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
event = str(input('！发现随机任务 是否接受（输入[是]接受）'))
while True:
        if event =='是':
           print('#######【任务】抓捕偷盗电瓶的周某#####')
           print('周某家住河南新乡因偷盗电瓶车电瓶被通缉')
           print('抓住周某获奖金500金（概率可得偷盗指南）')
           break
        else:
            print('任务接受失败')
ren = str(input('输入确认前往周末最后出现点'))
while True:
        if ren =='确认':
           print('出发')
           break
        else:
            print('出发失败')
import turtle
turtle.forward(200)
turtle.circle(300)
 
zhou = str(input('发现周某 是否抓捕：'))
while True:
        if zhou =='是':
           print('抓捕成功 +5000金 +偷盗指南')
           print('抓捕成功 +500金 +偷盗指南')
           break
        else:
            print('抓捕失败 HP-100')
            break



print('#######################')
print('广告：充电五小时 通话两分钟 欧普手机值得信赖')
print('VIP可跳过广告')
pay = str(input('是否选择充值'))
while True:
    if pay =='是':
       print('请选择充值价格')
       break
    else:
        print('充值失败HP-100 需看6000秒广告获得血量')
        pay = str(input('是否选择充值'))
        break
afford = str(input('请选择充值金额：￥100 ￥200 ￥300 ￥400 ￥500：'))
zhi = str(input('请选择充值途径：【支付宝】【微信】【银行卡】'))
print('充值成功 恭喜您被大奖砸中成为尊贵的SVIP200 每月充值1000元续费（自动充值）')
