# -*- coding: utf-8 -*-

import qtMaximHr
import sys
from PyQt5 import PyQt5.QtWidgets

class RPGame(QtWidgets.QMainWindow, qtMaximHr.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.attack.clicked.connect(self.react)
        self.defense.clicked.connect(self.react)
        self.heal.clicked.connect(self.react)
        self.inventory.clicked.connect(self.react)
        self.trade.clicked.connect(self.react)
        self.hp = 100
        self.heal_count = 3
        self.loot_count = 0
        self.lvl = 1
        self.lcdlevel.display(self.lvl)
        self.weapon = 15

    def react(self):
        c = self.sender()
        if c == self.attack:
            pass
        elif c == self.defense:
            pass
        elif c == self.heal:
            if self.heal_count == 0:
                print("no")
            elif self.heal_count != 0:
                self.hp += 30
                if self.hp > 100:
                    self.hp = 100
        elif c == self.inventory:
            pass
        elif c == self.trade:
            pass

    def _on_radio_button_clicked(self, button):
        self.weapon = 0



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    game = RPGame()
    game.show()
    sys.exit(app.exec())