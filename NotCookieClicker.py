import pygame
import time 
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not Cookie Clicker")

# Font
pygame.font.init()
font = pygame.font.Font("times new roman.ttf", 36)

BG = pygame.transform.scale(pygame.image.load("spacebg.jpg"), (WIDTH, HEIGHT))

# Initializing Cookie Count
cookie_count = 0
text_color = (255, 255, 255)

def draw():
    WIN.blit(BG, (0, 0))
    # Draw the Cookie Count
    cookie_label = font.render(f"Cookies: {int(cookie_count)}", True, text_color)
    WIN.blit(cookie_label, (20, 20))

# Setting Up Main Button for Cookies
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (0, 255, 0)  # Normal color
        self.hover_color = (0, 200, 0)  # Color when hovered
        self.font = pygame.font.Font("times new roman.ttf", 36)

    def draw(self, surface):
        # Change Color on Hover
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)  # Draw hover color
        else:
            pygame.draw.rect(surface, self.color, self.rect)  # Draw normal color

        # Draw the text on top of the button
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self):
        mouse_click = pygame.mouse.get_pressed()
        return mouse_click[0] and self.rect.collidepoint(pygame.mouse.get_pos())

def main():
    run = True

    button = Button(400, 350, 200, 150, "Click For Cookie")  # Adjusted button position and size

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
       # Check for mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):  # Check if the button was clicked
                    global cookie_count  # Use global to modify the cookie_count variable
                    cookie_count += 1
        
        draw()
        button.draw(WIN)  # Draw the button on the main window
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
