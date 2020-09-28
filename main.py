from core.monde import Monde
from GUI import PygameGui


if __name__ == '__main__':
    monde = Monde((20,20))
    gui = PygameGui(monde,(700,700))
    gui.start()
    print("Programme fini")

