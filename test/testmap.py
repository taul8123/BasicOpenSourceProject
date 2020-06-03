import pygame
import Wall
import Star
import Ball

import time
img=['Setting','Exit']

def map(screen):#스크린을 전달받음
    done = 1
    FPS = 60        #프레임
    key = 0         #공의 이동 방향 0이 바뀌지 않음 1이 오른쪽, -1이 왼쪽

    wall_list=pygame.sprite.Group()
    background= pygame.Surface(screen.get_size())#스크린과 동일크기의 surface생성 이곳에 그린후 스크린에 복사
    clock=pygame.time.Clock()
    #이미지를 불러와서 리스트에 저장
    image_list=[]
    for i in img:
        image_list.append(pygame.image.load("image/{}.png".format(i)).convert_alpha())


    star=Star.Star(image_list[0],(350,350),(50,50))

    ball=Ball.Ball(image_list[0],(250,900),(25,15))


    wall_list.add(Wall.Wall(image_list[1],(400,1000),(2000,150)))
    wall_list.add(Wall.Wall(image_list[1], (10, 800), (150, 1000)))
    wall_list.add(Wall.Wall(image_list[1], (230, 400), (150, 1000)))
    wall_list.add(Wall.Wall(image_list[1], (800, 800), (150, 1000)))

    while done:

        clock.tick(FPS)


        event = pygame.event.get()
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN:
                done=0
            #키보드 누름
            if e.type ==pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    key-=1
                elif e.key ==pygame.K_RIGHT:
                    key+=1

            #키보드 뗌
            if e.type ==pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    key+=1
                elif e.key ==pygame.K_RIGHT:
                    key-=1

        ball.move_check(key)
        collision_list = pygame.sprite.spritecollide(ball, wall_list, False, pygame.sprite.collide_mask)

        for c in collision_list:
            ball.wall_collision(c)

        #백르라운드에 그리기
        background.fill((255,255,255))                #그려진거 비우기
        background.blit(star.image, star.rect)
        background.blit(ball.image, ball.rect)
        wall_list.draw(background)
        #스크린에 그리고 새로고침
        screen.blit(background,(0,0))
        pygame.display.flip()


