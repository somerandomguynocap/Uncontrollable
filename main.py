import pygame
import random
import math
from pygame import mixer

#init
pygame.init()

width = 800
height = 500
run = True
speed = 5

#title and logo
pygame.display.set_caption("Uncontrollable-BY ALAN")
icon = pygame.image.load("iconfile.png")
pygame.display.set_icon(icon)


#player
playerone = pygame.transform.scale(pygame.image.load("ufo.png"), (70, 70))
playeroneX = 370
playeroneY = 410
playerX_change = 0

#bullet
bullet = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 410
bulletY_change = 5
bullet_state = "ready"


# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_text = pygame.font.Font("freesansbold.ttf", 64)
#game over


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))

def game_over_text():
    over = over_text.render("Game Over!", True, (255, 255, 255))
    window.blit(over, (200, 280))

# background
bg = pygame.transform.scale(pygame.image.load("space.jpg"), (800, 500))
bgX = 0
bgY = 0


# enemy
enemymain = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5


for i in range(num_of_enemies):
    enemymain.append(pygame.image.load("enemy1.png"))
    enemyX.append(random.randint(10, 736))
    enemyY.append(random.randint(1, 100))
    enemyX_change.append(3)
    enemyY_change.append(40)

def player(x, y):
    window.blit(playerone, (x, y))

def enemy(x, y, i):
    window.blit(enemymain[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bullet, (x + 20, y + 35))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX ,2)) + (math.pow(enemyY-bulletY, 2))
    if distance < 30:
        return True
    else:
        return False



#screen
window = pygame.display.set_mode((width, height))
fps = 60
clock = pygame.time.Clock()
while run:
    clock.tick(fps)
    window.blit(bg, (bgX, bgY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -4
            if event.key == pygame.K_d:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playeroneX
                    fire_bullet(bulletX, bulletY)


       #player movement 
        if playeroneX <= 0:
            playeroneX = 0
        elif playeroneX >= 745:
            playeroneX = 745

    #enemy movement [inside for loop]
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
        
        
        enemyX[i] = enemyX[i] + enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = +3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 750:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        #collison
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 410
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(10, 736)
            enemyY[i] = random.randint(1, 100)
        enemy(enemyX[i], enemyY[i], i)
    
    #bullet movement
    if bulletY <= 0:
        bulletY = 410
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    # X + -0.3 = X - 0.3    X + +0.3 = X + 0.3
    playeroneX += playerX_change
    player(playeroneX, playeroneY)
    show_score(textX, textY)
    pygame.display.update()
