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

#定义小球反弹函数
x = 100
y = 100
x_step = 1
y_step = 2
def fantan():
    global x,y,x_step,y_step #如果函数里全局变量改变，那最终全局变量改变
    screen.fill(COLOR1)
    x += x_step
    y += y_step
    if x > screen.get_width() or x < 0:
        x_step = -x_step
    if y > screen.get_width() or y < 0:
        y_step = -y_step
        
    screen.blit(img,(x,y))
    pygame.display.update()

#获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    fantan()
    




    
