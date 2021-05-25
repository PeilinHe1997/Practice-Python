'''
开发游戏的四个步骤
   1、引入pygame和sys
   2、初始化init和设置
   3、获取事件并响应事件
   4、刷新屏幕

'''

#  一、引入pygame和sys
import pygame,sys

#  二、初始化init和设置
pygame.init()
screen = pygame.display.set_mode(size = (200,300),flags = pygame.RESIZABLE)
  #set_mode(size = (0,0),flags = 0,depth = 0,display = 0)
  #flag 屏幕具备什么样的模式
pygame.display.set_caption("hello pygame!")#设置当前窗口标题


#  三、获取事件并响应事件
while True:
    for event in pygame.event.get():
        '''print(event.type)输出打印事件类型'''
        if event.type == pygame.QUIT:#点击×号
            pygame.quit()#取消初始化模块
            sys.exit() #退出程序

#  四、刷新屏幕
    pygame.display.update()
'''
