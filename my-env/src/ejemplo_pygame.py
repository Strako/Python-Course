import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Brick Breaker")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Paleta
palette_width = 100
palette_height = 10
palette_x = (screen_width - palette_width) // 2
palette_y = screen_height - palette_height - 20
palette_speed = 10

# Pelota
ball_radius = 10
ball_x = screen_width // 2
ball_y = palette_y - ball_radius - 1
ball_speed_x = 5
ball_speed_y = -5

# Ladrillos
brick_width = 81
brick_height = 20
num_bricks_rows = 10
num_bricks_cols = 9
brick_spacing = 10
bricks = []

for row in range(num_bricks_rows):
    brick_row = []
    for col in range(num_bricks_cols):
        brick_x = col * (brick_width + brick_spacing)
        brick_y = row * (brick_height + brick_spacing) + 50
        brick_row.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))
    bricks.append(brick_row)

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# Función para mostrar un mensaje en pantalla
def show_message(message, color, y_offset=0):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
    screen.blit(text, text_rect)

# Bucle principal del juego
game_over = False
victory = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and palette_x > 0:
        palette_x -= palette_speed
    if keys[pygame.K_RIGHT] and palette_x < screen_width - palette_width:
        palette_x += palette_speed
    
    if game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            victory = False
            palette_x = (screen_width - palette_width) // 2
            ball_x = screen_width // 2
            ball_y = palette_y - ball_radius - 1
            ball_speed_x = 5
            ball_speed_y = -5
            bricks = []
            for row in range(num_bricks_rows):
                brick_row = []
                for col in range(num_bricks_cols):
                    brick_x = col * (brick_width + brick_spacing)
                    brick_y = row * (brick_height + brick_spacing) + 50
                    brick_row.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))
                bricks.append(brick_row)
    
    else:
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Rebote de la pelota en los bordes
        if ball_x <= 0 or ball_x >= screen_width:
            ball_speed_x = -ball_speed_x
        if ball_y <= 0:
            ball_speed_y = -ball_speed_y
        
        # Rebote de la pelota en la paleta
        if ball_y >= palette_y - ball_radius and ball_x >= palette_x and ball_x <= palette_x + palette_width:
            ball_speed_y = -ball_speed_y
        
        # Colisión con los ladrillos
        for row in bricks:
            for brick in row:
                if brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
                    row.remove(brick)
                    ball_speed_y = -ball_speed_y
                    print(len(bricks))
                    if len(bricks) == 1:
                        victory = True
                    break
        
        screen.fill(white)
        pygame.draw.rect(screen, blue, (palette_x, palette_y, palette_width, palette_height))
        pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
        for row in bricks:
            for brick in row:
                pygame.draw.rect(screen, blue, brick)
        
        if victory:
            show_message("¡Ganaste! Presiona R para volver a jugar.", green)
            game_over = True
        elif ball_y > screen_height:
            show_message("¡Perdiste! Presiona R para reintentar.", red, -50)
            game_over = True
        
        pygame.display.update()
    
    clock.tick(60)

pygame.quit()