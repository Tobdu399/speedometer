# NOTE: I know I know this code is pretty messy. This program was just
#       a side project because I got distracted

# USAGE: Use UP and DOWN arrow keys to accelerate or deaccelerate.
#        To accelerate faster, hold SPACE key down.

import pygame

WIDTH, HEIGHT = 400, 400

pygame.init()

process_interrupted = False
elapsed_time        = 0

display = pygame.display.set_mode((WIDTH, HEIGHT))
clock   = pygame.time.Clock()

pygame.display.set_caption("Speedometer")
pygame.display.set_icon(pygame.image.load("lib/images/icon.png"))

SPEED = 0  # KPH

speedometer = pygame.transform.scale(
    pygame.image.load("lib/images/speedometer.png").convert_alpha(),
    (WIDTH, HEIGHT)
)

speedometer_arrow = pygame.transform.scale(
    pygame.image.load("lib/images/speedometer_arrow.png").convert_alpha(),
    (WIDTH, HEIGHT)
)

digital_font = pygame.font.Font("lib/fonts/digital.ttf", 40)
pixel_font   = pygame.font.Font("lib/fonts/fixedsys.ttf", 15)

speedometer_rect = speedometer.get_rect(center=(WIDTH/2, HEIGHT/2))

while not process_interrupted:
    display.fill((50, 50, 50))

    rotated_speedometer_arrow = pygame.transform.rotate(speedometer_arrow, 120 + (SPEED * ((218/180) * -1))) # 120=0kph, -95=180kph
    speedometer_arrow_rect    = rotated_speedometer_arrow.get_rect(center=(WIDTH/2, HEIGHT/2))

    digital_speed        = digital_font.render(str(int(SPEED)), True, (255, 255, 255))
    info_text_firstline  = pixel_font.render("Use UP and DOWN arrow keys", True, (255, 255, 255))
    info_text_secondline = pixel_font.render("to accelerate or deaccelerate", True, (255, 255, 255))

    digital_speed_rect        = digital_speed.get_rect(center=(WIDTH/2, HEIGHT/3 + 15))
    info_text_firstline_rect  = info_text_firstline.get_rect(center=(WIDTH/2, HEIGHT - 45))
    info_text_secondline_rect = info_text_secondline.get_rect(center=(WIDTH/2, HEIGHT - 30))
    
    display.blit(digital_speed, digital_speed_rect)
    display.blit(info_text_firstline,  info_text_firstline_rect)
    display.blit(info_text_secondline, info_text_secondline_rect)

    display.blit(speedometer, speedometer_rect)
    display.blit(rotated_speedometer_arrow, speedometer_arrow_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_interrupted = True

    keys = pygame.key.get_pressed()

    acceleration_speed = 0.05
    if keys[pygame.K_SPACE]:
        acceleration_speed = 0.5

    if keys[pygame.K_UP]:
         SPEED += acceleration_speed * elapsed_time
    if keys[pygame.K_DOWN]:
        SPEED -= 1 * elapsed_time

    if SPEED > 180:
        SPEED = 180
    elif SPEED < 0:
        SPEED = 0

    elapsed_time = clock.tick(0) / 10
    pygame.display.flip()

pygame.quit()
