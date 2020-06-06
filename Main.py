# Bouncy Dungeon Tech-alpha 0.1
import pygame, sys, os, configparser
from pygame.locals import *


# Setting before Main
mainClock = pygame.time.Clock()

# Load Config.cfg
configParser = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), 'game/data/Setting.cfg')
configParser.read(configFilePath)
FullToggle = configParser.get("Setting", "Fullscreen_Toggle")
SoundFX = configParser.get("Setting", "Sound_Fx")
SoundToggle = configParser.get("Setting", "Sound")
ScoreToggle = configParser.get("Setting", "Display_Score")

# Pygame Initialize
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('BOUNCY DUNGEON')
width, height = 1920, 1080
if FullToggle == "True":
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((0, 0))


Start_background = pygame.image.load("game/image/Background.png")
Start_Button = pygame.image.load("game/image/Game Start.png")
Help_Button = pygame.image.load("game/image/Help.png")
Score_Button = pygame.image.load("game/image/Score Board.png")
Setting_Button = pygame.image.load("game/image/Setting.png")
Exit_Button = pygame.image.load("game/image/Exit.png")
Gray_Background = pygame.image.load("game/image/Gray Background.png")
Score_Board = pygame.image.load("game/image/Score_Board.png")
Click_Sound = pygame.mixer.Sound("game/audio/click.wav")

class button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True


s_button = button(0.64583*width, 0.5*height, 615, 141)
score_button = button(1240, 715, 615, 141)
setting_button = button(1770, 20, 122, 121)
help_button = button(1680, 20, 66, 105)
exit_button = button(1300, 880, 481, 110)


# Here is Main
def Start_Menu():
    pygame.mixer.music.load('game/audio/Main-bgm.mp3')
    pygame.mixer.music.play(-1)
    while True:
        screen.blit(Start_background, (0, 0))
        screen.blit(Setting_Button, (1770, 20))
        screen.blit(Help_Button, (1680, 20))
        screen.blit(Start_Button, (1240, 540))
        screen.blit(Score_Button, (1240, 715))
        screen.blit(Exit_Button, (1300, 880))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    pygame.mixer.music.pause()
                    Game_Menu()
                    pygame.mixer.music.unpause()
                if setting_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Setting_Menu()
                if score_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Score_Menu()
                if help_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Help_Menu()
                if exit_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    pygame.time.wait(100)
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


def Game_Menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def Setting_Menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def Score_Menu():
    running = True
    screen.blit(Score_Board, (0, 0))
    textheight = height // 2 - 160
    textwidth = width // 2 - 250
    while running:
        f = open('game/data/rank.txt', 'r')
        textheight = height / 2 - 160
        textwidth = width / 2 - 250
        while True:
            line = f.readline()
            if not line:
                break
            name, score = line.split(' ')
            text = name + "                                       " + score
            textfont = pygame.font.Font('game/data/NanumGothic.ttf', 40)
            text = textfont.render(text, True, (0, 0, 0))
            textpos = text.get_rect()
            textheight += 45
            textpos.center = (textwidth, textheight)
            screen.blit(text, textpos)
        f.close()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0


def Help_Menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


Start_Menu()