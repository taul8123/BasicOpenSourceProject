import pygame
import Wall
import Star
import Ball
import time
import LoadMap

img=['Setting','Exit']#이미지 이름

def map(screen):#스크린을 전달받음
    done = 1
    FPS = 60        #프레임
    key = 0         #공의 이동 방향 0이 바뀌지 않음 1이 오른쪽, -1이 왼쪽

    background = pygame.Surface(screen.get_size())  # 스크린과 동일크기의 surface생성 이곳에 그린후 스크린에 복사
    clock = pygame.time.Clock()  # 프레임 설정시 사용

    wall_list, star, ball = LoadMap.loadmap(screen)

    while done:
        clock.tick(FPS)     #프레임 설정

        #이벤트 받아오기
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

        #벽과충돌
        collision_list = pygame.sprite.spritecollide(ball, wall_list, False, pygame.sprite.collide_mask)
        for c in collision_list:
            ball.wall_collision(c)

        #공이동
        ball.move_check(key)

        #클리어 체크
        if(pygame.sprite.collide_mask(ball,star)):
            done = 0

        #백르라운드에 그리기
        background.fill((255,255,255))                #그려진거 비우기
        background.blit(star.image, star.rect)
        background.blit(ball.image, ball.rect)
        wall_list.draw(background)
        #스크린에 그리고 새로고침
        screen.blit(background,(0,0))
        pygame.display.flip()

    else:
        print("클리어")
        return 0


screen = pygame.display.set_mode((0, 0))
map(screen)
