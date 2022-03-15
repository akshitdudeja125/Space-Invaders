import pygame
import math
import random
import time
from pygame import mixer

screen_dims = (800, 600)
bg = (0, 0, 0)
speed_player_x = 4
speed_player_y = 4
# speed_enemy_x = 1
# speed_enemy_y = 1

collection_spaceship = ['/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/spaceship.png', '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/spaceship1.png','/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/spaceship2.png', '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/spaceship3.png', '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/spaceship4.png']

collection_enemy = ['/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/enemy2.png', '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/enemy3.png','/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/enemy4.png', '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/enemy5.png', '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/enemy.png']

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode(screen_dims)

# Title /Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(
    "/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/spaceship.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load(
    '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/background1.png')
background = pygame.transform.scale(background, screen_dims)

# Sound
mixer.music.load('Python/PYGAME/background.wav')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load(collection_spaceship[random.randint(0, 4)])
playerImg = pygame.transform.scale(playerImg, (50, 50))
player_X = 370
player_Y = 475
player_X_change = 0
player_Y_change = 0

# Enemy
enemy_Images = []
enemy_X = []
enemy_Y = []
enemy_X_change = []
enemy_Y_change = []
# n_enemies = random.randint(5, 10)
n_enemies = 4
for i in range(n_enemies):
    enemy_Img = pygame.image.load(collection_enemy[random.randint(0, 4)])
    enemy_Img = pygame.transform.scale(enemy_Img, (60, 60))
    enemy_Images.append(enemy_Img)
    enemy_X.append(random.randint(0, 736))
    enemy_Y.append(random.randint(50, 150))
    enemy_X_change.append(random.randint(2, 4))
    enemy_Y_change.append(random.randint(0, 1))

# Bullet
bulletImg = pygame.image.load('Python/PYGAME/bullet.png')
bullet_X = 0
bullet_Y = player_Y
bullet_Y_change = 20
bullet_state = 'ready'


# SCORE
score = 0
# font=pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.Font('FONTS/sweet_kiss/Sweet Kiss.ttf', 32)
font2 = pygame.font.Font('FONTS/sweet_kiss/Sweet Kiss.ttf', 64)
text_X = 10
text_Y = 10
lives = 3


