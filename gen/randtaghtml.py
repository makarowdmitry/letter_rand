# -*- coding: utf-8 -*-
import string
import random
import re



class Tag():
	spaces = [' ','']
	spaces_words = [' ','   ','  ']
	tabs = ['\n','','\n\n','\t','\t\n','\n\n\n\n','\n\n\n']
	punctuation = [',','!','?','.','.','.',',','','','-',';',':']
	br_tag=['<br >','<br/>','<br>','','']
	

	tag = {
	'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
	'td':['align','valign','width','id','class','border','style'],
	'a':['align','valign','width','id','class','border','style'],
	'img':['align','valign','width','id','class','border','style'],
	'tr':[],
	'tbody':[],
	}

	def word_gen(self,count,lang='eng'):
		words =''
		for i,ws in enumerate(range(count)):
			if lang and lang=='eng':
				vowels = ['e','y','u','i','o','a']
				consonants = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
			else:
				vowels = ['а','у','е','ы','о','э','я','и','ю','ё']
				consonants = ['й','ц','к','н','г','ш','щ','з','х','ъ','ф','в','п','р','л','д','ж','ч','с','м','т','ь','б']

			word = ''
			for w in range(random.randint(1,2)):
				abc_list = [''.join(random.sample(vowels,random.randint(1,2))), ''.join(random.sample(consonants,random.randint(1,2)))]
				random.shuffle(abc_list)
				word += ''.join(abc_list)

			if i>0:
				words+=word+random.choice(self.spaces_words)
				if i%4==0:
					words+=random.choice(self.punctuation)
			else:
				words+=word
		return words

	def style_gen(self,opacity="no",attr_effect='yes'):
		# Атрибуты и значения не влияющие на отображение
		if attr_effect=="no":
			attr = {
			'align':random.choice(['']),
			'width': random.choice(['auto','inherit','']),
			'border':'0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'padding':random.choice(['inherit',str(random.randint(0,3))+'px', str(random.randint(0,3))+'px'+str(random.randint(0,3))+'px'+str(random.randint(0,3))+'px'+str(random.randint(0,3))+'px']),
			# 'color':random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'font-family':random.choice(['Helvetica, Arial, sans-serif','Arial','Tahoma','Verdana','Helvetica']),
			'font-style':random.choice(['normal','italic','oblique','inherit']),
			'background-color': '' ,#random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'font-size':random.choice([str(random.randint(7,18))+random.choice(['px']),'inherit', 'x-small', 'small', 'medium', 'large']),
			'font-weight':random.choice(['bold','bolder','lighter','normal','100','200','300','400','500','600','700','800','900']),
			'height':random.choice(['auto','inherit','']),
			'border-top':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')'])]),
			'border-bottom':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')'])]),
			'border-left':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')'])]),
			'border-right':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')'])]),
			'line-height':random.choice(['normal','inherit','']),
			'display':random.choice(['block','']),
			# 'opacity':str(random.random()),
			}

		else:
			attr = {
			'align':random.choice(['center','left','right','']),
			'width': random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
			'border':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'padding':random.choice(['inherit',str(random.randint(0,23))+random.choice(['px','%']), str(random.randint(0,23))+random.choice(['px ','% '])+str(random.randint(0,23))+random.choice(['px ','% '])+str(random.randint(0,23))+random.choice(['px ','% '])+str(random.randint(0,23))+random.choice(['px ','% '])]),
			'color':random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'font-family':random.choice(['Helvetica, Arial, sans-serif','Arial','Tahoma','Verdana','Helvetica']),
			'font-style':random.choice(['normal','italic','oblique','inherit']),
			'background-color':random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'font-size':random.choice([str(random.randint(3,18))+random.choice(['px','pt']),str(random.randint(73,216))+'%','inherit','xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']),
			'font-weight':random.choice(['bold','bolder','lighter','normal','100','200','300','400','500','600','700','800','900']),
			'height':random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
			'border-top':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'border-bottom':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'border-left':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'border-right':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'line-height':random.choice(['normal','inherit',str(random.randint(0,20))+'px',str(random.randint(0,4))+'%',str(random.randrange(0,2))]),
			'display':random.choice(['inline-block','block','none','inline','inline-table','list-item','run-in','table','table-caption','table-cell','table-column','table-row','table-row-group','table-footer-group','table-header-group','table-column-group']),
			# 'opacity':str(random.random()),
			}

		# Случайное количество атрибутов
		count_random = random.randint(0,round(len(attr.keys())/2))

		if opacity=="opacity":
			# Удаляем из словаря display и opacity
			attr.pop('display')
			# attr.pop('opacity')
			attr_style = attr.keys()[:count_random]
			attr['display'] = 'none'
			attr['opacity'] = '0'
			# attr_style+=[random.choice(['display','opacity'])]
			attr_style+=['display']+['opacity']



		else:
			attr_style = attr.keys()[:count_random]


		# Выбираем случайные атрибуты и рандомим их если больше одного
		if len(attr_style)>0:
			random.shuffle(attr_style)

		# Формируем строку из атрибутов и их значений
		list_attr = []
		for a in attr_style:
			qoutes = random.choice(['\'','\"'])
			a = random.choice(self.spaces)+a+random.choice(self.spaces)+':'+random.choice(self.spaces)+attr[a]+random.choice(self.spaces)+';'
			list_attr.append(a)

		string_style = ' '.join(list_attr)
		return string_style


	def attr_gen(self,tagname,opacity="no",attr_effect='yes'):
		if attr_effect=="no":
			# Атрибуты и значения не влияющие на отображение
			tag_this = {
			'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
			'td':['align','valign','width','id','class','border','style'],
			'tr':[],
			'tbody':[],
			'a':['align','valign','width','id','class','border','style'],
			'img':['align','valign','width','id','class','border','style'],
			}

			attr = {
			'dir':random.choice(['auto','']),
			'align':random.choice(['']),
			'valign':random.choice(['']),
			'width': random.choice(['auto','inherit','']),
			'cellpadding':'0',
			'cellspacing':'0',
			'border':'0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'style':self.style_gen(attr_effect='no'),
			'id':self.word_gen(1,'eng'),
			'class':self.word_gen(1,'eng'),
			}

		else:
			tag_this = {
			'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
			'td':['align','valign','width','id','class','border','style'],
			'tr':[],
			'tbody':[],
			'a':['align','valign','width','id','class','border','style'],
			'img':['align','valign','width','id','class','border','style'],
			}

			attr = {
			'dir':random.choice(['ltr','rtl','auto','']),
			'align':random.choice(['center','left','right','']),
			'valign':random.choice(['top','middle','bottom','baseline','']),
			'width': random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
			'cellpadding':str(random.randint(0,5)),
			'cellspacing':str(random.randint(0,5)),
			'border':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' '+random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'style':self.style_gen(),
			'id':self.word_gen(1,'eng'),
			'class':self.word_gen(1,'eng'),
			}


		count_random = random.randint(0,len(tag_this[tagname]))

		if opacity=="opacity":
					
			# Удаляем из словаря style
			attr.pop('style')
			tag_this[tagname].pop(6)

			attr_tags = tag_this[tagname][:count_random]
			attr['style']=self.style_gen('opacity')	
			attr_tags +=['style']

		else:
			# Выбираем случайные атрибуты и рандомим их если больше одного
			attr_tags = self.tag[tagname][:count_random]



		if len(attr_tags)>0:
			random.shuffle(attr_tags)


		# Формируем строку из атрибутов и их значений
		list_attr = []
		for a in attr_tags:
			qoutes = random.choice(['\'','\"'])
			a = random.choice(self.spaces)+a+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes+random.choice(self.spaces)+attr[a]+random.choice(self.spaces)+qoutes+random.choice(self.spaces)
			list_attr.append(a)

		qoutes = random.choice(['\'','\"'])
		string_attrs = ' '.join(list_attr+[random.choice(['data-'+self.word_gen(1,'eng')+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes+random.choice(self.spaces)+self.word_gen(1,'eng')+random.choice(self.spaces)+qoutes,'','','',''])])

		return string_attrs

	def tag_fake(self,tagname,count=1,opacity='no',lang='eng'):
		if opacity=='opacity':
			style_table = self.attr_gen(tagname,opacity)
		else:
			style_table = self.attr_gen(tagname)
		
		tag_str = ''
		for i in range(0,count):
			table = '<'+tagname+' '+random.choice(self.spaces)+style_table+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			table += '<tbody '+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			# Генерим tr 
			for tr in xrange(random.randint(1,7)):
				# td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+attr_gen('td')+random.choice(self.spaces)+'>'
				table += '<tr '+random.choice(self.spaces)+'>'+random.choice(self.tabs)
				for i in xrange(random.randint(1,4)):
					td = '<td '+random.choice(self.spaces)+self.attr_gen('td')+random.choice(self.spaces)+'>'+self.word_gen(random.randint(1,27),lang)+'</td'+random.choice(self.spaces)+'>'
					table += td+random.choice(self.tabs)
				table += '</tr'+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			table += '</tbody'+random.choice(self.spaces)+'>'+random.choice(self.tabs)+'</'+tagname+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			tag_str += table

		return tag_str


	def tag_general(self,tagname,count=1,opacity='no',lang="eng"):
		domain = open('domain.txt','r').read().strip()
		if opacity=='opacity':
			style_table = self.attr_gen(tagname,opacity)
		else:
			style_table = self.attr_gen(tagname,attr_effect='no')
		
		tag_str = ''
		for i in range(0,count):
			table = '<'+tagname+' '+random.choice(self.spaces)+style_table+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			table += '<tbody '+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			# Генерим tr 
			for i,tr in enumerate(xrange(random.randint(1,7))):
				# td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+attr_gen('td')+random.choice(self.spaces)+'>'
				table += '<tr '+random.choice(self.spaces)+'>'+random.choice(self.tabs)

				if i == 0:
					count_td = random.randint(1,4)
					for c,m in enumerate(xrange(count_td)):
						if c == 0:
							random_for_a = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
							random_for_a2 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
							random_for_img = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
							qoutes_a = random.choice(['\'','\"'])
							qoutes_a2 = random.choice(['\'','\"'])
							qoutes_img = random.choice(['\'','\"'])
							# Картинка в ссылке + текст + ссылки текстовые							
							td = '<td '+random.choice(self.spaces)+self.attr_gen('td',attr_effect='no')+random.choice(self.spaces)+'>'+'<p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'[%%ORandText,paysystem3713_hello%%]'+random.choice(self.spaces)+random.choice(['<br/>'+random.choice(self.spaces),'<br/>'+random.choice(self.spaces)+'<br/>'])+random.choice(self.spaces)+'[%%ORandText,title_17_07_aws%%] '+random.choice(self.spaces)+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+qoutes_a2+'http://'+domain+'/'+random_for_a2+qoutes_a2+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'[%%ORandText,paysystem3713_link%%]'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'</p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'<br/>'+random.choice(self.spaces)+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+'http://'+domain+'/'+random_for_a+qoutes_a+random.choice(self.spaces)+' '+self.attr_gen('a',attr_effect='no')+'>'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+'http://'+domain+'/'+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+self.attr_gen('img',attr_effect='no')+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+'</td'+random.choice(self.spaces)+'>'

							# Рандом строка вместо текстов. Картинки и ссылки
							# td = '<td '+random.choice(self.spaces)+self.attr_gen('td',attr_effect='no')+random.choice(self.spaces)+'>'+'<p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+self.word_gen(random.randint(3,38),lang)+random.choice(self.spaces)+random.choice(['<br/>'+random.choice(self.spaces),'<br/>'+random.choice(self.spaces)+'<br/>'])+random.choice(self.spaces)+self.word_gen(random.randint(3,48),lang)+random.choice(self.spaces)+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+qoutes_a2+'http://'+domain+'/'+random_for_a2+qoutes_a2+random.choice(self.spaces)+'>'+random.choice(self.spaces)+self.word_gen(random.randint(1,2),lang)+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'</p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'<br/>'+random.choice(self.spaces)+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+'http://'+domain+'/'+random_for_a+qoutes_a+random.choice(self.spaces)+' '+self.attr_gen('a',attr_effect='no')+'>'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+'http://'+domain+'/'+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+self.attr_gen('img',attr_effect='no')+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+'</td'+random.choice(self.spaces)+'>'
							
							# Только картинка в ссылке
							# td = '<td '+random.choice(self.spaces)+self.attr_gen('td',attr_effect='no')+random.choice(self.spaces)+'>'+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+'http://'+domain+'/'+random_for_a+qoutes_a+random.choice(self.spaces)+' '+self.attr_gen('a',attr_effect='no')+'>'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+'http://'+domain+'/'+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+self.attr_gen('img',attr_effect='no')+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+'</td'+random.choice(self.spaces)+'>'

							# На месте картинок и ссылок просто рандом
							# td = '<td '+random.choice(self.spaces)+self.attr_gen('td',attr_effect='no')+random.choice(self.spaces)+'>'+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+random_for_img+random_for_a+qoutes_a+random.choice(self.spaces)+' '+self.attr_gen('a',attr_effect='no')+'>'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+random_for_a2+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+self.attr_gen('img',attr_effect='no')+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+'</td'+random.choice(self.spaces)+'>'
							
						else:
							td = '<td '+random.choice(self.spaces)+self.attr_gen('td','opacity')+random.choice(self.spaces)+'>'+'</td'+random.choice(self.spaces)+'>'

						table += td+random.choice(self.tabs)
				else:
					for i in xrange(random.randint(1,3)):
						td = '<td '+random.choice(self.spaces)+self.attr_gen('td','opacity')+random.choice(self.spaces)+'>'+self.word_gen(random.randint(3,38),lang)+'</td'+random.choice(self.spaces)+'>'
						table += td+random.choice(self.tabs)

				table += '</tr'+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			table += '</tbody'+random.choice(self.spaces)+'>'+random.choice(self.tabs)+'</'+tagname+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			tag_str += table

		return tag_str

	def tag_simple(self,tag):
		random_for_a = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
		random_for_img = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
		random_for_a2 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
		qoutes_a = random.choice(['\'','\"'])
		qoutes_a2 = random.choice(['\'','\"'])
		qoutes_img = random.choice(['\'','\"'])
		domain = open('domain.txt','r').read().strip()

		if tag=="img":
			tag = '<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+'http://'+domain+'/'+random_for_a+qoutes_a+random.choice(self.spaces)+' >'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+'http://'+domain+'/'+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'
		elif tag=='p+a+img':
			tag = '<p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'[%%ORandText,paysystem3713_hello%%]'+random.choice(self.spaces)+random.choice(['<br/>'+random.choice(self.spaces),'<br/>'+random.choice(self.spaces)+'<br/>'])+random.choice(self.spaces)+'[%%ORandText,title_17_07_aws%%] '+random.choice(self.spaces)+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+qoutes_a2+'http://'+domain+'/'+random_for_a2+qoutes_a2+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'[%%ORandText,paysystem3713_link%%]'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'</p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'<br/>'+random.choice(self.spaces)+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+'http://'+domain+'/'+random_for_a+qoutes_a+random.choice(self.spaces)+' >'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+'http://'+domain+'/'+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'
		elif tag=='p+img':
			tag = '<p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'[%%ORandText,paysystem3713_hello%%]'+random.choice(self.spaces)+random.choice(['<br/>'+random.choice(self.spaces),'<br/>'+random.choice(self.spaces)+'<br/>'])+random.choice(self.spaces)+'[%%ORandText,title_17_07_aws%%] '+random.choice(self.spaces)+random.choice(self.spaces)+'</p'+random.choice(self.spaces)+'>'+random.choice(self.spaces)+'<br/>'+random.choice(self.spaces)+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+'http://'+domain+'/'+random_for_a+qoutes_a+random.choice(self.spaces)+' >'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+'http://'+domain+'/'+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'
		
		return tag

	def synonyms(self,match):
			list_words = match.group().split('|')
			words = random.choice(list_words).replace('{','').replace('}','')
			return words
	def mix(self,match):
			list_words = match.group().replace('[','').replace(']','').split('%%')
			random.shuffle(list_words)
			words =' '.join(list_words)
			return words

	def spaces(self,match):
		spaces = random.choice(self.spaces_words)
		return spaces

	def tabss(self,match):
		tabsr = random.choice(self.tabs)
		return tabsr

	def replace_br(self,match):
		br = random.choice(self.br_tag)
		return br

	def replace_qoutes(self,match):
		qoutes = random.choice(['\'','\"'])
		b=match.group().replace('_QOUTE_',qoutes)

		return b

	def body(self,filename,counttext):
		# _BORDER_ 
		# _WIDTH_X_Y_
		# _HEIGHT_X_Y_
		# _COLOR_X_
		# _FONT_STYLE_
		# _FONT_FAMILY_
		# _FONT_SIZE_
		# _SPACES_
		# _TAB_
		# _CLASS_
		# _DATA_
		#_BACKGROUND_
		#_FAKE_DIV_TEXT_RU
		# _LINK1_
		# _LINK2_
		# _IMG_
		# _LINKTEXT_		

		html = open('gen/templates/body/'+filename,'r').read()
		body = ''

		###CONTENT GENERATE

		#HELLO GENERATE
		hello_raw = open('gen/templates/hello.txt','r').readlines()
		hello = hello_raw[counttext%len(hello_raw)]

		#TEXT GENERATE
		text = open('gen/templates/text.txt','r').readlines()
		text = text[counttext%len(text)]

		# Processing synonyms
		regex_synonyms = re.compile(r'(?P<synonyms>{[^{}]+})')
		while text.find('{')!= -1:
			text = regex_synonyms.sub(self.synonyms,text)

		# Processing mix
		regex_mix = re.compile(r'(?P<mix>\[[^\[\]]+\])')
		while text.find('[')!= -1:
			text = regex_mix.sub(self.mix,text)

		# Replace spaces
		spaces = re.compile(r'(_SPACES_)')
		while text.find('_SPACES_')!= -1:
			text = spaces.sub(self.spaces,text)

		# Replace tabs
		tabs = re.compile(r'(_TAB_)')
		while text.find('_TAB_')!= -1:
			text = tabs.sub(self.tabss,text)

		# Replace br
		brs = re.compile(r'(_BR_)')
		while text.find('_BR_')!= -1:
			text = brs.sub(self.replace_br,text)

		#TEXT_BUTTON GENERATE
		button_text_raw = open('gen/templates/button_text.txt','r').readlines()
		button_text = button_text_raw[counttext%len(button_text_raw)]

		#LINKS GENERATE
		random_link1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(random.randint(3,13)))
		random_link2 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(random.randint(3,13)))
		random_img = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(random.randint(3,13)))		
		domain = open('gen/templates/domain.txt','r').read().strip()
		link1 = domain+'/'+random_link1
		link2 = domain+'/'+random_link2
		img = domain+'/'+random_img+'.jpg'

		body += html.replace('_HELLO_', hello).replace('_TEXT_', text).replace('_LINK1_',link1).replace('_LINK2_',link2).replace('_IMG_',img).replace('_BUTTONTEXT_',button_text)

		###CONTENT GENERATE END

		###STYLE GENERATE

		# Replace spaces
		spaces = re.compile(r'(_SPACES_)')
		while body.find('_SPACES_')!= -1:
			body = spaces.sub(self.spaces,body)

		# Replace tabs
		tabs = re.compile(r'(_TAB_)')
		while body.find('_TAB_')!= -1:
			body = tabs.sub(self.tabss,body)

		# Replace qoutes
		qoutes = re.compile(r'(_QOUTE_.*[.]*_QOUTE_)')
		while body.find('_QOUTE_')!= -1:
			body = qoutes.sub(self.replace_qoutes,body)

		###STYLE GENERATE END
		return body