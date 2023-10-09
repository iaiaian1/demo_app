# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if not filters: filters = {}
	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		frappe.msgprint("No records found")
		return columns, data

	data = []
	for d in cs_data:
		row = frappe._dict({
			'first_name': d.first_name,
			'dob': d.dob,
			'age': d.age,
		})
		data.append(row)
	return columns, data

def get_columns():
	return [
		{
			'fieldname': 'first_name',
			'label': ('Name'),
			'fieldtype': 'Data',
			'width': '120'
		},
		{
			'fieldname': 'dob',
			'label': ('DOB'),
			'fieldtype': 'Date',
			'width': '120'
		},
		{
			'fieldname': 'age',
			'label': ('Age'),
			'fieldtype': 'Data',
			'width': '100'
		},
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype='Server Side Scripting',
		fields=['first_name', 'dob', 'age'],
		filters=conditions,
		order_by='first_name desc'
	)
	return data

def get_conditions(filters):
	conditions={}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value

	return conditions