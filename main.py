#by E2Z1   e2z1.ml   https://github.com/E2Z1/


import random
import pygame
import sys
from pygame.locals import *
import os
from os import listdir
from os.path import isfile, join
import time
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import webbrowser

import maze

# searchstamp
howmanydogs = 3
showfps = True
max_fps = 1000
width = 15
zoom = False
height = 15
volume = 1
sounds = True
mousecontrol = False
pxl_width = 800
pxl_height = 800
settings = open("settings.txt","r")
color = [0,0,0]
font = ""
texturepack = "default"
texturepackslist = [f for f in listdir("texturepacks") if not isfile(join("texturepacks", f))]
fulls = False


settings = open("settings.txt","r")
exec(settings.read())
settings.close()
settings = open("settings.txt","r")
settingsall = settings.read().splitlines()
settings.close()


pygame.init()
FB = min(pxl_width // width, pxl_height // height)
screen = pygame.display.set_mode((pxl_width,pxl_height), RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Labyrinth")
pygame.display.set_allow_screensaver(False)
pygame.display.set_icon(pygame.image.load("texturepacks/icon.png"))
legit = True

# searchstamp

class timer:
    def __init__(self):
        self.startpoint = time.time()
        self.ispause = False
    def start(self):
        self.startpoint = time.time()
    def gettime(self):
        return time.time()-self.startpoint
    def pause(self):
        if not self.ispause:
            self.timeofpause = self.gettime()
            self.ispause = True
    def resume(self):
        if self.ispause:
            self.startpoint = time.time()-self.timeofpause
            self.ispause = False
# searchstamp
class dog:
    def __init__(self):
        matrixl = []
        self.richtung = 0
        row = 0
        self.anzahlrichtungen = 0
        self.fastrichtung = 0
        for i in range(int(len(l) / width)):
            matrixl.append(l[row:row + width])
            row += width
        for i in range(len(matrixl)):
            for j in range(len(matrixl[i])):
                matrixl[i][j] = 0 if matrixl[i][j] == "w" else 1

        grid = Grid(matrix=matrixl)
        while True:
            self.x = random.randint(0, width - 1) + 0.5
            self.y = random.randint(0, height - 1) + 0.5
            if l[int(self.x) + int(self.y) * height][0] == "p" and abs(self.x-x) > 4 and abs(self.y-y) > 4:
                break
        self.start = grid.node(int(self.x), int(self.y))
        self.end = grid.node(int(x), int(y))
        self.path = []
    def pathfind(self):
        matrixl = []
        row = 0
        for i in range(int(len(l) / width)):
            matrixl.append(l[row:row + width])
            row += width
        for i in range(len(matrixl)):
            for j in range(len(matrixl[i])):
                matrixl[i][j] = 0 if matrixl[i][j] == "w" else 1
        grid = Grid(matrix=matrixl)
        self.start = grid.node(int(self.x), int(self.y))
        self.end = grid.node(int(x), int(y))
        finder = AStarFinder()
        self.path, _ = finder.find_path(self.start, self.end, grid)
    def run(self):

        if len(self.path) != 0:
            if mousepoweractivated.gettime() > 45:

                geschw = 0.01



                self.fastrichtung = 0
                self.anzahlrichtungen = 0
                if self.x < int(self.path[0][0])+0.475:
                    self.fastrichtung += 3
                    self.anzahlrichtungen += 1
                    self.x += geschw * 60 / (clock.get_fps() + 0.00000001)
                if self.x > int(self.path[0][0])+0.525:

                    self.fastrichtung += 1
                    self.anzahlrichtungen += 1
                    self.x -= geschw * 60 / (clock.get_fps() + 0.00000001)
                if self.y < int(self.path[0][1])+0.475:

                    self.fastrichtung += 2
                    self.anzahlrichtungen += 1
                    self.y += geschw * 60 / (clock.get_fps() + 0.00000001)
                if self.y > int(self.path[0][1])+0.525:

                    self.fastrichtung += 0
                    self.anzahlrichtungen += 1
                    self.y -= geschw * 60 / (clock.get_fps() + 0.00000001)
                if int(self.y) == int(self.path[0][1]) and int(self.x) == int(self.path[0][0]) and not len(self.path) == 0:
                    self.path.pop(0)
                if self.anzahlrichtungen != 0:
                    self.richtung = self.fastrichtung/self.anzahlrichtungen
                if int(self.y) == int(y) and int(self.x) == int(x):
                    damage()


    def draw(self):
        global zoom,legit
        if zoom and legit and not inhole:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(dogimg, (ZOOM_FB,ZOOM_FB)), self.richtung * 90),
                        ((2.5 + (self.x - x)) * ZOOM_FB+BreiVer
                         - (pygame.transform.rotate(pygame.transform.scale(dogimg, (ZOOM_FB, ZOOM_FB)),
                                                            self.richtung * 90).get_width()) // 2,
                         (2.5 + (self.y - y)) * ZOOM_FB+HohVer - (
                             pygame.transform.rotate(pygame.transform.scale(dogimg, (ZOOM_FB, ZOOM_FB)), self.richtung * 90)
                                 .get_height()) / 2))
        else:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)), self.richtung * 90),
                        (self.x * FB +
                         BreiVer - (pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)),
                                                            self.richtung * 90).get_width()) // 2,
                         self.y * FB + HohVer - (
                             pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)), self.richtung * 90)
                             .get_height()) / 2))
    def draw_at(self,xdraw,ydraw,richtungdraw):
        screen.blit(pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)), richtungdraw * 90),
                    (xdraw * FB +
                     BreiVer - (pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)),
                                                        richtungdraw * 90).get_width()) // 2,
                     ydraw * FB + HohVer - (
                         pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)), richtungdraw * 90)
                             .get_height()) / 2))

    def sleep_draw_at(self,xdraw,ydraw,richtungdraw):
        screen.blit(pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)), richtungdraw * 90),
                    (xdraw * FB +
                     BreiVer - (pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)),
                                                        richtungdraw * 90).get_width()) // 2,
                     ydraw * FB + HohVer - (
                         pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)), richtungdraw * 90)
                             .get_height()) / 2))
    def sleep_draw(self):
        global zoom, legit
        if zoom and legit and not inhole:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(sldogimg, (ZOOM_FB, ZOOM_FB)), self.richtung * 90),
                        ((2.5 + (self.x - x)) * ZOOM_FB + BreiVer
                         - (pygame.transform.rotate(pygame.transform.scale(sldogimg, (ZOOM_FB, ZOOM_FB)),
                                                    self.richtung * 90).get_width()) // 2,
                         (2.5 + (self.y - y)) * ZOOM_FB + HohVer - (
                             pygame.transform.rotate(pygame.transform.scale(sldogimg, (ZOOM_FB, ZOOM_FB)),
                                                     self.richtung * 90)
                                 .get_height()) / 2))
        else:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)), self.richtung * 90),
                        (self.x * FB +
                         BreiVer - (pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)),
                                                            self.richtung * 90).get_width()) // 2,
                         self.y * FB + HohVer - (
                             pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)), self.richtung * 90)
                             .get_height()) / 2))


speedruntimer = timer()
dogshowtimer = timer()
mousepoweractivated = timer()


def toggle_fullscreen():
    global fulls, screen, old_pxl_width, old_pxl_height
    if fulls:

        screen = pygame.display.set_mode((old_pxl_width, old_pxl_height), RESIZABLE)
        fulls = not fulls
    else:
        old_pxl_width, old_pxl_height = pxl_width, pxl_height
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        fulls = not fulls





