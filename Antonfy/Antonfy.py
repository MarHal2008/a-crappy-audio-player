import sys
import os
import pygame
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from pygame import USEREVENT

pygame.init()
pygame.mixer.init()

path = "./moosic"
tracks = os.listdir(path)


class AntonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.current_index = 0

        pygame.mixer.music.set_endevent(USEREVENT + 1)

        self.playlist = [os.path.join(path, track) for track in tracks]

        self.setGeometry(20, 40, 350, 100)

        left_up_layout = QHBoxLayout()
        time_label = QLabel("an amount of seconds")
        left_up_layout.addWidget(time_label)

        right_up_layout = QVBoxLayout()
        self.track_name = QLabel("Not playing")
        bit_and_mix = QHBoxLayout()
        bitrate_label = QLabel(f"Bitrate: Not found :/")
        sample_rate_label = QLabel(f"Sample Rate: Not found :/")
        bit_and_mix.addWidget(bitrate_label)
        bit_and_mix.addWidget(sample_rate_label)

        volume = QSlider(Qt.Horizontal, self)
        volume.setMinimum(0)
        volume.setMaximum(100)
        right_up_layout.addWidget(self.track_name)
        right_up_layout.addLayout(bit_and_mix)
        right_up_layout.addWidget(volume)

        down_layout = QHBoxLayout()
        previous_btn = QPushButton()
        previous_btn.setIcon(QIcon("icons/BACKWARD.png"))
        previous_btn.clicked.connect(self.play_previous)

        self.play_btn = QPushButton()
        self.play_btn.setIcon(QIcon("icons/PLAY.png"))
        self.play_btn.clicked.connect(self.toggle_play_pause)

        stop_btn = QPushButton()
        stop_btn.setIcon(QIcon("icons/STOP.png"))
        stop_btn.clicked.connect(self.stop_music)

        next_btn = QPushButton()
        next_btn.setIcon(QIcon("icons/FORWARD.png"))
        next_btn.clicked.connect(self.play_next)

        shuffle_btn = QPushButton("Shuffle")

        loop_btn = QPushButton()
        loop_btn.setIcon(QIcon("icons/LOOP.png"))

        down_layout.addWidget(previous_btn)
        down_layout.addWidget(self.play_btn)
        down_layout.addWidget(stop_btn)
        down_layout.addWidget(next_btn)
        down_layout.addWidget(shuffle_btn)
        down_layout.addWidget(loop_btn)
        up_layout = QHBoxLayout()
        up_layout.addLayout(left_up_layout)
        up_layout.addLayout(right_up_layout)

        full_layout = QVBoxLayout()
        full_layout.addLayout(up_layout)
        full_layout.addLayout(down_layout)

        self.setLayout(full_layout)
        self.show()

    def play_track(self, index=None):
        if index is None:
            index = self.current_index

        if 0 <= index < len(self.playlist):
            pygame.mixer.music.load(self.playlist[index])
            pygame.mixer.music.play()
            self.track_name.setText(f"Now playing: {os.path.basename(self.playlist[index])}")
            self.current_index = index

    def play_next(self):
        next_index = (self.current_index + 1) % len(self.playlist)
        self.play_track(next_index)

    def play_previous(self):
        prev_index = (self.current_index - 1) % len(self.playlist)
        self.play_track(prev_index)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.track_name.setText("Not playing")

    def toggle_play_pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
            self.play_btn.setIcon(QIcon("icons/PLAY.png"))


app = QApplication(sys.argv)
anton_app = AntonApp()
sys.exit(app.exec_())

# czy to poprawie? Czy jest to nawet pytanie?
