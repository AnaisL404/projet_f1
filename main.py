from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse
from menu import Menu
from quiz import Quiz

gestion = Gestion_donnees()

gestion.collecter_donnee()
quiz = Quiz()

quitter = 1000000000

while quitter != 0:
    print()
    Menu.menu_principal()
    print()
    
    try:
        choix1 = int(input("Entre le numéro du choix voulu: "))
        print()
        
        match choix1:
            
            #principal
            case 0:
                print("Merci")
                quitter = 0
            #principal    
            case 1:
                Menu.menu_stat()
                print()
                
                try:
                    choix2 = int(input("Entre le numéro du choix voulu: "))
                    print()
                    
                    match choix2:
                        
                        #stat
                        case 1:
                            pass
                        #stat
                        case 2:
                            print()
                            Menu.menu_ecuries()
                            print()
                
                            try:
                                choix3 = int(input("Entre le numéro du choix voulu: "))
                                print()
                                
                                match choix3:
                                    
                                    #win
                                    case 1:
                                        pass
                                    #points
                                    case 2:
                                        pass
                                    #podiums
                                    case 3:
                                        pass
                            except:
                                print()
                                print("Choix  out of range")
                                print()
                            
                             
                        #stat       
                        case 3:
                            print()
                            Menu.menu_pilotes()
                            print()
                
                            try:
                                choix4 = int(input("Entre le numéro du choix voulu: "))
                                print()
                                
                                match choix4:
                                    
                                    #win
                                    case 1:
                                        pass
                                    #points
                                    case 2:
                                        
                                        #input des pilotes
                                        #choisir le pilote
                                        lst_pilote = []
                                        liste_nom = []

                                        for pilote in gestion.lst_pilotes:
                                                
                                            if pilote.driver_id not in liste_nom:
                                                lst_pilote.append(pilote)
                                                liste_nom.append(pilote.driver_id)

                                        index = 0
                                        for driver in lst_pilote:
                                            print(f"{index}. {driver.prenom}  {driver.nom}")
                                            index += 1
                                        try:
                                            print()
                                            pilote_int = int(input("Entrez le numéro du pilote voulu: "))
                                            pilote_str = lst_pilote[pilote_int]

                                        except:
                                            print()
                                            print("Choix out of range")
                                            print()

                                
                                        print()
                                        print(Analyse.plus_de_points(gestion, pilote_str))
                                    #podiums
                                    case 3:
                                        pass
                                    #wc
                                    case 4:
                                        print()
                                        Analyse.wc(gestion)
                            except Exception as e :
                                print(e) 
                                
                        #stat       
                        case 4:
                            print()
                            Menu.menu_saisons()
                            print()
                
                            try:
                                choix5 = int(input("Entre le numéro du choix voulu: "))
                                print()
                                
                                match choix5:
                                    
                                    #win
                                    case 1:
                                        pass
                                    #points
                                    case 2:
                                        pass
                                    #podiums
                                    case 3:
                                        pass
                            except:
                                print()
                                print("Choix out of range") 
                                print()
                
                except:
                    print("Choix  out of range")  
               
            #principal
            case 2:
                print()
                Menu.menu_quiz()
                print()
            
                try:
                    choix6 = int(input("Entre le numéro du choix voulu: "))
                    print()
                    
                    match choix6:
                        
                        #palmarès
                        case 1:
                            quiz.lire_json_palma("palmares.json")
                            quiz.trier_palma()
                        #quiz
                        case 2:
                            quiz.lire_json_question("questions.json")
                            quiz.quiz()
                            quiz.sauvegarder_json_palma("palmares.json")
                     
                except:
                    print()
                    print("Choix out of range")  
                    print()
        
    except:
        print("Choix out of range") 