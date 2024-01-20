# modules
import pygame as pg
import random as rd
import os
pg.init()
img=pg.image.load(r"C:\Users\DELL\Desktop\courses\projects\batrun_bg.jpg")
img=pg.transform.scale(img,[480,720])
charimg=pg.image.load(r"C:\Users\DELL\Desktop\courses\projects\bat.jpg")
bat=pg.transform.scale(charimg,[40,40])
# window
hit=720
wit=480
gwin=pg.display.set_mode((wit,hit))
pg.display.set_caption("Batrun")
pg.display.update()
fspd=pg.time.Clock()
# storage
if not os.path.exists("batrun_hs.txt"):
    f=open("batrun_hs.txt","w")
    hs=f.write("0")
else:
    f=open("batrun_hs.txt","r")
    hs=f.read()

# text data
fnt=pg.sysfont.SysFont("",40,True,True)
def txt_scrn(stxt,clr,bgclr,x,y):
    txt=fnt.render(stxt,True,clr,bgclr)
    gwin.blit(txt,[x,y])

# game specified var
gext=False
govr=False
bx=220
by=640
bs=40
dir=""
fps=30
# obstacles
r=0
oy1=0
oy2=0
oy3=0
oy4=0
ot=5
ox1=rd.randint(0,360)
ox2=rd.randint(0,360)
ox3=rd.randint(0,360)
ox4=rd.randint(0,360)
ow=180
# score
scr=0
nhs=False
# wdv
home=True
start=False
ext=False
hisc=False
abt=False
men=0
clrs="white"
clrh="white"
clra="white"
clre="white"
# application loop
while gext==False:
    # welcome display loop
    while start==False and ext==False and hisc==False and abt==False and gext==False and home==True:
        gwin.blit(img,[0,0])
        txt_scrn("   START  ","black",clrs,160,120)
        txt_scrn("HIGH SCORE","black",clrh,160,240)
        txt_scrn("   ABOUT  ","black",clra,160,360)
        txt_scrn("   EXIT   ","black",clre,160,480)
        for i in pg.event.get():
            if i.type==pg.QUIT:
                gext=True
            if i.type==pg.KEYDOWN:
                if i.key==pg.K_DOWN:
                    if men==3:
                        men=0
                    else:
                        men+=1
                if i.key==pg.K_UP:
                    if men==0:
                        men=3
                    else:
                        men-=1
                if men==0 and i.key==pg.K_RETURN:        
                    start=True
                    home=False
                if men==1 and i.key==pg.K_RETURN:
                    hisc=True
                    home=False
                if men==2 and i.key==pg.K_RETURN:
                    abt=True
                    home=False
                if men==3 and i.key==pg.K_RETURN:
                    gext=True
                    home=False   

            if men==0:
                clrh="white"
                clrs="grey"
                clre="white"
            if men==1:
                clra="white"
                clrh="grey"
                clrs="white"
            if men==2:
                clre="white"
                clra="grey"
                clrh="white"
            if men==3:
                clre="grey"
                clra="white" 
                clrs="white"

        pg.display.update()

    # highscore 
    while home==False and gext==False and hisc==True:
        gwin.blit(img,[0,0])
        txt_scrn("   EXIT   ","black","grey",180,280)
        for i in pg.event.get():
            if i.type==pg.QUIT:
                gext=True
            if i.type==pg.KEYDOWN:
                if i.key==pg.K_RETURN or i.key==pg.K_ESCAPE:
                    home=True
                    hisc=False
        text1=fnt.render("Highest Score made ",True,"white")
        gwin.blit(text1,[100,100])
        text2=fnt.render("on this system is: ",True,"white")
        gwin.blit(text2,[100,140])
        score=fnt.render(hs,True,"white")
        gwin.blit(score,[220,180])
        pg.display.update()

    # About
    while home==False and gext==False and abt==True:
        gwin.blit(img,[0,0])
        txt_scrn("   EXIT   ","black","grey",180,380)
        for i in pg.event.get():
            if i.type==pg.QUIT:
                gext=True
            if i.type==pg.KEYDOWN:
                if i.key==pg.K_RETURN or i.key==pg.K_ESCAPE:
                    home=True
                    abt=False
        text1=fnt.render("This game is developed by",True,"white")
        gwin.blit(text1,[40,100])
        text2=fnt.render("Dhruv Gupta and his colleague",True,"white")
        gwin.blit(text2,[40,140])
        text3=fnt.render("with the help of",True,"white")
        gwin.blit(text3,[40,180])
        text4=fnt.render("pygame module in python.",True,"white")
        gwin.blit(text4,[40,220])
        text5=fnt.render("To operate bat you need to click",True,"white")
        gwin.blit(text5,[40,260])
        text6=fnt.render("arrow keys,",True,"white")
        gwin.blit(text6,[40,300])
        text7=fnt.render("To score dodge the falling bars",True,"white")
        gwin.blit(text7,[40,340])

        pg.display.update()

    # game loop
    while gext==False and start==True:
        gwin.blit(img,[0,0])        
        # display
        score=fnt.render("Score: "+f"{scr}",True,"white")
        gwin.blit(score,[5,5])

        if govr==True:
            if nhs==True:
                sc=fnt.render("You conquer all with "+str(scr)+" score",True,"white")
                gwin.blit(sc,[40,340])
            else:
                sc=fnt.render("Game Over!",True,"white")
                gwin.blit(sc,[150,340])
            pg.display.update()
            pg.time.wait(2000)
            start=False
            home=True
            govr=False  
            r=0
            oy1=0
            oy2=0
            oy3=0
            oy4=0
            ot=5
            ox1=rd.randint(0,360)
            ox2=rd.randint(0,360)
            ox3=rd.randint(0,360)
            ox4=rd.randint(0,360)
            ow=180
            scr=0

            
        # user events
        for i in pg.event.get():
            if i.type==pg.QUIT:
                gext=True
            if i.type==pg.KEYDOWN:
                if i.key==pg.K_LEFT:
                    dir="left"
                elif i.key==pg.K_RIGHT:
                    dir="right"
                elif i.key==pg.K_UP:
                    by-=20
            if i.type==pg.KEYUP:
                if i.key==pg.K_LEFT:
                    dir=""
                elif i.key==pg.K_RIGHT:
                    dir=""
                elif i.key==pg.K_UP:
                    by+=20

        # movement
        if dir=="left":
            if bx<=0:
                bx=0
            else:
                bx-=10
        elif dir=="right":
            if bx>=440:
                bx=440
            else:
                bx+=10
        # char
        if govr==False:
            # pg.draw.rect(gwin,"white",[bx,by,bs,bs])
            gwin.blit(bat,[bx,by])
        # obstacle looping
        if govr==False:
            oy1+=ot
            pg.draw.rect(gwin,"white",[ox1,oy1,ow,ot])
            if oy1>=180 or (r==2 and oy2!=0):
                oy2+=ot
                pg.draw.rect(gwin,"white",[ox2,oy2,ow,ot])
            if oy2>=180 or (r==2 and oy3!=0):
                oy3+=ot
                pg.draw.rect(gwin,"white",[ox3,oy3,ow,ot])
            if oy3>=180 or (r==2 and oy4!=0):
                oy4+=ot
                pg.draw.rect(gwin,"white",[ox4,oy4,ow,ot])

        # user experience activities are done here 
        if oy1>hit:
            oy1=0
            r=2
            scr+=5
            fps+=0.5
            ox1=rd.randint(0,75)

        if oy2>hit:
            oy2=0
            scr+=5
            fps+=0.5
            ox2=rd.randint(75,150)

        if oy3>hit:
            oy3=0
            scr+=5
            fps+=0.5
            ox3=rd.randint(225,300)

        if oy4>hit:
            oy4=0
            scr+=5
            fps+=0.5
            ox4=rd.randint(150,225)

        # high score
        if int(hs)<scr:
            nhs=True
            hsf=open("batrun_hs.txt","w")
            hsf.write(f"{scr}")
        # game over
        if (oy1 in range(by,by+40) and bx in range(ox1,(ox1+180))) or (oy2 in range(by,by+40) and bx in range(ox2,(ox2+180))) or (oy3 in range(by,by+40) and bx in range(ox3,(ox3+180))) or (oy4 in range(by,by+40) and bx in range(ox4,(ox1+180))):
            govr=True
        pg.display.update()
        fspd.tick(fps)
pg.quit()
quit()
