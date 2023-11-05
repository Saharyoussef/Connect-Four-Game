import numpy as n
import pygame
import sys
import math
from pygame import mixer

blanc_pion=(245,245,245)
noir_pion=(31,31,31)
bleu=(146,181,200)
fond=(62,101,122)
lignes = 6
colonnes = 7
def creation_grille():
		grille = n.zeros((lignes,colonnes))
		return grille
	#fonction pour la création d'une grille qui est une matrice 6lignes 7 colonnes dont les cases libres sont initilisés à 0.
	#n.zeros() est une méthode spécifique de numpy

class Creation_jeu:
	def __init__ (self,grille):
		self.grille=grille

	def inverser_orientation(self,grille):
		print(n.flip(self.grille, 0))
	#fonction pour changer l'orientation des indices dans la grille car en numpy l'indice 0 commence en haut.
	#pour que le pion coulisse jusqu'à la position la plus basse possible.

	def valide(self,grille, col):
		return self.grille[lignes-1][col] == 0
	#fonction pour vérifier si la grille est encore valide pour la remplir donc on vérifie dernier ligne.

	def ligne_vide(self,grille, col):
		for l in range(lignes):
			if self.grille[l][col] == 0:
				return l
	#fonction pour retourner la ligne dont la case est libre pour n'importe quelle colonne.

class joueur:
	def __init__ (self,grille,pion):
		self.grille=grille
		self.pion=pion

	def remplir_pion(self,grille, l, col, pion):
		self.grille[l][col] = self.pion
	#fonction pour remplir la grille avec les pions

	def gagner(self,grille, pion):
		#alignement horizontal:
		for c in range(colonnes-3):
			for l in range(lignes):
				if self.grille[l][c] == self.pion and self.grille[l][c+1] == self.pion and self.grille[l][c+2] == self.pion and self.grille[l][c+3] == self.pion:
					return True
		#alignement vertical:
		for c in range(colonnes):
			for l in range(lignes-3):
				if self.grille[l][c] == self.pion and self.grille[l+1][c] == self.pion and self.grille[l+2][c] == self.pion and self.grille[l+3][c] == self.pion:
					return True
		#alignement diagonale positif:
		for c in range(colonnes-3):
			for l in range(lignes-3):
				if self.grille[l][c] == self.pion and self.grille[l+1][c+1] == self.pion and self.grille[l+2][c+2] == self.pion and self.grille[l+3][c+3] == self.pion:
					return True
		#alignement diagonale négatif:
		for c in range(colonnes-3):
			for l in range(3, lignes):
				if self.grille[l][c] == self.pion and self.grille[l-1][c+1] == self.pion and self.grille[l-2][c+2] == self.pion and self.grille[l-3][c+3] == self.pion:
					return True
class graphique:
	def __init__(self,fenetre,a):
		self.fenetre=fenetre
		self.a=a

	def dessiner_grille(self,a):
		for c in range(colonnes):
			for l in range(lignes):
				pygame.draw.rect(self.fenetre, bleu, (c*taille_cercle, l*taille_cercle+taille_cercle, taille_cercle, taille_cercle))
				pygame.draw.circle(self.fenetre, fond, (int(c*taille_cercle+taille_cercle/2), int(l*taille_cercle+taille_cercle+taille_cercle/2)), rayon)
		for c in range(colonnes):
			for l in range(lignes):		
				if self.a[l][c] == 1:
					pygame.draw.circle(self.fenetre, blanc_pion, (int(c*taille_cercle+taille_cercle/2), hauteur-int(l*taille_cercle+taille_cercle/2)), rayon)
				elif self.a[l][c] == 2: 
					pygame.draw.circle(self.fenetre, noir_pion, (int(c*taille_cercle+taille_cercle/2), hauteur-int(l*taille_cercle+taille_cercle/2)), rayon)
		pygame.display.update()
	#fonction pour dessiner background avec pygame

grille=creation_grille()
jeu=Creation_jeu(grille)
joueur1=joueur(grille,1)
joueur2=joueur(grille,2)
jeu.inverser_orientation(grille)
jeu_fini = False
tour = 0
taille_cercle = 100
largeur = colonnes * taille_cercle
hauteur = (lignes+1) * taille_cercle
taille = (largeur, hauteur)
rayon = int(taille_cercle/2 - 5)


pygame.init()
fenetre = pygame.display.set_mode(taille)
interface=graphique(fenetre,grille)
interface.dessiner_grille(grille)
pygame.display.set_caption("Puissance 4")
icone=pygame.image.load('puissance4.png')
pygame.display.set_icon(icone)
mixer.music.load('music.mp3')
mixer.music.play(-1)
pygame.display.update()
font=pygame.font.Font('freesansbold.ttf',70)

while not jeu_fini:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			#pour sortir du jeu

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(fenetre, fond, (0,0, largeur, taille_cercle))
			posx = event.pos[0]
			if tour == 0:
				pygame.draw.circle(fenetre, blanc_pion, (posx, int(taille_cercle/2)), rayon)
			else: 
				pygame.draw.circle(fenetre, noir_pion, (posx, int(taille_cercle/2)), rayon)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(fenetre, fond, (0,0, largeur, taille_cercle))

			if tour == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/taille_cercle))

				if jeu.valide(grille, col):
					l = jeu.ligne_vide(grille, col)
					joueur1.remplir_pion(grille, l, col, 1)

					if joueur1.gagner(grille, 1):
						label = font.render("Joueur 1 gagne!", 1,blanc_pion )
						fenetre.blit(label, (70,10))
						jeu_fini = True

			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/taille_cercle))

				if jeu.valide(grille, col):
					l = jeu.ligne_vide(grille, col)
					joueur2.remplir_pion(grille, l, col, 2)

					if joueur2.gagner(grille, 2):
						label = font.render("Joueur 2 gagne!", 1, noir_pion)
						fenetre.blit(label, (70,10))
						jeu_fini = True

			jeu.inverser_orientation(grille)
			interface.dessiner_grille(grille)

			tour += 1
			tour = tour % 2
			#pour alterner entre le joueur1 et joueur2
        	#Tour à tour les deux joueurs placent un pion dans la colonne de leur choix
			
			if jeu_fini:
				pygame.time.wait(1500)