def textures():
    global kitty,wall,heartimg,path,glowf,deadf,dogimg,dogsound,winsound,diesound,damagesound,holeimg,mouseimg,sldogimg
    try:
        kitty = pygame.image.load("texturepacks/"+texturepack+"/kitty.png")
    except:
        kitty = pygame.image.load("texturepacks/default/kitty.png")
    try:
        dogimg = pygame.image.load("texturepacks/"+texturepack+"/dog.png")
    except:
        dogimg = pygame.image.load("texturepacks/default/dog.png")
    try:
        sldogimg = pygame.image.load("texturepacks/"+texturepack+"/sleeping_dog.png")
    except:
        sldogimg = pygame.image.load("texturepacks/default/sleeping_dog.png")
    try:
        wall = pygame.image.load("texturepacks/"+texturepack+"/wall.png")
    except:
        wall = pygame.image.load("texturepacks/default/wall.png")
    try:
        heartimg = pygame.image.load("texturepacks/"+texturepack+"/heart.png")
    except:
        heartimg = pygame.image.load("texturepacks/default/heart.png")
    try:
        path = pygame.image.load("texturepacks/"+texturepack+"/path.png")
    except:
        path = pygame.image.load("texturepacks/default/path.png")
    try:
        glowf = [pygame.image.load("texturepacks/"+texturepack+"/glowing_fish/1.png"),pygame.image.load("texturepacks/"+texturepack+"/glowing_fish/2.png")]
    except:
        glowf = [pygame.image.load("texturepacks/default/glowing_fish/1.png"),pygame.image.load("texturepacks/default/glowing_fish/2.png")]
    try:
        deadf = pygame.image.load("texturepacks/"+texturepack+"/fish_dead.png")
    except:
        deadf = pygame.image.load("texturepacks/default/fish_dead.png")
    try:
        holeimg = pygame.image.load("texturepacks/"+texturepack+"/hole.png")
    except:
        holeimg = pygame.image.load("texturepacks/default/hole.png")
    try:
        mouseimg = pygame.image.load("texturepacks/"+texturepack+"/mouse.png")
    except:
        mouseimg = pygame.image.load("texturepacks/default/mouse.png")






    try:
        dogsound = pygame.mixer.Sound("texturepacks/"+texturepack+"/audio/dog.wav")
    except:
        dogsound = pygame.mixer.Sound("texturepacks/default/audio/dog.wav")
    try:
        diesound = pygame.mixer.Sound("texturepacks/"+texturepack+"/audio/die.wav")
    except:
        diesound = pygame.mixer.Sound("texturepacks/default/audio/die.wav")
    try:
        winsound = pygame.mixer.Sound("texturepacks/"+texturepack+"/audio/win.wav")
    except:
        winsound = pygame.mixer.Sound("texturepacks/default/audio/win.wav")
    try:
        damagesound = pygame.mixer.Sound("texturepacks/"+texturepack+"/audio/damage.wav")
    except:
        damagesound = pygame.mixer.Sound("texturepacks/default/audio/damage.wav")


hearts = 7

richtung = 0
#richtung = 0,1,2,3

whereru = "play"

fat = 0

textures()
old_width, old_height = pxl_width,pxl_height
BreiVer,HohVer = 0,0
if pxl_width > pxl_height:

    BreiVer = (max(pxl_width, pxl_height) - min(pxl_width, pxl_height)) / 2
else:

    HohVer = (max(pxl_width, pxl_height) - min(pxl_width, pxl_height)) / 2


def doeselementinlistexist(list,index):
    try:
        if list[index]:
            return True
    except:
        return False

# searchstamp

def changesettings(key,inhalt):
    for i in range(len(settingsall)):
        dings = 0
        try:
            for j in range(len(key)):
                if settingsall[i][j] == key[j]:
                    dings += 1
            if dings == len(key):
                finalline = key + " = " + inhalt
                settingsall[i] = finalline
        except:
            pass
    settings = open("settings.txt", "w")
    settings.write("")
    settings.close()
    settings = open("settings.txt","a")
    for i in range(len(settingsall)):
        settings.write(settingsall[i] + "\n")
    settings.close()
# searchstamp

