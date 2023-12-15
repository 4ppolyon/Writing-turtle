from turtle import *


# Fonction qui dessine un espace
def dessine_():
    up()
    forward(50)
    down()


# Fonction qui dessine la lettre A
def dessine_a():
    left(70)
    forward(100)
    right(180 - 40)
    forward(100)
    left(180)
    forward(20)
    left(70)
    forward(55)
    left(180)
    forward(55)
    right(70)
    forward(20)
    left(70)

def dessine_a_grave():
#     first draw the accent
    left(90)
    up()
    forward(100)
    right(90)
    forward(50)
    right(180)
    down()
    right(10)
    forward(30)
    left(180)
    forward(30)
    left(190)
    up()
    forward(50)
    left(90)
    forward(100)
    left(90)
    down()
#     then draw the letter
    dessine_a()



# Fonction qui dessine la lettre B arrondie
def dessine_b():
    up()
    forward(25)
    down()
    circle(25, 180)
    forward(25)
    left(180)
    forward(25)
    circle(25, 180)
    forward(25)
    left(90)
    forward(100)
    left(90)
    forward(25)
    up()
    forward(25)
    down()


# Fonction qui dessine la lettre C
def dessine_c():
    up()
    forward(50)
    down()
    circle(50, -180)
    left(90)
    up()
    forward(100)
    down()
    left(90)


# Fonction qui dessine la lettre D
def dessine_d():
    circle(50, 180)
    left(90)
    forward(100)
    left(90)
    up()
    forward(50)
    down()


# Fonction qui dessine la lettre E
def dessine_e():
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

def dessine_e_grave():
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(180)
    forward(10)
    right(90)
    up()
    forward(10)
    down()
    left(80)
    forward(30)
    left(180)
    forward(30)
    right(80)
    up()
    forward(10)
    down()
    right(90)
    forward(40)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

