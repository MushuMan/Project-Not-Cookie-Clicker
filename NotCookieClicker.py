import pygame
import time 
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not Cookie Clicker")

# Font
# Font path needs to be defined
font_path = 
font = pygame.font.Font(None, 36)

BG = pygame.transform.scale(pygame.image.load("spacebg.jpg"), (WIDTH, HEIGHT))

# Intalizing Cookie Count
cookie_count = 0

# Function to handle cookie clicks
def click_cookie():
    global cookie_count
    cookie_count =+ 1


# Draw the Cookie Count
cookie_label = font.render(f"Cookies: {int(cookie_count)}", True, BLACK)
WIN.blit(cookie_label, (20,20))


def draw():
    WIN.blit(BG, (0, 0))
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