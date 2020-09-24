# le choix de l'utilisateur
######################################################################
def choix_utilisateur ():
    resultat = False
    choix = 0
    print("choix : 1 ----> 15% du prix HT")
    print("choix : 2 ----> 19% du prix HT")
    print("choix : 3 ----> 20% du prix HT")

    while resultat != True :
        while True :
            try :
                choix = int(input("entrer votre choix : ") )
                break

            except ValueError :
                print("erreur !!! ")

        if choix == 1 or choix == 2 or choix == 3 :
            resultat = True
        else:
            resultat = False

    return choix
#######################################################################



# le prix de l'utilisateur apres les taxes
#######################################################################

def prix_utilisateur (choix) :

    while True :
        try :
            prix_HT = float(input("entrer le prix du produit "))
            break
        except ValueError :
            print("erreur !!!!")

    if choix == 1 :
        prix_HT = prix_HT -( (prix_HT*15)/100 )
    elif choix == 2 :
        prix_HT = prix_HT -( (prix_HT*19)/100 )
    else :
        prix_HT = prix_HT - ((prix_HT * 20) / 100)

    return prix_HT

########################################################################
