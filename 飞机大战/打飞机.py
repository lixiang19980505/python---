import pygame
import sys
from pygame.locals import *
import random

class Hero(): #主机类
    #方法一：
    # def __init__(self,img,x,y,window):
    #     self.img=pygame.image.load(img)
    #     self.x=x
    #     self.y=y
    #     self.window=window
    #方法二：
    def __init__(self,window): #窗口初始化
        self.window=window
        self.x=150
        self.y=485
        self.img=pygame.image.load('2.png')
        #创建储存生成子弹列表
        # self.shoot_list=[]  #方法1
    def display(self):
        self.window.blit(self.img,(self.x,self.y))
    #向左移动，判断边界
    def move_left(self):
        if self.x<0:
            self.x=0
        else:
            self.x-=5
    #向右移动，判断边界
    def move_right(self):
        if self.x>=WIDTH-100:
            self.x=WIDTH-100
        else:
            self.x+=5
    # 向上移动，判断边界
    def move_up(self):
        if self.y<0:
            self.y=0
        else:
            self.y-=5

    # 向下移动，判断边界
    def move_down(self):
        if self.y>=HEIGHT-95:
            self.y=HEIGHT-95
        else:
            self.y+=5

    #因为子弹的位置和主机的相关，所以写在主机里
    def shoot(self):
        hero_shoot=Bullet(self.x+55,self.y-20,self.window)
        # self.shoot_list.append(hero_shoot)  #方法1
        bullet_list.append(hero_shoot)  #方法2

    def shoot_biu(self):
        for i in bullet_list:  #方法2
            i.display()
            i.run()
        # for i in self.shoot_list:   #方法1
        #     i.display()
        #     i.run()
            # for diji in enemy_list: #方法1
            #     if i.if_boom(diji):
            #         diji.is_boom=True
            #         break


class Enemy():  #敌机类
    def __init__(self,window):
        self.window=window
        self.x=random.randint(0,350)  #随机生成数
        self.y=0
        self.img=pygame.image.load('enemy.png')
        # self.is_boom=False  #1

    # def display(self):
    #     self.window.blit(self.img,(self.x,self.y))
    def run(self):
        self.y+=0.5
        if self.y>HEIGHT:
            self.x=random.randint(0,350)
            self.y=0

    def diji_display(self):
        # if self.is_boom:   #方法1
        #     self.x = random.randint(0, 350)
        #     self.y = 0
        #     self.is_boom=False
        self.window.blit(self.img,(self.x,self.y))


# 子弹类
class Bullet():
    def __init__(self,x,y,window):
        self.window=window
        self.x=x
        self.y=y
        self.img=pygame.image.load('bullet.png')
    def display(self):
        self.window.blit(self.img,(self.x,self.y))
    def run(self):
        self.y -= 2

    #判断子弹与敌机是否接触
    def if_boom(self,diji):
        if pygame.Rect.colliderect(pygame.Rect(self.x,self.y,22,22),pygame.Rect(diji.x,diji.y,51,39)):
            return True
        else:
            return False

#敌机子弹类
class Enemy_bullet():
    def __init__(self, x, y, window):
        self.window = window
        self.x = x
        self.y = y
        self.img = pygame.image.load('bullet1.png')

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def run(self,enemy):
        self.y += 1
        if self.y>600:
            self.y=enemy.y+30
            self.x=enemy.x+20

    #判断敌机子弹是否与主机碰撞
    def if_boom(self,zhuji):
        if pygame.Rect.colliderect(pygame.Rect(self.x,self.y,10,22),pygame.Rect(zhuji.x,zhuji.y,110,110)):
            return True
        else:
            return False


class Zhadan():
    def __init__(self,window):
        self.window = window
        self.x =random.randint(0,350)
        self.y =0
        self.img = pygame.image.load('bomb_supply.png')
    
    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def run(self):
        self.x+=random.randint(-2,2)
        self.y+=1
        if self.y>HEIGHT:
            self.x =random.randint(0,350)
            self.y =0

    #判断炸弹是否与主机碰撞
    def if_boom(self,zhuji):
        if pygame.Rect.colliderect(pygame.Rect(self.x,self.y,60,107),pygame.Rect(zhuji.x,zhuji.y,110,110)):
            return True
        else:
            return False

WIDTH=400
HEIGHT=600
count=0

