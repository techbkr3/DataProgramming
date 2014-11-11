#!/usr/bin/env python

file = open("students.csv")
for line in file:
	l = line.strip()
	print("DEBUG: ", l)
	student = l.split(",")
	print(student)

	record = {}

	keys = ( "FULLNAME", "GENDER", "COURSE", "DEPARTMENT_CODE", "COLLEGE", "DATE_OF_VISIT" )


	certificate = {}
	k = 0
	for key in keys:
		value = student[k]
		certificate[key] = value.strip()
		k += 1

	for key in certificate.keys():
		print(key, certificate[key])

