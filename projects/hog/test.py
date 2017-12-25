def cake():
	print('beets')
	def pie():
		print('sweets')
		return 'cake'
	return pie

a=cake()
print (a())