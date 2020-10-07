 # importation des modules necessaires
from core.monde import Monde
from GUI import PygameGui


#lancement des programmes
if __name__ == '__main__':
    monde = Monde((70,70))
    gui = PygameGui(monde,(700,700))
    gui.start()
    print("Programme fini")


