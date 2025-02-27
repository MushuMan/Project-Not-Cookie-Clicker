import pygame
import time 
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not Cookie Clicker")

# Font
# Font path needs to be defined
pygame.font.init()
font = pygame.font.Font("times new roman.ttf", 36)

BG = pygame.transform.scale(pygame.image.load("spacebg.jpg"), (WIDTH, HEIGHT))

# Intalizing Cookie Count
cookie_count = 0



# Function to handle cookie clicks
def click_cookie():
    global cookie_count
    cookie_count =+ 1

text_color =(255, 255, 255)

def draw():
    WIN.blit(BG, (0, 0))
    # Draw the Cookie Count
    cookie_label = font.render(f"Cookies: {int(cookie_count)}", True, text_color)
    WIN.blit(cookie_label, (20,20))
    pygame.display.update()

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()