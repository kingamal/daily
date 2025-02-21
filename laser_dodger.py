import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor, QKeyEvent
from PyQt6.QtCore import Qt, QTimer

class LaserDodgerGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laser Dodger")
        self.setGeometry(100, 100, 400, 600)
        self.game_widget = GameWidget(self)
        self.setCentralWidget(self.game_widget)
        self.show()

class GameWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.player_x = 200
        self.player_y = 550
        self.lasers = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(30)
        self.spawn_timer = QTimer(self)
        self.spawn_timer.timeout.connect(self.spawn_laser)
        self.spawn_timer.start(1000)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_player(painter)
        self.draw_lasers(painter)

    def draw_player(self, painter):
        painter.setBrush(QColor(0, 255, 0))
        painter.drawEllipse(self.player_x, self.player_y, 20, 20)

    def draw_lasers(self, painter):
        painter.setBrush(QColor(255, 0, 0))
        for laser in self.lasers:
            painter.drawRect(laser[0], laser[1], 10, 30)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Left:
            self.player_x -= 20
        elif event.key() == Qt.Key.Key_Right:
            self.player_x += 20
        self.update()

    def update_game(self):
        for laser in self.lasers:
            laser[1] += 10
        self.lasers = [laser for laser in self.lasers if laser[1] < 600]
        self.check_collision()
        self.update()

    def spawn_laser(self):
        x = random.randint(0, 790)
        self.lasers.append([x, 0])

    def check_collision(self):
        for laser in self.lasers:
            if (self.player_x < laser[0] < self.player_x + 20 or self.player_x < laser[0] + 10 < self.player_x + 20) and \
               (self.player_y < laser[1] < self.player_y + 20 or self.player_y < laser[1] + 30 < self.player_y + 20):
                self.game_over()

    def game_over(self):
        self.timer.stop()
        self.spawn_timer.stop()
        print("Game Over! You were hit by a laser.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = LaserDodgerGame()
    sys.exit(app.exec())