#创建储存敌机的列表
enemy_list=[]
bullet_list=[]   #方法2
enemy_bullet_list=[]
zhadan_list=[]
def main():
    pygame.init()#显示窗口，初始化
    pygame.mixer.init()#混音器初始化
    pygame.mixer.music.load("music.mp3")#加载音乐
    pygame.mixer.music.set_volume(0.6)#设置音量
    pygame.mixer.music.play(2)#播放
    bullet_sound = pygame.mixer.Sound("shoot.wav")#设置子弹音效
    bullet_sound.set_volume(0.6)
    bomb_sound = pygame.mixer.Sound("boom.wav")#设置发生碰撞爆炸音效
    bomb_sound.set_volume(0.6)

    window=pygame.display.set_mode((WIDTH,HEIGHT)) #引用窗口大小
    bg_img=pygame.image.load("2.jpg")#设置背景图片
    # hero=Hero("hero.png",150,500,window)
    hero=Hero(window)
    enemy=Enemy(window)
    enemy_list.append(enemy)

    enemy_bullet=Enemy_bullet(enemy.x+20,enemy.y+30,window)
    enemy_bullet_list.append(enemy_bullet)

    zhadan=Zhadan(window)
    zhadan_list.append(zhadan)
    while True:
        window.blit(bg_img,(0,0))#blit也是显示 的意思
        hero.display()
        hero.shoot_biu()

        global count #定义一个全局变量技术得分
        my_font = pygame.font.SysFont("fangsong", 54) #设置字体，字号
        text_fmt = my_font.render('socre=%s' % str(count), True, (255, 255, 255))
        window.blit(text_fmt, (0, 0)) #在窗口显示
        for i in bullet_list:     #方法2
            for dj in enemy_list:
                if i.if_boom(dj):
                    bomb_sound.play()#爆炸音效播放
                    img=pygame.image.load("aa1.png")#加载爆炸后的图片
                    window.blit(img,(enemy.x,enemy.y))#显示图片
                    pygame.display.update()#刷新
                    pygame.time.delay(50)#图片停顿0.5秒
                    count+=1
                    enemy.x = random.randint(0, 350)
                    enemy.y = 0
                    bullet_list.remove(i)
                    
        for i in bullet_list:
            for zhadan in zhadan_list:
                if i.if_boom(zhadan):
                    bomb_sound.play()
                    img=pygame.image.load("1.png")
                    window.blit(img,(zhadan.x,zhadan.y))
                    pygame.display.update()
                    pygame.time.delay(50)
                    count+=1
                    zhadan.x=random.randint(0,350)
                    zhadan.y=0
                    bullet_list.remove(i)

        for i in enemy_list:
            i.run()
            i.diji_display()

        # enemy.display()
        # enemy.run()

        enemy_bullet.run(enemy)  #敌机子弹运行
        enemy_bullet.display()    #显示
        for i in enemy_bullet_list:
            if i.if_boom(hero):
                img=pygame.image.load("2222.gif")
                window.blit(img,(0,0))
                pygame.display.update()
                pygame.time.delay(5000)
                print("游戏结束！！！")
                sys.exit()
                pygame.quit()

        zhadan.run()    #炸弹运行
        zhadan.display()
        for i in zhadan_list:
            if i.if_boom(hero):
                img=pygame.image.load("2222.gif")
                window.blit(img,(0,0))
                pygame.display.update()
                pygame.time.delay(500)
                print("游戏结束！！！")
                sys.exit()
                pygame.quit()
        pygame.display.update()#刷新页面
        for event in pygame.event.get(): #检测窗口的键盘事件
            if event.type==QUIT: #退出事件
                sys.exit()
                pygame.quit()
            elif event.type==KEYDOWN:#键盘按下
                if event.key==K_SPACE:
                    # print('space')
                    hero.shoot()
                    bullet_sound.play()
            #     if event.key==K_LEFT or event.key==K_a:
            #         # print('left')
            #         hero.move_left()
            #     if event.key==K_RIGHT or event.key==K_d:
            #         # print('right')
            #         hero.move_right()
            #     if event.key==K_UP or event.key==K_w:
            #         # print('up')
            #         hero.move_up()
            #     if event.key==K_DOWN or event.key==K_s:
            #         # print("down")
            #         hero.move_down()

        # 获取键盘事件（上下左右按键）
        key_pressed = pygame.key.get_pressed()
        # 处理键盘事件（移动飞机的位置）

        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            hero.move_up()

        if key_pressed[K_s] or key_pressed[K_DOWN]:
            hero.move_down()

        if key_pressed[K_a] or key_pressed[K_LEFT]:
            hero.move_left()

        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            hero.move_right()

if __name__== "__main__":
    main()
