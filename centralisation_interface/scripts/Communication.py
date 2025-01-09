from scripts.import_variable import *



class Communication(threading.Thread) :
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self) :
        sleep(3)
        #test avec 3 messages de prevention qui arrive avec 3-7 secondes d'intervale 
        #le choice permet de choisir entre un message qui s'arrête tout seul ou qui attent un message d'arêt
        for k in range(3) : 
            prevention_queue.append({"message" : f"Moteur trop chaud k={k}", "start" : int(time()), "end" : choice([None, 7])})
            print(prevention_queue)
            sleep(randint(3, 7))
        
       


    #fonction pour arrêter un message de prévention sans ou avec délai. Identification par le message
    def arret_prevention(self, message) :
        for k in range(len(prevention_queue)) :
            if message == prevention_queue[k]["message"] :
                prevention_queue.pop(k)
                return