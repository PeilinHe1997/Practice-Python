#引入pygame和sys
import pygame,sys

#初始化和init设置
pygame.init()
screen = pygame.display.set_mode(size = (600,300),flags = pygame.RESIZABLE)
pygame.display.set_caption("hello pygame!")#标题

'''
r(red) g(green) b(blue)
'''
RED = (23,59,200)#大写字母一般表示常量
BLUE = pygame.Color("blue")
COLORS = pygame.Color("#000000")

#获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.circle(screen,RED,(200,200),50)
    #circle(surface,color,center,radius)
    #刷新屏幕
    pygame.display.update()
