from core.monde import Monde
from GUI import PygameGui


if __name__ == '__main__':
    monde = Monde()
    gui = PygameGui(monde,(700,700))
    gui.start()
    print("Programme fini")