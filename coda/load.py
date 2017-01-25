#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from coda.image_button import *

class Load(QMainWindow):
    '''this class creates game load layout and functions'''

    def __init__(self):
        super().__init__()

    def create_load_layout(self, status):

        print(status)

        pixel_ratio = QWindow().devicePixelRatio()

        #set QWidget class
        self.load_widget = QWidget()

        #set load page background
        self.background_pixmap = QPixmap(':/sys/load_background.png')
        self.background_pixmap = self.background_pixmap.scaledToHeight(
                self.background_pixmap.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.background_pixmap.setDevicePixelRatio(pixel_ratio)
        self.background = QLabel(self.load_widget)
        self.background.setPixmap(self.background_pixmap)
        self.background.setGeometry(0, 0, 1024, 576)

        #create a strat button(temporary)
        self.main_start_button = ImageButton('main_start', self.load_widget)
        self.main_start_button.setGeometry(100, 490, 96, 32)

        #create a back button
        self.load_back_button = ImageButton('load_back', self.load_widget)
        self.load_back_button.setGeometry(844, 490, 96, 32)
