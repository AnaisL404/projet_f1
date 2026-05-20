from gestion_donnees import Gestion_donnees
from analyse import Analyse
from menu import Menu
from quiz import Quiz

gestion = Gestion_donnees()

gestion.collecter_donnee()

quiz = Quiz()

quiz.lire_json_question("questions.json")
quiz.lire_json_palma("palmares.json")

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
                                        pilote_str = Menu.choix_pilote(gestion)
                                        
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
                            quiz.trier_palma()
                        #quiz
                        case 2:
                            quiz.quiz()
                     
                except Exception as e :
                    print()
                    print(e) 
        
    except:
        print("Choix out of range") 