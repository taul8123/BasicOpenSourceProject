import pygame

MAX_SPEED=3     #최대 속도
def to_Zero(num):
    '''관성구현을 휘한 함수'''
    if num < 0:
        return 1
    elif num > 0:
        return -1
    else:
        return 0


class Ball(pygame.sprite.Sprite):
    def __init__(self, img, location, area,FPS=30):     # 이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달  ex: (가로,세로),FPS
        pygame.sprite.Sprite.__init__(self)             #스프라이트 초기화
        self.image = pygame.transform.scale(img, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()               # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.center = location                     #위치 설정
        self.mask = pygame.mask.from_surface(self.image)#충돌감지를 위한 마크 생성

        #함수내용 구현시 필요 한것
        self.gravity=MAX_SPEED/FPS                        #왕복하는데 걸리는 프레임
        self.speed=[0,-MAX_SPEED]                         #공의 속도를 조정 [x,y]
        self.dontchangespeed=0                            # 좌우스피드 변경 불가능하게 하는 프레임수


    def move_y(self):
        '''y이동을 계산하는 함수로 y는 공기준으로 위가 - 아래가 +'''
        x,y=self.rect.center

        #속도변화
        self.speed[1]+=self.gravity

        #y이동
        y+=self.speed[1]
        self.rect.center=(x,y)      #좌표값변경

    def move_x(self,a):
        '''x를 이동 a는 가속도(속도 최대 값 있음)'''
        #x는 공기준으로 오른쪽이 + 왼쪽이 -
        x,y=self.rect.center

        #속도변화
        if a==0:
            self.speed[0]+=to_Zero(self.speed[0])
        else:
            self.speed[0] += a

            #최대 속도 제한
        if self.speed[0]<-MAX_SPEED:
            self.speed[0]=-MAX_SPEED

        elif self.speed[0]>MAX_SPEED:
            self.speed[0]=MAX_SPEED

        #x이동
        x += self.speed[0]
        self.rect.center=(x,y)      #좌표값변경



    def wall_collision(self,wall):
        '''벽과 충돌시의 행동'''
        #벽의 옆면과 부딪혔을때
        if (wall.rect.right<=self.rect.center[0] and self.speed[0]<0) or (wall.rect.left>self.rect.center[0] and self.speed[0]>0):
            self.dontchangespeed=10         #벽에 닿아서 튕겨 나올때 x축 속도를 못 바꾸게 하기위해서 사용(현재 10프레임동안 불가능)
            self.speed[0]=-self.speed[0]
            #떨어질때 닿은 것이 아니라 올라갈때 닿으면 더 올라갈 수 있도록 y축 설정 (벽타기)
            if self.speed[1]<=0:
                self.speed[1] = -MAX_SPEED//2


        #벽의 아래 또는 윗면과 부딧혔을때
        #y좌표는 낮을수록 위이기에 ball이 더 작을 경우가 wall이 아래 있음
        if(wall.rect.top>self.rect.center[1]):
            self.speed[1]=-MAX_SPEED

        #wall의 좌표가 작을때 즉 더 위에 있을 경우
        elif wall.rect.bottom<self.rect.center[1]:
            self.speed[1]=1

    def movex(self):
        '''x를 외부 요인 없이 그냥이동'''
        x,y=self.rect.center

        x += self.speed[0]

        self.rect.center = (x, y)  # 좌표값변경


    def move_check(self,key):
        '''어떻게 이동할 것인지 체크 후 이동'''
        if self.dontchangespeed==0:
            self.move_x(key)
        #x축 속도 변화 없음
        else:
            self.dontchangespeed-=1
            self.movex()

        self.move_y()





