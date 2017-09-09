people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
	if age >= 18:
		driver = (person, age)
		print(driver)
else:
	print('Driver not found')