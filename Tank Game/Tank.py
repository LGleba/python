# 2020
# Tank - game
# Designed and powered by LGleba


import pygame
import random


def createMap():
    # Black ground
    screen.fill((255, 255, 255))
    for i in range(sizeY):
        for j in range(sizeX):
            # True - active zone
            if map[i][j]:
                screen.blit(groundImage, (j * sizeBlock, i * sizeBlock))
            # False - walls
            else:
                screen.blit(wallImage, (j * sizeBlock, i * sizeBlock))


def activeShoots():
    global scoreGreen
    global scoreRed
    global stop
    # shoots[i][0] = x
    # shoots[i][1] = y
    # shoots[i][2] = direction (0 - Up, 1 - Right, 2 - Down, 3 - Left)
    if shoots:
        for i in range(len(shoots) - 1, -1, -1):
            direction = shoots[i][2]
            # Left
            if direction == 3:
                if walls[int(shoots[i][1] / speed)][int((shoots[i][0] - speedShoot) / speed)]:
                    shoots[i][0] -= speedShoot
                    bulletImage = pygame.image.load("img/bulletLeft.png")
                    screen.blit(bulletImage, (shoots[i][0], shoots[i][1]))
                    if (x2 <= shoots[i][0] <= x2 + sizeBlock) and y2 <= shoots[i][1] <= y2 + sizeBlock:
                        scoreGreen += 1
                        shoots.pop(i)
                        if scoreGreen > 9:
                            stop = 1
                else:
                    shoots.pop(i)
            # Right
            elif direction == 1:
                if walls[int(shoots[i][1] / speed)][int((shoots[i][0] + speedShoot) / speed)]:
                    shoots[i][0] += speedShoot
                    bulletImage = pygame.image.load("img/bulletRight.png")
                    screen.blit(bulletImage, (shoots[i][0], shoots[i][1]))
                    if (x2 <= shoots[i][0] <= x2 + sizeBlock) and y2 <= shoots[i][1] <= y2 + sizeBlock:
                        scoreGreen += 1
                        shoots.pop(i)
                        if scoreGreen > 9:
                            stop = 1
                else:
                    shoots.pop(i)
            # Up
            elif direction == 0:
                if walls[int((shoots[i][1] - speedShoot) / speed)][int(shoots[i][0] / speed)]:
                    shoots[i][1] -= speedShoot
                    bulletImage = pygame.image.load("img/bulletUp.png")
                    screen.blit(bulletImage, (shoots[i][0], shoots[i][1]))
                    if (x2 <= shoots[i][0] <= x2 + sizeBlock) and y2 <= shoots[i][1] <= y2 + sizeBlock:
                        scoreGreen += 1
                        shoots.pop(i)
                        if scoreGreen > 9:
                            stop = 1
                else:
                    shoots.pop(i)
            # Down
            elif direction == 2:
                if walls[int((shoots[i][1] + speedShoot) / speed)][int(shoots[i][0] / speed)]:
                    shoots[i][1] += speedShoot
                    bulletImage = pygame.image.load("img/bulletDown.png")
                    screen.blit(bulletImage, (shoots[i][0], shoots[i][1]))
                    if (x2 <= shoots[i][0] <= x2 + sizeBlock) and y2 <= shoots[i][1] <= y2 + sizeBlock:
                        scoreGreen += 1
                        shoots.pop(i)
                        if scoreGreen > 9:
                            stop = 1
                else:
                    shoots.pop(i)

    if shoots2:
        for i in range(len(shoots2) - 1, -1, -1):
            direction = shoots2[i][2]
            # Left
            if direction == 3:
                if walls[int(shoots2[i][1] / speed)][int((shoots2[i][0] - speedShoot) / speed)]:
                    shoots2[i][0] -= speedShoot
                    bulletImage = pygame.image.load("img/bulletLeft.png")
                    screen.blit(bulletImage, (shoots2[i][0], shoots2[i][1]))
                    if (x <= shoots2[i][0] <= x + sizeBlock) and y <= shoots2[i][1] <= y + sizeBlock:
                        scoreRed += 1
                        shoots2.pop(i)
                        if scoreRed > 9:
                            stop = 2
                else:
                    shoots2.pop(i)
            # Right
            elif direction == 1:
                if walls[int(shoots2[i][1] / speed)][int((shoots2[i][0] + speedShoot) / speed)]:
                    shoots2[i][0] += speedShoot
                    bulletImage = pygame.image.load("img/bulletRight.png")
                    screen.blit(bulletImage, (shoots2[i][0], shoots2[i][1]))
                    if (x <= shoots2[i][0] <= x + sizeBlock) and y <= shoots2[i][1] <= y + sizeBlock:
                        scoreRed += 1
                        shoots2.pop(i)
                        if scoreRed > 9:
                            stop = 2
                else:
                    shoots2.pop(i)
            # Up
            elif direction == 0:
                if walls[int((shoots2[i][1] - speedShoot) / speed)][int(shoots2[i][0] / speed)]:
                    shoots2[i][1] -= speedShoot
                    bulletImage = pygame.image.load("img/bulletUp.png")
                    screen.blit(bulletImage, (shoots2[i][0], shoots2[i][1]))
                    if (x <= shoots2[i][0] <= x + sizeBlock) and y <= shoots2[i][1] <= y + sizeBlock:
                        scoreRed += 1
                        shoots2.pop(i)
                        if scoreRed > 9:
                            stop = 2
                else:
                    shoots2.pop(i)
            # Down
            elif direction == 2:
                if walls[int((shoots2[i][1] + speedShoot) / speed)][int(shoots2[i][0] / speed)]:
                    shoots2[i][1] += speedShoot
                    bulletImage = pygame.image.load("img/bulletDown.png")
                    screen.blit(bulletImage, (shoots2[i][0], shoots2[i][1]))
                    if (x <= shoots2[i][0] <= x + sizeBlock) and y <= shoots2[i][1] <= y + sizeBlock:
                        scoreRed += 1
                        shoots2.pop(i)
                        if scoreRed > 9:
                            stop = 2
                else:
                    shoots2.pop(i)


