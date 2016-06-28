import pygame
import sys
import time

pygame.init()

size = width, height = 800, 600

backgroundcolor = (10, 200, 10)

screen = pygame.display.set_mode(size)

isRunning = True

speed = [0,0]
speed2 = [0,0]
speedball = [0,0]

ball = pygame.image.load("Soccer Ball.png")
ball = pygame.transform.scale(ball, (50, 50))
player1 = pygame.image.load("Red Player.png")
player1 = pygame.transform.scale(player1, (200, 200))
player2 = pygame.image.load("Blue Player.png")
player2 = pygame.transform.scale(player2, (200, 200))
goal1 = pygame.image.load("Goal.png")
goal1 = pygame.transform.scale(goal1, (200, 200))
goal2 = pygame.image.load("Goal.png")
goal2 = pygame.transform.scale(goal2, (200, 200))
ballrect = ball.get_rect()
player1rect = player1.get_rect()
player2rect = player2.get_rect()
goal1rect = goal1.get_rect()
goal2rect = goal2.get_rect()

goal1rect.move_ip(100, 300)
goal2rect.move_ip(700, 300)

lasttime = 0
lasttime2  = 0

while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			print event.key 
			if event.key == pygame.K_UP:
				speed[1] = -1
			elif event.key == pygame.K_DOWN:
				speed[1] = 1
			elif event.key == pygame.K_LEFT:
				speed[0] = -1
			elif event.key == pygame.K_RIGHT:
				speed[0] = 1
			elif event.key == pygame.K_w:
				speed[1] = -1
			elif event.key == pygame.K_s:
				speed2[1] = 1
			elif event.key == pygame.K_a:
				speed[0] = -1
			elif event.key == pygame.K_d:
				speed[0] = 1
	if (pygame.time.get_ticks() - lasttime > 15):
		ballrect = ballrect.move(speedball)
		lasttime = pygame.time.get_ticks() 

	if (pygame.time.get_ticks() - lasttime2 > 15):
		player1rect = player1rect.move(speed)
		player2rect = player2rect.move(speed2)
		lasttime2 = pygame.time.get_ticks()

	if ballrect.left < 0 or ballrect.right > width:
			speedball[0] = -speedball[0]*2
	if ballrect.top < 0 or ballrect.bottom > height:
		speedball[1]=-speedball[1]*2
		
	if player1rect.left < 0 or player1rect.right > width:
			speed[0] = -speed[0]
	if player1rect.top < 0 or player1rect.bottom > height:
		speed[1]=-speed[1]

	if player2rect.left < 0 or player2rect.right > width:
			speed2[0] = -speed2[0]
	if player2rect.top < 0 or player2rect.bottom > height:
		speed2[1]=-speed2[1]


	if player1rect.colliderect(ballrect):
		speedball[0] = -1
		speedball[1] = -1 * speedball[1]
	if player2rect.colliderect(ballrect):
		speedball[0] = 1
		speedball[1] = -1 * speedball[1]

	if ballrect.colliderect(goal1rect):
		isRunning = False
	if ballrect.colliderect(goal2rect):
		isRunning = False
		
	screen.fill(backgroundcolor)
	screen.blit(ball,ballrect)
	screen.blit(player1,player1rect)
	screen.blit(ball,ballrect)
	screen.blit(player2,player2rect)	
	pygame.display.flip()

