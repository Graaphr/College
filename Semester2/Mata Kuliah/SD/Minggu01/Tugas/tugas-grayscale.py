import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GRAYSCALE")

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(220,220,220)

font=pygame.font.Font(None,28)
title_font=pygame.font.Font(None,40)

# Fungsi Grayscale
def toGray(R,G,B):

    grayscale = (0.3*R)+(0.59*G)+(0.11*B)

    return int(grayscale)

def rgb_to_hex(R,G,B):

    return '#{:02X}{:02X}{:02X}'.format(R,G,B)


# ======================
# Color Picker
# ======================

picker = pygame.Surface((256,256))

for x in range(256):
    for y in range(256):

        picker.set_at((x,y),(x,y,150))


picker_x=50
picker_y=120

circle_x=picker_x
circle_y=picker_y

dragging=False


selected_color=(255,0,0)
gray_value=0


running=True

while running:

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False


        if event.type==pygame.MOUSEBUTTONDOWN:

            mx,my=event.pos

            if picker_x<=mx<=picker_x+256 and picker_y<=my<=picker_y+256:

                dragging=True


        if event.type==pygame.MOUSEBUTTONUP:

            dragging=False


        if event.type==pygame.MOUSEMOTION and dragging:

            mx,my=event.pos

            mx=max(picker_x,min(mx,picker_x+255))
            my=max(picker_y,min(my,picker_y+255))

            circle_x=mx
            circle_y=my

            px=mx-picker_x
            py=my-picker_y

            selected_color=picker.get_at((px,py))

            R,G,B=selected_color[:3]

            gray_value=toGray(R,G,B)


    R,G,B=selected_color[:3]

    hex_color=rgb_to_hex(R,G,B)


    # Judul Atas
    title=title_font.render("COLOR to GRAYSCALE",True,BLACK)
    screen.blit(title,(250,30))



    screen.blit(picker,(picker_x,picker_y))

    screen.blit(font.render("Palet Warna",True,BLACK),(120,90))



    pygame.draw.circle(screen,BLACK,(circle_x,circle_y),8,2)



    pygame.draw.rect(screen,GRAY,(50,400,255,40))
    pygame.draw.rect(screen,BLACK,(50,400,255,40),2)

    rgb_text=f"RGB : {R}, {G}, {B}"

    screen.blit(font.render(rgb_text,True,BLACK),(70,410))



    pygame.draw.rect(screen,GRAY,(50,460,255,40))
    pygame.draw.rect(screen,BLACK,(50,460,255,40),2)

    hex_text=f"HEX : {hex_color}"

    screen.blit(font.render(hex_text,True,BLACK),(70,470))



    pygame.draw.rect(screen,selected_color,(400,120,350,150))

    screen.blit(font.render("Warna Asli",True,BLACK),(520,90))


    # Hasil

    gray_color=(gray_value,gray_value,gray_value)

    pygame.draw.rect(screen,gray_color,(400,330,350,150))

    screen.blit(font.render("Grayscale",True,BLACK),(520,300))


    # Hasil

    text=font.render("Gray = "+str(gray_value),True,BLACK)

    screen.blit(text,(530,490))


    pygame.display.flip()


pygame.quit()
sys.exit()