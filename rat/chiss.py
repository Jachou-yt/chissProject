import time


def waits(sec):
    time.sleep(sec)

class chiss():

    # Des idées pour économiser
    def économie(self):
        économie = input('Séléctionner le prix : ')
        if int(économie) < 20:
            print("Négocier le prix avec un accent bizzare ou faite semblant de ne pas comprendre. Cela énervera le vendeur et il vous fera sortir avec l'objet de son magasin")
        else:
            if int(économie) > 20 & int(économie) < 100:
                print("Cela commence à devenir compliquer. Nous avons plusieurs méthodes. Vous pouvez tout d'abord demander gentiment, dire que il en vend plein et qu'il pourrait faire une exception ou alors vous faite le crevard comme chiss et vous partez sans rien dire si il a oublier (c'est la méthode la plus efficace !)")
            else:
                print('Dans la vie il y a des limites. Là vous les avez dépassés !')
        waits(3)        

    # Test de crevaritude    
    def crevaritude(self):
        résultat = 0
        print("Répondez par oui ou par non. ")
        crevard = input("Vou n'aimez pas dépsenser de l'argent ? ")
        crevard2 = input("Vous n'aimez pas offrir des cadeux aux autres si c'est vous qui dépensez de l'argent ? ")
        crevard3 = input("Aimez-vous chiss ? ")
        crevard4 = input("Vous négociez dès que vous en avez l'opportunité ? ")
        crevard5 = input("Vous vous pensez crevard ? ")
        if crevard == "yes":
            toto = résultat + 1
        if crevard2 == "yes":
            toto1 = toto + 1
        if crevard3 == "yes":
            toto2 = toto1 + 1
        if crevard4  == "yes":
            result = toto2 + 1
        if crevard5  == "yes":
            result + 1

        if result < 1:
            print("Tu es ultra généreux !")
            waits(3)
        else:
            if result > 1 & result < 3:
                print("Tu a un peu de gène du chiss")
                waits(3)
            else:
                if result == 4 & result > 4:
                    print("Chiss tout puissant ! C'est toi qui est là !!!!!!!!!!!!!!")
                    waits(3)
    
    # Produit le son du chiss sauvage

    # 

    # Toutes les fonctionnalités
    def all(self):
        self.crevaritude
        self.économie        