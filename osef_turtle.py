# acces au fonctions du fichier lettre.py
from lettre import *

# cree un dictionnaire qui associe chaque lettre a une fonction
fonctions = {' ': dessine_, 'a': dessine_a, 'b': dessine_b, 'c': dessine_c, 'd': dessine_d, 'e': dessine_e,
             'f': dessine_f, 'g': dessine_g, 'h': dessine_h, 'i': dessine_i, 'j': dessine_j, 'k': dessine_k,
             'l': dessine_l, 'm': dessine_m, 'n': dessine_n, 'o': dessine_o, 'p': dessine_p, 'q': dessine_q,
             'r': dessine_r, 's': dessine_s, 't': dessine_t, 'u': dessine_u, 'v': dessine_v, 'w': dessine_w,
             'x': dessine_x, 'y': dessine_y, 'z': dessine_z, 'A': dessine_a, 'B': dessine_b, 'C': dessine_c,
             'D': dessine_d, 'E': dessine_e, 'F': dessine_f, 'G': dessine_g, 'H': dessine_h, 'I': dessine_i,
             'J': dessine_j, 'K': dessine_k, 'L': dessine_l, 'M': dessine_m, 'N': dessine_n, 'O': dessine_o,
             'P': dessine_p, 'Q': dessine_q, 'R': dessine_r, 'S': dessine_s, 'T': dessine_t, 'U': dessine_u,
             'V': dessine_v, 'W': dessine_w, 'X': dessine_x, 'Y': dessine_y, 'Z': dessine_z, '0': dessine_0,
             '1': dessine_1, '2': dessine_2, '3': dessine_3, '4': dessine_4, '5': dessine_5, '6': dessine_6,
             '7': dessine_7, '8': dessine_8, '9': dessine_9, '.': dessine_point, "'": dessine_apostrophe,
             ',': dessine_comma, ':': dessine_deux_points, '!': dessine_exclamation, '?': dessine_interrogation,
             '(': dessine_parenthese_ouvrante, ')': dessine_parenthese_fermante}


def ecrit(line, lettre):
    if xcor() >= 47 * 19:
        up()
        goto(-900, 100 - 110 * line)
        down()
        line += 1
    if line >= 4:
        #     on efface la fenetre et on recommence
        clear()
        up()
        goto(-880, 100)
        down()
        line = 0
    fonctions[lettre]()
    up()
    forward(15)
    down()
    return line


def main():
    blabla = "Choisissez ce que vous voulez faire :\n1 : pour taper une ligne\n2 : pour que le programme affiche les " \
             "lettres toutes d'un coup\n"
    reponse = input(blabla)
    setup(1900, 500, -100, -50)  # titre de la fenêtre graphique
    title("OSEF")
    # couleur de fond de la fenêtre graphique
    bgcolor("black")
    # couleur du stylo
    pencolor("white")
    # épaisseur du trait
    pensize(5)
    speed(10)
    # se placer à gauche
    up()
    goto(-900, 100)
    down()
    line = 1
    nb_char = 0
    if reponse == "1":
        ligne = input("Tapez \"stop\" pour arretez\n")
        while ligne != "stop":
            for lettre in list(ligne):
                line = ecrit(line, lettre)
            up()
            goto(-900, 100 - 110 * line)
            down()
            line += 1
            ligne = input()
    elif reponse == "2":
        for lettre in fonctions.keys():
            line = ecrit(line, lettre)
    print("Merci d'avoir utilisé ce programme !")


main()
