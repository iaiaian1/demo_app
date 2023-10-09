# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ClientSideScripting(Document):
	pass

# Remember not to indent inside the class. took my time bruh.
@frappe.whitelist()
def frappe_call(msg):
	import time
	time.sleep(2)
	# frappe.msgprint(msg)

	return "this is from frappe global call"
