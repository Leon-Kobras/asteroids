import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import AsteroidField
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)
playee = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
elayee = AsteroidField()
clock2 = pygame.time.Clock()
dt = 0
while True:
    dt =  clock2.tick(60) / 1000
    log_state()
    clock2.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill('black')
    updatable.update(dt)
    playee.timer -= dt
    for aster in asteroids:
        if playee.collides_with(aster):
            log_event('player_hit')
            print('Game over!')
            sys.exit()
        for shot in shots:
            if shot.collides_with(aster):
                log_event('asteroid_shot')
                shot.kill()
                aster.split()
    for drawa in drawable:
        drawa.draw(screen)
    pygame.display.flip(), clock2.tick(60)
def main():
    print('Starting Asteroids with pygame version: 2.6.1')
    print('Screen width: 1280')
    print('Screen height: 720')
    print(dt)
if __name__ == '__main__':
    main()
