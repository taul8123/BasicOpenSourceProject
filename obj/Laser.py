import pygame
from obj import Wall
'''레이저 출력수정'''

class Layser(pygame.sprite.Sprite):
    width = 40
    def __init__(self,img,location):
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, (Layser.width,10))  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성



    def Move(self):
        self.rect.left=self.rect.left+Layser.width




class Layserblock(Wall.Wall):
    def __init__(self,block_img,layser_img,location,area,obj):
        Wall.Wall.__init__(self,block_img,location,area)
        self.layser_img=layser_img
        self.col_obj = obj

    def layser(self,layser_list):
        for layser in layser_list:
            layser.Move()

        for obj in self.col_obj:
            collision_list = pygame.sprite.spritecollide(obj, layser_list, False, pygame.sprite.collide_mask)
            for layser in collision_list:
                layser_list.remove(layser)

        layser_list.add(Layser(self.layser_img,self.rect.topright))





