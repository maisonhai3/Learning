# -*- coding: utf-8 -*-
import os
import numpy as np
from PIL import Image
import cv2
import struct


# haims: don't worry about this block. It's perfect.
def loop_gnt_dir(gnt_dir=str_training_data_dir):
    def extract_file_info(filename):
        header_size = 10
        # the main loop
        while True:
            header = np.fromfile(filename, dtype='uint8', count=header_size)
            if not header.size:
                break
            # check size of data
            sample_size = header[0] \
                              + (header[1] << 8) \
                              + (header[2] << 16) \
                              + (header[3] << 24)
            width         = header[6] \
                              + (header[7] << 8)
            height        = header[8] \
                              + (header[9] << 8)
            if header_size + width * height != sample_size:
                break

            np_hw_image = np.fromfile(filename, dtype='uint8', count=width * height).reshape((height, width))
            tag_code = header[5] + (header[4] << 8)
            yield np_hw_image, tag_code

    for file_name in os.listdir(gnt_dir):
        if file_name.endswith('.gnt'):
            file_path = os.path.join(gnt_dir, file_name)
            with open(file_path, 'rb') as f:
                for np__hw_image, tagcode in extract_file_info(f):
                    yield np__hw_image, tagcode

def resize_padding(np_hw_image):
    # HBLab - Haims
    #TODO: this doesn't work properly
    np_hw_image = Image.fromarray(np_hw_image, 'L')
    np_hw_image = cv2.copyMakeBorder(np_hw_image, 20, 20, 20, 20, cv2.BORDER_CONSTANT)
    np_hw_image.resize((94, 94))
    return image

def tagcode_to_unicode(str_tagcode):
    # HBLab - Haims
    unicode_tag = struct.pack('>H', tagcode).decode('gb2312', 'ignore')
    return unicode_tag


### driving code ###
str_interfering_characters = '''
一丁下三不天五民正平可再百否武夏中内出本世申由史冊央向曲印州表果半必永求九丸千久少夫午失末未包年危后兵我束卵承垂刷重省看勉七乳才予事二元亡六主市交忘夜育京卒商率就人化今仁付代仕他令以合全任休件仲作何位住余低似命使念例供信保便値修借候倍俳俵健停働像先入八分公共弟並典前益善尊同周次兆冷弱刀切別判制券刻副割力加助努勇勤句北疑十古孝直南真裁博上反灰厚原台能友収口司右兄吸告君味呼品唱器四回因困固土去地在寺均志坂幸型城基域喜境士冬各夕外名多大太奏女好始妻姉妹姿子存安字守宅宇完定官宙宗室客宣家害案容宮寄密宿寒富察寸小光常堂尺局居屋展山岸岩炭川工左功己改布希干刊幼序店底府度座席庭康延建式弓引強形役往径待律徒得街心快性忠急恩情感想成戸所手打投折技批招持指拾接推探授提操支政故教救散敬文新方放旅族旗日早明易昔春星昨映昭最量景晴暗暖暴曜月木札材村板林松枚枝相査染柱格校根株械植棒森模歌止整死列段母毒比毛氏水池汽法治波油注河泣沿泳洋活派洗流消酒浴深混清液港測湖源演潮激火然照熟燃受父片版牛物牧特犬犯王玉班理球望生用田男町思界胃留略病痛登白的皇泉皮皿盛盟目具眼矢知短石砂破磁示祭禁利私和委季科秋秒移税程穴究空立童竹笑第笛等答策筋算管箱米料粉精糖素置罪羊美差着群羽翌老考耕耳取有肉服肥背肺胸期朝腹臣自息至舌航船良色花苦若英芽草茶荷菜落幕墓蒸暮血行衣初西要票角解言警谷欲豆象赤走起足路身射返近述送追退逆迷通速造道郡部配酸番里野防限院降除陛障集雨雪青非悲面革音章意食首骨高
''' # haims: using 600 characters which are inferences between Chinese and Japanese

str_data_dir = '../data'
str_training_data_dir = os.path.join(str_data_dir, 'Gnt1.1Train')
str_output_dir_name = '../data/train/'

for image, tagcode in loop_gnt_dir(gnt_dir=str_training_data_dir):
    unicode_tag = tagcode_to_unicode(tagcode)
    if unicode_tag in str_interfering_characters:
        # Haims: writing images to files
        image = resize_padding(image)
        str_filename = str_output_dir_name + unicode_tag + '.png'
        image.save(str_filename)
