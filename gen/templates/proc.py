# -*- coding: utf-8 -*-
import random
import math
import os
import re
import datetime
import pdb



def replace_digit_raw_body(match):
		sym = match.group('sym')
		digit = match.group('digit')
		if int(digit) in range(10,90):
			new_digit = '_DIGIT_'+digit+'_3_3_'+sym
		elif int(digit)>100:
			new_digit = '_DIGIT_'+digit+'_13_13_'+sym
		else:
			new_digit = digit+sym			
		return new_digit

def proc():
	new_html_list = os.listdir('body_raw')
	for html in new_html_list:
		html_this = open('body_raw/'+html,'r').read()		
		# Замена всех не нулевых числовых значений на _DIGIT_100_0_1. Если 0 не заменяем. Если от 10 до 90 - делаем вилку +-3. Если Больше 100 вилку +-13
		digit_html = re.compile(r'(?P<digit>[0-9]+)\s*(?P<sym>[\)|px|%|;|"|,]+)')
		# pdb.set_trace()
		html_this = digit_html.sub(replace_digit_raw_body,html_this)

		# Замена всех дата тегов
		# Замена всех классов
		# Замена шрифтов на _FONT_FAMILY_
		# Подстановка нескольких _TAB_ между тегами
		# Замена всех пробелов на _SPACES_
		html_name = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S_")+str(random.randint(17,289))+'.html'
		record_html = open('body/'+html_name,'w')
		record_html.write(html_this)
		record_html.close()

	print 'ok'
	return True

proc()