import pygame
import time
import random

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not Cookie Clicker")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
pygame.font.init()
font = pygame.font.Font("times new roman.ttf", 36)

BG = pygame.transform.scale(pygame.image.load("spacebg.jpg"), (WIDTH, HEIGHT))

# Load images
pringle_img = pygame.image.load("Pringle.png")  # Ensure you have a "Pringle.png" file
pringle_img = pygame.transform.scale(pringle_img, (100, 100))

# Initializing Pringle Count and other variables
pringle_count = 0
auto_clickers = 0
grandmas = 0
text_color = (255, 255, 255)

def draw():
    WIN.blit(BG, (0, 0))
    # Draw the Pringle Count
    pringle_label = font.render(f"Pringles: {int(pringle_count)}", True, text_color)
    WIN.blit(pringle_label, (20, 20))

    # Draw the Auto Clickers and Grandmas Count
    auto_clicker_label = font.render(f"Auto Clickers: {int(auto_clickers)}", True, text_color)
    WIN.blit(auto_clicker_label, (20, 50))
    grandma_label = font.render(f"Grandmas: {int(grandmas)}", True, text_color)
    WIN.blit(grandma_label, (20, 80))

    # Draw the pringle image
    WIN.blit(pringle_img, (450, 300))

# Setting Up Main Button for Pringles
class Button:
    def __init__(self, x, y, width, height, text, image=None, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (0, 255, 0)  # Normal color
        self.hover_color = (0, 200, 0)  # Color when hovered
        self.font = pygame.font.Font("times new roman.ttf", 36)
        self.action = action
        if image:
            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        else:
            self.image = None

    def draw(self, surface):
        # Change Color on Hover
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)  # Draw hover color
        else:
            pygame.draw.rect(surface, self.color, self.rect)  # Draw normal color

        # Draw the image if available
        if self.image:
            surface.blit(self.image, self.rect.topleft)
        else:
            # Draw the text on top of the button
            text_surface = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def is_clicked(self):
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.action:
                self.action()
            return True
        return False

def click_pringle():
    global pringle_count
    pringle_count += 1

def buy_auto_clicker():
    global pringle_count, auto_clickers
    if pringle_count >= 10:
        pringle_count -= 10
        auto_clickers += 1

def buy_grandma():
    global pringle_count, grandmas
    if pringle_count >= 1000:
        pringle_count -= 1000
        grandmas += 1

def update_pringles():
    global pringle_count
    pringle_count += auto_clickers + (grandmas * 10)

def main():
    global pringle_count
    run = True

    pringle_button = Button(450, 300, 100, 100, "", "Pringle.png", click_pringle)  # Pringle button with image
    auto_clicker_button = Button(200, 250, 200, 40, "Buy Auto Clicker (10 pringles)", action=buy_auto_clicker)
    grandma_button = Button(200, 300, 200, 40, "Buy Grandma (1000 pringles)", action=buy_grandma)

    last_update = time.time()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            # Check for mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pringle_button.is_clicked()
                auto_clicker_button.is_clicked()
                grandma_button.is_clicked()

        # Update pringles every second
        if time.time() - last_update >= 1:
            update_pringles()
            last_update = time.time()

        draw()
        pringle_button.draw(WIN)
        auto_clicker_button.draw(WIN)
        grandma_button.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
