import pygame,sys

#初始化和init设置
pygame.init()
screen = pygame.display.set_mode(size=(1000, 600), flags=pygame.RESIZABLE)
pygame.display.set_caption("hello pygame")
filename = r".\A\ball.png"

#创建对象颜色
RED = pygame.Color("red")
COLOR1 = (123,45,90)

screen.fill(COLOR1)
img = pygame.image.load(filename)

#定义移动的函数
x = 100
y = 100
x_step = 0.4
y_step = 0.6


def move():
    global x,y
    x += x_step
    y += y_step
    screen.fill(COLOR1)
    screen.blit(img,(x,y))

#获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    move()
    
    pygame.display.update()
