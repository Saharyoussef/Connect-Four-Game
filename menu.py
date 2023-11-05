import pygame, sys
from button import Bouton

pygame.init()

fenetre = pygame.display.set_mode((1024, 680))
pygame.display.set_caption("Menu")
icone=pygame.image.load('puissance4.png')
pygame.display.set_icon(icone)
pygame.display.update()
BG = pygame.image.load("BG1.jpg")

def get_font(size):
    return pygame.font.Font("font.ttf", size)
def get_font1(size):
    return pygame.font.Font("freesansbold.ttf", size)

def jouer():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        cond = pygame.image.load("conditions.jpg")
        fenetre.blit(cond,(0,0))
        txt = get_font1(70).render("Merci d'avoir joué!! ", True, "White")
        rectangle = txt.get_rect(center=(500, 200))
        fenetre.blit(txt, rectangle)
        retour = Bouton(image=None, pos=(520, 420), 
                            text_input="Menu", font=get_font1(75), base_color="#47EBD5", hovering_color="White")

        retour.changer_couleur(PLAY_MOUSE_POS)
        retour.miseàjour(fenetre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour.vérification_entrée(PLAY_MOUSE_POS):
                    menu_principale()

        pygame.display.update()
    
def conditions():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        cond = pygame.image.load("conditions.jpg")
        fenetre.blit(cond,(0,0))
        txt = get_font1(40).render("Les conditions du jeu sont : ", True, "White")
        rectangle = txt.get_rect(center=(400, 80))
        fenetre.blit(txt, rectangle)
        
        txt1 = get_font1(30).render("*2 joueurs chacun posséde 21 pions. ", True, "White")
        rectangle = txt1.get_rect(center=(400, 150))
        fenetre.blit(txt1, rectangle)

        txt2 = get_font1(30).render("*Chaque joueur doit aligner 4 pions. ", True, "White")
        rectangle = txt2.get_rect(center=(395, 220))
        fenetre.blit(txt2, rectangle)

        txt3 = get_font1(30).render("*Le vainqueur est celui qui aligne ses pions le premier.", True, "White")
        rectangle = txt3.get_rect(center=(524, 290))
        fenetre.blit(txt3, rectangle)


        retour = Bouton(image=None, pos=(520, 420), 
                            text_input="Menu", font=get_font1(75), base_color="#47EBD5", hovering_color="White")

        retour.changer_couleur(OPTIONS_MOUSE_POS)
        retour.miseàjour(fenetre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour.vérification_entrée(OPTIONS_MOUSE_POS):
                    menu_principale()

        pygame.display.update()

def menu_principale():
    while True:
        fenetre.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("MENU", True, "#B33878")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 180))
        
        bouton_condition = Bouton(image=None, pos=(500, 300), 
                            text_input="CONDITIONS", font=get_font(50), base_color="#92B5B0", hovering_color="White")
        bouton_jouer = Bouton(image=None, pos=(500, 400), 
                            text_input="JOUER", font=get_font(50), base_color="#92B5B0", hovering_color="White")
        bouton_sortir = Bouton(image=None, pos=(500, 500), 
                            text_input="SORTIR", font=get_font(50), base_color="#92B5B0", hovering_color="White")

        fenetre.blit(MENU_TEXT, MENU_RECT)

        for button in [bouton_jouer, bouton_condition, bouton_sortir]:
            button.changer_couleur(MENU_MOUSE_POS)
            button.miseàjour(fenetre)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_jouer.vérification_entrée(MENU_MOUSE_POS):
                    jouer()
                if bouton_condition.vérification_entrée(MENU_MOUSE_POS):
                    conditions()
                if bouton_sortir.vérification_entrée(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu_principale()