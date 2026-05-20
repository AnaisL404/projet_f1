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
                            print()
                            Menu.menu_circuit()
                            print()
                            
                            try:
                                choix3 = int(input("Entre le numéro du choix voulu: "))
                                print()
                                
                                match choix3:
                                    
                                    #circuit les plus vieux
                                    case 1:
                                        
                                        Analyse.circuit_plus_longtemps(gestion)
                                        
                                    # best time
                                    case 2:
                                        
                                        Analyse.meilleur_temps_circuit(gestion)
                     
                            except :
                                print("Choix out of range")   
                            
                        #stat
                        case 2:
                            print()
                            Menu.menu_ecuries()
                            print()
                
                            try:
                                choix4 = int(input("Entre le numéro du choix voulu: "))
                                print()
                                
                                match choix4:
                                    
                                    #win
                                    case 1:
                                        ecurie_str = Menu.choix_ecurie()
                                        
                                        print()
                                        
                                        results = Analyse.win_ecurie(gestion, ecurie_str)
                                        
                                        Analyse.afficher_top3(results)
                                        
                                        
                                    #points
                                    case 2:
                                        ecurie_str = Menu.choix_ecurie()
                                        
                                        print()
                                        
                                        results = Analyse.points_ecurie(gestion, ecurie_str)
                                        
                                        Analyse.afficher_top3(results)
                                        
                                    #podiums
                                    case 3:
                                        ecurie_str = Menu.choix_ecurie()
                                        
                                        print()
                                        
                                        results = Analyse.podiums_ecurie(gestion, ecurie_str)
                                        
                                        Analyse.afficher_top3(results)
                                        
                            except:
                                print()
                                print("Choix  out of range")
                                print()
                            
                             
                        #stat       
                        case 3:
                
                            Menu.menu_pilotes()
                            print()
                
                            try:
                                choix5 = int(input("Entre le numéro du choix voulu: "))
                                print()
                                
                                match choix5:
                                    
                                    #win
                                    case 1:
                                        pilote_str = Menu.choix_pilote(gestion)
                                        
                                        print()
                                        print(Analyse.plus_de_win(gestion, pilote_str))
                                    
                                        
                                    #points
                                    case 2:
                                        pilote_str = Menu.choix_pilote(gestion)
                                        
                                        print()
                                        print(Analyse.plus_de_points(gestion, pilote_str))
                                        
                                    #podiums
                                    case 3:
                                        pilote_str = Menu.choix_pilote(gestion)
                                        
                                        print()
                                        print(Analyse.plus_de_podium(gestion, pilote_str))
                                        
                                    #wc
                                    case 4:
                                        print()
                                        Analyse.wc(gestion) 
                                        
                            except :
                                print()
                                print("Choix out of range") 
                                
                        #stat       
                        case 4:
                            print()
                            Menu.menu_saisons()
                            print()
                
                            try:
                                choix6 = int(input("Entre le numéro du choix voulu: "))
                                print()
                                
                                match choix6:
                                    
                                    #win
                                    case 1:
                                        saison_voulue = Menu.choix_saison()
                                        
                                        print()
                                        
                                        Analyse.pourcentage_win_saison(gestion, saison_voulue)
                                        
                                    #points
                                    case 2:
                                        saison_voulue = Menu.choix_saison()
                                        
                                        print()
                                        
                                        lst_lst = Analyse.points_saison(gestion, saison_voulue)
                                        
                                        liste = Analyse.tri(lst_lst)
                                        
                                        for pilote in liste:
                                            print(f"Le pilote {pilote[0]} à fait {pilote[1]} points dans la saison {saison_voulue}")
                                    
                                    
                                    
                                    #podiums
                                    case 3:
                                        saison_voulue = Menu.choix_saison()
                                        
                                        print()
                                        
                                        lst_lst = Analyse.podiums_saison(gestion, saison_voulue)
                                        
                                        liste = Analyse.tri(lst_lst)
                                        
                                        for pilote in liste:
                                            print(f"Le pilote {pilote[0]} à fait {pilote[1]} podiums dans la saison {saison_voulue}")
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
                    choix7 = int(input("Entre le numéro du choix voulu: "))
                    print()
                    
                    match choix7:
                        
                        #palmarès
                        case 1:
                            quiz.trier_palma()
                        #quiz
                        case 2:
                            quiz.quiz()
                     
                except :
                    print()
                    print("Choix out of range") 
        
    except:
        print("Choix out of range") 