# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect,render
import gen
from randtaghtml import *
import random
import math
import os
import re
import datetime


# 1. Вычленяем из макета все что можно зарандомить
# 2. Выбираем все переменные из файла. Заменяем их на значение и выводим
# 3. Делаем под каждую переменную функцию
# 4. Создаем несколько макетов кидаем их в папку и выбираем случайный файл при запросе
# ...

def body(request):
	tag = Tag()

	# How sent letter
	count = 1

	counter_file = open('gen/templates/counter.txt','r')
	counter = int(counter_file.read().strip())
	counter_file.close()

	counttext = int(math.ceil(counter/count))

	new_counter = open('gen/templates/counter.txt','w')
	new_counter.write(str(1+counter))
	new_counter.close()

	files_html = os.listdir('gen/templates/body')
	filename = random.choice(files_html)


	a = tag.body(filename=filename,counttext=counttext)

	# a = ''.join(random.sample([tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus')],random.randint(1,7)))
	# fake_tag2 = ''.join(random.sample([tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus'),tag.tag_fake('table',1,'opacity',lang='rus')],random.randint(1,7)))
	
	# a = fake_tag1+tag.tag_general('table',1,lang='rus')+fake_tag2
	# a = tag.tag_general('table',random.randint(1,3))
	# tag.tag_fake('table',1,'opacity')
	# Просто картинки в ссылку обернутую или текст. Бес стилей и прочего. Можно ставить или img или p+a+img или p+img
	# a = tag.tag_simple('img')
	return render_to_response('body.html',{'rand':a})


def proc(request):
	tag = Tag()
	new_html_list = os.listdir('gen/templates/body_raw')
	for html in new_html_list:
		html_this = open('gen/templates/body_raw/'+html,'r').read()

		# Замена всех дата тегов
		data_tag = re.compile(r'(data[-\w*\d*]+=".+?")')
		html_this = data_tag.sub(tag.replace_datatag_raw_body,html_this)

		# Замена всех классов
		class_attr = re.compile(r'(class="\w*\d*")')
		html_this = class_attr.sub(tag.replace_class_raw_body,html_this)

		# Замена шрифтов на _FONT_FAMILY_
		font_family = re.compile(r'(font-family:.+?;)')
		html_this = font_family.sub(tag.replace_fontf_raw_body,html_this)		

		# Замена ссылок на _LINK1_ или _LINK2_
		href_attr = re.compile(r'(a\s*href=".+?")')
		html_this = href_attr.sub(tag.replace_href_raw_body,html_this)

		# Замена картинки на _IMG_
		src_attr = re.compile(r'(img\s*src="http.+?")')
		html_this = src_attr.sub(tag.replace_src_raw_body,html_this)

		# Замена всех не нулевых числовых значений на _DIGIT_100_0_1. Если 0 не заменяем. Если от 10 до 90 - делаем вилку +-3. Если Больше 100 вилку +-13
		# pdb.set_trace()
		digit_html = re.compile(r'(?P<sym1>[\(|"|,|\s*]+)\s*(?P<digit>[0-9]+)\s*(?P<sym>[\)|px|%|;|"|,|px;|]+)')
		html_this = digit_html.sub(tag.replace_digit_raw_body,html_this)

		# Подстановка нескольких _TAB_ между тегами
		tad_temp = re.compile(r'(?P<tab></.+?>|<.+?>)')
		html_this = tad_temp.sub(tag.replace_tabs_raw_body,html_this)

		# # Замена всех пробелов на _SPACES_
		# spaces_temp = re.compile(r'(\s+)')
		# html_this = spaces_temp.sub(tag.replace_spaces_raw_body,html_this)

		# # Замена кавычек на _QOUTE_
		# qoutes_temp = re.compile(r'(["]+)')
		# html_this = qoutes_temp.sub(tag.replace_qoutes_raw_body,html_this)

		html_name = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S_")+str(random.randint(17,28908))+'.html'
		record_html = open('gen/templates/body/'+html_name,'w')
		record_html.write(html_this)
		record_html.close()

	return render_to_response('body.html',{'rand':'Ready'})
