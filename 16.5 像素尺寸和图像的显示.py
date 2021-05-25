import pygame,sys

#初始化和init设置
pygame.init()
screen = pygame.display.set_mode(size = (800,600),flags = pygame.RESIZABLE)
pygame.display.set_caption("hello pygame！")

#创建对象颜色
RED = pygame.Color("red")
COLOR1 = (123,45,90)
filename = "生活照.jpg"#相对路径
#绝对路径
filename = r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\生活照2.jpg"
filename = r".\A\ball.png"#相对路径，在一个文件夹下

#获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    img = pygame.image.load(filename)
    screen.blit(img,(100,100))#把图像放到坐标上
    pygame.display.update()
    
