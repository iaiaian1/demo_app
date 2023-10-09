// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Server Side Scripting Script Report"] = {
	"filters": [
		{
			"fieldname" : "name",
			"label" : ("Server Side Scripting"),
			"fieldtype" : "Link",
			"options" : "Client Side Scripting"
		},
		{
			"fieldname" : "dob",
			"label" : ("DOB"),
			"fieldtype" : "Date",
			// "default":frappe.datetime.now_date(),
		},
		{
			"fieldname" : "age",
			"label" : ("Age"),
			"fieldtype" : "Data",
		},
	]
};
