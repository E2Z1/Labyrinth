#by E2Z1   e2z1.ml   https://github.com/E2Z1/


import random
import pygame
import sys
from pygame.locals import *
from os import listdir
from os.path import isfile, join
import time
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import webbrowser

import maze


howmanydogs = 3
showfps = True
max_fps = 10000000000
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
        if mousepoweractivated.gettime() > 45:

            geschw = 0.01


            if int(self.x) == int(x) and int(self.y) == int(y):
                damage()
                return True


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
            if int(self.y) == int(self.path[0][1]) and int(self.x) == int(self.path[0][0]):
                self.path.pop(0)
            if self.anzahlrichtungen != 0:
                self.richtung = self.fastrichtung/self.anzahlrichtungen

    def draw(self):
        screen.blit(pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)), self.richtung * 90),
                    (self.x * FB +
                     BreiVer - (pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)),
                                                        self.richtung * 90).get_width()) // 2,
                     self.y * FB + HohVer - (
                         pygame.transform.rotate(pygame.transform.scale(dogimg, (FB, FB)), self.richtung * 90)
                         .get_height()) / 2))
    def sleep_draw(self):
        screen.blit(pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)), self.richtung * 90),
                    (self.x * FB +
                     BreiVer - (pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)),
                                                        self.richtung * 90).get_width()) // 2,
                     self.y * FB + HohVer - (
                         pygame.transform.rotate(pygame.transform.scale(sldogimg, (FB, FB)), self.richtung * 90)
                         .get_height()) / 2))


speedruntimer = timer()
mousepoweractivated = timer()

def switchboolean(b):
    global legit
    #das ist nur weil if in execute blöd ist
    if b:
        return False
    else:
        return True

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

def button(x,y,width,height,colorbox,colortext,font,text,action,size):
    writething = pygame.font.SysFont(font,size).render(text,True,colortext)
    pygame.draw.rect(screen,colorbox,(x,y,width,height),0,4,4,4,4)
    screen.blit(writething,(x+(width - writething.get_width())//2,y+(height - writething.get_height())//2))
    if x+width > pygame.mouse.get_pos()[0] > x and y+height > pygame.mouse.get_pos()[1] > y and mouse == 1:
        exec(action)
startx = 0
starty = 0
def reset():
    global l,x,y,hearts,fish,feld,fat,geschw,startx,starty,holes,mice,dogs,whereru,howmanydogs
    fat = 0
    l = generate(width, height)
    geschw = 0.03
    mousepoweractivated.startpoint = 0

    while True:
        startx = random.randint(0,width-1) + 0.5
        starty = random.randint(0,height-1) + 0.5
        x, y = startx, starty
        if l[int(x)+int(y)*height][0] == "p":
            break



    fish = []
    hearts = 7
    speedruntimer.start()
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
    #print('richtung: ', richtung)

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










    # lab[28] = "p"
    # print(lab)

    #row = 0
    #for i in range(int(len(lab) / width)):
    #    print(lab[row:row+width])
    #    row += width

    return maze.maze(width)


yourtime = 0
lastposkitty = (0,0)
def player():
    global richtung,y,x,hearts,l,whereru,fat,geschw,inhole,mousevis,mice,lastposkitty,dogs,finaltime
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
    if (key[pygame.K_s] or key[pygame.K_DOWN]) and y < height:
        fastrichtung += 2
        anzahlrichtungen += 1
        y += geschw*60/(clock.get_fps()+0.00000001)
    if (key[pygame.K_d] or key[pygame.K_RIGHT]) and x < width:
        fastrichtung += 3
        anzahlrichtungen += 1
        x += geschw*60/(clock.get_fps()+0.00000001)
    if anzahlrichtungen != 0:
        richtung = fastrichtung/anzahlrichtungen

    if mousecontrol and pygame.mouse.get_pressed()[0]:
        x,y = (pygame.mouse.get_pos()[0]-BreiVer)/FB,(pygame.mouse.get_pos()[1]-HohVer)/FB
        mousevis = True
    if not mousecontrol and not inhole:
        mousevis = False
    else:
        mousevis = True
    if legit and zoom:
        if mousepoweractivated.gettime() < 45:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty, (
            (ZOOM_FB + fat * 3) * (mousepoweractivated.gettime() / 45), ZOOM_FB * (mousepoweractivated.gettime() / 45))),
                                                richtung * 90), (width/2 * ZOOM_FB + BreiVer - (pygame.transform.rotate(
                pygame.transform.scale(kitty, (
                (ZOOM_FB + fat * 3) * (mousepoweractivated.gettime() / 45), ZOOM_FB * (mousepoweractivated.gettime() / 45))),
                richtung * 90).get_width()) // 2, height/2 * ZOOM_FB + HohVer - (pygame.transform.rotate(
                pygame.transform.scale(kitty, (
                (ZOOM_FB + fat * 3) * (mousepoweractivated.gettime() / 45), ZOOM_FB * (mousepoweractivated.gettime() / 45))),
                richtung * 90).get_height()) / 2))
        else:
            screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty, (
                ZOOM_FB + fat * 3,
                ZOOM_FB)), richtung * 90), (width / 2 * ZOOM_FB + BreiVer - (
                pygame.transform.rotate(pygame.transform.scale(kitty, (ZOOM_FB + fat * 3, ZOOM_FB)),
                                        richtung * 90).get_width()) // 2,
                                       height / 2 * ZOOM_FB + HohVer - (
                                           pygame.transform.rotate(
                                               pygame.transform.scale(kitty, (
                                                   ZOOM_FB + fat * 3, ZOOM_FB)),
                                               richtung * 90).get_height()) / 2))
            pygame.draw.circle(screen,(255,255,255),(width/2*FB+BreiVer,height/2*FB+HohVer),15)
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

