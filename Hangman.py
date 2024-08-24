import random

debug: bool = False
#zum debuggen True setzen

Wörter = ["ayri", "Leo", "Drank", "Ktrinken"]

Leben: int

rnd_wort_num = random.randrange(0, len(Wörter))

if debug:
    ("rndwortnum: "+str(rnd_wort_num)+"\nlen(Wörter): "+str(len(Wörter)))
    
rnd_wort = Wörter[rnd_wort_num]

if len(rnd_wort) <5:
    Leben = len(rnd_wort)
else:
    Leben = 5

def ProgressHang(max_leben, hang_progress):
    """
    Returns the right hang_progress considering the max_lives.
    Function not working in the moment
    """
    return "function not done rn"

def Hangman(wort: str, game_is_active: bool = False, leben: int = 5):
    unterstrichwort = "_" * len(wort)
    while game_is_active:
        
        if leben > 0:
            input_raten = input("Du hast "+str(leben)+" Leben.\nDas Wort ist: "+unterstrichwort+"\nMöchtest du raten? (y/n)\n")
                
            if input_raten == "y":
                input_ratung = input("Deine Ratung:")
                if wort == input_ratung:
                    print("Du hast gewonnen!!!!")
                    break
                else:
                    print("Falsch geraten, ein Leben weniger!")
                    leben = leben - 1
                    continue
                    
            elif input_raten == "n":    
                input_buchstabe = input("Gebe einen Buchstaben ein:\n")
            else:
                print("invalid input")
                continue
                
            if debug:
                print(wort+" "+unterstrichwort)
                
            if input_buchstabe.__len__() == 1 and input_buchstabe.isalpha():
                if wort.lower().__contains__(input_buchstabe.lower()):
                    start = 0
                    for S in range(wort.lower().count(input_buchstabe.lower())):             

                        richtiger_buchstabe_index = wort.lower().index(input_buchstabe.lower(), start)
                        
                        if wort.__getitem__(richtiger_buchstabe_index).isupper():
                            richtiger_buchstabe = wort.__getitem__(richtiger_buchstabe_index).capitalize()
                        else:
                            richtiger_buchstabe = wort.__getitem__(richtiger_buchstabe_index)
                        
                        start = richtiger_buchstabe_index+1
                        
                        unterstrichwort_neu = unterstrichwort[:richtiger_buchstabe_index]+richtiger_buchstabe+unterstrichwort[richtiger_buchstabe_index+1:]
                        unterstrichwort = unterstrichwort_neu
                        
                        if debug:
                            print(str(S)+" "+str(richtiger_buchstabe_index)+" "+str(start)+" "+unterstrichwort)
                    if debug:
                        print("beinhaltet")
                else:
                    leben = leben - 1 
                    print("Dieser Buchstabe ist nicht dabei, du verlierst ein Leben!") 
            else:
                print("gebe nur 1 Buchstaben ein!")
        else:
            print(f"Du hast keine Leben mehr, Verloren!\nEs wäre: {wort}!")
            break
            

yninput = input("Hangman starten? (y/n)\n")
if yninput == "y":
    Hangman(rnd_wort, True, Leben)
elif yninput == "n":
    print("spiel nicht gestartet")
    KeyboardInterrupt
else:
    print("invalid input")