import pygame
import time 
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pringle Clicker")

# Font
pygame.font.init()
font = pygame.font.Font("times new roman.ttf", 36)

#Initiate Clock
clock = pygame.time.Clock()

# Initializing Pringle Count and Auto Pringle Upgrade Counter
pringle_count = 0
text_color = (255, 0, 0)
text_color = (255, 255, 255)
auto_pringle = 0

# Background Image
BG_original = pygame.image.load("spacebg.jpg")
BG = pygame.transform.scale(BG_original, (WIDTH, HEIGHT))

# Centers Images and Buttons when resizing window
def setGet(screenSize):
    global WIDTH, HEIGHT, BG
    WIDTH, HEIGHT = screenSize
    BG = pygame.transform.scale(BG_original, (WIDTH, HEIGHT))

def draw():
    WIN.blit(BG, (0, 0))
    # Draw the Pringle Count
    pringle_label = font.render(f"Pringles: {int(pringle_count)}", True, text_color)
    WIN.blit(pringle_label, (20, 20))

# Setting Up Main Button for Pringles
class Button:
    def __init__(self, x, y, width, height, text, image=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (255, 255, 255)  # Normal color
        self.hover_color = (200, 200, 200)  # Color when hovered
        self.hover_width = (width + 20)
        self.hover_height = (height + 20)
        self.click_width = (width + 10)
        self.click_height = (height + 10)
        self.font = pygame.font.Font("times new roman.ttf", 36)
        self.original_image = None
        if image:
            self.original_image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))
        self.update_position(x, y)
        self.tick = 0

    def change_tick(self, tick):
        self.tick = tick

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x - (self.width // 2), y - (self.height // 2), self.width, self.height)

    def draw(self, surface):
        # Change size on Hover
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and self.tick == 0:
            self.change_size(self.hover_width, self.hover_height)
        elif self.rect.collidepoint(mouse_pos) and self.tick > 0:
            self.change_size(self.click_width, self.click_height)
            self.tick -= 1
        else:
            self.change_size(self.width, self.height)
        
        # Draw the button background (white for auto button or image if available)
        if self.original_image:
            surface.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        # Draw the text on top of the button
        text_surface = self.font.render(self.text, True, (60, 0, 150))  # Using black text for contrast on white
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def change_size(self, width, height):
        # Keep the button centered while changing size
        center = self.rect.center
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center
        if self.original_image:
            self.image = pygame.transform.scale(self.original_image, (self.rect.width, self.rect.height))

# Define a custom event for auto pringle increment every 2 seconds
AUTO_PRINGLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(AUTO_PRINGLE_EVENT, 1000)

def main():
    global pringle_count, auto_pringle
    run = True

    # Main pringle click button at center of screen
    click_button = Button(WIDTH // 2, HEIGHT // 2, 200, 150, "Click For Pringle", "Pringle.png")
    # Auto pringle upgrade button, placed on the side (adjust x,y as desired)
    autobutton = Button(850, HEIGHT // 2, 200, 150, "AutoClicker (10 pringles)", "pringle_can.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.VIDEORESIZE:
                setGet(event.size)
                click_button.update_position(WIDTH // 2, HEIGHT // 2)
                autobutton.update_position((WIDTH - 150), HEIGHT // 2)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if main click button was clicked
                if click_button.rect.collidepoint(event.pos):
                    pringle_count += 1
                    click_button.change_tick(5)

                # Check if auto upgrade button was clicked
                if autobutton.rect.collidepoint(event.pos):
                    autobutton.change_tick(5)
                    if pringle_count >= 10:
                        auto_pringle += 1
                        pringle_count -= 10

            # Handle the auto pringle event triggered every 2 seconds
            if event.type == AUTO_PRINGLE_EVENT:
                pringle_count += auto_pringle

        draw()
        click_button.draw(WIN)
        autobutton.draw(WIN)
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