def activeKeys():
    global x
    global y
    global directionShoot
    global tankImage

    global x2
    global y2
    global directionShoot2
    global tankEnemyImage

    global scoreGreen
    global scoreRed

    standX = int(x / 10)
    standY = int(y / 10)
    standX2 = int(x2 / 10)
    standY2 = int(y2 / 10)

    keys = pygame.key.get_pressed()

    # Reload Map
    if keys[pygame.K_m]:
        # Base stand tanks
        x = int(sizeBlock)
        y = int(sizeBlock)
        x2 = int(displayX - twoSizeBlock)
        y2 = int(displayY - twoSizeBlock)
        # Generate random map
        for i in range(1, sizeY - 1):
            for j in range(1, sizeX - 1):
                map[i][j] = bool(random.randint(0, 3))
                if map[i][j]:
                    for k in range(countSteps):
                        for l in range(countSteps):
                            walls[i * countSteps + k][j * countSteps + l] = True
                else:
                    for k in range(countSteps):
                        for l in range(countSteps):
                            walls[i * countSteps + k][j * countSteps + l] = False
        map[1][1] = True
        map[12][26] = True
        for k in range(countSteps):
            for l in range(countSteps):
                walls[1 * countSteps + k][1 * countSteps + l] = True
        for k in range(countSteps):
            for l in range(countSteps):
                walls[12 * countSteps + k][26 * countSteps + l] = True

    # Reload Score
    if keys[pygame.K_r]:
        scoreRed = 0
        scoreGreen = 0

    # Green tank go Left
    if keys[pygame.K_a] and walls[standY + 1][standX - 1] and walls[standY + 2][standX - 1] and walls[standY + 3][standX - 1]:
        x -= speed
        tankImage = pygame.image.load("img/tankLeft.png")
        directionShoot = int(3)
        if not walls[standY][standX - 1]:
            y += speed
        elif not walls[standY + 4][standX - 1]:
            y -= speed
    # Green tank go Right
    elif keys[pygame.K_d] and walls[standY + 1][standX + countSteps] and walls[standY + 2][standX + countSteps] and walls[standY + 3][standX + countSteps]:
        x += speed
        tankImage = pygame.image.load("img/tankRight.png")
        directionShoot = int(1)
        if not walls[standY][standX + countSteps]:
            y += speed
        elif not walls[standY + 4][standX + countSteps]:
            y -= speed
    # Green tank go Up
    elif keys[pygame.K_w] and walls[standY - 1][standX + 1] and walls[standY - 1][standX + 2] and walls[standY - 1][standX + 3]:
        y -= speed
        tankImage = pygame.image.load("img/tankUp.png")
        directionShoot = int(0)
        if not walls[standY - 1][standX]:
            x += speed
        elif not walls[standY - 1][standX + 4]:
            x -= speed
    # Green tank go Down
    elif keys[pygame.K_s] and walls[standY + countSteps][standX + 1] and walls[standY + countSteps][standX + 2] and walls[standY + countSteps][standX + 3]:
        y += speed
        tankImage = pygame.image.load("img/tankDown.png")
        directionShoot = int(2)
        if not walls[standY + countSteps][standX]:
            x += speed
        elif not walls[standY + countSteps][standX + 4]:
            x -= speed
    # Green tank Shoot
    if keys[pygame.K_SPACE]:
        if len(shoots) < limitShoots:
            # Add shoot
            shoots.append([x + sizeForShootBullet, y + sizeForShootBullet, directionShoot])
            # Left
            if directionShoot == 3:
                xShoot = x - halfSizeFire
                yShoot = y + halfSizeBlock - halfSizeFire
            # Right
            elif directionShoot == 1:
                xShoot = x + sizeBlock - halfSizeFire
                yShoot = y + halfSizeBlock - halfSizeFire
            # Up
            elif directionShoot == 0:
                xShoot = x + halfSizeBlock - halfSizeFire
                yShoot = y - halfSizeFire
            # Down
            elif directionShoot == 2:
                xShoot = x + halfSizeBlock - halfSizeFire
                yShoot = y + sizeBlock - halfSizeFire
            # Show fire
            screen.blit(fireImage, (xShoot, yShoot))
    # Red tank go Left
    if keys[pygame.K_LEFT] and walls[standY2 + 1][standX2 - 1] and walls[standY2 + 2][
        standX2 - 1] and walls[standY2 + 3][standX2 - 1]:
        x2 -= speed
        tankEnemyImage = pygame.image.load("img/tankEnemyLeft.png")
        directionShoot2 = int(3)
        if not walls[standY2][standX2 - 1]:
            y2 += speed
        elif not walls[standY2 + 4][standX2 - 1]:
            y2 -= speed
    # Red tank go Right
    elif keys[pygame.K_RIGHT] and walls[standY2 + 1][standX2 + countSteps] and \
            walls[standY2 + 2][standX2 + countSteps] and walls[standY2 + 3][standX2 + countSteps]:
        x2 += speed
        tankEnemyImage = pygame.image.load("img/tankEnemyRight.png")
        directionShoot2 = int(1)
        if not walls[standY2][standX2 + countSteps]:
            y2 += speed
        elif not walls[standY2 + 4][standX2 + countSteps]:
            y2 -= speed
    # Red tank go Up
    elif keys[pygame.K_UP] and walls[standY2 - 1][standX2 + 1] and walls[standY2 - 1][
        standX2 + 2] and walls[standY2 - 1][standX2 + 3]:
        y2 -= speed
        tankEnemyImage = pygame.image.load("img/tankEnemyUp.png")
        directionShoot2 = int(0)
        if not walls[standY2 - 1][standX2]:
            x2 += speed
        elif not walls[standY2 - 1][standX2 + 4]:
            x2 -= speed
    # Red tank go Down
    elif keys[pygame.K_DOWN] and walls[standY2 + countSteps][standX2 + 1] and \
            walls[standY2 + countSteps][standX2 + 2] and walls[standY2 + countSteps][standX2 + 3]:
        y2 += speed
        tankEnemyImage = pygame.image.load("img/tankEnemyDown.png")
        directionShoot2 = int(2)
        if not walls[standY2 + countSteps][standX2]:
            x2 += speed
        elif not walls[standY2 + countSteps][standX2 + 4]:
            x2 -= speed
    # Red tank Shoot
    if keys[pygame.K_RSHIFT]:
        if len(shoots2) < limitShoots:
            # Add shoot
            shoots2.append([x2 + sizeForShootBullet, y2 + sizeForShootBullet, directionShoot2])
            # Left
            if directionShoot2 == 3:
                xShoot2 = x2 - halfSizeFire
                yShoot2 = y2 + halfSizeBlock - halfSizeFire
            # Right
            elif directionShoot2 == 1:
                xShoot2 = x2 + sizeBlock - halfSizeFire
                yShoot2 = y2 + halfSizeBlock - halfSizeFire
            # Up
            elif directionShoot2 == 0:
                xShoot2 = x2 + halfSizeBlock - halfSizeFire
                yShoot2 = y2 - halfSizeFire
            # Down
            elif directionShoot2 == 2:
                xShoot2 = x2 + halfSizeBlock - halfSizeFire
                yShoot2 = y2 + sizeBlock - halfSizeFire
            # Show fire
            screen.blit(fireImage, (xShoot2, yShoot2))


