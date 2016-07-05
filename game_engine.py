#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button import *
from fader import *
from fader_widget import *
from letter_print import *
from effect import *
from background import *
from portrait import *
from parser import *

import sys
import resources

class GameEngine(QMainWindow):
    '''this class creates game engine layout and functions'''

    def __init__(self):
        super().__init__()

    def create_game_engine_layout(self, game_engine_id):

        self.script = ':/totono.xml'
        self.game_engine_id = game_engine_id
        print(self.game_engine_id)

        #set game status
        self.init_status = True
        self.effect_status = False

        #set QWidget class
        self.game_engine_widget = QWidget()
        self.basic_widget = QWidget(self.game_engine_widget)
        self.text_box_widget = QWidget(self.game_engine_widget)
        self.menu_widget = QWidget(self.game_engine_widget)

        #create basic layout
        #create background label
        self.background = Background(self.basic_widget)

        #create disable hide label to show all widget
        self.disable_hide_label = QLabel(self.basic_widget)
        self.disable_hide_label.setGeometry(0, 0, 960, 540)

        #create text box layout
        #create text background label
        self.text_background_pixmap = QPixmap(':/text_background.png')
        self.text_background_pixmap.setDevicePixelRatio(2)
        self.text_background_label = QLabel(self.text_box_widget)
        self.text_background_label.setPixmap(self.text_background_pixmap)
        self.text_background_label.setGeometry(0, 340, 960, 200)

        #set the text character label
        self.text_font = QFont('Noto Sans CJK TC Regular', 18)
        self.text_character_label = QLabel(self.text_box_widget)
        self.text_character_label.setFont(self.text_font)
        self.text_character_label.setAlignment(Qt.AlignLeft)
        self.text_character_label.setGeometry(90, 390, 695, 30)
        self.text_character_label.setStyleSheet('QLabel {color: rgba(255, 255, 255, 100%)}')

        #set the text box label
        self.text_font = QFont('Noto Sans CJK TC Regular', 16)
        self.text_box_label = LetterPrint(self.text_box_widget)
        self.text_box_label.setFont(self.text_font)
        self.text_box_label.setAlignment(Qt.AlignLeft)
        self.text_box_label.setGeometry(100, 430, 685, 100)
        self.text_box_label.setStyleSheet('QLabel {color: rgba(255, 255, 255, 100%)}')
        self.text_box_label.setWordWrap(True)

        #create transparent label to add game engine id(next)
        self.next_label = QLabel(self.text_box_widget)
        self.next_label.setGeometry(0, 0, 960, 540)

        #create a auto button
        self.auto_button = ImageButton('auto', self.text_box_widget)
        self.auto_button.setGeometry(810, 435, 35, 35)

        #create a skip button
        self.skip_button = ImageButton('skip', self.text_box_widget)
        self.skip_button.setGeometry(855, 435, 35, 35)

        #create a log button
        self.log_button = ImageButton('log', self.text_box_widget)
        self.log_button.setGeometry(900, 435, 35, 35)

        #create a save button
        self.save_button = ImageButton('save', self.text_box_widget)
        self.save_button.setGeometry(810, 480, 35, 35)

        #create a load button
        self.load_button = ImageButton('load', self.text_box_widget)
        self.load_button.setGeometry(855, 480, 35, 35)

        #create a menu button
        self.menu_button = ImageButton('menu', self.text_box_widget)
        self.menu_button.setGeometry(900, 480, 35, 35)

        #create a hide button
        self.hide_button = ImageButton('hide', self.text_box_widget)
        self.hide_button.setGeometry(760, 400, 25, 25)

        #create effect label
        self.effect = Effect(self.basic_widget)

        #create menu layout
        #create menu background
        self.menu_background_pixmap = QPixmap(':/menu_background.png')
        self.menu_background_pixmap.setDevicePixelRatio(2)
        self.menu_background_label = QLabel(self.menu_widget)
        self.menu_background_label.setPixmap(self.menu_background_pixmap)
        self.menu_background_label.setGeometry(0, 0, 960, 540)

        #create back button
        self.back_button = ImageButton('menu_back', self.menu_widget)
        self.back_button.setGeometry(400, 64, 160, 55)

        #create title button
        self.title_button = ImageButton('menu_title', self.menu_widget)
        self.title_button.setGeometry(400, 183, 160, 55)

        #create config button
        self.config_button = ImageButton('menu_config', self.menu_widget)
        self.config_button.setGeometry(400, 302, 160, 55)

        #create exit button
        self.exit_button = ImageButton('menu_exit', self.menu_widget)
        self.exit_button.setGeometry(400, 421, 160, 55)

        #hide widget
        self.menu_widget.hide()
        self.text_box_widget.hide()
        self.disable_hide_label.hide()
        self.effect.hide()

        #connection
        self.back_button.clicked.connect(self.hide_menu)
        self.menu_button.clicked.connect(self.show_menu)
        self.hide_button.clicked.connect(self.hide_widget)
        self.disable_hide_label.mousePressEvent = self.show_widget
        self.next_label.mousePressEvent = self.update

        #set parser
        self.parser = Parser()
        self.init_parser()

    ################################################## MAIN PROGRAM START ##################################################

    def init_parser(self):

        print('init_parser')

        self.parser.parse(self.script, self.game_engine_id)

        self.bgm_id = self.parser.bgm_id

        self.sd_id = self.parser.sd_id

        self.eff_id = self.parser.eff_id
        self.eff_du = self.parser.eff_du

        self.bg_id = self.parser.bg_id
        self.bg_x = self.parser.bg_x
        self.bg_y = self.parser.bg_y
        self.bg_xf = self.parser.bg_xf
        self.bg_yf = self.parser.bg_yf
        self.bg_du = self.parser.bg_du

        self.pt_id = self.parser.pt_id
        self.pt_x = self.parser.pt_x
        self.pt_y = self.parser.pt_y
        self.pt_xf = self.parser.pt_xf
        self.pt_yf = self.parser.pt_yf

        self.tb_sh = self.parser.tb_sh
        self.tb_td = self.parser.tb_td
        self.tb_vc = self.parser.tb_vc
        self.tb_char = self.parser.tb_char
        self.tb_txt = self.parser.tb_txt
        self.tb_hi = self.parser.tb_hi

        self.init_background_music()

    def init_background_music(self):

        print('init_background_music')

        self.init_sound()

    def init_sound(self):

        print('init_sound')

        self.init_effect()

    def init_effect(self):

        print('init_effect')

        if self.eff_id != '':

            self.background.timeline.stop()
            self.next_label.hide()

            if not self.init_status:
                self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
                self.fader.fade(1500)

            self.init_status = False
            self.effect.show()
            self.effect.create(self.eff_id)
            QTimer.singleShot(int(self.eff_du), self.hide_effect)

        else:
            self.effect_status = False
            self.init_background()

    def init_background(self):

        print('init_background')

        if self.bg_id != '':

            if not self.effect_status:
                self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
                self.fader.fade(500)

            if self.bg_du != '':
                self.background.create_mv_bg(self.bg_id, int(self.bg_x), int(self.bg_y), int(self.bg_xf), int(self.bg_yf), int(self.bg_du))
            else:
                self.background.create_bg(self.bg_id)

        print(self.bg_id)

        self.init_portrait()

    def init_portrait(self):

        print('init_portrait')

        self.init_text_box()

    def init_text_box(self):

        print('init_text_box')

        if self.tb_sh != '':
            self.show_text_box()

        else:
            self.init_voice()

    def init_voice(self):

        print('init_voice')

        self.init_text()

    def init_text(self):

        print('init_text')

        if self.tb_char != '':
            if self.tb_char == 'del':
                self.text_character_label.clear()
            else:
                self.text_character_label.setText(self.tb_char)

        self.text_box_label.set_text(self.tb_txt)

    def update(self, event):

        print('update')

        self.game_engine_id += 1
        print(self.game_engine_id)

        self.set_background_music()

    def set_background_music(self):

        print('set_background_music')

        self.set_sound()

    def set_sound(self):

        print('set_sound')

        self.set_voice()

    def set_voice(self):

        print('set_voice')

        self.set_text()

    def set_text(self):

        print('set_text')

        self.text_character_label.clear()
        self.text_box_label.clear()

        self.set_portrait()

    def set_portrait(self):

        print('set_portrait')

        self.set_text_box()

    def set_text_box(self):

        print('set_text_box')

        if self.tb_hi != '':
            self.hide_text_box()

        else:
            self.init_parser()

    ################################################## MAIN PROGRAM END ##################################################

    def hide_menu(self):

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)
        self.menu_widget.hide()
        self.text_box_widget.show()

    def show_menu(self):

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)
        self.menu_widget.show()
        self.text_box_widget.hide()

    def hide_widget(self):

        self.hide_button.setEnabled(False)
        self.fader_widget = FaderWidget(self.text_box_widget, 1.0)
        self.fader_widget.hide(250)
        self.fader_widget.timeline.finished.connect(self.finsh_hide)

    def finsh_hide(self):

        self.text_box_widget.hide()
        self.disable_hide_label.show()

    def show_widget(self, event):

        self.text_box_widget.show()
        self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
        self.fader_widget.show(250)
        self.fader_widget.timeline.finished.connect(self.finish_show)

    def finish_show(self):

        self.disable_hide_label.hide()
        self.hide_button.setEnabled(True)

    def hide_effect(self):

        self.effect_status = True
        self.next_label.show()
        self.text_box_label.clear()
        self.text_character_label.clear()

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(1500)

        self.effect.hide()
        self.init_background()

    def show_text_box(self):

        self.next_label.hide()
        self.hide_button.setEnabled(False)

        if self.tb_td != '':
            QTimer.singleShot(int(self.tb_td), self.delay_show_text_box)

        else:
            self.text_box_widget.show()
            self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
            self.fader_widget.show(400)
            self.fader_widget.timeline.finished.connect(self.finish_show_text_box)

    def delay_show_text_box(self):

        self.text_box_widget.show()
        self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
        self.fader_widget.show(400)
        self.fader_widget.timeline.finished.connect(self.finish_show_text_box)

    def finish_show_text_box(self):

        self.disable_hide_label.hide()
        self.next_label.show()
        self.hide_button.setEnabled(True)
        self.init_voice()

    def hide_text_box(self):

        self.next_label.hide()
        self.disable_hide_label.hide()
        self.hide_button.setEnabled(False)
        self.fader_widget = FaderWidget(self.text_box_widget, 1.0)
        self.fader_widget.hide(400)
        self.fader_widget.timeline.finished.connect(self.finsh_hide_text_box)

    def finsh_hide_text_box(self):

        self.next_label.show()
        self.text_box_widget.hide()
        self.init_parser()