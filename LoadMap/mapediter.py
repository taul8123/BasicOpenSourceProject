import pygame
import sys
pygame.init()
#아래 코드는 다음과 같은 해상도에 맞춰 작성되었습니다 이외의 해상도에서 정상적인 작동은 확인되지 않았습니다.
width, height = 1920, 1080  #1920*1080 (윈도우 디스플레이 배율 설정에 따라 원활히 동작되지 않을 수 있습니다.)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

Start_Screen = True
MoveToolbox = False
CreateWall = False
CreateThorn = False
CreateStar = False
CreateBall = False
Erase = False

Start_background = pygame.image.load("mapeditimage/Background.png")
default_toolbox = pygame.image.load('mapeditimage/toolbox.png')
default_move = pygame.image.load('mapeditimage/move.png')
default_wall = pygame.image.load('mapeditimage/wall.png')
default_thorn = pygame.image.load('mapeditimage/thorn.png')
default_star = pygame.image.load('mapeditimage/star.png')
default_ball = pygame.image.load('mapeditimage/ball.png')


class newicon():
    def __init__(self, x, y, blocktype, width, height):
        self.x = x
        self.y = y
        self.blocktype = blocktype
        self.width = width
        self.height = height

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True



################################################################

#아래에서 pixel_size(크기)를 지정할 수 있습니다.
#디스플레이 해상도에 따라 변경시 올바르게 동작하지 않을 수 있습니다.
#해당 해상도(1920*1080)에서는 최대공약수인 120의 약수만 사용할 것을 권고합니다.
pixel_size = 40

################################################################

display = []

try:
    f = open('map.txt', 'r')
except:
    for i in range(width // pixel_size):
        temp = []
        for j in range(height // pixel_size):
            temp.append("0\n")
        display.append(temp)
else:
    size = f.readline().split(' ')
    width = int(size[0])
    height = int(size[1])
    pixel_size = int(size[2])
    for i in range(width//pixel_size):
        temp = []
        for j in range(height//pixel_size):
            line = f.readline()
            temp.append(line)
        display.append(temp)
    f.close()

# 파일 입력 수정

size = 0


default_toolbox = pygame.transform.scale(default_toolbox, (pixel_size * 6, pixel_size*2))
default_move = pygame.transform.scale(default_move, (int(pixel_size/2), int(pixel_size/2)))
default_wall = pygame.transform.scale(default_wall, (pixel_size, pixel_size))
default_thorn = pygame.transform.scale(default_thorn, (pixel_size, pixel_size))
default_star = pygame.transform.scale(default_star, (pixel_size, pixel_size))
default_ball = pygame.transform.scale(default_ball, (pixel_size, pixel_size))


toolbox = newicon(0, 0, "toolbox", pixel_size*6, pixel_size*2)
move = newicon(toolbox.x, toolbox.y, "move", int(pixel_size/2), int(pixel_size/2))
wall = newicon(toolbox.x + pixel_size*1, toolbox.y, "wall", pixel_size, pixel_size)
thorn = newicon(toolbox.x + pixel_size*2, toolbox.y, "thorn", pixel_size, pixel_size)
star = newicon(toolbox.x + pixel_size*3, toolbox.y, "star", pixel_size, pixel_size)
ball = newicon(toolbox.x + pixel_size*4, toolbox.y, "ball", pixel_size, pixel_size)


while True:
    if Start_Screen:
        screen.blit(Start_background, (0, 0))

        for i in range(width//pixel_size):
            for j in range(height//pixel_size):
                pygame.draw.rect(screen, (50, 50, 50), [i*pixel_size, j*pixel_size, pixel_size, pixel_size], 1)
        screen.blit(default_toolbox, (toolbox.x, toolbox.y))
        screen.blit(default_move, (move.x, move.y))
        screen.blit(default_wall, (wall.x, wall.y))
        screen.blit(default_thorn, (thorn.x, thorn.y))
        screen.blit(default_star, (star.x, star.y))
        screen.blit(default_ball, (ball.x, ball.y))
        for i in range(width//pixel_size):
            for j in range(height//pixel_size):
                #추후 사용한다면 수정필요
                if display[i][j].find('wall') != -1:
                    screen.blit(default_wall, (i*pixel_size, j*pixel_size))
                elif display[i][j].find('thorn') != -1:
                    screen.blit(default_thorn, (i*pixel_size, j*pixel_size))
                elif display[i][j].find('star') != -1:
                    screen.blit(default_star, (i*pixel_size, j*pixel_size))
                elif display[i][j].find('ball') != -1:
                    screen.blit(default_ball, (i * pixel_size, j * pixel_size))
                else:
                    continue

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if wall.isOver(pos):
                CreateWall = True
            elif thorn.isOver(pos):
                CreateThorn = True
            elif star.isOver(pos):
                CreateStar = True
            elif ball.isOver(pos):
                CreateBall = True
            elif move.isOver(pos):
                MoveToolbox = True
            elif toolbox.isOver(pos):
                Erase = True
            else:
                continue

        if CreateWall and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "wall" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size) + "\n"
            CreateWall = False

        if CreateThorn and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "thorn" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size) + "\n"
            CreateThorn = False

        if CreateStar and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "star" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size) + "\n"
            CreateStar = False

        if CreateBall and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "ball" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size) + "\n"
            CreateBall= False

        if MoveToolbox and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            toolbox.x, toolbox.y = pos[0], pos[1]
            move.x, move.y = toolbox.x, toolbox.y
            wall.x, wall.y = toolbox.x + pixel_size * 1, toolbox.y
            thorn.x, thorn.y = toolbox.x + pixel_size * 2, toolbox.y
            star.x, star.y = toolbox.x + pixel_size * 3, toolbox.y
            ball.x, ball.y = toolbox.x + pixel_size * 4, toolbox.y
            MoveToolbox = False

        if Erase and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "0\n"
            Erase = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "0\n"
            Erase = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                f = open('map.txt', 'w')
                save = "" + str(width) + " " + str(height) + " " + str(pixel_size) + "\n"
                f.write(save)
                for i in range(width // pixel_size):
                    for j in range(height // pixel_size):
                        f.write(display[i][j])
                f.close()
                pygame.quit()
                sys.exit()

    pygame.display.update()

#최종수정시간:2020.06.06.19.47