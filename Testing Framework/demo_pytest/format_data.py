def format_data_for_display(people):
	res = []
	for x in people:
		res.append(x['given_name'] + ' '+  x['family_name'] + ': ' + x['title'])
	return res

def format_data_for_excel(people):
	res = "given, family, title"
	for x in people:
		temp = x['given_name'] + ',' + x['family_name'] + ',' + x['title']
		res += temp

	return res