def button(x,y,width,height,colorbox,colortext,font,text,action,size):
    global mouse,scrollverschiebung
    writething = pygame.font.SysFont(font,size).render(text,True,colortext)
    pygame.draw.rect(screen,colorbox,(x,y,width,height),0,4,4,4,4)
    screen.blit(writething,(x+(width - writething.get_width())//2,y+(height - writething.get_height())//2))
    if x+width > pygame.mouse.get_pos()[0] > x and y+height > pygame.mouse.get_pos()[1] > y and mouse == 1:
        exec(action)
        mouse = 0
        scrollverschiebung = 0



startx = 0
starty = 0
# searchstamp

def reset():
    global l,x,y,hearts,fish,feld,fat,geschw,startx,starty,holes,mice,dogs,whereru,howmanydogs,dogpos,dogrichtungen,savedas
    fat = 0
    l = generate(width, height)
    geschw = 0.03
    mousepoweractivated.startpoint = 0
    dogpos = []
    dogrichtungen = []

    while True:
        startx = random.randint(0,width-1) + 0.5
        starty = random.randint(0,height-1) + 0.5
        x, y = startx, starty
        if l[int(x)+int(y)*height][0] == "p":
            break



    fish = []
    hearts = 7
    speedruntimer.resume()
    dogshowtimer.resume()
    speedruntimer.start()
    dogshowtimer.start()
    paths = 0
    for i in l:
        if i[0] == "p":
            paths += 1

    for i in range(min(paths, 5)):
        go = True
        while go:
            feld = random.randint(0, width * height - 1)
            if l[feld][0] == "p" and fish.count(feld) == 0:
                fish.append(feld)
                go = False


    holes = []


    for i in range(min(paths, 3)):
        go = True
        while go:
            feld = random.randint(0, width * height - 1)
            if l[feld][0] == "p" and fish.count(feld) == 0 and holes.count(feld) == 0:
                holes.append(feld)
                go = False

    mice = []

    for i in range(min(paths, 2)):
        go = True
        while go:
            feld = random.randint(0, width * height - 1)
            if l[feld][0] == "p" and fish.count(feld) == 0 and holes.count(feld) == 0 and mice.count(feld) == 0:
                mice.append(feld)
                go = False
    dogs = []
    for _ in range(howmanydogs):
        dogs.append(dog())
    for i in dogs:
        i.pathfind()
    whereru = "play"
    savedas = False

def neue_richtung():
    # willkürliche permutation aus den 4 himmelsrichtungen. osten, sueden, westen, norden
    richtungen = list('oswn')
    random.shuffle(richtungen)

    # danach teilstring davon auswählen, anhand gegebener wkeiten
    num = random.randint(0,99)
    richtung = ''
    # prozent für nur eine richtung
    if num < 70:
        richtung = richtungen[0]
    # prozent für zwei richtungen
    elif 70 <= num < 90:
        richtung = richtungen[2]
    # prozent für drei richtungen
    elif 90 <= num:
        richtung = richtungen[3]

    return richtung


def generate(width, hight):

    return maze.maze(width)

    # e: empty, w: wall, p: path
    lab = ['e'] * width * hight

    start = len(lab) // 2 + (width // 2 * (len(lab) % 2 == 0))
    lab[start] = 'pu'

    verbotene_richtungen = []
    cur = start
    path_fields = []
    richtung = neue_richtung()

    cnt = 0
    for _ in range(1000):


        if doeselementinlistexist(lab,cur+1) and richtung == 'o' and lab[cur+1] == 'e' and (cur+1) % width != 0:
            lab[cur+1] = 'p' + str(cnt)
            path_fields.append(cur+1)
            if doeselementinlistexist(lab,cur-1) and cur-1 >=0 and lab[cur-1] == 'e':
                lab[cur-1] = 'w' + str(cnt)
            if doeselementinlistexist(lab,cur-width-1) and cur -width -1 >=0 and lab[cur -width -1] == 'e':
                lab[cur -width -1] = 'w' + str(cnt)
            if doeselementinlistexist(lab,cur+width-1) and cur +width -1 >=0 and lab[cur +width -1] == 'e':
                lab[cur +width -1] = 'w' + str(cnt)
            verbotene_richtungen = []
        elif doeselementinlistexist(lab,cur+width) and richtung == 's' and lab[cur -width] == 'e' and (cur // width) < height:
            lab[cur +width] = 'p' + str(cnt)
            path_fields.append(cur +width)
            if doeselementinlistexist(lab,cur-width-1) and cur -width -1 >=0 and lab[cur -width -1] == 'e':
                lab[cur -width -1] = 'w' + str(cnt)
            if doeselementinlistexist(lab,cur-width) and cur -width >=0 and lab[cur -width] == 'e':
                lab[cur -width] = 'w' + str(cnt)
            if doeselementinlistexist(lab,cur-width+1) and cur -width +1 >=0 and lab[cur -width +1] == 'e':
                lab[cur -width +1] = 'w' + str(cnt)
            verbotene_richtungen = []
        elif doeselementinlistexist(lab,cur-1) and richtung == 'w' and lab[cur -1] == 'e' and (cur-1) % width != width-1:
            lab[cur -1] = 'p' + str(cnt)
            path_fields.append(cur -1)
            if doeselementinlistexist(lab,cur+1) and cur+1 < len(lab) and lab[cur+1] == 'e':
                lab[cur+1] = 'w' + str(cnt)
            if doeselementinlistexist(lab,cur-width+1) and cur -width +1 >=0 and lab[cur -width +1] == 'e':
                lab[cur -width +1] = 'w' + str(cnt)
            if doeselementinlistexist(lab,cur+width+1) and cur +width +1 >=0 and lab[cur +width +1] == 'e':
                lab[cur +width +1] = 'w' + str(cnt)
            verbotene_richtungen = []
        # nach norden
        elif doeselementinlistexist(lab,cur-width) and richtung == 'n' and lab[cur -width] == 'e' and cur // width > 0:
            lab[cur -width] = 'p' + str(cnt)
            path_fields.append(cur -width)
            if cur +width -1 >=0 and lab[cur +width -1] == 'e':
                lab[cur +width -1] = 'w' + str(cnt)
            if cur +width >=0 and lab[cur +width] == 'e':
                lab[cur +width] = 'w' + str(cnt)
            if cur +width +1 >=0 and lab[cur +width +1] == 'e':
                lab[cur +width +1] = 'w' + str(cnt)
            verbotene_richtungen = []
        # testet nur auf empty, nicht ob eine wall oder path vorliegt


        # wenn p auf w stoesst, dann neue richtung



        elif verbotene_richtungen.count(richtung) == 0:
            verbotene_richtungen.append(richtung)

        cnt += 1
        if len(verbotene_richtungen) == 4:
            break
        richtung = neue_richtung()
        while verbotene_richtungen.count(richtung) != 0:
            richtung = neue_richtung()

        if path_fields:
            cur = path_fields[0]
            path_fields.pop(0)












    return maze.maze(width)


yourtime = 0
lastposkitty = (0,0)

def scrolling():
    global scrollverschiebung
    #up
    if scroll == 4:
        scrollverschiebung -= 10
    #down
    if scroll == 5:
        scrollverschiebung += 10
# searchstamp

def player():
    global richtung,y,x,hearts,l,whereru,fat,geschw,inhole,mousevis,mice,lastposkitty,dogs,finaltime,mouse,whereru
    fastrichtung = 0
    anzahlrichtungen = 0
    key = pygame.key.get_pressed()
    if (key[pygame.K_w] or key[pygame.K_UP]) and y >= 0:
        fastrichtung += 0
        anzahlrichtungen += 1
        y -= geschw*60/(clock.get_fps()+0.00000001)
    if (key[pygame.K_a] or key[pygame.K_LEFT]) and x >= 0:
        fastrichtung += 1
        anzahlrichtungen += 1
        x -= geschw*60/(clock.get_fps()+0.00000001)
    if (key[pygame.K_s] or key[pygame.K_DOWN]) and y < height-geschw*60/(clock.get_fps()+0.00000001):
        fastrichtung += 2
        anzahlrichtungen += 1
        y += geschw*60/(clock.get_fps()+0.00000001)
    if (key[pygame.K_d] or key[pygame.K_RIGHT]) and x < width-geschw*60/(clock.get_fps()+0.00000001):
        fastrichtung += 3
        anzahlrichtungen += 1
        x += geschw*60/(clock.get_fps()+0.00000001)
    if anzahlrichtungen != 0:
        richtung = fastrichtung/anzahlrichtungen

    if mousecontrol and mouse == 1:
        x,y = (pygame.mouse.get_pos()[0]-BreiVer)/FB,(pygame.mouse.get_pos()[1]-HohVer)/FB
        mousevis = True
        mouse = 0

    if not mousecontrol and not inhole:
        mousevis = False
    else:
        mousevis = True
    if legit and zoom and not inhole and whereru != "tut":
        if mousepoweractivated.gettime() < 45:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty, (
            (ZOOM_FB + fat * 3) * (mousepoweractivated.gettime() / 45), ZOOM_FB * (mousepoweractivated.gettime() / 45))),
                                                richtung * 90), (2.5 * ZOOM_FB + BreiVer - (pygame.transform.rotate(
                pygame.transform.scale(kitty, (
                (ZOOM_FB + fat * 3) * (mousepoweractivated.gettime() / 45), ZOOM_FB * (mousepoweractivated.gettime() / 45))),
                richtung * 90).get_width()) // 2, 2.5 * ZOOM_FB + HohVer - (pygame.transform.rotate(
                pygame.transform.scale(kitty, (
                (ZOOM_FB + fat * 3) * (mousepoweractivated.gettime() / 45), ZOOM_FB * (mousepoweractivated.gettime() / 45))),
                richtung * 90).get_height()) / 2))
        else:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty, (
                ZOOM_FB + fat * 3,
                ZOOM_FB)), richtung * 90), (2.5 * ZOOM_FB + BreiVer - (
                pygame.transform.rotate(pygame.transform.scale(kitty, (ZOOM_FB + fat * 3, ZOOM_FB)),
                                        richtung * 90).get_width()) // 2,
                                       2.5 * ZOOM_FB + HohVer - (
                                           pygame.transform.rotate(
                                               pygame.transform.scale(kitty, (
                                                   ZOOM_FB + fat * 3, ZOOM_FB)),
                                               richtung * 90).get_height()) // 2))
            pygame.draw.circle(screen,(255,255,255),(2.5*ZOOM_FB+BreiVer,2.5*ZOOM_FB+HohVer),10)
    else:
        if mousepoweractivated.gettime() < 45:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty,((FB+fat*3)*(mousepoweractivated.gettime()/45),FB*(mousepoweractivated.gettime()/45))),richtung*90),(x*FB+BreiVer-(pygame.transform.rotate(pygame.transform.scale(kitty,((FB+fat*3)*(mousepoweractivated.gettime()/45),FB*(mousepoweractivated.gettime()/45))),richtung*90).get_width())//2,y*FB+HohVer-(pygame.transform.rotate(pygame.transform.scale(kitty,((FB+fat*3)*(mousepoweractivated.gettime()/45),FB*(mousepoweractivated.gettime()/45))),richtung*90).get_height())/2))
        else:

            screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty, (
                FB + fat * 3,
                FB)), richtung * 90), (x * FB + BreiVer - (
                pygame.transform.rotate(pygame.transform.scale(kitty, (FB + fat * 3, FB)),
                                        richtung * 90).get_width()) // 2,
                                       y * FB + HohVer - (
                                           pygame.transform.rotate(
                                               pygame.transform.scale(kitty, (
                                                   FB + fat * 3, FB)),
                                               richtung * 90).get_height()) / 2))

    if l[int(x)+int(y)*height][0] == "w":
        damage()
    if doeselementinlistexist(fish, 0):
        if fish[0] == int(x)+int(y)*height:
            fish.pop(0)
            geschw -= 0.003
            fat += 3
            if hearts < 9:
                hearts += 1
            plymusic(winsound,1,False)
    else:
        if len(fish) == 0:
            whereru = "win"
            finaltime = speedruntimer.gettime()
    inhole = False
    for i in range(len(mice)):
        if doeselementinlistexist(mice,i) and mice[i] == int(x) + int(y) * height:
            mice.pop(i)
            plymusic(winsound,1,False)
            mousepoweractivated.start()
    for i in holes:
        if i == int(x)+int(y)*height and mousepoweractivated.gettime() < 45:
            inhole = True

    #pygame.draw.circle(screen,(255,255,255),(x*FB+BreiVer,y*FB+HohVer),5)
    if lastposkitty[0] != int(x) or lastposkitty[1] != int(y):
        for i in dogs:
            i.pathfind()
    lastposkitty = (int(x),int(y))

dogsavinglist = ["richtung","anzahlrichtungen","fastrichtung","x","y"]
dogsavingvariable = ""
savingvariable = ""
savinglist = ["l","x","y","hearts","fish","feld","fat","geschw","startx","starty","howmanydogs","holes","mice","dogs","dogpos","dogrichtungen"]
# searchstamp