def generateRandomMap():
    for i in range(1, sizeY - 1):
        for j in range(1, sizeX - 1):
            map[i][j] = bool(random.randint(0, 3))
            if map[i][j]:
                for k in range(countSteps):
                    for l in range(countSteps):
                        walls[i * countSteps + k][j * countSteps + l] = True
            else:
                for k in range(countSteps):
                    for l in range(countSteps):
                        walls[i * countSteps + k][j * countSteps + l] = False
    map[1][1] = True
    map[12][26] = True
    for k in range(countSteps):
        for l in range(countSteps):
            walls[1 * countSteps + k][1 * countSteps + l] = True
    for k in range(countSteps):
        for l in range(countSteps):
            walls[12 * countSteps + k][26 * countSteps + l] = True


def resetPositionScore():
    global stop
    global scoreRed
    global scoreGreen
    global x
    global y
    global x2
    global y2

    stop = 0
    scoreRed = 0
    scoreGreen = 0
    x = int(sizeBlock)
    y = int(sizeBlock)
    x2 = int(displayX - twoSizeBlock)
    y2 = int(displayY - twoSizeBlock)


def showScore():
    greenScoreImage = pygame.image.load("img/{:}-.jpg".format(scoreGreen))
    redScoreImage = pygame.image.load("img/-{:}.jpg".format(scoreRed))
    screen.blit(greenScoreImage, (int(displayX - 5 * sizeBlock), int(0)))
    screen.blit(redScoreImage, (int(displayX - 2.5 * sizeBlock), int(0)))
    infoImage = pygame.image.load("img/info.jpg")
    screen.blit(infoImage, (0, 0))


