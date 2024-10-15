import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
infoObject = pygame.display.Info()

SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h
FPS = 10
room = 1

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
background_image4 = pygame.image.load('Room4.png')
background_image4 = pygame.transform.scale(background_image4, (SCREEN_WIDTH, SCREEN_HEIGHT))
#scale the image to 100x100
right_arrow_image = pygame.image.load('arrow.png')
right_arrow_image = pygame.transform.scale(right_arrow_image, (100, 100))
left_arrow_image = pygame.transform.flip(right_arrow_image, True, False)

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
        # Add logic for what happens when interactable is clicked
        pass

    def is_clicked(self, position):
        x, y = position
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

class Arrow(Interactable):
    def __init__(self, x, y, width, height, image, name="Interactable", direction="left"):
        super().__init__(x, y, width, height, image, name)
        self.direction = direction

    def click_effect(self):
        global room
        # Add logic for what happens when interactable is clicked
        if self.direction == "left":
            if room == 2 or 3 or 4:
                room -= 1
            else:
                pass
        elif self.direction == "right":
            if room == 4:
                room = 1
            elif room == 1 or 2 or 3:
                room += 1
            else:
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
        # Add logic to handle clicks here
        for interactable in interactables:
            if interactable.is_clicked(position):
                interactable.click_effect()

# Game loop
def game_loop():
    left_arrow = Arrow(100, SCREEN_HEIGHT/2-50, 100, 100, left_arrow_image, "Left Arrow", "left")
    right_arrow = Arrow(SCREEN_WIDTH-200, SCREEN_HEIGHT/2-50, 100, 100, right_arrow_image, "Right Arrow", "right")
    dining_room1 = Room(background_image1, [])
    living_room1 = Room(background_image2, [])
    bedroom1 = Room(background_image3, [])
    attic1 = Room(background_image4, [])
    dining_room1.interactables.append(left_arrow)
    dining_room1.interactables.append(right_arrow)
    living_room1.interactables.append(right_arrow)
    bedroom1.interactables.append(left_arrow)
    bedroom1.interactables.append(right_arrow)
    attic1.interactables.append(left_arrow)
    attic1.interactables.append(right_arrow)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if room == 2:
                    dining_room1.handle_click(dining_room1.interactables, event.pos)
                elif room == 1:
                    living_room1.handle_click(living_room1.interactables, event.pos)
                elif room == 3:
                    bedroom1.handle_click(bedroom1.interactables, event.pos)
                elif room == 4:
                    attic1.handle_click(attic1.interactables, event.pos)

        # Draw everything
        screen.fill(WHITE)
        if room == 2:
            dining_room1.draw()
        elif room == 1:
            living_room1.draw()
        elif room == 3:
            bedroom1.draw()
        elif room == 4:
            attic1.draw()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)
    
if __name__ == "__main__":
    game_loop()