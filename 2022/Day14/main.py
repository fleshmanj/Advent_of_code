import pygame, sys
import time

from main_a import InputHandler
from data import test_data, raw_data


def make_ball():
    ball = pygame.Surface(size=(10, 10))
    ball.fill(color="White")
    ballrect = ball.get_rect()

    ballrect.x = 100
    ballrect.y = 0
    return (ball, ballrect)


pygame.init()

ih = InputHandler(test_data)
ih.find_walls()

size = width, height = 600, 600
speed = [0, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

balls = []
ballrects = []

walls = []
wallrects = []
for wall in ih.walls:
    temp = pygame.Surface(size=(10, 10))
    temp.fill(color="Red")
    temprect = temp.get_rect()
    temprect.x = ((wall[0] - 500) * 10) + 100
    temprect.y = wall[1] * 10
    walls.append((temp, temprect))
    wallrects.append(temprect)

print(walls[0][1])

# current_ball = balls[0][0]
# current_ballrect = balls[0][1]
spawn_ball = True
left_free_space = True
right_free_space = True

while True:
    if spawn_ball:
        current_ball, current_ballrect = make_ball()
        balls.append((current_ball, current_ballrect))
        speed[1] = 1
        spawn_ball = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ball = balls[-1]
    balls[-1] = (ball[0], ball[1].move(speed))
    if balls[-1][1].left < 0 or balls[-1][1].right > width:
        speed[0] = -speed[0]
    if balls[-1][1].top < 0 or balls[-1][1].bottom > height:
        speed[1] = -speed[1]
    if balls[-1][1].collidelist(wallrects) != -1 or balls[-1][1].collidelist(ballrects) != -1:
        balls[-1][1].y -= 1
        x = balls[-1][1].x
        y = balls[-1][1].y
        for wall in wallrects:
            if wall.y == y+10 and wall.x == x-10:
                print("stopped rolling on wall")
                left_free_space = False
                break
        for wall in wallrects:
            if wall.y == y+10 and wall.x == x+10:
                print("stopped rolling on wall")
                right_free_space = False
                break

        for wall in wallrects:
            if wall.y == y and wall.x == x-10:
                print("found a wall")
                left_free_space = False
                break

        for wall in wallrects:
            if wall.y == y and wall.x == x+10:
                print("found a wall")
                right_free_space = False
                break

        for ball in ballrects:
            print(ball.x, ball.y, x-10,y+10)
            if ball.y == y+10 and ball.x == x-10:
                print("stopped rolling off ball")
                left_free_space = False
                break

        for ball in ballrects:
            print(ball.x, ball.y, x+10,y+10)
            if ball.y == y+10 and ball.x == x+10:
                print("stopped rolling off ball")
                left_free_space = False
                break

        if left_free_space:
            balls[-1][1].x = x-10
            balls[-1][1].y = y - 1
            left_free_space = True

        if right_free_space:
            balls[-1][1].x = x+10
            balls[-1][1].y = y - 1
            right_free_space = True

        else:
            # speed[1] = -speed[1]
            speed[1] = 0
            ballrects.append(balls[-1][1])
            left_free_space = True
            spawn_ball = True
    time.sleep(.007)

    screen.fill(black)
    for ball in balls:
        screen.blit(ball[0], ball[1])
    for wall in walls:
        screen.blit(wall[0], wall[1])
    pygame.display.flip()
