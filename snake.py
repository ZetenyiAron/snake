import pygame
import random
import math
import time

pygame.init()

clock = pygame.time.Clock()
FPS = 30

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

snakeX = 400
snakeY = 300
snakeX_change = 0
snakeY_change = 0
snake_width = 10
snake_height = 10

apple_width = 10
apple_height = 10
appleX = random.randrange(apple_width, display_width-apple_width)
appleY = random.randrange(apple_height, display_height-apple_height)

snakeImg = pygame.image.load("snake.png")

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
pygame.display.set_icon(snakeImg)

screen.blit(snakeImg, (0, 0))
time.sleep(2)


def grow(snakeX, snakeY, appleX, appleY):
    distance = math.sqrt((math.pow(snakeX - appleX, 2)) + (math.pow(snakeY - appleY, 2)))
    if distance < 10:
        return True
    else:
        return False

def snake(snake_width, snake_height, snake_List):
    for XnY in snake_List:
        pygame.draw.rect(screen, black, [XnY[0], XnY[1], snake_width, snake_height])

def apple(appleX, appleY, apple_width, apple_height):
    pygame.draw.rect(screen, red, [appleX, appleY, apple_width, apple_height])

score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)
def show_score():
    score_text = score_font.render("Score: " + str(score), True, blue)
    screen.blit(score_text, (16, 16))


game_over_font = pygame.font.Font("freesansbold.ttf", 40)
game_over = False
def show_game_over():
    global game_over
    game_over = True
    game_over_text = game_over_font.render("Game Over", True, red)
    score_text = game_over_font.render("Your score is " + str(score), True, black)
    screen.blit(game_over_text, (display_width/2-100, display_height/2))
    screen.blit(score_text, (display_width/2-130, display_height/2+50))

snake_List = []
snake_Length = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not game_over:
                snakeX_change = -5
                snakeY_change = 0
            if event.key == pygame.K_RIGHT and not game_over:
                snakeX_change = 5
                snakeY_change = 0
            if event.key == pygame.K_UP and not game_over:
                snakeY_change = -5
                snakeX_change = 0
            if event.key == pygame.K_DOWN and not game_over:
                snakeY_change = 5
                snakeX_change = 0
    if not game_over:
        snakeX += snakeX_change
        snakeY += snakeY_change

    screen.fill(white)

    if snakeX > 790 or snakeX < 10 or snakeY > 590 or snakeY < 10:
        show_game_over()

    eat = grow(snakeX, snakeY, appleX, appleY)
    if eat:
        snake_Length += 1
        score += 1
        appleX = random.randrange(apple_width, display_width - apple_width)
        appleY = random.randrange(apple_height, display_height - apple_height)


    show_score()
    apple(appleX, appleY, apple_width, apple_height)

    snake_Head = []
    snake_Head.append(snakeX)
    snake_Head.append(snakeY)
    snake_List.append(snake_Head)


    if len(snake_List) > snake_Length:
        del(snake_List[0])

    for i in snake_List[:-1]:
        if i == snake_Head:
            show_game_over()

    snake(snake_width, snake_height, snake_List)
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
quit()