# Game Loop
run_state = True
init_time = time.time()
time_live_0 = time.time()
Game_Status='Ongoing'
lst2 = []
while run_state:
    screen.fill(bg)
    screen.blit(background, (0, 0))

    if lives != 0 and Game_Status!='Won':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_X_change -= speed_player_x
                elif event.key == pygame.K_RIGHT:
                    player_X_change += speed_player_x
                elif event.key == pygame.K_UP:
                    player_Y_change -= speed_player_y
                elif event.key == pygame.K_DOWN:
                    player_Y_change += speed_player_y
                elif event.key == pygame.K_SPACE:
                    if bullet_state is 'ready':
                        bullet_X = player_X
                        bullet_Y = player_Y
                        bullet_state = 'fire'
                        bullet_sound = mixer.Sound(
                            '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/laser.wav')
                        bullet_sound.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_X_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_Y_change = 0
        if player_X < 0:
            player_X = 0
        if player_X >= 751:
            player_X = 751
        if player_Y < 0:
            player_Y = 0
        if player_Y >= 550:
            player_Y = 550
        player_Y += player_Y_change
        player_X += player_X_change
        ci = 0
        collision = False
        collision_player = False
        for i in range(n_enemies):
            if enemy_X[i] < 0:
                enemy_X[i] = 0
                enemy_X_change[i] = -enemy_X_change[i]
            if enemy_X[i] >= 751:
                enemy_X[i] = 751
                enemy_X_change[i] = -enemy_X_change[i]
            if enemy_Y[i] < 0:
                enemy_Y[i] = 0
                enemy_Y_change[i] = -enemy_Y_change[i]
            if enemy_Y[i] >= 400:
                enemy_Y_change[i] = -enemy_Y_change[i]
                enemy_Y[i] = 400
            enemy_X[i] += enemy_X_change[i]
            enemy_Y[i] += enemy_Y_change[i]

            # Collision
            if abs(bullet_X-enemy_X[i]) <= 10 and abs(bullet_Y-enemy_Y[i]) <= 10:
                collision = True
                ci = i
                bullet_state = 'ready'
            else:
                screen.blit(enemy_Images[i], (enemy_X[i], enemy_Y[i]))
            if abs(player_X-enemy_X[i]) <= 10 and abs(player_Y-enemy_Y[i]) <= 10:
                collision_player = True
                ci_2 = i
                bullet_state = 'ready'
            else:
                screen.blit(enemy_Images[i], (enemy_X[i], enemy_Y[i]))
        if collision_player:
            explosion_Img = pygame.image.load('Python/PYGAME/explosion1.png')
            explosion_Img = pygame.transform.scale(explosion_Img, (60, 60))
            screen.blit(explosion_Img, (enemy_X[ci_2], enemy_Y[ci_2]))
            collision_sound = mixer.Sound(
                '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/explosion.wav')
            collision_sound.play()
            score -= 1
            lives -= 1
            enemy_Images.pop(ci_2)
            enemy_X.pop(ci_2)
            enemy_Y.pop(ci_2)
            enemy_X_change.pop(ci_2)
            enemy_Y_change.pop(ci_2)
            n_enemies -= 1
            player_X = 370
            player_Y = 475

        if collision:
            explosion_Img = pygame.image.load('Python/PYGAME/explosion1.png')
            explosion_Img = pygame.transform.scale(explosion_Img, (60, 60))
            screen.blit(explosion_Img, (enemy_X[ci], enemy_Y[ci]))
            collision_sound = mixer.Sound(
                '/Users/akshitdudeja/VS Code/main_folder/Python/PYGAME/explosion.wav')
            collision_sound.play()
            score += 1
            enemy_Images.pop(ci)
            enemy_X.pop(ci)
            enemy_Y.pop(ci)
            enemy_X_change.pop(ci)
            enemy_Y_change.pop(ci)
            n_enemies -= 1

        #  Bullet _Movement
        if bullet_Y <= 0:
            bullet_Y = 0
            bullet_state = "ready"
        if bullet_state == "fire":
            screen.blit(bulletImg, (bullet_X + 9, bullet_Y))
            bullet_Y -= bullet_Y_change
        if n_enemies == 0:
            Game_Status='Won'
        final_time = time.time()
        if (int(final_time-init_time)) % 5 == 0 and (int(final_time-init_time)) not in lst2 and n_enemies <= 10:
            lst2.append((int(final_time-init_time)))
            enemy_Img = pygame.image.load(
                collection_enemy[random.randint(0, 4)])
            enemy_Img = pygame.transform.scale(enemy_Img, (50, 50))
            enemy_Images.append(enemy_Img)
            enemy_X.append(random.randint(0, 736))
            enemy_Y.append(random.randint(50, 150))
            enemy_X_change.append(random.randint(2, 6))
            enemy_Y_change.append(random.randint(0, 3))
            n_enemies += 1

        screen.blit(playerImg, (player_X, player_Y))
    elif lives==0 and Game_Status!='Won':
        go = font2.render("Game Over", True, (255, 255, 255))
        screen.blit(go, (300, 300))
        re = font.render("Press Space to restart", True, (255, 255, 255))
        screen.blit(re, (300, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_state = False
            if event.type == pygame.KEYDOWN:
                run_state = True
                if event.key == pygame.K_SPACE:
                    lives = 3
                    score=0
    if Game_Status=='Won':
        go = font2.render("Game Over : You Win", True, (255, 255, 255))
        screen.blit(go, (200, 300))
        re = font.render("Press Space to restart", True, (255, 255, 255))
        screen.blit(re, (300, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_state = False
            if event.type == pygame.KEYDOWN:
                run_state = True
                if event.key == pygame.K_SPACE:
                    Game_Status='Ongoing'
                    lives = 3
                    score=0
    sc = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(sc, (text_X, text_Y))
    li = font.render("Lives : " + str(lives), True, (255, 255, 255))
    screen.blit(li, (text_X, text_Y+30))
    pygame.display.update()
