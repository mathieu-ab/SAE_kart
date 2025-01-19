


###############################################################################################
#
#
#
#               ░░▒▒       ▓▒▓▓▓▓▓▓▓▓░████▒░░░░▒▒▒▒░
#             ▒▓▓▓▓▓▓▒     █▓▓▓▓▓▓▓▓▓████▓░░░░░░▒▒▒▒░░░
#            ▓▓▓▓▓▓▒▓▒▒▒▒░▒▒▒▒▒▒▒▒▒▓█▓▒▓██▒░░░░░░▒░▒░░▒▒
#            ▒▓▒▓▓▒▓▓▓▓▒▒▒░░▒▒▒▒▒▒▓█▓▒▓▓██▓▒░░░░░░░▒░░░░░
#       ▒▓███▓███▓▓▓█▓▓▓▓▓▒▒▒▒▒▓▒▒▒▓▓██▓▓▓▓▓▓▒░░░░░░▒▒▒▒░▒█
#        ▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▒▓▓███▓▒░░░░░░░░░▒█
#   ██████████▓▓▓███▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓██▓▓▓█▓▓▒░░░░░░░░░    ██▓▓▓▓▓
#█████▓▓▓▓███████▓███████▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓█▓██▓▓▓▓▓▓▓▓▒░░░░░░░░███████▓▓██
#█▓██▓▓▒░░▒▓████████████████████▓▒░▒▒▒▒▓█▓▓█▓▒▒▒▓▓▓▓▓▒▒▒▒░░░░░▒▓█████████  ░░█
#█▓▓██▓▒▒▒░░▒▒▓███████████▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▒▓█▓▓▓▓▓█▓▓▓▓▓▒▒▒▒░░░▒░░▒▓█████▓▒▒░░░░
#  ▒██▓▒▒▒▒▒▒▒░▒▒▓▓█▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████▓██▓▓▒▓▓▓▓▒▓▓▓▓▒▒░░░░░░░▒▒▒▒▒▒▒▒░░░░░
#  ▓███▒▒▒▒▒▓▒▒▒▒░░▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▒▒▓████▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒
#    ██▓▒▒▒▒▒▒▒▒▒▒░▒█████▓▓▓▓▓▓███▓▓▓▓▓▓█▓▓▓▓▓▒▓▒▓▒▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒▒░░░▒
#        ▒▒▒▒▒▒▒▒▒▒▓█████▓▓▓▓▓▓████▓▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░▒
#           ▓▒▒▒▒▒▒██▓▒▒████████████▓▒▒▓▓███▓▓▓▓▓▒▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
#                ▒▒██▓▓▒▓██████████▓░░░░░░▒▒▒▒▒▓▒▒▒░░░░░░░░░░░▒▒░░░░░░▒▒▒▓▓▓▓▒▒▒█
#                  ██▓▒▒▒██████████▓▒▒░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒
#                   ███▓▓████████▓▒▒░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓█
#                     █████████▓  ▒▒▒▒░░░▒▒▒▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒█
#                        █          ▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒███▓▒▒▓
#
#                                  by mathieu
#
##############################################################################################



#import des autres fichiers python

from module_import import *
from scripts import Interface




if __name__ == "__main__" :
    interface = Interface()
    # Création de l'instance de thread MQTT pour s'abonner au différents topics
    # mqtt_thread_handler = MQTTMessageHandler(topics, interface)
    # interface.mqtt_thread_handler = mqtt_thread_handler
    
    # Démarrage des thread
    # mqtt_thread_handler.start()
    interface.start()
    os._exit(1)
    

    