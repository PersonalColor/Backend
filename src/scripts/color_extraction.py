from PIL import Image
import numpy as np
import sys
import json
import os

def spring():
    ivory =  (255, 255, 240) #FFFFF0
    buff = (240, 220, 130) #F0DC82 
    clear_gold = (246, 212, 100) #F6D464
    apricot = (251, 206, 177) # FBCEB1 
    light_orange = (251, 191, 119) #FBBF77
    coral_peach = (255, 179, 142) #FFB38E
    coral_pink = (248, 131, 121) #F88379 
    warm_pink =  (246, 198, 189) #F6C6BD
    bright_red = (255, 22, 12) #FF160C
    orange_red = (255, 69, 0) #FF4500
    periwinkle = (204, 204, 255) #CCCCFF
    medium_turquoise = (72, 209, 204) #48D1CC
    vivid_tangerine = (254, 150, 137) #FE9689
    pink_coral = (230, 91, 96)  
    
    Pure_white = (240, 237, 255) 
    ligh_true_gray=(217, 217, 214)
    charcoal_gray = (54, 69, 79) 
    black = (0, 0, 0)
    navy_blue = (45, 35, 99)
    true_blue = (0, 115, 207)
    lemon_yellow = (254,242,80)#FEF250
    true_green = (16, 119, 26)#10771A
    pine_green = (1, 121, 111) #01796F
    dark_hot_pink = (229, 80, 155) #E5509B
    magenta_night = (197, 34, 124)#C5227C
    royal_purple= (86, 29, 84)#561D5E 
    bright_burgundy= (194, 14, 53)#C20E35 
    true_red = (191, 25, 50) #BF1932
    icy_green = (135, 216, 195) #87D8C3 
    aqua_hint = (230, 252, 254) # E6FCFE
    violet_scent_soft_blue = (188, 198, 223) #BCC6DF
    ice_hot_pink = (228, 189, 194)#E4BDC2 
    icy_blue = (153, 255, 255) #99FFFF

    warm_beige = (216, 188, 171) #D8BCAB
    coffe_brown = (138, 98, 74)  #8A624A 
    dark_chocolate_brown = (51, 36, 33) # 332421
    camel = (193, 154, 107) # C19A6B
    yellow_gold = (241, 207, 59) #F1CF3B
    mustard = (255, 219, 88) #FFDB58
    pumpkin = (255, 117, 24) #FF7518
    deep_peach = (232, 193, 143) #E8C18F
    salmon = (250, 128, 114)#FA8072
    orange = (255, 127, 0) #FF7F00
    orange_red = (255, 69, 0)#FF4500
    lime_green = (159, 193, 49)  #9FC131 
    moss_green = (138, 154, 91)#8A9A5B
    olive_green = (203, 175, 20) #CBAF14
    jade_green = (117, 148, 101)#759465
    
    softwhite = (251, 250, 245) #FBFAF5
    cocoa = (108, 80, 66) #6C5042
    charcoal_blue = (45, 66, 86) #2D4256
    blue_gray = (102, 153, 204) #6699CC
    powder_blue = (176, 224, 230) #B0E0E6
    pastel_aqua = (213, 246, 251 )  #D5F6FB
    lemon_ice_yellow = (246, 226, 167) #F6E2A7
    powder_pink = (236, 178, 179) #ECB2B3
    rose_pink = (255, 102, 204) #FF66CC
    watermelon_red = (218, 91, 110) #DA5B6E
    red_burgundy = (115, 5, 7)  #730507
    mauve_mist = (196, 157, 180) #C49DB4 
    plum = (142, 49, 121) #8E3179

    if rgb == ivory: 
        print(json.dumps({"result": "이 제품의 색상은 ivory 이고, 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == pink_coral:
        print(json.dumps({"result": "이 제품의 색상은 핑크 코랄색 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == buff: 
        print(json.dumps({"result": "이 제품의 색상은 buff 이고  봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb ==  clear_gold: 
        print(json.dumps({"result": "이 제품의 색상은 clear gold 이고  봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == apricot:
        print(json.dumps({"result": "이 제품의 색상은 apricot 이고  봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == light_orange : 
        print(json.dumps({"result": "이 제품의 색상은 light orange 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == coral_peach: 
        print(json.dumps({"result": "이 제품의 색상은 coral orange이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == coral_pink: 
        print(json.dumps({"result": "이 제품의 색상은 coral pink 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == warm_pink: 
        print(json.dumps({"result": "이 제품의 색상은 warm pink 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == bright_red:
        print(json.dumps({"result": "이 제품의 색상은 bright pink 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == orange_red: 
        print(json.dumps({"result": "이 제품의 색상은 orange red 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == periwinkle: 
        print(json.dumps({"result": "이 제품의 색상은 periwinkle 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == medium_turquoise: 
        print(json.dumps({"result": "이 제품의 색상은 medium turquoise 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == vivid_tangerine:
        print(json.dumps({"result": "이 제품의 색상은 vivid_tangerine 이고 봄 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == Pure_white: 
        print(json.dumps({"result": "이 색상은 Pure white이고 회색 주황색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == ligh_true_gray: 
        print(json.dumps({"result": "이 색상은 light gray 이고 밝은 회색톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == charcoal_gray: 
        print(json.dumps({"result": "이 색상은 charcoal gray 이고 짙은 회색의 파란색톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == black: 
        print(json.dumps({"result": "이 색상은 Perfect Black 이고, 검정톤입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == navy_blue: 
        print(json.dumps({"result": "이 색상은 navy blue로 둔한 네이비 톤입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == true_blue: 
        print(json.dumps({"result": "이 색상은 true blue로 생생한 파란색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == lemon_yellow: 
        print(json.dumps({"result": "이 색상은 lemon yellow 로 선명한 노란색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == true_green: 
        print(json.dumps({"result": "이 색상은 TRUE GREEN 로 깊은 녹색톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == pine_green: 
        print(json.dumps({"result": "이 색상은 pine green 로 강한 청록색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == dark_hot_pink: 
        print(json.dumps({"result": "이 색상은 dark hot pink 로 선명한 핑크 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == magenta_night: 
        print(json.dumps({"result": "이 색상은 magenta night로 생생한 핑크 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == royal_purple: 
        print(json.dumps({"result": "이 색상은 royal purple 이고 깊은 핑크 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == bright_burgundy: 
        print(json.dumps({"result": "이 색상은 bright burgundy 이고 강한 빨간색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == true_red: 
        print(json.dumps({"result": "이 색상은 true red이고 강한 빨간색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == icy_green: 
        print(json.dumps({"result": "이 색상은 ice green이고 , 밝은 청록색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == aqua_hint: 
        print(json.dumps({"result": "이 색상은 aqua hint이고, 창백한 청록색 톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == violet_scent_soft_blue: 
        print(json.dumps({"result": "이 색상은 Violet Scent Soft Blue Color이고, 창백한 네이비톤 입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == ice_hot_pink: 
        print(json.dumps({"result": "이 색상은 ice hot pink 이고, 창백한 빨간색 톤입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == icy_blue:
        print(json.dumps({"result": "이 색상은 ice blue이고 창백한 청록색 톤입니다. 겨울 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == warm_beige: 
        print(json.dumps({"result": "이 색상은 warm beige이고 밝은 회색 주황색 톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == coffe_brown: 
        print(json.dumps({"result": "이 색상은 coffe brown 이고 회색 주황색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == dark_chocolate_brown: 
        print(json.dumps({"result": "이 색상은 dark chocolate brown 이고 짙은 회색의 빨간색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == camel: 
        print(json.dumps({"result": "이 색상은 camel 이고 부드러운 주황색 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == yellow_gold: 
        print(json.dumps({"result": "이 색상은 yellow gold 이고 선명한 주황색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == mustard: 
        print(json.dumps({"result": "이 색상은 mustard 이고 밝은 주황색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == pumpkin: 
        print(json.dumps({"result": "이 색상은 pumpkin 이고 생생한 주황색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == deep_peach : 
        print(json.dumps({"result": "이 색상은 deep peach  이고 창백한 주황색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == orange_red: 
        print(json.dumps({"result": "이 색상은 orange_red 이고 생생한 빨간색 톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == orange: 
        print(json.dumps({"result": "이 색상은 orange 이고 생생한 주황색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == salmon: 
        print(json.dumps({"result": "이 색상은 salmon 이고 빛 빨간색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")       
    elif rgb == lime_green: 
        print(json.dumps({"result": "이 색상은 lime green 이고 둔한 연두색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == moss_green: 
        print(json.dumps({"result": "이 색상은 moss green이고 회색 연두색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == olive_green: 
        print(json.dumps({"result": "이 색상은 olive green 이고 강한 노란색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")    
    elif rgb == jade_green : 
        print(json.dumps({"result": "이 색상은 jade green  이고 회색 녹색톤 입니다. 가을 웜톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == softwhite: 
        print(json.dumps({"result": "이 색상은 soft white 이고 흰색 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == cocoa: 
        print(json.dumps({"result": "이 색상은 cocoa brown 이고 짙은 회색의 빨간색 톤 입니다. 여름 쿨톤톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == charcoal_blue: 
        print(json.dumps({"result": "이 색상은 charcoal blue 이고 회색 파란색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == blue_gray: 
        print(json.dumps({"result": "이 색상은 gray blue 이고 밝은 파란색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == powder_blue: 
        print(json.dumps({"result": "이 색상은 powder blue 이고 창백한 청록색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == pastel_aqua : 
        print(json.dumps({"result": "이 색상은 pastel aqua 이고 창백한 청록색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == lemon_ice_yellow : 
        print(json.dumps({"result": "이 색상은 lemon ice yellow 이고 창백한 주황색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == powder_pink: 
        print(json.dumps({"result": "이 색상은 powder pink 이고 창백한 빨간색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == rose_pink: 
        print(json.dumps({"result": "이 색상은 rose pink 이고 선명한 핑크톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")       
    elif rgb == watermelon_red: 
        print(json.dumps({"result": "이 색상은 watermelon red 이고 선명한 빨간색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == red_burgundy: 
        print(json.dumps({"result": "이 색상은 red burgundy 이고 깊은 빨간색 톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")    
    elif rgb == mauve_mist : 
        print(json.dumps({"result": "이 색상은 mauve mist 이고 창백한 핑크톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    elif rgb == plum : 
        print(json.dumps({"result": "이 색상은 plum 이고 강한 핑크톤 입니다. 여름 쿨톤 분들에게 잘 어울리는 색상입니다."}), end="")
    else:
        print(json.dumps({"result": "제품의 주요 색이 사진의 중앙에 오도록 배치해주세요."}))

def winter():
    pass

def fall():
    pass

def summer(): 
    pass

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print(json.dumps({"result": "인자가 충분하지 않음"}), end="")
        exit(0)

    img = Image.open(os.getcwd() + "/temp/" + sys.argv[1]) #image 읽어오기 #이미지 정보 array로 변환
    img_resize = img.resize((512,512))# 사진 크기 바꾸기
    rgb_im = img_resize.convert('RGB')
    rgb = rgb_im.getpixel((216,216))

    spring()
    summer()
    fall()
    winter()
