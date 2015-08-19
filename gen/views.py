# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect,render
import gen
from randtaghtml import *
import random
import math
import os


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


