'''
#BAI 4
class Time():
    def __init__(self, time_second):
        self.time_second = time_second

    def convert_to_minutes(self):
        minutes = self.time_second // 60
        seconds_m = self.time_second % 60
        return f"{minutes}:{seconds_m}"


    def convert_to_hours(self):
        hours = self.time_second // 3600
        minutes_h = (self.time_second % 3600) // 60
        seconds_h = self.time_second % 60
        return f"{hours}:{minutes_h}:{seconds_h}"


print(Time(91).convert_to_minutes())
print(Time(3711).convert_to_hours())

#BAI 5
class Wordplay():
    def __init__(self, list_of_words):
        self.list_of_words = list_of_words

    def words_with_length(self, length):
        word_len = []
        for i in self.list_of_words:
            if len(i) == length:
                word_len.append(i)
        return print(word_len)

    def starts_with_s(self):
        word_start_with_s = []
        for i in self.list_of_words:
            if i.startswith("s"):
                word_start_with_s.append(i)
        return print(word_start_with_s)

    def ends_with_s(self):
        word_end_with_s = []
        for i in self.list_of_words:
            if i.endswith('s'):
                word_end_with_s.append(i)
        return print(word_end_with_s)

    def palindromes(self):
        word_palindromes = []
        for i in self.list_of_words:
            if i == i[::-1]:
                word_palindromes.append(i)
        return print(word_palindromes)

    def only(self, L):
        allowed = list(L)
        word_allowed = []
        for i in self.list_of_words:
            for j in i:
                if j in allowed:
                    word_allowed.append(i)
                    break
        return print(word_allowed)

    def avoids(self, L):
        forbidden = set(L)
        result = [word for word in self.list_of_words if not any(char in forbidden for char in word)]
        return print(result)

Wordplay = Wordplay(["world", "level", "python", "madam", "racecar", 'thinh', 'tran', 'van', 'sexual',
                      'simple', 'simpson', 'stress'])

words_with_length = Wordplay.words_with_length(5)
starts_with_s = Wordplay.starts_with_s()
ends_with_s = Wordplay.ends_with_s()
palindromes = Wordplay.palindromes()
only = Wordplay.only('abc')
avoids = Wordplay.avoids('abc')


#BAI 6
class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit      

        self._to_meters = {'inches': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'miles': 1609.344,
            'kilometers': 1000,
            'meters': 1,
            'centimeters': 0.01,
            'millimeters': 0.001} 

        self._from_meters = {'inches': 39.3701,
            'feet': 3.28084,
            'yards': 1.09361,
            'miles': 0.000621371,
            'kilometers': 0.001,
            'meters': 1,
            'centimeters': 100,
            'millimeters': 1000}

        if self.unit not in self._to_meters:
            raise ValueError(f"đơn vị '{unit}' không được hỗ trợ")
    
    def _convert_to_meters(self):
        return self.length * self._to_meters[self.unit]
    
    def _convert_from_meters(self, target_unit):
        meters = self._convert_to_meters()
        return meters * self._from_meters[target_unit]
    
    def inches(self):
        return self._convert_from_meters('inches')
    
    def feet(self):
        return self._convert_from_meters('feet')
    
    def yards(self):
        return self._convert_from_meters('yards')
    
    def miles(self):
        return self._convert_from_meters('miles')
    
    def kilometers(self):
        return self._convert_from_meters('kilometers')
    
    def meters(self):
        return self._convert_from_meters('meters')
    
    def centimeters(self):
        return self._convert_from_meters('centimeters')
    
    def millimeters(self):
        return self._convert_from_meters('millimeters')

c0 = Converter(9, 'inches')
print(f"9 inches = {c0.feet()} feet")
print(f'9 inches = {c0.meters()} meters')
c1 = Converter(200, 'meters')
print(f'200 meters = {c1.feet()} feet')
print(f'200 meters = {c1.inches()} inches')
print(f'200 meters = {c1.kilometers()} kilometers')
c2 = Converter(1000, 'millimeters')
print(f"1000 mm = {c2.meters()} meters")

#Bài 7
import random
import numpy as np
import matplotlib.pyplot as plt
class Rock_paper_scissors():
    def __init__(self):
        self.tong_vong_choi = 0
        self.vong_choi_hien_tai = 1
        self.so_tran_thang_cua_nguoi_choi = 0
        self.so_tran_thang_cua_computer = 0
        self.choices = ['keo', 'bua', 'bao']

    def play(self):

        dieu_kien_win = {'keo': 'bao', 'bua': 'keo', 'bao': 'bua'}
        while self.so_tran_thang_cua_computer < 3 and self.so_tran_thang_cua_nguoi_choi < 3:
            player_choice = input("Chọn keo, bua hoặc bao: ")
            computer_choice = random.choice(self.choices)
            print(f"Computer chose: {computer_choice}")
            if player_choice not in self.choices:
                print('chon lai di')
                continue
            if computer_choice == dieu_kien_win[player_choice]:
                self.so_tran_thang_cua_nguoi_choi += 1
                self.vong_choi_hien_tai += 1
                self.tong_vong_choi += 1
                print("YOU WIN")

            elif computer_choice == player_choice:
                self.vong_choi_hien_tai += 1
                self.tong_vong_choi += 1
                print("DRAW")

            else:
                self.so_tran_thang_cua_computer += 1
                self.vong_choi_hien_tai += 1
                self.tong_vong_choi += 1
                print("YOU LOSE")
            print(f'so vong choi hien tai: {self.vong_choi_hien_tai}')
            print(f"So tran thang cua nguoi choi: {self.so_tran_thang_cua_nguoi_choi}")
            print(f"So tran thang cua computer: {self.so_tran_thang_cua_computer}")
            print("_____________________________________________________________________")
        print(f"Total rounds played: {self.tong_vong_choi}")
        if self.so_tran_thang_cua_nguoi_choi > self.so_tran_thang_cua_computer:
            print("YOU WIN THE GAME")
        elif self.so_tran_thang_cua_nguoi_choi < self.so_tran_thang_cua_computer:
            print("YOU LOSE THE GAME")
        else:
            print("DRAW THE GAME")

game = Rock_paper_scissors()
game.play()
'''

class Standard_deck():
    def 



