import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
infoObject = pygame.display.Info()

SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h
FPS = 24
room = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point and Click Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load images
background_image1 = pygame.image.load('Room1.png')
background_image1 = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image2 = pygame.image.load('Room2.jpg')
background_image2 = pygame.transform.scale(background_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image3 = pygame.image.load('Room3.png')
background_image3 = pygame.transform.scale(background_image3, (SCREEN_WIDTH, SCREEN_HEIGHT))
#scale the image to 100x100
left_arrow_image = pygame.image.load('left_arrow.png')
left_arrow_image = pygame.transform.scale(left_arrow_image, (100, 100))
right_arrow_image = pygame.transform.flip(left_arrow_image, True, False)

class Interactable:
    def __init__(self, x, y, width, height, image, name="Interactable"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.name = name

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
    def click_effect(self):
        print(self.name + " was clicked!")
        # Add logic for what happens when interactable is clicked

    def is_clicked(self, position):
        x, y = position
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

class Arrow(Interactable):
    def __init__(self, x, y, width, height, image, name="Interactable", direction="left"):
        super().__init__(x, y, width, height, image, name)
        self.direction = direction

    def click_effect(self):
        global room
        print(self.name + " was clicked!")
        # Add logic for what happens when interactable is clicked
        if self.direction == "left":
            if room == 2 or 3:
                print("jabba1")
                room -= 1
            else:
                print("jabba2")
                pass
        elif self.direction == "right":
            if room == 1 or 2:
                print("jabba3")
                room += 1
            else:
                print("jabba4") 
                pass

class Room:
    def __init__(self, background_image, interactables):
        self.background_image = background_image
        self.interactables = interactables

    def draw(self):
        screen.blit(self.background_image, (0, 0))
        for interactable in self.interactables:
            interactable.draw()

    def handle_click(self, interactables, position):
        x, y = position
        print(f"Clicked at position: {x}, {y}")
        # Add logic to handle clicks here
        for interactable in interactables:
            if interactable.is_clicked(position):
                interactable.click_effect()

# Game loop
def game_loop():
    left_arrow = Arrow(100, SCREEN_HEIGHT/2-50, 100, 100, left_arrow_image, "Left Arrow", "left")
    right_arrow = Arrow(SCREEN_WIDTH-200, SCREEN_HEIGHT/2-50, 100, 100, right_arrow_image, "Right Arrow", "right")
    main_room1 = Room(background_image1, [])
    left_room1 = Room(background_image2, [])
    right_room1 = Room(background_image3, [])
    main_room1.interactables.append(left_arrow)
    main_room1.interactables.append(right_arrow)
    left_room1.interactables.append(right_arrow)
    right_room1.interactables.append(left_arrow)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if room == 2:
                    main_room1.handle_click(main_room1.interactables, event.pos)
                elif room == 1:
                    left_room1.handle_click(left_room1.interactables, event.pos)
                elif room == 3:
                    right_room1.handle_click(right_room1.interactables, event.pos)

        # Draw everything
        screen.fill(WHITE)
        if room == 2:
            main_room1.draw()
        elif room == 1:
            left_room1.draw()
        elif room == 3:
            right_room1.draw()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)
    
if __name__ == "__main__":
    game_loop()