def save(filename):
    global savinglist,savingvariable,mousepoweractivated,speedruntimer,dogshowtimer,savedas
    for i in savinglist:
        exec("global "+i)
    file = open("saves/"+filename,"w")

    for i in savinglist:
        if i != "dogs":

            if i == "whereru":
                exec("global i,savingvariable;savingvariable = " + i)
                file.write(i + " = '" + str(savingvariable) + "'\n")
            else:
                exec("global i,savingvariable;savingvariable = "+i)
                file.write(i+" = "+str(savingvariable)+"\n")
        else:
            file.write("dogs = []\n")
            for k in range(howmanydogs):
                file.write("dogs.append(dog())\n")
                for j in dogsavinglist:
                    exec("global j,dogsavingvariable,dogs;dogsavingvariable = dogs["+str(k)+"]." + j)
                    file.write("dogs["+str(k)+"]."+j + " = " + str(dogsavingvariable) + "\n")
    file.write("mousepoweractivated.startpoint = "+str(mousepoweractivated.startpoint)+ "\n")
    file.write("mousepoweractivated.ispause = "+str(mousepoweractivated.ispause)+ "\n")
    file.write("mousepoweractivated.timeofpause = "+str(mousepoweractivated.timeofpause)+ "\n")
    file.write("speedruntimer.startpoint = "+str(speedruntimer.startpoint)+ "\n")
    file.write("speedruntimer.ispause = "+str(speedruntimer.ispause)+ "\n")
    file.write("speedruntimer.timeofpause = "+str(speedruntimer.timeofpause)+ "\n")
    file.write("dogshowtimer.startpoint = "+str(dogshowtimer.startpoint)+ "\n")
    file.write("dogshowtimer.ispause = "+str(dogshowtimer.ispause)+ "\n")
    file.write("dogshowtimer.timeofpause = "+str(dogshowtimer.timeofpause)+ "\n")

    file.close()
    savedas = filename
# searchstamp

def getsaved(filename):
    global savinglist,savedas
    globalstring = "global "
    for i in range(len(savinglist)):
        if i+1 == len(savinglist):
            globalstring += savinglist[i]+";"
        else:
            globalstring += savinglist[i]+","
    file = open("saves/"+filename, "r")
    exec(globalstring+file.read())
    savedas = filename
    file.close()
def plymusic(music,channel,loop):
    pygame.mixer.Channel(1).set_volume(volume*sounds)

    #channel 0 ambient
    #channel 1 else
    if not loop:
        pygame.mixer.Channel(channel).play(music)
    else:
        pygame.mixer.Channel(channel).play(music,-1)

onslider = 0
waspressed = False
def damage():
    global x,y,starty,startx,hearts,whereru
    hearts -= 1
    x, y = startx, starty
    if hearts > 0:
        plymusic(damagesound,1,False)
    if hearts < 1:
        plymusic(diesound,1,False)
        whereru = "deadscreen"

#unixtime when the mouse power was activated

timebetweenpauseandplay = 0

pausewru = "main"
asktosave = False
tick = 0
fishmodel = 0
dogpos = []
dogrichtungen = []
lastwhereru = ["main"]
savedas = False

reset()
mousevis = mousecontrol
inhole = False
scrollverschiebung = 0
selectedworld = -1
whereru = "main"
nameofworld = ""
quitaction = ""
tutstage = 0
serverip = ""
servername = ""
selectedfieldserverip = False

# searchstamp