tick = 0
fishmodel = 0


reset()
mousevis = mousecontrol
inhole = False
while True:
    #print(str(int(clock.get_fps())))
    global x,y

    mouse = 0
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


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
            if event.key == pygame.K_ESCAPE and whereru == "play" and timebetweenpauseandplay > 10:
                whereru = "pause"
                timebetweenpauseandplay = 0
                pausewru = "main"
            if event.key == pygame.K_ESCAPE and whereru == "pause" and timebetweenpauseandplay > 10:
                whereru = "play"
                timebetweenpauseandplay = 0
            if whereru == "showcase":
                whereru = "win"
            if whereru == "showcasebcdead":
                whereru = "deadscreen"


            if event.key == pygame.K_LCTRL:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.button

    if whereru == "play":
        yourtime = round(speedruntimer.gettime(),2)
        pygame.mouse.set_visible(mousevis)
        if not mousevis:
            pygame.mouse.set_pos(pxl_width//2, pxl_height//2)






        FB = min(pxl_width // width, pxl_height // height)
        ZOOM_FB = min(pxl_width // 5, pxl_height // 5)
        if legit:
            if zoom:
                row_idx = 0
                col_idx = 0
                for j in range(len(l)):
                    if (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (j // width) > y - 3:
                        if l[j][0] == "w":
                            screen.blit(pygame.transform.scale(wall, (ZOOM_FB, ZOOM_FB)), (col_idx*ZOOM_FB+BreiVer, row_idx*ZOOM_FB+HohVer))
                            col_idx += 1
                            if col_idx % 5 == 0:
                                col_idx = 0
                                row_idx += 1

                        if l[j][0] == "p":
                            #pygame.draw.rect(screen, (0, 0, 255), (col_idx, row_idx, FB, FB))
                            screen.blit(pygame.transform.scale(path, (ZOOM_FB, ZOOM_FB)), (col_idx*ZOOM_FB+BreiVer, row_idx*ZOOM_FB+HohVer))
                            col_idx += 1
                            if col_idx % 5 == 0:
                                col_idx = 0
                                row_idx += 1
                            # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                        if l[j] == "e":
                            pygame.draw.rect(screen, (123, 92, 19), (col_idx*ZOOM_FB+BreiVer, row_idx*ZOOM_FB+HohVer, ZOOM_FB, ZOOM_FB))
                            col_idx += 1
                            if col_idx % 5 == 0:
                                col_idx = 0
                                row_idx += 1








            else:
                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer
                    if (j % width) < x + 2 and (j % width) > x - 3 and (j // width) < y + 2 and (j //width) > y - 3:
                        if l[j][0] == "w":
                            screen.blit(pygame.transform.scale(wall,(FB,FB)),(col_idx,row_idx))
                            #screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                            #print(col_idx, row_idx)
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
                if yourtime > 10:
                    for i in dogs:
                        if abs(i.x-x) < 3 and abs(i.y-y) < 3:
                            i.draw()
                if yourtime < 10:
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

                if inhole:
                    mousecontrol = False
                    for j in range(len(l)):
                        row_idx = (j // width) * FB + HohVer
                        col_idx = (j % width) * FB + BreiVer
                        if holes.count(j) != 0:
                            screen.blit(pygame.transform.scale(holeimg, (FB, FB)), (col_idx, row_idx))

                    mousevis = True
                    if pygame.mouse.get_pressed()[0] and holes.count(int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + int(
                            (pygame.mouse.get_pos()[1] - HohVer) / FB)*width) != 0:
                        x, y = int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + 0.5, int(
                            (pygame.mouse.get_pos()[1] - HohVer) / FB) + 0.5


        else:
            for j in range(len(l)):
                row_idx = (j // width) * FB + HohVer
                col_idx = (j % width) * FB + BreiVer
                if l[j][0] == "w":
                    screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
                    # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                    # print(col_idx, row_idx)
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

                mousevis = True
                if pygame.mouse.get_pressed()[0] and holes.count(int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + int(
                        (pygame.mouse.get_pos()[1] - HohVer) / FB)*width) != 0:
                    x, y = int((pygame.mouse.get_pos()[0] - BreiVer) / FB) + 0.5, int(
                        (pygame.mouse.get_pos()[1] - HohVer) / FB) + 0.5
            if yourtime > 10:
                for i in dogs:
                    i.draw()
            if yourtime < 10:
                for i in dogs:
                    i.sleep_draw()
        player()
        if yourtime > 10:
            for i in dogs:
                i.run()



        screen.blit(pygame.font.SysFont(font, 50).render(str(yourtime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))
        for i in range(hearts + 1):
            screen.blit(pygame.transform.scale(heartimg, (FB // 2, FB // 2)), (pxl_width - i * (FB // 2 + 2), 0))
        speedruntimer.resume()
        mousepoweractivated.resume()

    if whereru == "pause":
        pygame.mouse.set_visible(True)
        mousepoweractivated.pause()
        speedruntimer.pause()

        if pausewru == "main":
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/5,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global whereru;whereru = 'play'",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.8,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Look","global pausewru;pausewru = 'textures'",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.4,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Debug","global pausewru;pausewru = 'debug'",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.15,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Help","webbrowser.open(r'https://e2z1.ml/projects/KittyLabyrinth')",80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/2.5,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Audio","global pausewru;pausewru = 'audio'",80)
        if pausewru == "textures":
            button(10,pxl_height-pxl_height/2.5,(pxl_width-30)/2,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Colors","global pausewru;pausewru = 'colors'",80)
            changesettings("zoom",str(zoom))
            button(20+(pxl_width-30)/2,pxl_height-pxl_height/2.5,(pxl_width-30)/2,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Zoom: "+str(zoom),"global zoom;zoom = switchboolean(zoom)",80)
            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'main'",80)
            texturepackslist = [f for f in listdir("texturepacks") if not isfile(join("texturepacks", f))]
            for i in range(len(texturepackslist)):
                if texturepackslist[i] == texturepack:
                    button(pxl_height/2 / len(texturepackslist) + 10, i * (
                        pxl_height/2 / len(texturepackslist)) + i * 10, 500,
                           pxl_height/2 / len(texturepackslist),
                           (0,0,200), (color[0], color[1], color[2]), font,
                           texturepackslist[i],
                           "global texturepack;texturepack = '" + texturepackslist[i] + "'", 50)
                else:
                    button(pxl_height/2 / len(texturepackslist)+10, i*(pxl_height/2 / len(texturepackslist))+i*10, 500, pxl_height/2 / len(texturepackslist),
                           (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, texturepackslist[i],
                           "global texturepack;texturepack = '"+texturepackslist[i]+"'", 50)
                screen.blit(
                    pygame.transform.scale(pygame.image.load("texturepacks/" + texturepackslist[i] + "/logo.png"), (
                    pxl_height/2 / len(texturepackslist),
                    pxl_height/2 / len(texturepackslist))),
                    (0, i * (pxl_height/2 / len(texturepackslist)) + i * 10))

            textures()
            changesettings("texturepack","'"+texturepack+"'")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #hi
        if pausewru == "debug":
            button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 2, pxl_width - 20, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Legit: " + " " + str(legit), "global legit; legit = switchboolean(legit)", 80)
            button(pxl_width / 2 - (pxl_width - 20) // 2, pxl_height - pxl_height / 2.9, pxl_width - 20, 100,
                   (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
                   "Show FPS: " + " " + str(showfps), "global showfps; showfps = switchboolean(showfps)", 80)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.15,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Mousecontrol: "+str(mousecontrol),"global mousecontrol;mousecontrol = switchboolean(mousecontrol)",80)
            changesettings("mousecontrol",str(mousecontrol))
            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'main'",80)
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




            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'main'",80)

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
                   "Sounds: " + " " + str(sounds), "global sounds; sounds = switchboolean(sounds)", 100)
            changesettings("sounds",str(sounds))
            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'main'",80)

        screen.blit(pygame.font.SysFont(font, 50).render(str(yourtime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))

    if whereru == "showcase" or whereru == "showcasebcdead":
        for j in range(len(l)):
            row_idx = (j // width) * FB + HohVer
            col_idx = (j % width) * FB + BreiVer
            if l[j][0] == "w":
                screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
                # screen.blit(pygame.font.SysFont(font,FB).render(l[j][1],True,(0,0,0)),(col_idx,row_idx))

                # print(col_idx, row_idx)
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
               "reset();global whereru;whereru = 'play';speedruntimer.start()", 50)

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
               "reset();global whereru;whereru = 'play';speedruntimer.start()", 50)
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