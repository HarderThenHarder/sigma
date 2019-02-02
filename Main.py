import speech_recognition as sr
import pygame
from pygame.time import Clock
from pygame.locals import *
from sys import exit
from Pencil import Pencil
import time
import speech
import re

SCREEN_WIDTH_HEIGHT = [860, 500]


def generate_text(screen, text, i):
    Pencil.write_text(screen, text, font_pos=[15, 20 * i], font_size=15, color=(100, 200, 100))


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT)
    pygame.display.set_caption("SigmaV1.0")
    clock = Clock()

    bg = pygame.transform.scale(pygame.image.load(r"wallpaper\bg.jpg"), SCREEN_WIDTH_HEIGHT)
    screen.blit(bg, (0, 0))
    pygame.display.update()
    r = sr.Recognizer()
    command = None

    while True:
        clock.tick(5)
        screen.blit(bg, (0, 0))
        generate_text(screen, "Press SPACE To Speak", 1)
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
                    generate_text(screen, "say something...", 2)
                    pygame.display.update()
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    generate_text(screen, "Wait...", 3)
                    pygame.display.update()
                    command = r.recognize_google(audio, language="en-US")
                    generate_text(screen, command, 4)
                    pygame.display.update()

        if command:
            if re.match(".*who are you.*", command, re.I) or re.match(".*what's your name.*", command, re.I):
                response = "My name is Sigma, sir."
            else:
                response = "That's out of my ability."

            time.sleep(1)
            generate_text(screen, response, 5)
            pygame.display.update()
            speech.say(response)
            command = None

        pygame.display.update()


if __name__ == '__main__':
    main()
