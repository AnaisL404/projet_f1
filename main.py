from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse
from menu import Menu

gestion = Gestion_donnees()

gestion.collecter_donnee()

quitter = 1000000000


while quitter != 0:
    Menu.menu_principal()
    
    try:
        choix1 = int(input("Entre le numéro du choix voulu: "))
        
        match choix1:
            
            #principal
            case 0:
                print("Merci")
                quitter = 0
            #principal    
            case 1:
                Menu.menu_stat()
                
                try:
                    choix2 = int(input("Entre le numéro du choix voulu: "))
                    
                    match choix2:
                        
                        #stat
                        case 1:
                            pass
                        #stat
                        case 2:
                            Menu.menu_ecuries()
                
                            try:
                                choix3 = int(input("Entre le numéro du choix voulu: "))
                                
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
                                print("Choix du circuit out of range") 
                             
                        #stat       
                        case 3:
                            Menu.menu_pilotes()
                
                            try:
                                choix4 = int(input("Entre le numéro du choix voulu: "))
                                
                                match choix4:
                                    
                                    #win
                                    case 1:
                                        pass
                                    #points
                                    case 2:
                                        pass
                                    #podiums
                                    case 3:
                                        pass
                                    #wc
                                    case 4:
                                        pass
                            except:
                                print("Choix du circuit out of range") 
                                
                        #stat       
                        case 4:
                            Menu.menu_saisons()
                
                            try:
                                choix5 = int(input("Entre le numéro du choix voulu: "))
                                
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
                                print("Choix du circuit out of range") 
                
                except:
                    print("Choix du circuit out of range")  
               
            #principal
            case 2:
                
                Menu.menu_quiz()
            
                try:
                    choix6 = int(input("Entre le numéro du choix voulu: "))
                    
                    match choix6:
                        
                        #palmarès
                        case 1:
                            pass
                        #jeux
                        case 2:
                            pass
                     
                except:
                    print("Choix du circuit out of range")  
        
    except:
        print("Choix du circuit out of range") 