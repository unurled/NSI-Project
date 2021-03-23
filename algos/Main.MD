# Main algo

import pygame

pygame init

compteur=0
speed=1

def main:
    taille window = 270x337
    title = Jump Bird
    player = image/bird.png
    background = image/background.png
    running = 1

def main_screen:
    background flou en couleur + pipes gen auto en fond
    milieu écran première ligne Jump Bird
                seconde press space to play
    si espace pressé alors continuer programme sinon rien faire

def game_over:
    make player image/bird_dead.png
    affiche gameover screen() 

def gameover_screen:
    mettre flou background noir et blanc + faire avance pipes
    afficher milieu de l'écran( première ligne "score %score_player%", seconde "Menu principal", thirnd "rejouer  (image rechage)" )

main()

while running:
    main_screen()
    faire aller background vers gauche at speed 0.2
    si background ne rempli pas tout windows alors remmetre background a la suite
    générer aléatoirement pipes haut et pipes bas a distance 30 pixel l'un de l'autre avec hauteur entre bas+5 et haut-5 tout les 30 ms
    if presse espace alors faire +10 pixel up player + mettre player image/annimation_up.png
    if touche pipe alors fonction game_over
    if player touche pas pipe mais passe dedans add 1 to compteur
    if compteur = 100: add 1 to speed