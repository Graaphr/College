import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DATA 2D")

WHITE = (255,255,255)
LIGHTGRAY = (230,230,230)
BLACK = (0,0,0)
GRAY = (180,180,180)
BLUE = (70,130,255)

font = pygame.font.Font(None,28)
title_font = pygame.font.Font(None,40)

baris_box = pygame.Rect(200,120,200,40)
kolom_box = pygame.Rect(200,180,200,40)
nilai_box = pygame.Rect(200,240,200,40)

buttonUbah = pygame.Rect(440,500,140,45)
buttonTambah = pygame.Rect(250,500,140,45)

baris_text = ""
kolom_text = ""
nilai_text = ""

active_baris = False
active_kolom = False
active_nilai = False

# ARRAY
data = [[123, 124, 126],
        [1, 2, 3],
        [10, 20, 30]]

running = True

while running:

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            active_baris = baris_box.collidepoint(event.pos)
            active_kolom = kolom_box.collidepoint(event.pos)
            active_nilai = nilai_box.collidepoint(event.pos)

            if buttonUbah.collidepoint(event.pos):
                if baris_text.isdigit() and kolom_text.isdigit() and nilai_text.isdigit():
                    b = int(baris_text)
                    k = int(kolom_text)
                    n = int(nilai_text)

                    if 0 <= b < len(data) and 0 <= k < len(data[0]):
                        data[b][k] = n
                        
            if buttonTambah.collidepoint(event.pos):
                data.append([0,0,0])

        if event.type == pygame.KEYDOWN:

            if active_baris:
                if event.key == pygame.K_BACKSPACE:
                    baris_text = baris_text[:-1]
                else:
                    if event.unicode.isdigit():
                        baris_text += event.unicode

            if active_kolom:
                if event.key == pygame.K_BACKSPACE:
                    kolom_text = kolom_text[:-1]
                else:
                    if event.unicode.isdigit():
                        kolom_text += event.unicode

            if active_nilai:
                if event.key == pygame.K_BACKSPACE:
                    nilai_text = nilai_text[:-1]
                else:
                    if event.unicode.isdigit():
                        nilai_text += event.unicode


    # VIEW
    title = title_font.render("DATA 2D", True, BLACK)
    screen.blit(title, (350,30))

    screen.blit(font.render("Baris (0-n)",True,BLACK),(60,130))
    screen.blit(font.render("Kolom (0-n)",True,BLACK),(60,190))
    screen.blit(font.render("Nilai Baru",True,BLACK),(60,250))

    pygame.draw.rect(screen, LIGHTGRAY, baris_box)
    pygame.draw.rect(screen, LIGHTGRAY, kolom_box)
    pygame.draw.rect(screen, LIGHTGRAY, nilai_box)

    pygame.draw.rect(screen, GRAY, baris_box,2)
    pygame.draw.rect(screen, GRAY, kolom_box,2)
    pygame.draw.rect(screen, GRAY, nilai_box,2)

    screen.blit(font.render(baris_text,True,BLACK),(baris_box.x+10,baris_box.y+10))
    screen.blit(font.render(kolom_text,True,BLACK),(kolom_box.x+10,kolom_box.y+10))
    screen.blit(font.render(nilai_text,True,BLACK),(nilai_box.x+10,nilai_box.y+10))

    # TOMBOL
    pygame.draw.rect(screen, BLUE, buttonUbah)
    tombol_text = font.render("UBAH",True,WHITE)
    screen.blit(tombol_text,(buttonUbah.x+40,buttonUbah.y+12))
    
    pygame.draw.rect(screen, BLUE, buttonTambah)
    tombol_text = font.render("TAMBAH",True,WHITE)
    screen.blit(tombol_text,(buttonTambah.x+28,buttonTambah.y+12))

    x = 500
    y = 130

    for baris in range(len(data)):
        for kolom in range(len(data[0])):
            teksdata = "[" + str(data[baris][kolom]) + "]"
            screen.blit(font.render(teksdata,True,BLACK),(x,y))
            x += 70
        x = 500
        y += 40

    pygame.display.flip()

pygame.quit()
sys.exit()