while True:
    global x,y
    if lastwhereru[-1] != whereru:
        lastwhereru.append(whereru)
    if len(lastwhereru) == 11:
        lastwhereru.pop(0)
    mouse = 0
    scroll = 0
    tick += 1
    pxl_width, pxl_height = pygame.display.get_surface().get_size()

    if old_width != pxl_width or old_height != pxl_height:
        BreiVer, HohVer = 0, 0

        if pxl_width > pxl_height:

            BreiVer = (max(pxl_width, pxl_height) - min(pxl_width, pxl_height)) / 2
        else:

            HohVer = (max(pxl_width, pxl_height) - min(pxl_width, pxl_height)) / 2
        old_width, old_height = pxl_width, pxl_height
    fishmodel = int(time.time()) % 2


    screen.fill((color[0], color[1], color[2]))

    # searchstamp

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if asktosave:
                whereru = "quit"
                quitaction = "sys.exit()"
            else:
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if whereru == "saveas":
                nameofworld += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    nameofworld = nameofworld[:-2]

            if whereru == "addserver":
                if selectedfieldserverip:
                    serverip += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        serverip = serverip[:-2]

                else:
                    servername += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        servername = servername[:-2]
                if event.key == pygame.K_TAB or event.key == pygame.K_RETURN:
                    if selectedfieldserverip:
                        serverip = serverip[:-1]
                    else:
                        servername = servername[:-1]

                    selectedfieldserverip = not selectedfieldserverip

            if event.key == pygame.K_r:
                reset()
            if event.key == pygame.K_ESCAPE and (whereru == "play" or whereru == "tut") and timebetweenpauseandplay > 10:
                whereru = "pause"
                timebetweenpauseandplay = 0
                pausewru = "main"
            if event.key == pygame.K_ESCAPE and whereru == "pause" and timebetweenpauseandplay > 10:
                whereru = lastwhereru[-2]
                timebetweenpauseandplay = 0
            if whereru == "showcase":
                whereru = "win"
            if whereru == "showcasebcdead":
                whereru = "deadscreen"



        if event.type == pygame.MOUSEBUTTONUP:
            mouse = event.button

        if event.type == pygame.MOUSEBUTTONDOWN:
            scroll = event.button
    # searchstamp

    if whereru == "main":
        pygame.mouse.set_visible(True)
        mousepoweractivated.pause()
        speedruntimer.pause()
        dogshowtimer.pause()
        button(10, pxl_height - pxl_height / 1.4, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Play",
               "global whereru;reset();whereru = 'play'", 80)
        button(pxl_width / 2 + 5, pxl_height - pxl_height / 1.4, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Play Saved",
               "global whereru;whereru = 'saved'", 80)
        button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 1.15, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Create a server",
               "webbrowser.open(r'https://e2z1.ml/projects/KittyLabyrinth')", 80)
        button(pxl_width / 2 + 5, pxl_height - pxl_height / 1.15, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Play online",
               "global whereru;whereru = 'onlinescreen'", 80)
        button(10, pxl_height - pxl_height / 2.5, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Exit",
               "sys.exit()", 80)
        button(pxl_width / 2 + 5, pxl_height - pxl_height / 2.5, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Fullscreen",
               "toggle_fullscreen()", 80)
        button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 1.8, pxl_width - 20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Settings",
               "global whereru,pausewru;whereru = 'pause';pausewru = 'settings'", 80)
        button(10, pxl_height - pxl_height / 5, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Help",
               "webbrowser.open(r'https://e2z1.ml/projects/KittyLabyrinth')", 80)
        button(pxl_width / 2 + 5, pxl_height - pxl_height / 5, pxl_width / 2 - 15, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Tutorial",
               "global whereru;whereru = 'tut'", 80)
        asktosave = False
    # searchstamp

    if whereru == "onlinescreen":
        pygame.mouse.set_visible(True)
        mousepoweractivated.pause()
        speedruntimer.pause()
        dogshowtimer.pause()
        scrolling()
        servers = []
        exec(open("servers.txt", "r").read())

        for i in range(len(servers)):
            if selectedworld == i:
                button(5, i * (100 + 5) + scrollverschiebung, 500, 100,
                       (0, 0, 200), (color[0], color[1], color[2]), font,
                       servers[i][0],
                       "global whereru; whereru = 'serverplay'", 50)
            else:
                button(5, i * (100 + 5) + scrollverschiebung, 500, 100,
                       (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                       servers[i][0],
                       "global selectedworld; selectedworld = i", 50)

        pygame.draw.rect(screen, color, (
            0, pxl_height - pxl_height / 1.85 - 5, pxl_width, pxl_height - (pxl_height - pxl_height / 2.5 - 5)))
        if selectedworld != -1:
            button(10, pxl_height - pxl_height / 1.85, (pxl_width - 30) / 2, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Delete",
                   "global selectedworld, servers; servers.pop(selectedworld);selectedworld = -1",
                   80)
            button(20 + (pxl_width - 30) / 2, pxl_height - pxl_height / 1.85, (pxl_width - 30) / 2, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Edit",
                   "global whereru,servername,serverip;whereru = 'addserver';servername = servers[i][0];serverip = servers[i][1]",
                   80)
        button(10, pxl_height - pxl_height / 2.5, pxl_width - 20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Add",
               "global whereru,servername,serverip;whereru = 'addserver'; servername = ''; serverip = ''", 80)
        button(pxl_width / 2 - 500 / 2, pxl_height - pxl_height / 5, 500, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Back",
               "global whereru,selectedworld;whereru = 'main';selectedworld = -1", 80)
        stringthatwillbewritten = "["
        for i in servers:
            stringthatwillbewritten += "["
            for j in i:
                stringthatwillbewritten += "'"+j+"',"
            stringthatwillbewritten += "],"


        open("servers.txt", "w").write("servers = "+stringthatwillbewritten+"]")

    if whereru == "addserver":
        exec(open("servers.txt", "r").read())

        if servername == "":
            writething = pygame.font.SysFont(font, 150).render('(Name)', True,
                                                            (color))
        else:
            writething = pygame.font.SysFont(font, 150).render(servername, True,
                                                            (color))
        if serverip == "":
            writething1 = pygame.font.SysFont(font, 150).render('(IP)', True,
                                                               (color))
        else:
            writething1 = pygame.font.SysFont(font, 150).render(serverip, True,
                                                               (color))
        pygame.draw.rect(screen, (255 - color[0], 255 - color[1], 255 - color[2]), ((pxl_width - writething.get_width()) // 2-5, (pxl_height - writething.get_height()) // 5-5, writething.get_width()+10, writething.get_height()+10))
        screen.blit(writething,
                    ((pxl_width - writething.get_width()) // 2, (pxl_height - writething.get_height()) // 5))
        pygame.draw.rect(screen, (255 - color[0], 255 - color[1], 255 - color[2]), ((pxl_width - writething1.get_width()) // 2-5, (pxl_height - writething1.get_height()) // 2-5, writething1.get_width()+10, writething1.get_height()+10))
        screen.blit(writething1,
                    ((pxl_width - writething1.get_width()) // 2, (pxl_height - writething1.get_height()) // 2))
        button(10, pxl_height - pxl_height / 5, (pxl_width - 30) / 2, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Cancel",
               "global whereru; whereru = 'onlinescreen'",
               80)
        button(20 + (pxl_width - 30) / 2, pxl_height - pxl_height / 5, (pxl_width - 30) / 2, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
               "Save",
               "global whereru,servers; whereru = 'onlinescreen';servers.append([servername,serverip])",
               80)

        stringthatwillbewritten = "["
        for i in servers:
            stringthatwillbewritten += "["
            for j in i:
                stringthatwillbewritten += "'" + j + "',"
            stringthatwillbewritten += "],"

        open("servers.txt", "w").write("servers = " + stringthatwillbewritten + "]")


    if whereru == "quit":
        pygame.mouse.set_visible(True)
        mousepoweractivated.pause()
        speedruntimer.pause()
        dogshowtimer.pause()

        button(0, 0, pxl_width/2, pxl_height/2,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Save & Quit",
               "global whereru,savedas,quitaction\nif not savedas: whereru = 'saveas'\nelse: save(savedas); exec(quitaction)", 70)
        button(pxl_width / 2+3, 0, pxl_width / 2-3, pxl_height / 2,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Just Quit",
               "global quitaction; exec(quitaction)", 70)
        button(0, pxl_height/2+3, pxl_width, pxl_height / 2-3,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Cancel",
               "global whereru,lastwhereru;whereru = lastwhereru[-2];lastwhereru.pop(-1)", 70)
        asktosave = False
    # searchstamp

    if whereru == "saveas":
        writething = pygame.font.SysFont(font, 150).render(nameofworld, True, (255 - color[0], 255 - color[1], 255 - color[2]))
        pygame.draw.rect(screen, (255 - color[0], 255 - color[1], 255 - color[2]), ((pxl_width - writething.get_width()) // 2-5, (pxl_height - writething.get_height()) // 5-5, writething.get_width()+10, writething.get_height()+10))
        screen.blit(writething,
                    ((pxl_width - writething.get_width()) // 2,(pxl_height - writething.get_height()) // 2))
        button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 5, pxl_width - 20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Save & Quit",
               "global nameofworld,quitaction;save(nameofworld+'.labyrinth');exec(quitaction)", 70)
        # searchstamp

    if whereru == "saved":
        pygame.mouse.set_visible(True)
        mousepoweractivated.pause()
        speedruntimer.pause()
        dogshowtimer.pause()


        scrolling()
        worldlist = [f for f in listdir(os.path.join("saves"))]
        try:
            worldlist.remove(".DS_Store")
        except:
            pass
        for i in range(len(worldlist)):
            worldlist[i] = worldlist[i][0:-10]
        for i in range(len(worldlist)):
            if selectedworld == i:
                button(5, i * (100 + 5) + scrollverschiebung, 500, 100,
                       (0,0,200), (color[0], color[1], color[2]), font,
                       worldlist[i],
                       "global whereru; whereru = 'play'; getsaved(worldlist[selectedworld]+'.labyrinth')", 50)
            else:
                button(5, i * (100 + 5) + scrollverschiebung, 500, 100,
                       (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                       worldlist[i],
                       "global selectedworld; selectedworld = i", 50)


        pygame.draw.rect(screen, color, (
        0, pxl_height - pxl_height / 2.5 - 5, pxl_width, pxl_height - (pxl_height - pxl_height / 2.5 - 5)))
        if selectedworld != -1:
            button(10, pxl_height - pxl_height / 2.5, (pxl_width - 30) / 2, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Delete",
                   "global selectedworld, worldlist ;os.remove('saves/'+worldlist[selectedworld]+'.labyrinth');selectedworld = -1", 80)
            button(20 + (pxl_width - 30) / 2, pxl_height - pxl_height / 2.5, (pxl_width - 30) / 2, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Play", "global whereru,selectedworld; whereru = 'play'; getsaved(worldlist[selectedworld]+'.labyrinth');selectedworld = -1", 80)
        button(pxl_width / 2 - 500 / 2, pxl_height - pxl_height / 5, 500, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Back",
               "global whereru,selectedworld,lastwhereru;whereru = lastwhereru[-2];selectedworld = -1", 80)

    # searchstamp

    if whereru == "tut":
        ZOOM_FB = min(pxl_width // 5, pxl_height // 5)
        pygame.mouse.set_visible(False)
        mousepoweractivated.pause()
        speedruntimer.pause()
        dogshowtimer.pause()


        asktosave = False
        if tutstage == 0:
            l = 49*["p"]
            width = 7
            height = 7
            x,y = 3.5,3.5
            dogs = []
        FB = min(pxl_width // width, pxl_height // width)
        for j in range(len(l)):
            row_idx = (j // width) * FB + HohVer
            col_idx = (j % width) * FB + BreiVer
            if l[j][0] == "w":
                screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

            if l[j][0] == "p":
                screen.blit(pygame.transform.scale(path, (FB, FB)), (col_idx, row_idx))
                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))
        player()
        if int(tutstage) == 0:
            screen.blit(pygame.font.SysFont(font,50).render("Move with WASD or the arrowkeys",True,(251,72,196)),(0,0))
            screen.blit(pygame.font.SysFont(font,50).render(str(round(tutstage*10,1))+"/10",True,(251,72,196)),(0,80))
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
                tutstage += 0.001

    # searchstamp

    if whereru == "play":
        speedruntimer.resume()
        dogshowtimer.resume()
        mousepoweractivated.resume()
        asktosave = True
        yourtime = round(speedruntimer.gettime(),2)
        pygame.mouse.set_visible(mousevis)
        if not pygame.mouse.get_focused():
            whereru = "pause"
        if not mousevis:
            pygame.mouse.set_pos(pxl_width//2, pxl_height//2)





        FB = min(pxl_width // width, pxl_height // height)
        ZOOM_FB = min(pxl_width // 5, pxl_height // 5)
        if legit:
            if zoom:
                if not inhole:
                    row_idx = -1
                    col_idx = -1
                    for j in range(len(l)):
                        if (j % width) < x + 3 and (j % width) > x - 4 and (j // width) < y + 3 and (j // width) > y - 4:
                            if x < 3 and col_idx == -1:
                                col_idx += 3-int(x)
                            if width-int(x) == 2 and col_idx == 6-(width-int(x)):
                                col_idx = -1
                                row_idx += 1
                            if width-int(x) == 3 and col_idx == 5:
                                col_idx = -1
                                row_idx += 1
                            if y < 3 and row_idx == -1:
                                row_idx = 2-int(y)

                            if l[j][0] == "w":
                                screen.blit(pygame.transform.scale(wall, (ZOOM_FB, ZOOM_FB)), (col_idx*ZOOM_FB+BreiVer+(int(x)-x+0.5)*ZOOM_FB, row_idx*ZOOM_FB+HohVer+(int(y)-y+0.5)*ZOOM_FB))
                                col_idx += 1



                            if l[j][0] == "p":
                                #pygame.draw.rect(screen, (0, 0, 255), (col_idx, row_idx, FB, FB))
                                screen.blit(pygame.transform.scale(path, (ZOOM_FB, ZOOM_FB)), (col_idx*ZOOM_FB+BreiVer+(int(x)-x+0.5)*ZOOM_FB, row_idx*ZOOM_FB+HohVer+(int(y)-y+0.5)*ZOOM_FB))
                                col_idx += 1
                            if col_idx == 6:
                                col_idx = -1
                                row_idx += 1
                                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                    pygame.draw.rect(screen,color,(0,0,BreiVer,pxl_height))
                    pygame.draw.rect(screen,color,(pxl_width-BreiVer,0,BreiVer,pxl_height))
                    pygame.draw.rect(screen, color, (0, 0, pxl_width, HohVer))
                    pygame.draw.rect(screen, color, (0, pxl_height-HohVer, pxl_width, HohVer))

                    for j in range(len(l)):
                        if fish.count(j) != 0:
                            if fish.index(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (
                                    j // width) < y + 2 and (j // width) > y - 3:

                                screen.blit(pygame.transform.scale(deadf, (ZOOM_FB, ZOOM_FB)), ((2.5 + (j % width-x))*ZOOM_FB+BreiVer, (2.5 + (j // width-y))*ZOOM_FB+HohVer))
                    for j in range(len(l)):
                        if holes.count(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (
                                j // width) < y + 2 and (j // width) > y - 3:
                            screen.blit(pygame.transform.scale(holeimg, (ZOOM_FB, ZOOM_FB)), ((2.5 + (j % width-x))*ZOOM_FB+BreiVer, (2.5 + (j // width-y))*ZOOM_FB+HohVer))

                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if mice.count(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (
                                j // width) > y - 3:
                            screen.blit(pygame.transform.scale(mouseimg, (ZOOM_FB, ZOOM_FB)), ((2.5 + (j % width-x))*ZOOM_FB+BreiVer, (2.5 + (j // width-y))*ZOOM_FB+HohVer))
                    if yourtime > 10 and mousepoweractivated.gettime() > 45:
                        for i in dogs:
                            if abs(i.x - x) < 3 and abs(i.y - y) < 3:
                                i.draw()
                    if yourtime < 10 or mousepoweractivated.gettime() < 45:
                        for i in dogs:
                            if abs(i.x - x) < 3 and abs(i.y - y) < 3:
                                i.sleep_draw()


                    pygame.draw.circle(screen, (color[0], color[1], color[2]), (2.5*ZOOM_FB + BreiVer, 2.5*ZOOM_FB + HohVer), 4.5 * ZOOM_FB, int(2.5*ZOOM_FB))
                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if fish.count(j) != 0:
                            if fish.index(j) == 0:
                                if (j % width) < x + 4 and (j % width) > x - 5 and (j // width) < y + 4 and (
                                        j // width) > y - 5:
                                    screen.blit(pygame.transform.scale(glowf[fishmodel], (ZOOM_FB, ZOOM_FB)), (
                                    (2.5 + (j % width - x)) * ZOOM_FB + BreiVer,
                                    (2.5 + (j // width - y)) * ZOOM_FB + HohVer))

                    #minimap
                    pygame.draw.rect(screen,(0,0,0),(pxl_width-ZOOM_FB-10,pxl_height-ZOOM_FB-10,ZOOM_FB,ZOOM_FB),0,4,4,4,4)
                    pygame.draw.rect(screen,(255-color[0],255-color[1],255-color[2]),(pxl_width-ZOOM_FB-10,pxl_height-ZOOM_FB-10,ZOOM_FB,ZOOM_FB),3,4,4,4,4)

                    pygame.draw.circle(screen, (255,255,255),(pxl_width-ZOOM_FB-10+x/width*ZOOM_FB,pxl_height-ZOOM_FB-10+y/width*ZOOM_FB), max(ZOOM_FB/20,5))
                    for i in dogpos:
                        pygame.draw.circle(screen, (255,0,0),(pxl_width-ZOOM_FB-10+i[0]/width*ZOOM_FB,pxl_height-ZOOM_FB-10+i[1]/width*ZOOM_FB), max(ZOOM_FB/30,5))


                #inhole
                else:
                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (
                                j // width) > y - 3:
                            if l[j][0] == "w":
                                screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
                                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                            if l[j][0] == "p":
                                pygame.draw.rect(screen, (0, 0, 255), (col_idx, row_idx, FB, FB))
                                screen.blit(pygame.transform.scale(path, (FB, FB)), (col_idx, row_idx))
                                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                            if l[j] == "e":
                                pygame.draw.rect(screen, (123, 92, 19), (col_idx, row_idx, FB, FB))

                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if fish.count(j) != 0:
                            if fish.index(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (
                                    j // width) < y + 2 and (j // width) > y - 3:
                                screen.blit(pygame.transform.scale(deadf, (FB, FB)), (col_idx, row_idx))
                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if holes.count(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (
                                j // width) < y + 2 and (j // width) > y - 3:
                            screen.blit(pygame.transform.scale(holeimg, (FB, FB)), (col_idx, row_idx))

                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if mice.count(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (
                                j // width) < y + 2 and (j // width) > y - 3:
                            screen.blit(pygame.transform.scale(mouseimg, (FB, FB)), (col_idx, row_idx))
                    if yourtime > 10 and mousepoweractivated.gettime() > 45:
                        for i in dogs:
                            if abs(i.x - x) < 3 and abs(i.y - y) < 3:
                                i.draw()
                    if yourtime < 10 or mousepoweractivated.gettime() < 45:
                        for i in dogs:
                            if abs(i.x - x) < 3 and abs(i.y - y) < 3:
                                i.sleep_draw()
                    pygame.draw.circle(screen, (color[0], color[1], color[2]), (x * FB + BreiVer, y * FB + HohVer),
                                       4.25 * FB, int(2.25 * FB))

                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if fish.count(j) != 0:
                            if fish.index(j) == 0:
                                if (j % width) < x + 4 and (j % width) > x - 5 and (j // width) < y + 4 and (
                                        j // width) > y - 5:
                                    screen.blit(pygame.transform.scale(glowf[fishmodel], (FB, FB)), (col_idx, row_idx))

                    pygame.draw.circle(screen, (color[0], color[1], color[2]), (x * FB + BreiVer, y * FB + HohVer),
                                       6 * FB, int(2.25 * FB))

                    mousecontrol = False
                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if holes.count(j) != 0:
                            screen.blit(pygame.transform.scale(holeimg, (FB, FB)), (col_idx, row_idx))

                    if mouse == 1 and holes.count(
                            int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + int(
                                    (pygame.mouse.get_pos()[1] - HohVer) / FB) * width) != 0:
                        x, y = int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + 0.5, int(
                            (pygame.mouse.get_pos()[1] - HohVer) / FB) + 0.5
                        mouse = 0


            else:
                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer
                    if (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (j //width) > y - 3:
                        if l[j][0] == "w":
                            screen.blit(pygame.transform.scale(wall,(FB,FB)),(col_idx,row_idx))
                            #screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                        if l[j][0] == "p":
                            pygame.draw.rect(screen, (0,0,255), (col_idx, row_idx, FB, FB))
                            screen.blit(pygame.transform.scale(path,(FB,FB)),(col_idx,row_idx))
                            #screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))


                        if l[j] == "e":
                            pygame.draw.rect(screen, (123,92,19), (col_idx, row_idx, FB, FB))

                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer
                    if fish.count(j) != 0:
                        if fish.index(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (j //width) > y - 3:
                                screen.blit(pygame.transform.scale(deadf, (FB, FB)), (col_idx, row_idx))
                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer
                    if holes.count(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (j //width) > y - 3:
                            screen.blit(pygame.transform.scale(holeimg, (FB, FB)), (col_idx, row_idx))

                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer
                    if mice.count(j) != 0 and (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (j //width) > y - 3:
                            screen.blit(pygame.transform.scale(mouseimg, (FB, FB)), (col_idx, row_idx))
                if yourtime > 10 and mousepoweractivated.gettime() > 45:
                    for i in dogs:
                        if abs(i.x-x) < 3 and abs(i.y-y) < 3:
                            i.draw()
                if yourtime < 10 or mousepoweractivated.gettime() < 45:
                    for i in dogs:
                        if abs(i.x-x) < 3 and abs(i.y-y) < 3:
                            i.sleep_draw()




                pygame.draw.circle(screen, (color[0], color[1], color[2]), (x * FB + BreiVer, y * FB + HohVer), 4.25 * FB, int(2.25 * FB))

                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer
                    if fish.count(j) != 0:
                        if fish.index(j) == 0:
                            if (j % width) < x + 4 and (j % width) > x - 5 and (j // width) < y + 4 and (
                                    j // width) > y - 5:
                                screen.blit(pygame.transform.scale(glowf[fishmodel], (FB, FB)), (col_idx, row_idx))

                pygame.draw.circle(screen, (color[0], color[1], color[2]), (x * FB + BreiVer, y * FB + HohVer), 6 * FB, int(2.25 * FB))
                if yourtime > 10 and mousepoweractivated.gettime() > 45:
                    for i in dogpos:
                        dogs[0].draw_at(i[0],i[1],dogrichtungen[dogpos.index(i)])
                if yourtime < 10 or mousepoweractivated.gettime() < 45:
                    for i in dogpos:
                        dogs[0].sleep_draw_at(i[0], i[1], dogrichtungen[dogpos.index(i)])
                if inhole:
                    mousecontrol = False
                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if holes.count(j) != 0:
                            screen.blit(pygame.transform.scale(holeimg, (FB, FB)), (col_idx, row_idx))


                    if mouse == 1 and holes.count(int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + int(
                            (pygame.mouse.get_pos()[1] - HohVer) / FB)*width) != 0:
                        x, y = int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + 0.5, int(
                            (pygame.mouse.get_pos()[1] - HohVer) / FB) + 0.5
                        mouse = 0


        else:
            for j in range(len(l)):
                row_idx = (j // width) * FB + HohVer
                col_idx = (j % width) * FB + BreiVer
                if l[j][0] == "w":
                    screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
                    # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                if l[j][0] == "p":
                    pygame.draw.rect(screen, (0, 0, 255), (col_idx, row_idx, FB, FB))
                    screen.blit(pygame.transform.scale(path, (FB, FB)), (col_idx, row_idx))
                    # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                if l[j] == "e":
                    pygame.draw.rect(screen, (123, 92, 19), (col_idx, row_idx, FB, FB))

            for j in range(len(l)):
                row_idx = (j // width) * FB + HohVer
                col_idx = (j % width) * FB + BreiVer
                if fish.count(j) != 0:
                    if fish.index(j) == 0:
                        screen.blit(pygame.transform.scale(glowf[fishmodel], (FB, FB)), (col_idx, row_idx))
                    else:
                        screen.blit(pygame.transform.scale(deadf, (FB, FB)), (col_idx, row_idx))

            for j in range(len(l)):
                row_idx = (j // width) * FB + HohVer
                col_idx = (j % width) * FB + BreiVer
                if holes.count(j) != 0:
                        screen.blit(pygame.transform.scale(holeimg, (FB, FB)), (col_idx, row_idx))
            for j in range(len(l)):
                row_idx = (j // width) * FB + HohVer
                col_idx = (j % width) * FB + BreiVer
                if mice.count(j) != 0:
                        screen.blit(pygame.transform.scale(mouseimg, (FB, FB)), (col_idx, row_idx))


            if inhole:
                mousecontrol = False
                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer
                    if holes.count(j) != 0:
                        screen.blit(pygame.transform.scale(holeimg, (FB, FB)), (col_idx, row_idx))


                if mouse == 1 and holes.count(int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + int(
                        (pygame.mouse.get_pos()[1] - HohVer) / FB)*width) != 0:
                    x, y = int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + 0.5, int(
                        (pygame.mouse.get_pos()[1] - HohVer) / FB) + 0.5
                    mouse = 0

            if yourtime > 10 and mousepoweractivated.gettime() > 45:
                for i in dogs:
                    i.draw()
            if yourtime < 10 or mousepoweractivated.gettime() < 45:
                for i in dogs:
                    i.sleep_draw()
        player()
        if yourtime > 10:
            for i in dogs:
                i.run()
        if dogshowtimer.gettime() > 5 and whereru != "pause":
            dogpos = []
            dogrichtungen = []
            dogshowtimer.start()
            for i in dogs:
                dogpos.append([i.x,i.y])
                dogrichtungen.append(i.richtung)




        screen.blit(pygame.font.SysFont(font, 50).render(str(yourtime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))
        for i in range(hearts + 1):
            screen.blit(pygame.transform.scale(heartimg, (FB // 2, FB // 2)), (pxl_width - i * (FB // 2 + 2), 0))

    # searchstamp
    if whereru == "pause":
        pygame.mouse.set_visible(True)
        mousepoweractivated.pause()
        speedruntimer.pause()
        dogshowtimer.pause()

        if pausewru == "main":
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/5,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global whereru,lastwhereru;whereru = lastwhereru[-2]",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.8,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Go to Main","global whereru,quitaction\nif asktosave: whereru = 'quit';quitaction = "+'"'+"global whereru;whereru = 'main'"+'"\nelse: whereru = "main"',80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.4,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Settings","global pausewru;pausewru = 'settings'",80)
            button(10,pxl_height-pxl_height/1.15,pxl_width/2-15,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Help","webbrowser.open(r'https://e2z1.ml/projects/KittyLabyrinth')",80)
            button(pxl_width/2+5,pxl_height-pxl_height/1.15,pxl_width/2-15,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Tutorial","global whereru;whereru = 'tut'",80)
            #button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/2.5,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Audio","global pausewru;pausewru = 'audio'",80)
        if pausewru == "settings":
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.15,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Audio","global pausewru;pausewru = 'audio'",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.8,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Look","global pausewru;pausewru = 'textures'",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.4,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Debug","global pausewru;pausewru = 'debug'",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/5,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global whereru,lastwhereru;whereru = lastwhereru[-2]",80)

        if pausewru == "textures":
            scrolling()
            texturepackslist = [f for f in listdir("texturepacks") if not isfile(join("texturepacks", f))]
            for i in range(len(texturepackslist)):
                if texturepackslist[i] == texturepack:
                    button(105, i*(100+5) + scrollverschiebung, 500,
                           100,
                           (0,0,200), (color[0], color[1], color[2]), font,
                           texturepackslist[i],
                           "global texturepack;texturepack = '" + texturepackslist[i] + "'", 50)
                else:
                    button(105, i*(100+5)+scrollverschiebung, 500, 100,
                           (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, texturepackslist[i],
                           "global texturepack;texturepack = '"+texturepackslist[i]+"'", 50)
                screen.blit(
                    pygame.transform.scale(pygame.image.load("texturepacks/" + texturepackslist[i] + "/logo.png"), (
                    100,
                    100)),
                    (0, i*(100+5)+scrollverschiebung))

            pygame.draw.rect(screen,color,(0,pxl_height - pxl_height / 2.5-5,pxl_width,pxl_height-(pxl_height - pxl_height / 2.5-5)))
            button(10, pxl_height - pxl_height / 2.5, (pxl_width - 30) / 2, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Colors",
                   "global pausewru;pausewru = 'colors'", 80)
            changesettings("zoom", str(zoom))
            button(20 + (pxl_width - 30) / 2, pxl_height - pxl_height / 2.5, (pxl_width - 30) / 2, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Zoom: " + str(zoom), "global zoom;zoom = not zoom", 80)
            button(pxl_width / 2 - 500 / 2, pxl_height - pxl_height / 5, 500, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, "Done",
                   "global pausewru;pausewru = 'settings'", 80)
            textures()
            changesettings("texturepack","'"+texturepack+"'")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #hi
        if pausewru == "debug":
            button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 2, pxl_width - 20, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Legit: " + " " + str(legit), "global legit; legit = not legit", 80)
            button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 2.9, pxl_width - 20, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Show FPS: " + " " + str(showfps), "global showfps; showfps = not showfps", 80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.15,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Mousecontrol: "+str(mousecontrol),"global mousecontrol;mousecontrol = not mousecontrol",80)
            changesettings("mousecontrol",str(mousecontrol))
            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'settings'",80)
        if pausewru == "colors":
            m = pygame.mouse
            #ganz unten

            screen.blit(pygame.font.SysFont(font, 50).render("R: "+str(color[0]), True, (255 - color[0], 255 - color[1], 255 - color[2])),((pxl_width-pygame.font.SysFont(font, 60).render("R: "+str(color[0]), True, (255 - color[0], 255 - color[1], 255 - color[2])).get_width())//2,pxl_height-pxl_height/2.3))
            pygame.draw.rect(screen,(255 - color[0], 255 - color[1], 255 - color[2]),(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/2.9,pxl_width-20,10),0,4,4,4,4)
            pygame.draw.circle(screen,(255 - color[0], 255 - color[1], 255 - color[2]), ((color[0]/255*(pxl_width-20)+(pxl_width/2-(pxl_width-20)//2))-20,pxl_height-pxl_height/2.9+5),20)


            pygame.draw.circle(screen,(255 - color[0], 255 - color[1], 255 - color[2]), ((color[1]/255*(pxl_width-20)+(pxl_width/2-(pxl_width-20)//2))-20,pxl_height-pxl_height/1.9+5),20)
            pygame.draw.rect(screen,(255 - color[0], 255 - color[1], 255 - color[2]),(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.9,pxl_width-20,10),0,4,4,4,4)
            screen.blit(pygame.font.SysFont(font, 50).render("G: "+str(color[1]), True, (255 - color[0], 255 - color[1], 255 - color[2])),((pxl_width-pygame.font.SysFont(font, 60).render("G: "+str(color[1]), True, (255 - color[0], 255 - color[1], 255 - color[2])).get_width())//2,pxl_height-pxl_height/1.6))



            pygame.draw.rect(screen,(255 - color[0], 255 - color[1], 255 - color[2]),(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.4,pxl_width-20,10),0,4,4,4,4)
            pygame.draw.circle(screen,(255 - color[0], 255 - color[1], 255 - color[2]), ((color[2]/255*(pxl_width-20)+(pxl_width/2-(pxl_width-20)//2))-20,pxl_height-pxl_height/1.4+5),20)
            screen.blit(pygame.font.SysFont(font, 50).render("B: "+str(color[2]), True, (255 - color[0], 255 - color[1], 255 - color[2])),((pxl_width-pygame.font.SysFont(font, 60).render("B: "+str(color[2]), True, (255 - color[0], 255 - color[1], 255 - color[2])).get_width())//2,pxl_height-pxl_height/1.25))




            if not m.get_pressed()[0]:
                waspressed = False
            if m.get_pressed()[0] and onslider == 0:
                #wirdgepresst
                waspressed = True
                if pxl_height-pxl_height/2.9 < m.get_pos()[1] < pxl_height-pxl_height/2.9+10:
                    onslider = 1
                if pxl_height-pxl_height/1.9 < m.get_pos()[1] < pxl_height-pxl_height/1.9+10:
                    onslider = 2
                if pxl_height-pxl_height/1.4 < m.get_pos()[1] < pxl_height-pxl_height/1.4+10:
                    onslider = 3

            if not waspressed:
                onslider = 0

            #color 0
            if onslider == 1:
                if m.get_pos()[0] < pxl_width-26:
                    color[0] = int((m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20) * 255)
                    changesettings("color[0]",str(int((m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20) * 255)))
            if onslider == 2:
                if m.get_pos()[0] < pxl_width-26:
                    color[1] = int((m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20) * 255)
                    changesettings("color[1]",str(int((m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20) * 255)))
            if onslider == 3:
                if m.get_pos()[0] < pxl_width-26:
                    color[2] = int((m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20) * 255)
                    changesettings("color[2]",str(int((m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20) * 255)))




            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'settings'",80)

        if pausewru == "audio":
            pygame.draw.rect(screen,(255 - color[0], 255 - color[1], 255 - color[2]),(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.4,pxl_width-20,10),0,4,4,4,4)
            pygame.draw.circle(screen,(255 - color[0], 255 - color[1], 255 - color[2]), ((volume/1*(pxl_width-20)+(pxl_width/2-(pxl_width-20)//2))-20,pxl_height-pxl_height/1.4+5),20)
            screen.blit(pygame.font.SysFont(font, 50).render("Volume: "+str(int(volume*100))+"%", True, (255 - color[0], 255 - color[1], 255 - color[2])),((pxl_width-pygame.font.SysFont(font, 60).render("Volume: "+str(int(volume*100))+"%", True, (255 - color[0], 255 - color[1], 255 - color[2])).get_width())//2,pxl_height-pxl_height/1.25))

            m = pygame.mouse

            if not m.get_pressed()[0]:
                waspressed = False
            if m.get_pressed()[0]:
                #wirdgepresst
                waspressed = True
                if pxl_height-pxl_height/1.4 < m.get_pos()[1] < pxl_height-pxl_height/1.4+10 and onslider == 0:
                    onslider = 4

            if not waspressed:
                onslider = 0

            #color 0
            if onslider == 4:
                if m.get_pos()[0] < pxl_width-26:
                    volume = (m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20)
                    changesettings("volume",str((m.get_pos()[0] + pxl_width / 2 - (pxl_width - 20) // 2) / (pxl_width - 20)))

            button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 1.6, pxl_width - 20, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Sounds: " + " " + str(sounds), "global sounds; sounds = not sounds", 100)
            changesettings("sounds",str(sounds))
            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'settings'",80)

        screen.blit(pygame.font.SysFont(font, 50).render(str(yourtime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))

    if whereru == "showcase" or whereru == "showcasebcdead":
        for j in range(len(l)):
            row_idx = (j // width) * FB + HohVer
            col_idx = (j % width) * FB + BreiVer
            if l[j][0] == "w":
                screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

            if l[j][0] == "p":
                pygame.draw.rect(screen, (0, 0, 255), (col_idx, row_idx, FB, FB))
                screen.blit(pygame.transform.scale(path, (FB, FB)), (col_idx, row_idx))
                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

            if l[j] == "e":
                pygame.draw.rect(screen, (123, 92, 19), (col_idx, row_idx, FB, FB))
    if whereru == "deadscreen":
        pygame.mouse.set_visible(True)
        screen.blit(pygame.font.SysFont(font, 100).render("You died.", True,
                                                         (255 - color[0], 255 - color[1], 255 - color[2])), ((
                                                                                                                         pxl_width - pygame.font.SysFont(
                                                                                                                     font,
                                                                                                                     100).render(
                                                                                                                     "You died.",
                                                                                                                     True,
                                                                                                                     (
                                                                                                                     255 -
                                                                                                                     color[
                                                                                                                         0],
                                                                                                                     255 -
                                                                                                                     color[
                                                                                                                         1],
                                                                                                                     255 -
                                                                                                                     color[
                                                                                                                         2])).get_width()) // 2,
                                                                                                             pxl_height - pxl_height / 1.25))

        button(10,
               (pxl_height - 100) // 2, pxl_width - 20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
               "New Round",
               "reset();global whereru;whereru = 'play';speedruntimer.start();dogshowtimer.start()", 50)

        button(10,
               pxl_height // 1.25, pxl_width - 20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
               "Show Labyrinth",
               "global whereru;whereru = 'showcasebcdead'", 50)


    if whereru == "win":
        pygame.mouse.set_visible(True)
        paths = 0
        for i in l:
            if i[0] == "p":
                paths += 1

        for i in range(min(paths, 5)):
            screen.blit(pygame.transform.scale(glowf[fishmodel], ((pxl_width-20)//5, (pxl_width-20)//5)), ((pxl_width-20)//5*i, (pxl_height-100)//2-(pxl_width-20)//5))
        button(10,
               (pxl_height-100)//2, pxl_width-20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
               "New Round",
               "reset();global whereru;whereru = 'play';speedruntimer.start(),dogshowtimer.start()", 50)
        button(10,
               pxl_height // 1.25, pxl_width - 20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
               "Show Labyrinth",
               "global whereru;whereru = 'showcase'", 50)
        screen.blit(pygame.font.SysFont(font, 50).render(str(finaltime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))
    if showfps:
        screen.blit(pygame.font.SysFont(font, 50).render(str(clock.get_fps()), True,
                                                     (255 - color[0], 255 - color[1], 255 - color[2])), (
                    pxl_width - pygame.font.SysFont(font, 50).render(str(int(clock.get_fps())), True, (
                        255 - color[0], 255 - color[1], 255 - color[2])).get_width(), FB // 2 + 10))
    pygame.display.flip()
    clock.tick(max_fps)
    timebetweenpauseandplay += 1
