import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox

class CV2app():
    def __init__(self, name, width, height):
        self.windown_name = name
        self.windown_height = height
        self.windown_width = width

        self.buttons = []
        self.slider_value = 50
        self.slider_max = 100

        self.img = np.zeros((self.windown_height, self.windown_width, 3), np.uint8)
        self.setup_ui()
    
    def setup_ui():
        button_width = 150
        button_height = 50
        button_gap = 20

        button_y = self.windown_height // 2 - 100
        button_x = self.windown_width // 2 - 400

        self.button = [
            {"label": "Button 1", "pos": (button_x, button_x +200, button_y, button_y), "color": (200,100,50)}
        ]



cv2.imshow("Chinh anh", bg)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

cv2.destroyAllWindows()