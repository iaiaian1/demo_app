# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ServerSideScripting(Document):
	# pass
	# Need to bench start before it will take effect

	# def validate(self):
	# 	frappe.msgprint("Hello Frappe v2")

	# def validate(self):
	# 	frappe.msgprint("Hello my full name is {0} {1} and my last namne is {2} ".format(self.first_name, self.middle_name, self.last_name))

	# def before_save(self):
	# 	frappe.throw("Throw frappe")

	# Doesnt work maybe
	# def first_name(self):
	# 	frappe.throw("Throw frappe")

	# def before_insert(self):
	# 	command here
	
	# def after_insert(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint("{0}. The family member is {1} and their last namne is {2} ".format(row.idx, row.name1, row.relation))
		
	# def on_update(self):
	# 	command here

	# def before_submit(self):
	# 	command here

	# def on_submit(self):
	# 	command here

	# def on_cancel(self):
	# 	command here

	# def on_trash(self):
	# 	command here

	# def after_delete(self):
	# 	command here

	# def on_update(self):
	# 	command here

	# frappe.get_doc(doctype, name)
	# def validate(self):
		# self.get_document()
		# self.new_document()
		# frappe.delete_doc('Client Side Scripting', 'PR-0002') or doc = frappe.get_doc("doctype", "doc-id"), doc.delete()
		# self.save_document()
		# self.get_list()
		# self.get_value()

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	# frappe.msgprint("The first name is {0} na Age is {1}".format(doc.first_name, doc.age))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint("{0}. The family member name is {1} and relation is {2}".format(row.idx, row.name1, row.relation))

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'John'
	# 	doc.last_name = 'Elden Ring'
	# 	doc.age = 13
	# 	doc.append("family_members", {
	# 		"name1" : "Sekiro",
	# 		"relation" : "GOAT",
	# 		"age" : 14
	# 	})
	# 	doc.insert()
	# escape hatches on doc insert
	# doc.insert(
	# 	ignore_permissions=True, # ignore write permissions during insert
	# 	ignore_links=True, #ignore link validation in the document
	# 	ignore_if_duplicate=True, #ignore duplicateentryerror
	# 	ignore_mandatory=True #insert even if mandatory fields are not set
	# )

	# for inserting to database?
	# def save_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'DannyDeVito'
	# 	doc.age = 31
	# 	doc.save()

		# escape hatches on doc save
		# doc.save(
		# 	ignore_permissions=True, #ignore write permissions during insert
		# 	ignore_version=True #do not create a version record
		# )

	# GET
	# frappe.db.get_list(doctype, filters, or_filter. fields. order_by, group_by, start, page_length)
	
	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting', 
	# 		filters={
	# 			'enable' : 1,
	# 		},
	# 		fields=['first_name', 'age']
	# 	)
	# 	for d in doc:
	# 		frappe.msgprint('The parent first name is {0} and age is {1}'.format(d.first_name, d.age))

	# fetching
	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0001', ['first_name', 'age'])
	# 	frappe.msgprint("The parent first name is {0} and age is {1}".format(first_name, age))

	# Typing function above is a hassle just call later.
	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting', 'PR-0003', 'age', 25)

	# Exists
	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting', 'PR-0003'):
	# 		frappe.msgprint ("PR-0003 exists")
	# 	else:
	# 		frappe.msgprint ("PR-0003 does not exist")

	# Count
	# def validate(self):
		# doc_count = frappe.db.count('Cliend Side Scripting', {'enable': 1})
		# frappe.msgprint("Enabled count {0}".format(doc_count))

	# SQL
	# frappe.db.sql(query, filters, as_dict)
	# def sql(self):
	# 	data = frappe.db.sql("""SELECT first_name, age FROM `tabClient Side Scripting` WHERE enable = 1""", as_dict=1)

	# 	for d in data:
	# 		frappe.msgprint('The parent first name is {0} and age is {1}'.format(d.first_name, d.age))

	# SERVER SIDE CALL

	# Whitelist it so it can be called on the server side.
	# INDENT INSIDE
	@frappe.whitelist()
	def frm_call(self, msg):
		import time
		time.sleep(2)
		# This will be printed as a callback in JS
		# frappe.msgprint(msg)

		self.mobile_no = 7767656
		return "Hi This is from frm_call"