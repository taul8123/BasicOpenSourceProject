import pygame

from game.data.obj import Magnetic, Backblock, Star, Movewall, Blckhole, Spring, Fakewall, Thorn, Ball, Wall, iccle, Laser, lever, potal, Cannon, Blink_block



def loadmap(screen):
    try:
        f = open('map.txt', 'rt', encoding='UTF8')
    except:
        print("불러올 맵이 존재하지 않습니다.\a")
        return -1

    size = f.readline().split(' ')
    width = int(size[0])
    height = int(size[1])
    pixel_size = int(size[2])
    filename = f.readline()
    filename = filename.replace("\n", "")
    if filename == "0":
        filename = "Background.png"

    backblock_list = pygame.sprite.Group()
    #ball_list = pygame.sprite.Group()
    blckhole_list = pygame.sprite.Group()
    fakewal_list = pygame.sprite.Group()
    magnetic_list = pygame.sprite.Group()
    movewal_list = pygame.sprite.Group()
    #star_list = pygame.sprite.Group()
    thorn_list = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()       # 벽들을 모아둘 그룹
    spring_list = pygame.sprite.Group()

    icicle_list = pygame.sprite.Group()
    laser_list = pygame.sprite.Group()
    blinkblock_list = pygame.sprite.Group()
    portal_list = pygame.sprite.Group()
    lever_list = pygame.sprite.Group()
    cannon_list = pygame.sprite.Group()

    subportal_list = pygame.sprite.Group()

    cannonball_image = pygame.image.load('mapeditimage/cannonball.png')

    backblock_image = pygame.image.load('mapeditimage/move.png')
    ball_image = pygame.image.load('mapeditimage/ball.png')
    blckhole_image = pygame.image.load('mapeditimage/blckhole.png')
    fakewal_image = pygame.image.load('mapeditimage/fakewal.png')
    magnetic_image = pygame.image.load('mapeditimage/magnetic.png')
    movewal_image = pygame.image.load('mapeditimage/movewal.png')
    star_image = pygame.image.load('mapeditimage/star.png')
    thorn_image = pygame.image.load('mapeditimage/thorn.png')
    wall_image = pygame.image.load('mapeditimage/wall.png')
    spring_image = pygame.image.load('mapeditimage/spring.png')

    icicle_image = pygame.image.load('mapeditimage/icicle.png')
    laser_image = pygame.image.load('mapeditimage/laser.png')
    blinkblock_image = pygame.image.load('mapeditimage/blinkblock.png')
    lever_image = pygame.image.load('mapeditimage/lever.png')
    portal_image = pygame.image.load('mapeditimage/portal.png')
    cannon_image = pygame.image.load('mapeditimage/cannon.png')

    subportal_image = pygame.image.load('mapeditimage/subportal.png')



    while True:
        line = f.readline()
        if not line:
            break
        if line == 0:
            continue
        #temp = ['블럭형태', 'x좌표','y좌표','픽셀크기(정사각형임)']
        #저장방식 ['0:blocktype' '1:x위치' '2:y위치' '3:pixel_size' '4:방향' '5:기타 x위치' '6:기타 y위치']
        #방향 0: 12시 방향(default), 1: 3시 방향, 2: 6시 방향, 3: 9시 방향
        temp = line.split(' ')
        if temp[0].find('backblock') != -1:
            backblock_list.add(Backblock.Backblock(backblock_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('ball') != -1:
            ball = Ball.Ball(ball_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3])))
        elif temp[0].find('blckhole') != -1:
            blckhole_list.add(Blckhole.Blackhole(blckhole_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('fakewal') != -1:
            fakewal_list.add(Fakewall.Fakewall(fakewal_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('magnetic') != -1:
            magnetic_list.add(Magnetic.Magnetic(magnetic_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('movewal') != -1:
            movewal_list.add(Movewall.Movewall(movewal_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3])),\
                                               (int(temp[5]), int(temp[4]))))
        elif temp[0].find('star') != -1:
            star = Star.Star(star_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3])))
        elif temp[0].find('thorn') != -1:
            thorn_list.add(Thorn.Thorn(thorn_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('wall') != -1:
            wall_list.add(Wall.Wall(wall_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('spring') != -1:
            spring_list.add(Spring.Spring(spring_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))

        elif temp[0].find('icicle') != -1:
            icicle_list.add(iccle.Iccle(icicle_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('laser') != -1:
            continue
            laser_list.add(Laser.Layser(laser_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('blinkblock') != -1:
            blinkblock_list.add(Blink_block.block(blinkblock_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))

        elif temp[0].find('lever') != -1:
            continue
            lever_list.add(lever.Lever(lever_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('portal') != -1:
            continue
            portal_list.add(potal.Potal(portal_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        elif temp[0].find('cannon') != -1:
            cannon_list.add(Cannon.Cannon(cannon_image, cannonball_image, (int(temp[1]), int(temp[2])), (int(temp[3]), int(temp[3]))))
        else:
            continue

    f.close()


#여기는 나중에 어떻게 해야될것 같다
    try:
        return [backblock_list, ball, blckhole_list, fakewal_list, magnetic_list, movewal_list, star, thorn_list, wall_list\
            ,spring_list, icicle_list, laser_list, blinkblock_list, lever_list, portal_list, cannon_list]
    except:
        print("시작지점 혹은 종료지점이 존재하지 않습니다.\a")
        return -1

