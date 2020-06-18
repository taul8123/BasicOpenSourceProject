import pygame
import Wall
import Star
import Ball


def loadmap(screen):
    wall_list = pygame.sprite.Group()  # 벽들을 모아둘 그룹
    #star_list = pygame.sprite.Group()  #구현이 안됨
    #ball_list = pygame.sprite.Group()  #구현이 안됨
    thorn_list = pygame.sprite.Group()

    move_image = pygame.image.load('mapeditimage/move.png')
    wall_image = pygame.image.load('mapeditimage/wall.png')
    thorn_image = pygame.image.load('mapeditimage/thorn.png')
    star_image = pygame.image.load('mapeditimage/star.png')
    ball_image = pygame.image.load('mapeditimage/ball.png')

    try:
        f = open('map.txt', 'r')
    except:
        print("불러올 맵이 존재하지 않습니다.\a")
        return -1

    size = f.readline().split(' ')
    width = int(size[0])
    height = int(size[1])
    pixel_size = int(size[2])
    while True:
        line = f.readline()
        if not line:
            break
        if line == 0:
            continue
        #temp = ['블럭형태', 'x좌표','y좌표','픽셀크기(정사각형임)']
        temp = line.split(' ')
        if temp[0].find('wall') != -1:
            wall_list.add(Wall.Wall(wall_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        #가시는 구현이 안돼있어서 뺐음
        # elif temp[0].find('thorn') != -1:
        #     thorn_list.add(Thorn.Thorn(thorn_image, (temp[1], temp[2]), (temp[3], temp[3])))
        elif temp[0].find('star') != -1:
            star = Star.Star(star_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3])))
        elif temp[0].find('ball') != -1:
            ball = Ball.Ball(ball_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3])))
        else:
            continue
    f.close()


#여기는 나중에 어떻게 해야될것 같다
    return [wall_list, star, ball]
