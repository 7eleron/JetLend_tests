import pandas as pd

def excel_test_task1(file):
	df = pd.read_excel(file)
	result = df[df['registration_date'] < '2022-01-01']['amount'].sum()
	return result

def excel_test_task2(file):
	df = pd.read_excel(file).sort_values(by=['rating'])
	d = {'rating': [], 'sum': []}
	for x in range(1, 19):
		d['rating'].append(x)
		sum_rat = df[df['rating'] == x]['amount'].sum()
		d['sum'].append(sum_rat)
	return pd.DataFrame(d)
