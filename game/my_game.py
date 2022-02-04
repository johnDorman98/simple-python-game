# This code will be for my first python game using the pygame module.

# Imports for pygame and random modules needed for the game to work.
import random
import pygame

# Initialize the pygame modules
pygame.init()

# Setting the screen width and height and giving the screen the specified
# width and height.
screen_width = 1280
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# This create the player and enemy's using images found inside the same folder.
player = pygame.image.load('player.jpg')

enemy1 = pygame.image.load('monster.jpg')
enemy2 = pygame.image.load('monster.jpg')
enemy3 = pygame.image.load('monster.jpg')

prize = pygame.image.load('prize.jpg')

# Gets the width and height of the images for the player and enemies
# in order to do boundary detection.
player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Create variables to store the position of the player and enemies that can be
# changed later.
player_x_position = 100
player_y_position = 50

enemy1_x_position = screen_width
enemy1_y_position = screen_height - enemy1_height

enemy2_x_position = screen_width + enemy2_width
enemy2_y_position = screen_height - (enemy2_height * 2)

enemy3_x_position = screen_width + enemy3_width
enemy3_y_position = screen_height - (enemy2_height * 3)

prize_x_position = 900
prize_y_position = random.randint(0, screen_height - prize_height)

# This is used to check if keys are pressed up or down.
# They will start off as False for now to be updated later as they are pressed.
key_up = False
key_down = False
key_left = False
key_right = False

# This starts the game loop.
# It refresh/update the screen window and apply changes to represent
# real time game play.
while 1:
    # This renders the player and enemies on the screen.
    screen.fill(0)
    screen.blit(player, (player_x_position, player_y_position))
    screen.blit(enemy1, (enemy1_x_position, enemy1_y_position))
    screen.blit(enemy2, (enemy2_x_position, enemy2_y_position))
    screen.blit(enemy3, (enemy3_x_position, enemy3_y_position))
    screen.blit(prize, (prize_x_position, prize_y_position))

    # This updates the screen.
    pygame.display.flip()

    # For loop to loop through the game events.
    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so
        # it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:
            
            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP:
                key_up = True
            if event.key == pygame.K_DOWN:
                key_down = True
            if event.key == pygame.K_LEFT:
                key_left = True
            if event.key == pygame.K_RIGHT:
                key_right = True

        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:
            
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                key_up = False
            if event.key == pygame.K_DOWN:
                key_down = False
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_RIGHT:
                key_right = False
    
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    if key_up == True:
        if player_y_position > 0:
            player_y_position -= 1

    if key_down == True:
        if player_y_position < screen_height - player_height:
            player_y_position += 1

    if key_left == True:
        if player_x_position > 0:
            player_x_position -= 1

    if key_right == True:
        if player_x_position < screen_width - player_width:
            player_x_position += 1

    # Check for collision of the enemies with the player.
    # Boundary box for the player
    player_box = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position.
    player_box.top = player_y_position
    player_box.left = player_x_position

    # Boundary box for each of the enemies.
    enemy1_box = pygame.Rect(enemy1.get_rect())
    enemy2_box = pygame.Rect(enemy2.get_rect())
    enemy3_box = pygame.Rect(enemy3.get_rect())

    enemy1_box.top = enemy1_y_position
    enemy1_box.left = enemy1_x_position

    enemy2_box.top = enemy2_y_position
    enemy2_box.left = enemy2_x_position

    enemy3_box.top = enemy3_y_position
    enemy3_box.left = enemy3_x_position

    # Boundary box for the prize
    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = prize_y_position
    prize_box.left = prize_x_position

    # Test for collision between player and enemies and prize.
    if player_box.colliderect(enemy1_box):
        print("You lose you were caught by an enemy.")
        pygame.quit()
        exit(0)

    elif player_box.colliderect(enemy2_box):
        print("You lose you were caught by an enemy.")
        pygame.quit()
        exit(0)

    elif player_box.colliderect(enemy3_box):
        print("You lose you were caught by an enemy.")
        pygame.quit()
        exit(0)

    # Checks if the enemies have gone past the screen and if so declaring the
    # player the winner.
    if enemy1_x_position < 0 - enemy1_width:
        print("You win one of the enemies left the game!")
        pygame.quit()        
        exit(0)

    elif enemy2_x_position < 0 - enemy2_width:
        print("You win one of the enemies left the game!")
        pygame.quit()        
        exit(0)

    elif enemy3_x_position < 0 - enemy3_width:
        print("You win one of the enemies left the game!")
        pygame.quit()        
        exit(0)

    # Checking for collision between player and prize.
    if player_box.colliderect(prize_box):
        print("You win you got the prize!")
        pygame.quit()        
        exit(0)

    # Makes the enemies approach the player.
    enemy1_x_position -= 0.15
    enemy2_x_position -= 0.10
    enemy3_x_position -= 0.20