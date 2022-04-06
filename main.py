# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import pygame
import sys
from pygame.locals import *

width = 15
height = 15
pxl_width = 1000
pxl_height = 1000
settings = open("settings.txt","r")
color = [0,0,0]
font = ""

for i in range(sum(1 for line in open('settings.txt'))):
    exec(settings.readline())

pygame.init()
screen = pygame.display.set_mode((pxl_width,pxl_height), RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Labyrinth")
kitty = pygame.image.load("texturepacks/default/kitty.png")
x = (width/2-0.5) * pxl_width/width
y = (height/2-1.5) * pxl_height/height
richtung = 0
#richtung = 0,1,2,3

whereru = "play"


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
    for i in range(int(len(lab) / width)):
        print(lab[row:row+width])
        row += width

    return lab

relgeschwindigkeit = 0.000015

def player():
    global richtung,y,x
    xgeschw = (pxl_width-2*BreiVer)*relgeschwindigkeit
    ygeschw = (pxl_height-2*HohVer)*relgeschwindigkeit
    fastrichtung = 0
    anzahlrichtungen = 0
    key = pygame.key.get_pressed()
    screen.blit(pygame.transform.rotate(pygame.transform.scale(kitty,(FB,FB)),richtung*90),(x,y))
    #zu nach vorne gehen        and not l[int(((y-HohVer)//height-1)*width+(x+BreiVer)//width)] == "w"
    if key[pygame.K_w] and y-HohVer > 0 and not l[int((y-HohVer)//FB*width+(x-BreiVer)//FB)] == "w":
        fastrichtung += 0
        anzahlrichtungen += 1
        y -= ygeschw
        # and not l[int((y-HohVer)//FB*width+(x-BreiVer)//FB)-width-1] == "w"
    if key[pygame.K_a] and x-BreiVer > 0 and not l[int((y-HohVer)//FB*width+(x-BreiVer)//FB)-width-1] == "w":
        fastrichtung += 1
        anzahlrichtungen += 1
        x -= xgeschw
        # and not l[int((y-HohVer)//FB*width+(x-BreiVer)//FB)-width] == "w"
    if key[pygame.K_s] and y+FB+HohVer < pxl_height and not l[int((y-HohVer)//FB*width+(x-BreiVer)//FB)-width] == "w":
        fastrichtung += 2
        anzahlrichtungen += 1
        y += ygeschw
        # and not l[int((y - HohVer) // FB * width + (x - BreiVer) // FB) - width + 1] == "w"
    if key[pygame.K_d] and x+FB+BreiVer < pxl_width and not l[int((y - HohVer) // FB * width + (x - BreiVer) // FB) - width + 1] == "w":
        fastrichtung += 3
        anzahlrichtungen += 1
        x += xgeschw
    if anzahlrichtungen != 0:
        richtung = fastrichtung/anzahlrichtungen



l = generate(width, height)





blabla = 0




while True:
    mouse = 0
    #relx = pxl_width / x
    #rely = pxl_height / y
    screen.fill((color[0], color[1], color[2]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                l = generate(width, height)
                x = (width / 2 - 0.5) * pxl_width / width
                y = (height / 2 - 0.5) * pxl_height / height
            if event.key == pygame.K_ESCAPE and whereru == "play" and blabla > 10:
                whereru = "pause"
                blabla = 0
            if event.key == pygame.K_ESCAPE and whereru == "pause" and blabla > 10:
                whereru = "play"
                blabla = 0
            if event.key == pygame.K_LCTRL:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.button

    if whereru == "play":




        FB = min(pxl_width // width, pxl_height // height)

        for j in range(len(l)):
            row_idx = (j // width) * FB + HohVer
            col_idx = (j % width) * FB + BreiVer

            if l[j] == "w":
                pygame.draw.rect(screen, (0,0,0), (col_idx, row_idx, FB, FB))
                #print(col_idx, row_idx)
            if l[j] == "p":
                pygame.draw.rect(screen, (0,0,255), (col_idx, row_idx, FB, FB))
            if l[j] == "e":
                pygame.draw.rect(screen, (123,92,19), (col_idx, row_idx, FB, FB))

            player()


    if whereru == "pause":
        button(pxl_width/2-500/2,pxl_height-pxl_height/5,500,100,(255-color[0],255-color[1],255-color[2]),(color[0],color[1],color[2]),font,"Done","global whereru;whereru = 'play')",100)

    pxl_width, pxl_height = pygame.display.get_surface().get_size()


    if old_width != pxl_width or old_height != pxl_height:
        BreiVer, HohVer = 0, 0

        if pxl_width > pxl_height:

            BreiVer = (max(pxl_width, pxl_height) - min(pxl_width, pxl_height)) / 2
        else:

            HohVer = (max(pxl_width, pxl_height) - min(pxl_width, pxl_height)) / 2
        old_width, old_height = pxl_width, pxl_height
        #x = relx * pxl_width
        #y = rely * pxl_height

    pygame.display.flip()
    clock.tick(60)
    blabla += 1
    relx = pxl_width / x
    rely = pxl_height / y
