from ast import For
from time import time
from turtle import width
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((1280, 720))
s_width = 1280
s_hight = 720
clock = pygame.time.Clock()
running = True
b_jump = False


def game_begin():
    global spike_x
    spike_x = 900
    global spike_x1
    spike_x1 = 6360
    global spike_x2
    spike_x2 = 11820
    global spike_y
    spike_y = 601
    global finish_x
    finish_x = 15000
    global finish_y
    finish_y = 0
    global angle
    angle = 0
    global death_x
    death_x = 500
    global counter_x
    counter_x = 840


bg = pygame.image.load("image/bg.png")
player = pygame.image.load("image/avatar.png")
floor = pygame.image.load("image/floor.png")
spike = pygame.image.load("image/spike.png")
restart_pic = pygame.image.load("image/butt_res.png")
victory_pic = pygame.image.load("image/win_game.png")
finish = pygame.image.load("image/finish.png")
frame = pygame.image.load("image/frame.png")


player_s = pygame.transform.scale(player, (60, 60))
player_s1 = pygame.transform.scale(player, (60, 60))
spike_s = pygame.transform.scale(spike, (60, 60))
frame_s = pygame.transform.scale(frame, (1024, 576))
player_s = pygame.transform.scale(player, (60, 60))
player_s1 = pygame.transform.scale(player, (60, 60))
spike_s = pygame.transform.scale(spike, (60, 60))
spike_s1 = pygame.transform.scale(spike, (60, 60))
spike_s2 = pygame.transform.scale(spike, (60, 60))
finish_s = pygame.transform.scale(finish, (1200, 666))
victory_s = pygame.transform.scale(victory_pic, (660, 100))


pygame.font.init()
myfont = pygame.font.Font('pusab.ttf', 50)
player_x = 250
player_y = 600
floor_x = 0
floor_y = 660
spike_x = 900
spike_x1 = 6360
spike_x2 = 11820
spike_y = 601
finish_x = 15000
finish_y = 0
jump = 9
angle = 0
death = "attempt"
death_x = 500
counter = 1
counter_x = 840


def game_wait():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 540 <= mouse[0] <= 740 and 260 <= mouse[1] <= 460:
                    wait = False


def game_restart():
    screen.blit(frame_s, (128, 72))
    screen.blit(restart_pic, (540, 260))
    pygame.display.flip()
    game_wait()
    game_begin()


def game_win():
    screen.blit(frame_s, (128, 72))
    screen.blit(victory_s, (310, 120))
    screen.blit(restart_pic, (540, 260))
    pygame.display.flip()
    game_wait()
    game_begin()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if not(b_jump):
        if keys[pygame.K_SPACE]:
            b_jump = True
    else:
        if jump >= -9:
            if jump < 0:
                player_y += (jump**2) / 2
            else:
                player_y -= (jump**2) / 2
            jump -= 1
        else:
            b_jump = False
            jump = 9

    if floor_x > s_width - 2720:
        floor_x -= 15
    else:
        floor_x = 0

    if spike_x > -30:
        spike_x -= 15
    else:
        spike_x = 1300
    if spike_x1 > -30:
        spike_x1 -= 15
    else:
        spike_x1 = 1300
    if spike_x2 > -30:
        spike_x2 -= 15
    else:
        spike_x2 = 1300

    if finish_x > -10:
        finish_x -= 15
    else:
        finish_x = 15000

    if death_x != -200:
        death_x -= 15
    else:
        death_x != -200

    if counter_x != -200:
        counter_x -= 15
    else:
        counter_x != -200

    if (spike_x + 50) > player_x > (spike_x - 50) and player_y > (spike_y - 41):
        counter += 1
        game_restart()
    if (spike_x1 + 50) > player_x > (spike_x1 - 50) and player_y > (spike_y - 41):
        counter += 1
        game_restart()
    if (spike_x2 + 50) > player_x > (spike_x2 - 50) and player_y > (spike_y - 41):
        counter += 1
        game_restart()

    if (finish_x + 100) > player_x > (finish_x) and player_y > (finish_y - 500):
        counter = 1
        game_win()

    screen.blit(bg, (0, 0))
    screen.blit(floor, (floor_x, floor_y))
    screen.blit(player_s, (player_x, player_y))

    if jump != 9:
        player_s = pygame.transform.scale(player, (0, 0))
        rot_player = pygame.transform.rotate(player_s1, angle)
        angle -= 5
        screen.blit(rot_player, (player_x, player_y))
    else:
        if angle % 90 != 0 or angle == 0:
            if angle < 30:
                angle = 360
            elif 120 > angle > 60:
                angle = 90
            elif 210 > angle > 150:
                angle = 180
            elif 300 > angle > 240:
                angle = 270
        player_s = pygame.transform.scale(player, (60, 60))
        player_s = pygame.transform.rotate(player_s, angle)

    textsurface = myfont.render(str(death), False, (35, 200, 240))
    screen.blit(textsurface, (death_x, 350))
    digitalsurface = myfont.render(str(counter), False, (35, 200, 240))
    screen.blit(digitalsurface, (counter_x, 350))
    screen.blit(spike_s, (spike_x, spike_y))
    screen.blit(spike_s1, (spike_x1, spike_y))
    screen.blit(spike_s2, (spike_x2, spike_y))
    screen.blit(finish_s, (finish_x, finish_y))
    screen.blit(floor, (floor_x, floor_y))

    pygame.display.flip()
    clock.tick(50)

print("Игра закрывается")
pygame.quit()
sys.exit()
