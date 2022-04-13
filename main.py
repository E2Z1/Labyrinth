# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import pygame
import sys
from pygame.locals import *
from os import listdir
from os.path import isfile, join
import time

width = 15
height = 15
pxl_width = 1000
pxl_height = 1000
settings = open("settings.txt","r")
color = [0,0,0]
font = ""
texturepack = "default"
texturepackslist = [f for f in listdir("texturepacks") if not isfile(join("texturepacks", f))]

exec(settings.read())
settings.close()

pygame.init()
FB = min(pxl_width // width, pxl_height // height)
screen = pygame.display.set_mode((pxl_width,pxl_height), RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Labyrinth")
legit = False


class timer:
    def __init__(self):
        self.startpoint = time.time()
        self.ispause = False
        self.startofpause = time.time()
    def start(self):
        self.startpoint = time.time()
    def gettime(self):
        return time.time()-self.startpoint
    def pause(self):
        if not self.ispause:
            self.startofpause = time.time()
            self.ispause = True
    def resume(self):
        if self.ispause:
            self.startpoint += time.time()-self.startofpause
            self.ispause = False


speedruntimer = timer()

def switchlegit():
    global legit
    #das ist nur weil if in execute blöd ist
    if legit:
        legit = False
    else:
        legit = True

def textures():
    global kitty,wall,heartimg,path,glowf,deadf
    try:
        kitty = pygame.image.load("texturepacks/"+texturepack+"/kitty.png")
    except:
        kitty = pygame.image.load("texturepacks/default/kitty.png")
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
x = (width / 2 - 0.5) * pxl_width / width + FB // 2
y = (height / 2 - 1.5) * pxl_height / height + FB + FB // 2
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


def button(x,y,width,height,colorbox,colortext,font,text,action,size):
    writething = pygame.font.SysFont(font,size).render(text,True,colortext)
    pygame.draw.rect(screen,colorbox,(x,y,width,height))
    screen.blit(writething,(x+(width - writething.get_width())//2,y+(height - writething.get_height())//2))
    if x+width > pygame.mouse.get_pos()[0] > x and y+height > pygame.mouse.get_pos()[1] > y and mouse == 1:
        exec(action)

def reset():
    global l,x,y,hearts,fish,feld,relgeschwindigkeit,fat
    relgeschwindigkeit = 0.000025
    fat = 0
    l = generate(width, height)
    x = (width / 2 - 0.5) * pxl_width / width + FB // 2
    fish = []
    for i in range(min(l.count("p"), 5)):
        go = True
        while go:
            feld = random.randint(0, width * height-1)
            if l[feld] == "p" and fish.count(feld) == 0:
                fish.append(feld)
                go = False
    y = (height / 2 - 1.5) * pxl_height / height + FB + FB // 2
    hearts = 7
    speedruntimer.start()
    for j in range(len(l)):
        row_idx = (j // width) * FB + HohVer
        col_idx = (j % width) * FB + BreiVer

        if l[j] == "w":
            screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
            # print(col_idx, row_idx)
        if l[j] == "p":
            pygame.draw.rect(screen, (0, 0, 255), (col_idx, row_idx, FB, FB))
            screen.blit(pygame.transform.scale(path, (FB, FB)), (col_idx, row_idx))

        if l[j] == "e":
            pygame.draw.rect(screen, (123, 92, 19), (col_idx, row_idx, FB, FB))

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
    # e: empty, w: wall, p: path
    lab = ['e'] * width * hight

    start = len(lab) // 2 + (width // 2 * (len(lab) % 2 == 0))
    lab[start] = 'p'


    cur = start
    path_fields = []
    richtung = neue_richtung()

    for _ in range(500):

        # pfade bauen
        if doeselementinlistexist(lab,cur+1) and richtung == 'o' and lab[cur+1] == 'e':
            lab[cur+1] = 'p'
            path_fields.append(cur+1)
            if doeselementinlistexist(lab,cur-1) and cur-1 >=0 and lab[cur-1] == 'e':
                lab[cur-1] = 'w'
            if doeselementinlistexist(lab,cur-width-1) and cur -width -1 >=0 and lab[cur -width -1] == 'e':
                lab[cur -width -1] = 'w'
            if doeselementinlistexist(lab,cur+width-1) and cur +width -1 >=0 and lab[cur +width -1] == 'e':
                lab[cur +width -1] = 'w'

        elif doeselementinlistexist(lab,cur-width) and richtung == 's' and lab[cur -width] == 'e':
            lab[cur -width] = 'p'
            path_fields.append(cur -width)
            if doeselementinlistexist(lab,cur+width-1) and cur +width -1 >=0 and lab[cur +width -1] == 'e':
                lab[cur +width -1] = 'w'
            if doeselementinlistexist(lab,cur+width) and cur +width >=0 and lab[cur +width] == 'e':
                lab[cur +width] = 'w'
            if doeselementinlistexist(lab,cur+width+1) and cur +width +1 >=0 and lab[cur +width +1] == 'e':
                lab[cur +width +1] = 'w'

        elif doeselementinlistexist(lab,cur-1) and richtung == 'w' and lab[cur -1] == 'e':
            lab[cur -1] = 'p'
            path_fields.append(cur -1)
            if doeselementinlistexist(lab,cur+1) and cur+1 < len(lab) and lab[cur+1] == 'e':
                lab[cur+1] = 'w'
            if doeselementinlistexist(lab,cur-width+1) and cur -width +1 >=0 and lab[cur -width +1] == 'e':
                lab[cur -width +1] = 'w'
            if doeselementinlistexist(lab,cur+width+1) and cur +width +1 >=0 and lab[cur +width +1] == 'e':
                lab[cur +width +1] = 'w'

        elif doeselementinlistexist(lab,cur+width) and richtung == 'n' and lab[cur +width] == 'e':
            lab[cur +width] = 'p'
            path_fields.append(cur +width)
            if cur -width -1 >=0 and lab[cur -width -1] == 'e':
                lab[cur -width -1] = 'w'
            if cur -width >=0 and lab[cur -width] == 'e':
                lab[cur -width] = 'w'
            if cur -width +1 >=0 and lab[cur -width +1] == 'e':
                lab[cur -width +1] = 'w'

    # wo kein path und keine wall, wall bauen
        '''if cur-1 >=0 and lab[cur-1] == 'e':
            lab[cur-1] = 'w'
        if cur+1 < len(lab) and lab[cur+1] == 'e':
            lab[cur+1] = 'w'
        if cur -width -1 >=0 and lab[cur -width -1] == 'e':
            lab[cur -width -1] = 'w'
        if cur -width >=0 and lab[cur -width] == 'e':
            lab[cur -width] = 'w'
        if cur -width +1 >=0 and lab[cur -width +1] == 'e':
            lab[cur -width +1] = 'w'

        if cur +width -1 >=0 and lab[cur +width -1] == 'e':
            lab[cur +width -1] = 'w'
        if cur +width >=0 and lab[cur +width] == 'e':
            lab[cur +width] = 'w'
        if cur +width +1 >=0 and lab[cur +width +1] == 'e':
            lab[cur +width +1] = 'w'
        '''
        richtung = neue_richtung()
        if path_fields:
            cur = path_fields[0]
            path_fields.pop(0)










    # lab[28] = "p"
    # print(lab)

    row = 0
    #for i in range(int(len(lab) / width)):
     #   print(lab[row:row+width])
      #  row += width

    return lab


yourtime = 0
def player():
    global richtung,y,x,hearts,l,whereru,relgeschwindigkeit,fat
    xgeschw = (pxl_width-2*BreiVer)*relgeschwindigkeit
    ygeschw = (pxl_height-2*HohVer)*relgeschwindigkeit
    fastrichtung = 0
    anzahlrichtungen = 0
    key = pygame.key.get_pressed()
    screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty,(FB+fat*3,FB)),richtung*90),(x-(FB+fat*3)//2,y-FB//2))
    #zu nach vorne gehen        and not l[int(((y-HohVer)//height-1)*width+(x+BreiVer)//width)] == "w"
    if key[pygame.K_w] and y-HohVer > 0:
        fastrichtung += 0
        anzahlrichtungen += 1
        y -= ygeschw
        # and not l[int((y-HohVer)//FB*width+(x-BreiVer)//FB)-width-1] == "w"
    if key[pygame.K_a] and x-BreiVer > 0:
        fastrichtung += 1
        anzahlrichtungen += 1
        x -= xgeschw
        # and not l[int((y-HohVer)//FB*width+(x-BreiVer)//FB)-width] == "w"
    if key[pygame.K_s] and y+FB//2+HohVer < pxl_height:
        fastrichtung += 2
        anzahlrichtungen += 1
        y += ygeschw
        # and not l[int((y - HohVer) // FB * width + (x - BreiVer) // FB) - width + 1] == "w"
    if key[pygame.K_d] and x+FB//2+BreiVer < pxl_width:
        fastrichtung += 3
        anzahlrichtungen += 1
        x += xgeschw
    if anzahlrichtungen != 0:
        richtung = fastrichtung/anzahlrichtungen

    if l[int((y - HohVer) // FB * width + (x - BreiVer) // FB)] == "w":
        hearts -= 1
        x = (width / 2 - 0.5) * pxl_width / width + FB // 2
        y = (height / 2 - 1.5) * pxl_height / height + FB + FB // 2
    if hearts < 1:
        reset()
    if doeselementinlistexist(fish,0):
        if fish[0] == int((y - HohVer) // FB * width + (x - BreiVer) // FB):
            fish.pop(0)
            relgeschwindigkeit -= 0.000002
            fat += 3
            if hearts < 9:
                hearts += 1
    else:
        if len(fish) == 0:
            whereru = "win"
    pygame.draw.circle(screen,(255,255,255),(x,y),5)





l = generate(width, height)
speedruntimer.start()
fish = []
for i in range(min(l.count("p"),5)):

    go = True
    while go:
        feld = random.randint(0,width*height-1)
        if l[feld] == "p" and fish.count(feld) == 0:
            fish.append(feld)
            go = False


blabla = 0

pausewru = "main"

tick = 0
fishmodel = 0

reset()



while True:
    print(str(int(clock.get_fps())))
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
    if tick%20 == 0:
        if fishmodel == 0:
            fishmodel = 1
            fishmodel = 1
        else:
            fishmodel = 0
    #relx = pxl_width / x
    #rely = pxl_height / y
    screen.fill((color[0], color[1], color[2]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
            if event.key == pygame.K_ESCAPE and whereru == "play" and blabla > 10:
                whereru = "pause"
                blabla = 0
                pausewru = "main"
            if event.key == pygame.K_ESCAPE and whereru == "pause" and blabla > 10:
                whereru = "play"
                blabla = 0
                for j in range(len(l)):
                    row_idx = (j // width) * FB + HohVer
                    col_idx = (j % width) * FB + BreiVer

                    if l[j] == "w":
                        screen.blit(pygame.transform.scale(wall, (FB, FB)), (col_idx, row_idx))
                        # print(col_idx, row_idx)
                    if l[j] == "p":
                        pygame.draw.rect(screen, (0, 0, 255), (col_idx, row_idx, FB, FB))
                        screen.blit(pygame.transform.scale(path, (FB, FB)), (col_idx, row_idx))

                    if l[j] == "e":
                        pygame.draw.rect(screen, (123, 92, 19), (col_idx, row_idx, FB, FB))
            if event.key == pygame.K_LCTRL:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.button

    if whereru == "play":
        yourtime = speedruntimer.gettime()

        FB = min(pxl_width // width, pxl_height // height)

        for j in range(len(l)):
            row_idx = (j // width) * FB + HohVer
            col_idx = (j % width) * FB + BreiVer

            if l[j] == "w":
                screen.blit(pygame.transform.scale(wall,(FB,FB)),(col_idx,row_idx))
                #print(col_idx, row_idx)
            if l[j] == "p":
                pygame.draw.rect(screen, (0,0,255), (col_idx, row_idx, FB, FB))
                screen.blit(pygame.transform.scale(path,(FB,FB)),(col_idx,row_idx))

            if l[j] == "e":
                pygame.draw.rect(screen, (123,92,19), (col_idx, row_idx, FB, FB))
        for j in range(len(l)):
            row_idx = (j // width) * FB + HohVer
            col_idx = (j % width) * FB + BreiVer
            if fish.count(j) != 0:
                if fish.index(j) == 0:
                    screen.blit(pygame.transform.scale(glowf[fishmodel],(FB,FB)),(col_idx,row_idx))
                else:
                    screen.blit(pygame.transform.scale(deadf, (FB, FB)), (col_idx, row_idx))
            player()
        if legit:
            pygame.draw.circle(screen,(color[0],color[1],color[2]),(x,y),200,100)
        for j in range(len(l)):
            row_idx = (j // width) * FB + HohVer
            col_idx = (j % width) * FB + BreiVer
            if fish.count(j) != 0:
                if fish.index(j) == 0:
                    screen.blit(pygame.transform.scale(glowf[fishmodel],(FB,FB)),(col_idx,row_idx))
        if legit:
            pygame.draw.circle(screen,(0,0,0),(x,y),1000,800)
        screen.blit(pygame.font.SysFont(font, 50).render(str(yourtime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))
        for i in range(hearts + 1):
            screen.blit(pygame.transform.scale(heartimg, (FB // 2, FB // 2)), (pxl_width - i * (FB // 2 + 2), 2))
        speedruntimer.resume()

    if whereru == "pause":
        speedruntimer.pause()
        if pausewru == "main":
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/5,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global whereru;whereru = 'play'",100)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/2,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Textures","global pausewru;pausewru = 'textures'",100)
            button(pxl_width/2-(pxl_width-20)//2,pxl_height-pxl_height/1.5,pxl_width-20,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Legit: "+" "+str(legit),"switchlegit()",100)
        if pausewru == "textures":
            button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global pausewru;pausewru = 'main'",100)
            texturepackslist = [f for f in listdir("texturepacks") if not isfile(join("texturepacks", f))]
            for i in range(len(texturepackslist)):
                if texturepackslist[i] == texturepack:
                    button(min(pxl_height / len(texturepackslist) - pxl_height / 5 - 10, pxl_width - 500) + 10, i * (
                        min(pxl_height / len(texturepackslist) - pxl_height / 5 - 10, pxl_width - 500)) + i * 10, 500,
                           100,
                           (0,0,200), (color[0], color[1], color[2]), font,
                           texturepackslist[i],
                           "global texturepack;texturepack = '" + texturepackslist[i] + "'", 50)
                else:
                    button(min(pxl_height/len(texturepackslist)-pxl_height/5-10,pxl_width-500)+10, i*(min(pxl_height/len(texturepackslist)-pxl_height/5-10,pxl_width-500))+i*10, 500, 100,
                           (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font, texturepackslist[i],
                           "global texturepack;texturepack = '"+texturepackslist[i]+"'", 50)
                screen.blit(
                    pygame.transform.scale(pygame.image.load("texturepacks/" + texturepackslist[i] + "/logo.png"), (
                    min(pxl_height / len(texturepackslist) - pxl_height / 5 - 10, pxl_width - 500),
                    min(pxl_height / len(texturepackslist) - pxl_height / 5 - 10, pxl_width - 500))),
                    (0, i * (min(pxl_height / len(texturepackslist) - pxl_height / 5 - 10, pxl_width - 500)) + i * 10))

            textures()
            file = open("settings.txt", "r")
            settingstext = file.read()
            for i in range(5):
                altestexturepack = file.readline()
            file.close()
            if texturepack != altestexturepack[14:]:
                file = open("settings.txt", "w")
                file.write(settingstext[:78]+'"'+texturepack+'"')
                file.close()
        screen.blit(pygame.font.SysFont(font, 50).render(str(yourtime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))


        #x = relx * pxl_width
        #y = rely * pxl_height

    if whereru == "win":
        button(10,
               (pxl_height-100)//2, pxl_width-20, 100,
               (255 - color[0], 255 - color[1], 255 - color[2]), (color[0], color[1], color[2]), font,
               "New Round",
               "reset();global whereru;whereru = 'play';speedruntimer.start()", 50)
        screen.blit(pygame.font.SysFont(font, 50).render(str(yourtime), True, (255-color[0],255-color[1],255-color[2])), (0, 0))


    pygame.display.flip()
    clock.tick(60)
    blabla += 1
    relx = pxl_width / x
    rely = pxl_height / y
