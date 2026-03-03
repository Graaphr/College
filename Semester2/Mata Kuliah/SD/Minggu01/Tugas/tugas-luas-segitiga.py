import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 650, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luas Segitiga")

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGRAY = (230,230,230)
GRAY = (180,180,180)
BLUE = (70,130,255)
GREEN = (120,200,120)

title_font = pygame.font.Font(None,50)
font = pygame.font.Font(None,32)

alas_box = pygame.Rect(200,120,200,40)
tinggi_box = pygame.Rect(200,180,200,40)

button = pygame.Rect(230,250,140,45)

hasil_box = pygame.Rect(150,330,350,80)

alas_text=""
tinggi_text=""

active_alas=False
active_tinggi=False

hasil="Belum dihitung"

running=True

while running:

    screen.fill(WHITE)

    pygame.draw.rect(screen,BLUE,(0,0,650,80))
    title=title_font.render("KALKULATOR LUAS SEGITIGA",True,WHITE)
    screen.blit(title,(70,25))

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:

            active_alas=alas_box.collidepoint(event.pos)
            active_tinggi=tinggi_box.collidepoint(event.pos)

            if button.collidepoint(event.pos):

                try:

                    alas=float(alas_text)
                    tinggi=float(tinggi_text)

                    luas=0.5*alas*tinggi

                    hasil=f"Luas Segitiga = {luas}"

                except:

                    hasil="Input harus angka!"

        if event.type==pygame.KEYDOWN:

            if active_alas:

                if event.key==pygame.K_BACKSPACE:
                    alas_text=alas_text[:-1]
                else:
                    alas_text+=event.unicode

            if active_tinggi:

                if event.key==pygame.K_BACKSPACE:
                    tinggi_text=tinggi_text[:-1]
                else:
                    tinggi_text+=event.unicode

    # Tulisan
    screen.blit(font.render("Alas",True,BLACK),(120,130))
    screen.blit(font.render("Tinggi",True,BLACK),(120,190))

    # Kotak Masukan
    pygame.draw.rect(screen,LIGHTGRAY,alas_box)
    pygame.draw.rect(screen,LIGHTGRAY,tinggi_box)

    pygame.draw.rect(screen,GRAY,alas_box,2)
    pygame.draw.rect(screen,GRAY,tinggi_box,2)

    # Teks Input
    screen.blit(font.render(alas_text,True,BLACK),(alas_box.x+10,alas_box.y+10))
    screen.blit(font.render(tinggi_text,True,BLACK),(tinggi_box.x+10,tinggi_box.y+10))

    # Tombol
    pygame.draw.rect(screen,BLUE,button)
    tombol_text=font.render("HITUNG",True,WHITE)
    screen.blit(tombol_text,(button.x+30,button.y+10))

    # Hasil
    pygame.draw.rect(screen,LIGHTGRAY,hasil_box)
    pygame.draw.rect(screen,GRAY,hasil_box,3)

    screen.blit(font.render("HASIL",True,BLACK),(300,305))
    screen.blit(font.render(hasil,True,BLACK),(180,360))

    pygame.draw.polygon(screen,GREEN,
    [(500,250),(620,250),(560,150)])

    pygame.display.flip()

pygame.quit()
sys.exit()