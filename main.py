import pygame
from random import randint
from time import time

pygame.init()
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pic = pygame.image.load("background.png")
window.blit(pygame.transform.scale(pic, (800, 800)), (0, 0))
pygame.display.flip()

class Area():
    def __init__(self, x, y, width, height, fill_color, border_color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = fill_color
        self.border_color = border_color
        self.text = text

    def draw(self):
        pygame.draw.rect(window, self.fill_color, self.rect) # Fill color
        pygame.draw.rect(window, self.border_color, self.rect, 7) # Draw border
        # Create font
        txt_font = pygame.font.Font(None, 25)
        text = txt_font.render(self.text, True, (0, 0, 0))
        window.blit(text, (self.rect.x + 15, self.rect.y + 20))

class GameSprite():
    def __init__(self, x, y, width, height, img):
        self.img = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.img.get_rect() # get the rectangle area by the img
        # the rect is important -> collision handling
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.rect.x > 0:
                self.rect.x -= 4
        if keys[pygame.K_d]:
            if self.rect.x < 800 - self.rect.width:
                self.rect.x += 4
        if keys[pygame.K_s]:
            if self.rect.y < 800 - self.rect.height:
                self.rect.y += 4
        if keys[pygame.K_w]:
            if self.rect.y > 0:
                self.rect.y -= 4

pointer = Area(700, 0, 100, 150, (64, 204, 252), (64, 204, 252), 'Score: 0')

timer_label = Area(10, 0, 100, 150, (64, 204, 252), (64, 204, 252), 'Time: 0')

result = Area(280, 350, 0, 0, (64, 204, 252), (64, 204, 252), '')

fox = GameSprite(50, 0, 50, 50, "fox.png")
coin = GameSprite(50, 100, 50, 50, "coin.png")

bombs = list()
bomb = GameSprite(50, 100, 80, 80, "bomb.png")
bomb1 = GameSprite(50, 100, 80, 80, "bomb.png")
bomb2 = GameSprite(50, 100, 80, 80, "bomb.png")
bombs.append(bomb)
bombs.append(bomb1)
bombs.append(bomb2)

begin_timestamp = 0
end_timestamp = 0
timer = 60

timeout = 0

score = 0


# if score == 100:
# window.fill((0, 255, 0))



while True:
    timer -= end_timestamp - begin_timestamp
    timer_label.text = 'Timer: ' + str(int(timer))

    begin_timestamp = pygame.time.get_ticks() / 1000
    if timeout == -5:
        coin_posx = randint(0, 750)
        coin_posy = randint(0, 750)
        coin.rect.x = coin_posx
        coin.rect.y = coin_posy
        for bomb in bombs:
            bomb_posx = randint(0, 750)
            bomb_posy = randint(0, 750)
            bomb.rect.x = bomb_posx
            bomb.rect.y = bomb_posy
        
        timeout = 175
    else:
        timeout -= 1
    
    # collide = pygame.Rect.colliderect(fox, coin, bomb)
    if pygame.Rect.colliderect(fox.rect, coin.rect):
        score += 10
        pointer.text = "Score: " + str(score)
        timeout = -5

    for bomb in bombs:
        if pygame.Rect.colliderect(fox.rect, bomb.rect):
            score -= 20
            pointer.text = "Score: " + str(score)
            timeout = -5

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    # Move
    fox.move()

    # Draw
    # window.fill((0, 255, 0))
    if timer > 0 and score < 100: # and timer .....
        window.blit(pygame.transform.scale(pic, (800, 800)), (0, 0))
        pointer.draw()
        timer_label.draw()
        fox.draw()
        coin.draw()
        for bomb in bombs:
            bomb.draw()
    else:
        if score >= 100:
            window.fill((0, 255, 0))
            result.text = 'WIN! Your score is ' + str(score)
        elif score < -50:
            window.fill((255, 0, 0))
            result.text = 'LOSE! Your score is ' + str(score)
        else:
            window.fill((255, 255, 51))
            result.text = 'KEEP TRYING! Your score is ' + str(score)
        result.draw()
    
    end_timestamp = pygame.time.get_ticks() / 998.8
    pygame.display.update()
    clock.tick(40)





















# Class without set method: 2
# No inheritance: 0
# Gameplay: 1.5
# Advanced functions: 1
# Decoration: 0.5
# 5