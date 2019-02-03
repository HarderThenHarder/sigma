import speech_recognition as sr
import pygame
from pygame.time import Clock
from pygame.locals import *
from sys import exit
from Pencil import Pencil
import time
import win32com.client as client
import re
from random import randint
import webbrowser as web
import subprocess
import os
from math import sin

SCREEN_WIDTH_HEIGHT = [860, 500]


def generate_text(screen, text, i, text_color=(100, 200, 100), font_size=17):
    Pencil.write_text(screen, text, font_pos=[15, font_size * i], font_size=font_size, color=text_color)


def generate_help_text(screen, text, i, text_color=(100, 100, 100), font_size=16):
    Pencil.write_text(screen, text, font_pos=[SCREEN_WIDTH_HEIGHT[0]-200, SCREEN_WIDTH_HEIGHT[1] - font_size * i * 2], font_size=font_size, color=text_color)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT)
    pygame.display.set_caption("SigmaV1.0")
    clock = Clock()
    tick = 0

    first = pygame.mixer.Sound(r"sound\first.wav")
    start = pygame.mixer.Sound(r"sound\start.wav")
    over = pygame.mixer.Sound(r"sound\over.wav")

    bg = pygame.transform.scale(pygame.image.load(r"wallpaper\bg.jpg"), SCREEN_WIDTH_HEIGHT)
    icon = pygame.image.load(r"wallpaper\icon.ico")
    cover_pic = pygame.Surface(SCREEN_WIDTH_HEIGHT)
    cover_pic.fill(color=(10, 10, 10))
    cover_pic.set_alpha(10)
    pygame.display.set_icon(icon)
    screen.blit(bg, (0, 0))
    screen.blit(cover_pic, (0, 0))
    pygame.display.update()
    first.play()

    introduction = ["You Can Ask Me Like:", "who are you...", "give me some films...", "sing a song for me...", "close my computer...",
                    "create python file..."]

    r = sr.Recognizer()
    speaker = client.Dispatch("SAPI.SpVoice")
    command = None
    response = None

    while True:
        clock.tick(20)
        cover_pic.set_alpha(80 - 80 * sin(tick))
        screen.blit(bg, (0, 0))
        screen.blit(cover_pic, (0, 0))
        generate_text(screen, "Press SPACE To Speak", 2, text_color=(200, 200, 200))
        Pencil.draw_line(screen, [15, 52], [195, 52], color=(200, 200, 200), width=1)

        for i in range(len(introduction)):
            generate_help_text(screen, introduction[len(introduction)-1-i], i+1)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

                elif event.key == K_SPACE:
                    start.play()
                    generate_text(screen, "Say something...", 4)
                    pygame.display.update()
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    over.play()
                    generate_text(screen, "Wait...", 5.5)
                    pygame.display.update()
                    try:
                        command = r.recognize_google(audio, language="en-US")
                    except:
                        command = "<Can't Recognize...>"
                    generate_text(screen, command, 7)
                    pygame.display.update()

        if command:
            if re.match(".*who are you.*", command, re.I) or re.match(".*your name.*", command, re.I):
                response = "My name is Sigma sir."
            elif re.match(".*hello.*", command, re.I) or re.match(".*hi.*", command, re.I):
                response = "Hello, nice to meet you."
            elif re.match(".*movie.*", command, re.I) or re.match(".*film.*", command, re.I):
                response = "Here are some nice videos if you are VIP, sir."
                web.open_new("http://www.youku.com")
            elif re.match(".*song.*", command, re.I) or re.match(".*music.*", command, re.I):
                try:
                    subprocess.Popen(r"C:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe")
                    response = "Find some songs you like."
                except:
                    response = "I can't find your Music Application."
            elif re.match(".*close.*computer.*", command, re.I):
                response = "GoodNight sir."
                os.system("SlideToShutDown.exe")
            elif re.match(".*good night.*", command, re.I) or re.match(".*goodbye.*", command, re.I) or re.match(".*bye.*", command, re.I):
                pygame.quit()
                exit()
            elif re.match(".*python file.*", command, re.I):
                os.system('echo # new python file > %s' % "C:\\Users\\eve\\Desktop\\" + "new_file.py")
                response = "A new file has been created on your desktop."
            elif re.match(".*python.*game.*called(.*)", command, re.I):
                file_name = re.match(".*python.*game.*called(.*)", command, re.I)
                file_name = file_name.group(1).strip()
                os.system('echo import pygame > %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo from pygame.locals import * >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo from sys import eixt >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo # init the pygame>> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo pygame.init() >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo pygame.set_caption() >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo # set window size >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo SCREEN_WIDTH_HEIGHT = [] >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo # set the background Picture >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo bg = pygame.transform.scale(pygame.image.load(), SCREEN_WIDTH_HEIGHT) >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo # start while loop >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo while True: >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo     screen.blit(bg) >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo     for event in pygame.event.get(): >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo         if event.type == QUIT(): >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo             exit() >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo     # write your code here... >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo     # ... >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                os.system('echo     pygame.display.update() >> %s' % "C:\\Users\\eve\\Desktop\\" + file_name + ".py")
                response = "All have done, sir."
            elif re.match(".*search.*", command, re.I):
                web.open_new("http://www.baidu.com")
                response = "Use this for searching please."
            elif re.match(".*can.*do.*for.*me", command, re.I) or re.match(".*help.*", command, re.I):
                response = "Some advices are on the right side..."
            elif command == "<Can't Recognize...>":
                response = "I didn't hear you clearly."
            else:
                rand = randint(0, 2)
                if rand == 0:
                    response = "That's out of my ability."
                elif rand == 1:
                    response = "I don't understand."
                elif rand == 2:
                    response = "Sorry, I don't know."

            time.sleep(1)
            generate_text(screen, response, 8.5)
            pygame.display.update()
            speaker.Speak(response)
            time.sleep(1)
            command = None

        tick += 0.05
        pygame.display.update()


if __name__ == '__main__':
    main()