pygame.init()
pygame.display.set_caption("@LGleba 'Tanks for 2-players'")
displayX = int(1400)
displayY = int(700)
sizeBlock = int(50)
halfSizeBlock = int(sizeBlock / 2)
twoSizeBlock = int(sizeBlock * 2)
sizeShoot = int(10)
sizeFire = int(25)
halfSizeFire = int(sizeFire / 2)
speedShoot = int(20)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([displayX, displayY])
running = True
wallImage = pygame.image.load("img/wall.jpg")
tankImage = pygame.image.load("img/tankUp.png")
tankEnemyImage = pygame.image.load("img/tankEnemyUp.png")
fireImage = pygame.image.load("img/fire.png")
groundImage = pygame.image.load("img/ground.jpg")
x = int(sizeBlock)
y = int(sizeBlock)
x2 = int(displayX - twoSizeBlock)
y2 = int(displayY - twoSizeBlock)
sizeBullet = int(20)
sizeForShootBullet = int((sizeBlock - sizeBullet) / 2)
stop = 0
speed = int(10)
directionShoot = int(0)
directionShoot2 = int(0)
shoots = []
shoots2 = []
limitShoots = int(7)
sizeX = int(28)
sizeY = int(14)
scoreGreen = int(0)
scoreRed = int(0)
map = [False] * sizeY
for i in range(sizeY):
    map[i] = [False] * sizeX

countSteps = int(5)

wallX = int(sizeX * countSteps)
wallY = int(sizeY * countSteps)

walls = [False] * wallY
for i in range(wallY):
    walls[i] = [False] * wallX


for i in range(1, sizeY - 1):
    for j in range(1, sizeX - 1):
        map[i][j] = bool(random.randint(0, 3))
        if map[i][j]:
            for k in range(countSteps):
                for l in range(countSteps):
                    walls[i * countSteps + k][j * countSteps + l] = True
map[1][1] = True
map[12][26] = True
for k in range(countSteps):
    for l in range(countSteps):
        walls[1 * countSteps + k][1 * countSteps + l] = True
for k in range(countSteps):
    for l in range(countSteps):
        walls[12 * countSteps + k][26 * countSteps + l] = True


while running:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    createMap()
    activeKeys()
    activeShoots()
    # Green WIN
    if stop == 1:
        imageWin = pygame.image.load("img/greenWin.jpg")
        screen.blit(imageWin, (0, 0))
        pygame.display.flip()
        pygame.time.delay(2000)
        # Reset positions and score
        resetPositionScore()
        # Generate random map
        generateRandomMap()
    # Red WIN
    elif stop == 2:
        imageWin = pygame.image.load("img/redWin.jpg")
        screen.blit(imageWin, (0, 0))
        pygame.display.flip()
        pygame.time.delay(2000)
        # Reset positions and score
        resetPositionScore()
        # Generate random map
        generateRandomMap()
    showScore()

    screen.blit(tankImage, (x, y))
    screen.blit(tankEnemyImage, (x2, y2))

    pygame.display.flip()

pygame.quit()
