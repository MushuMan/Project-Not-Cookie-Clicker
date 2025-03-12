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
pringle_count = 0
text_color = (255, 255, 255)

def draw():
    WIN.blit(BG, (0, 0))
    # Draw the Cookie Count
    cookie_label = font.render(f"Pringles: {int(pringle_count)}", True, text_color)
    WIN.blit(cookie_label, (20, 20))

# Setting Up Main Button for Pringles
class Button:
    def __init__(self, x, y, width, height, text, image=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (0, 255, 0)  # Normal color
        self.hover_color = (100, 200, 0)  # Color when hovered
        self.hover_width = (width + 20)
        self.hover_height = (height + 20)
        self.font = pygame.font.Font("times new roman.ttf", 36)
        self.original_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))

    def draw(self, surface):
        # Change Color on Hover
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.change_size(self.hover_width, self.hover_height)
            # pygame.draw.rect(surface, self.hover_color, self.rect)  # Draw hover color
        else:
            self.change_size(self.width, self.height)
            # pygame.draw.rect(surface, self.color, self.rect)  # Draw normal color

        if hasattr(self, "image"):
            surface.blit(self.image, self.rect.topleft)

        # Draw the text on top of the button
        text_surface = self.font.render(self.text, True, (255, 255, 255)) 
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def change_size(self, width, height):
        self.rect = pygame.Rect((self.x - (width // 2)), (self.y - (height // 2)), width, height)
        self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))

def main():
    run = True

    button = Button((WIDTH // 2), (HEIGHT // 2), 200, 150, "Click For Pringle", "Pringle.png")  # Adjusted button position and size

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
       # Check for mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):  # Check if the button was clicked
                    global pringle_count  # Use global to modify the pringle_count variable
                    pringle_count += 1
        
        draw()
        button.draw(WIN)  # Draw the button on the main window
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
