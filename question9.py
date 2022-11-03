import requests
from bs4 import BeautifulSoup

# подключение к сайту
url = 'https://jetlend.ru/borrower/'
def req(url):
	request = requests.get(url)
	return request.text

site = req(url)

# поиск по сайту тегов
def search_all_tags(site, tag):
	soup = BeautifulSoup(site, 'html.parser')
	ser_tags = soup.find_all(tag)
	count = 0
	for x in ser_tags:
		count += 1
	return count

# количества всех тегов на странице
def count_tags():	
	list_tag = [ '!DOCTYPE', 'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'base', 'bdi', 'bdo', 'bdi', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'datalist', 'dd', 'dt', 'dl', 'del', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt', 'dl', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'figure', 'footer', 'form', 'h1', 'h6', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'fieldset', 'li', 'link', 'main', 'map', 'area', 'mark', 'menu', 'menuitem', 'meta', 'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'picture', 'pre', 'progress', 'q', 'rp', 'ruby', 'rt', 'ruby', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source', 'video', 'audio', 'picture', 'span', 'strong', 'style', 'sub', 'summary', 'details', 'sup', 'table', 'tbody', 'td', 'table', 'textarea', 'tfoot', 'table', 'th', 'thead', 'table', 'time', 'title', 'tr', 'track', 'audio', 'ul', 'var', 'video', 'wbr']
	list_tag = list(set(list_tag)) # удаление повторяющихся тегов в списке

	dict_tag = {}
	count_all_tags = 0
	for x in list_tag:
		find_tags = search_all_tags(site=site, tag=x)
		dict_tag[x] = find_tags
		count_all_tags += find_tags

	dict_tag = {x: y for (x, y) in dict_tag.items() if y > 0} # убирает теги из словаря с 0 значением
	#return dict_tag # возвращает конкретно сколько каких тегов на странице
	#return count_all_tags # возвращает общее количество тегов на странице

# поиск тегов с атрибутами
def search_all_tags_attr():
	soup = BeautifulSoup(site, 'html.parser')
	count = 0
	# из count_tags получаем словарь со всеми тегами на сайте
	for x in count_tags().keys():
		ser_tags_attr = soup.find_all(x)
		for i in ser_tags_attr:
			if i.attrs:
				count += 1
	return count