def dessine_e_aigue():
    left(90)
    forward(100)
    right(90)
    forward(10)
    left(90)
    up()
    forward(10)
    down()
    right(80)
    forward(30)
    left(180)
    forward(30)
    left(80)
    up()
    forward(10)
    down()
    left(90)
    forward(40)
    right(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

def dessine_e_trema():
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(180)
    forward(10)
    right(90)
    up()
    forward(10)
    down()
    left(90)
    forward(10)
    up()
    forward(10)
    down()
    forward(10)
    up()
    left(180)
    forward(30)
    right(90)
    forward(10)
    down()
    right(90)
    forward(40)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

# Fonction qui dessine la lettre F
def dessine_f():
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    up()
    forward(50)
    down()


# Fonction qui dessine la lettre G
def dessine_g():
    up()
    forward(50)
    down()
    circle(50, -180)
    left(90)
    up()
    forward(100)
    down()
    left(180)
    forward(50)
    left(90)
    forward(20)
    up()
    left(180)
    forward(20)
    right(90)
    forward(50)
    left(90)
    down()


# Fonction qui dessine la lettre H
def dessine_h():
    left(90)
    forward(100)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(100)
    left(90)


# Fonction qui dessine la lettre I
def dessine_i():
    left(90)
    forward(100)
    left(180)
    forward(100)
    left(90)


# Fonction qui dessine la lettre J
def dessine_j():
    left(90)
    up()
    forward(20)
    down()
    left(180)
    circle(20, 180)
    forward(80)
    left(180)
    up()
    forward(100)
    down()
    left(90)


# Fonction qui dessine la lettre K
def dessine_k():
    left(90)
    forward(100)
    left(180)
    forward(50)
    left(45)
    forward(70)
    left(180)
    forward(70)
    right(90)
    forward(70)
    up()
    right(135)
    forward(100)
    down()
    left(90)


# Fonction qui dessine la lettre L
def dessine_l():
    left(90)
    forward(100)
    left(180)
    forward(100)
    left(90)
    forward(50)


# Fonction qui dessine la lettre M
def dessine_m():
    left(90)
    forward(100)
    right(135)
    forward(45)
    left(90)
    forward(45)
    right(135)
    forward(100)
    left(90)


# Fonction qui dessine la lettre N
def dessine_n():
    left(90)
    forward(100)
    right(150)
    forward(115.47)
    left(150)
    forward(100)
    left(180)
    forward(100)
    left(90)


# Fonction qui dessine la lettre O
def dessine_o():
    up()
    forward(50)
    down()
    circle(50, 360)
    up()
    forward(50)
    down()


# Fonction qui dessine la lettre P arrondie
def dessine_p():
    left(90)
    forward(50)
    right(90)
    forward(25)
    circle(25, 180)
    forward(25)
    left(90)
    forward(100)
    left(90)
    up()
    forward(50)
    down()


# Fonction qui dessine la lettre Q
def dessine_q():
    up()
    forward(50)
    down()
    circle(50, 360)
    up()
    left(90)
    forward(50)
    right(90 + 45)
    down()
    forward(70)
    left(45)


# Fonction qui dessine la lettre R arrondie
def dessine_r():
    left(90)
    forward(50)
    right(90)
    forward(25)
    circle(25, 180)
    forward(25)
    left(90)
    forward(50)
    left(45)
    forward(70)
    left(45)


# Fonction qui dessine la lettre S arrondie
def dessine_s():
    forward(25)
    circle(25, 180)
    up()
    right(90)
    forward(50)
    right(90)
    down()
    forward(25)
    left(180)
    forward(25)
    circle(25, 180)
    up()
    forward(25)
    right(90)
    forward(50)
    left(90)
    down()


# Fonction qui dessine la lettre T
def dessine_t():
    up()
    left(90)
    forward(100)
    down()
    right(90)
    forward(50)
    right(180)
    forward(25)
    left(90)
    forward(100)
    left(90)
    up()
    forward(25)
    down()


# Fonction qui dessine la lettre U arrondie
def dessine_u():
    left(90)
    up()
    forward(100)
    down()
    left(180)
    forward(75)
    circle(25, 180)
    forward(75)
    left(180)
    up()
    forward(100)
    down()
    left(90)


# Fonction qui dessine la lettre V
def dessine_v():
    left(90)
    up()
    forward(96.16)
    down()
    right(90 + 70)
    forward(102.33)
    left(140)
    forward(102.33)
    right(70 + 90)
    up()
    forward(96.16)
    down()
    left(90)


# Fonction qui dessine la lettre W
def dessine_w():
    left(90)
    up()
    forward(96.16)
    down()
    right(90 + 70)
    forward(102.33)
    left(140)
    forward(102.33)
    right(140)
    forward(102.33)
    left(140)
    forward(102.33)
    right(70 + 90)
    up()
    forward(96.16)
    down()
    left(90)


# Fonction qui dessine la lettre X
def dessine_x():
    left(55)
    forward(122.06)
    left(180)
    forward(61.03)
    right(110)
    forward(61.03)
    left(180)
    forward(122)
    left(55)


# Fonction qui dessine la lettre Y
def dessine_y():
    left(55)
    forward(122.06)
    left(180)
    forward(61.03)
    right(110)
    forward(61.03)
    left(180)
    up()
    forward(122)
    down()
    left(55)


# Fonction qui dessine la lettre Z
def dessine_z():
    left(55)
    forward(122.07)
    left(125)
    forward(70)
    left(180)
    forward(70)
    right(125)
    forward(122.07)
    left(125)
    forward(70)


# Fonction qui dessine la lettre 0
def dessine_0():
    left(90)
    up()
    forward(25)
    down()
    forward(50)
    circle(-25, 180)
    forward(50)
    circle(-25, 180)
    up()
    right(90)
    forward(50)
    right(90)
    forward(25)
    down()
    left(90)


# Fonction qui dessine la lettre 1
def dessine_1():
    up()
    forward(20)
    down()
    left(90)
    forward(100)
    left(135)
    forward(28)
    left(180)
    forward(28)
    right(135)
    forward(100)
    left(90)


# Fonction qui dessine la lettre 2
def dessine_2():
    left(45)
    forward(93.81)
    left(45)
    circle(33.13, 180)
    up()
    circle(33.13, 180)
    left(135)
    forward(93.81)
    left(135)
    down()
    forward(66.26)


# Fonction qui dessine la lettre 3
def dessine_3():
    forward(25)
    circle(25, 180)
    forward(25)
    left(180)
    forward(25)
    circle(25, 180)
    forward(25)
    left(180)
    forward(25)
    right(90)
    up()
    forward(100)
    left(90)
    forward(25)
    down()


# Fonction qui dessine la lettre 4
def dessine_4():
    left(90)
    up()
    forward(100)
    down()
    left(180)
    forward(50)
    left(90)
    forward(50)
    right(180)
    forward(10)
    right(90)
    forward(20)
    left(180)
    forward(70)
    left(90)
    up()
    forward(20)
    down()


# Fonction qui dessine la lettre 5
def dessine_5():
    forward(25)
    circle(25, 180)
    forward(25)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    up()
    forward(100)
    down()
    left(90)


# Fonction qui dessine la lettre 6
def dessine_6():
    up()
    forward(25)
    down()
    circle(25, 270)
    left(180)
    forward(50)
    circle(-25, 180)
    up()
    circle(-25, 180)
    left(180)
    forward(50)
    down()
    circle(25, 90)
    up()
    forward(25)
    down()


# Fonction qui dessine la lettre 7
def dessine_7():
    left(55)
    forward(122.07)
    left(125)
    forward(70)
    left(180)
    forward(70)
    right(125)
    forward(122.07)
    right(55 + 180)
    up()
    forward(70)
    down()


# Fonction qui dessine la lettre 8
def dessine_8():
    up()
    forward(25)
    down()
    circle(25, 180)
    circle(-25, 360)
    circle(25, 180)
    up()
    forward(25)
    down()


# Fonction qui dessine la lettre 9
def dessine_9():
    forward(25)
    circle(25, 90)
    forward(50)
    circle(25, 360)
    up()
    left(180)
    forward(75)
    left(90)
    down()


# Fonction qui dessine la lettre .
def dessine_point():
    pensize(10)
    forward(1)
    pensize(5)
    up()
    forward(10)
    down()


# Fonction qui dessine la lettre ,
def dessine_comma():
    pensize(10)
    forward(1)
    pensize(8)
    right(90 + 45)
    forward(10)
    left(180)
    forward(10)
    right(45)
    up()
    forward(10)
    down()
    pensize(5)


# Fonction qui dessine la lettre !
def dessine_exclamation():
    pensize(10)
    forward(1)
    pensize(5)
    left(90)
    up()
    forward(25)
    down()
    forward(75)
    up()
    left(180)
    forward(100)
    left(90)
    forward(10)
    down()


# Fonction qui dessine la lettre ?
def dessine_interrogation():
    up()
    forward(10)
    down()
    pensize(10)
    forward(1)
    pensize(5)
    left(90)
    up()
    forward(25)
    down()
    forward(25)
    right(90)
    circle(25, 270)
    up()
    circle(25, 180)
    left(180)
    forward(75)
    left(90)
    forward(10)
    down()


# Fonction qui dessine la lettre :
def dessine_deux_points():
    dessine_()
    left(90)
    up()
    forward(10)
    down()
    right(90)
    pensize(10)
    forward(1)
    pensize(5)
    left(180)
    forward(1)
    right(90)
    up()
    forward(60)
    down()
    right(90)
    pensize(10)
    forward(1)
    pensize(5)
    right(90)
    up()
    forward(70)
    down()
    left(90)


# Fonction qui dessine la lettre '
def dessine_apostrophe():
    left(90)
    up()
    forward(70)
    down()
    pensize(8)
    right(45)
    forward(30)
    pensize(5)
    right(135)
    up()
    forward(91.22)
    left(90)
    down()


# Fonction qui dessine la lettre )
def dessine_parenthese_fermante():
    circle(20, 90)
    forward(60)
    circle(20, 90)
    up()
    circle(20, 90)
    forward(60)
    circle(20, 90)
    forward(20)
    down()


# Fonction qui dessine la lettre (
def dessine_parenthese_ouvrante():
    up()
    forward(20)
    down()
    left(180)
    circle(-20, 90)
    forward(60)
    circle(-20, 90)
    up()
    circle(-20, 90)
    forward(60)
    circle(-20, 90)
    left(180)
    down()

