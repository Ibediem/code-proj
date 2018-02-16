"""
LESSON: 5.1 - Sprites
EXERCISE: Code Your Own
"""
"""
LESSON: 4.3 - For Range
EXERCISE: Code Your Own
TITLE: [Your Title Here]
DESCRIPTION: [Your Description Here]
"""
"""
LESSON: 3.6 - Time
EXERCISE: Code Your Own

TITLE: [Your Title Here]
DESCRIPTION: [Your Description Here]
"""

import random
import pygame
pygame.init()
g21=3
hi=1
liljaden = ["paarth", "Big Shaq", "joon"] 
w=pygame.display.set_mode([400,400])
num=random.randint(0,255)
num1=random.randint(0,255)
num3=random.randint(0,255)
num4=(num,num1,num3)
w.fill((num,num1,num3))
pygame.display.flip()
name=input("Whats your name? ")
rg=input("What is the red value? 0-255 ")
gg=input("What is the green value? 0-255 ")
bg=input("What is the blue value? 0-255 ")
g=(rg,gg,bg)    
while hi == 1 :
    if num4 == g21:
        hi =input("Good job type enter to end")
    elif hi == "enter":
        break
    if g21==3 :
        print("So close")
        print("Here is the red color value. ")
        print(num)
        g21-=1
        rg1=input("What is the red value? 0-255 ")
        gg1=input("What is the green value? 0-255 ")
        bg1=input("What is the blue value? 0-255 ")
        g1=(rg1,gg1,bg1)
    if g21 == 2:
        print("Come on so close this time!")
        print("here is the green value")
        print(num1)
        g21-=1
        rg2=input("What is the red value? 0-255 ")
        gg2=input("What is the green value? 0-255 ")
        bg2=input("What is the blue value? 0-255 ")
        g2=(rg2,gg2,bg2)
    if g21 == 1  :   
        print("Super close!!!")
        print("Here is the last blue value")
        print(num3)
        g21-=1
        rg3=input("What is the red value? 0-255 ")
        gg3=input("What is the green value? 0-255 ")
        bg3=input("What is the blue value? 0-255 ")
        g3=(rg3,gg3,bg3)
    if g21 == 0 :
        break

s=input("Good job you guessed the anwser! type enter to leave!")
if s == 'secret':
    n=input("Enter 2 number code ::::: ")
    if n == "34":
        print("Welcome Back Colonel " +name+ " you have a board meeting with the illuminati pleas dont for get to wear your pants this time.YOU BUM")
        if name in liljaden:
            pancakes = input("You have bypassed all of my tricks and security! how did you do it?")
            if pancakes == "with chickenpowwow and mebutt":
                print("Welcome supereme leader you are now THE LEADER OF THE ILLUMINATI FOR CRACKING THIS CODE. your new assinment..........make this code better.")
            print ("good job you beat me you win " +name+ "i get you next time. this is the real ending of this program goodbye. ")
    if n == "29" :
        w1=pygame.display.set_mode([400,400])
        w1.fill((0,0,0))
        times=30
        animating=True
        x=0
        x1=400
        x2=200
        x3=160
        x4=200
        x5=75
        x6=30
        x7=160
        x8=200
        x9=37
        x10=15
        while animating:
            
            pygame.draw.polygon(w,(48, 108, 7),[(x,400),(x1,400),(x2,0)],10)
            rect=pygame.Rect(x3,x4,x5,x6)
            pygame.draw.ellipse(w,(48, 108, 7), rect,75)
            rect1=pygame.Rect(x7,x8,x9,x10)
            pygame.draw.ellipse(w,(0,0,0),rect1,37)
            x+=10
            x1+=10
            x2+=10
            x3+=10
            x4+=10
            x5+=10
            x6+=10
            x7+=10
            x8+=10
            x9+=10
            x10+=10
            times-=1
            pygame.time.wait(100)
            pygame.display.flip()
            pygame.draw.polygon(w,(48, 108, 7),[(x,400),(x1,400),(x2,0)],10)
            pygame.draw.ellipse(w,(48, 108, 7), rect,75)
            pygame.draw.ellipse(w,(0,0,0),rect1,37)
            pygame.display.flip()
            if times == 0:
                animating=False
        pygame.display.flip()
    
        print("Welcome to the Illuminati ")
        mma =input("Type anything to log out ")
        running=True
        c = pygame.time.Clock()
        de=pygame.display.set_mode([2100,900])
        
        xx=300
        yy=300
        x11=600
        x22=600
        if mma == "as":
            while running:
                de.fill((255,255,255))
                rec=pygame.Rect(xx,yy,300,300)
                pygame.draw.rect(de,(192, 57, 43),rec)
                see=pygame.Rect(x11,x22,300,300)
                pygame.draw.rect(w,(230,230,230),see)
                pygame.time.wait(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running=False
                    if pygame.MOUSEBUTTONDOWN and event.key == pygame.K_UP:
                        yy-=30
                    if pygame.MOUSEBUTTONDOWN and event.key == pygame.K_DOWN:
                        yy+=30
                    if pygame.MOUSEBUTTONDOWN and event.key == pygame.K_LEFT:
                        xx-=30
                    if pygame.MOUSEBUTTONDOWN and event.key == pygame.K_RIGHT:
                        xx+=30
                    if xx == x11 and yy == x22:
                        print("Welcome Colonel " +name+ " Your password is now 34")
                        running=False
                    pygame.time.wait(10)
                    pygame.display.flip()
# Turn in your Coding Exercise.












# Turn in your Coding Exercise.
