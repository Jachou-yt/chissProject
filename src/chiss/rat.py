import time
import webbrowser
import uuid
import random
from tkinter import *

def waits(sec):
    time.sleep(sec)


# Des idées pour économiser

def économie():
    économie = input('Séléctionner le prix : ')
    if int(économie) <= 20:
        print(
            "Négocier le prix avec un accent bizzare ou faite semblant de ne pas comprendre. Cela énervera le vendeur et il vous fera sortir avec l'objet de son magasin")
    else:
        if int(économie) > 20 & int(économie) <= 100:
            print(
                "Cela commence à devenir compliquer. Nous avons plusieurs méthodes. Vous pouvez tout d'abord demander gentiment, dire que il en vend plein et qu'il pourrait faire une exception ou alors vous faite le crevard comme chiss et vous partez sans rien dire si il a oublier (c'est la méthode la plus efficace !)")
        else:
            print('Dans la vie il y a des limites. Là vous les avez dépassés !')
    waits(3)


# Test de crevaritude

def crevaritude():
    total = 0
    print("Répondez par 'yes' ou par 'no'. ")
    crevard = input("Vou n'aimez pas dépsenser de l'argent ? ")
    crevard2 = input("Vous n'aimez pas offrir des cadeux aux autres si c'est vous qui dépensez de l'argent ? ")
    crevard3 = input("Aimez-vous chiss ? ")
    crevard4 = input("Vous négociez dès que vous en avez l'opportunité ? ")
    crevard5 = input("Vous vous pensez crevard ? ")
    if crevard == "yes":
        total += 1
    if crevard2 == "yes":
        total += 1
    if crevard3 == "yes":
        total += 1
    if crevard4 == "yes":
        total += 1
    if crevard5 == "yes":
        total += 1

    result = total
    print(result)

    if result < 1:
        print("Tu es ultra généreux !")
        waits(3)
    else:
        if result < 5:
            print("Tu a un peu de gène du chiss")
            waits(3)
        else:
            if result == 5:
                print("Chiss tout puissant ! C'est toi qui est là !!!!!!!!!!!!!!")
                waits(3)


# Produit le son du chiss sauvage

def bruit_du_chiss():
    print('Le son du chiss !')
    webbrowser.open('https://jachou-yt.github.io/My-website/chissProject-storage/rat.wav')


# Faire baisser le prix d'un objet facilement

def prix_objet():
    print("Remplacer l'étiquette par une autre ! Pour le chiss ça a marché, pourquoi pas vous ?")
    waits(3)


# Chiss s'enrichit

def enrichir_le_chiss():
    # Infos
    bitcoin_found = True
    sold = 0
    failed_attempt = 0
    btc_found = 0

    # Start fake mining
    fake_rd_generate = random.randint(1, 1000000)
    print('Bitcoin finding by Jachou.')
    waits(1)
    while bitcoin_found:
        # title cmd
        ws = Tk()
        ws.title('Bitcoin Miner by Jachou | Sold : ' + sold + ' | Attempt failed : ' + failed_attempt + ' | Bitcoin found : ' + btc_found)
        ws.mainloop()

        bitcoin_id = uuid.uuid4()
        rd = random.randint(1, 1000000)
        if rd == fake_rd_generate:
            print('\033[1;32;40m [Bitcoin Mining] Bitcoin has been found : \n' + str(bitcoin_id))
            btc_found += 1
            waits(1)
            rd_sold = random.uniform(0.000001, 0.123679)
            sold += rd_sold
            print('\033[1;32;40m [Bitcoin Mining]  Your sold is : \n' + str(sold))
            input('\033[1;32;40m [Bitcoin Mining] Press enter to continue...\n')
        else:
            print('[Bitcoin Mining] \033[1;31;40m Bitcoin failed attempt : \n' + str(bitcoin_id))
            failed_attempt += 1


# Toutes les fonctionnalités

def all():
    crevaritude()
    économie()
    prix_objet()
    enrichir_le_chiss()
