// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Side Scripting', {
	// refresh: function(frm) {

	// }

	// Call to own local server side scripting.py
	enable: function (frm){
		frm.call({
			doc: frm.doc,
			method: 'frm_call',
			args: {
				msg: "Hello v2"
			},
			// Freeze screen while calling
			freeze: true,
			freeze_message: ("Calling frm_call Method"),
			callback: function(r){
				// This will print the return of the python file. R can be anything.
				frappe.msgprint(r.message)
			}
		})
	}

	// Call to GLOBAL client side scripting.py 
	// enable: function (frm){
	// 	frappe.call({
	// 		method: "demo_app.programming_module.doctype.client_side_scripting.client_side_scripting.frappe_call",
	// 		args: {
	// 			msg: "Hello from global"
	// 		},
	// 		// Freeze screen while calling
	// 		freeze: true,
	// 		freeze_message: ("Calling frappe_call Method"),
	// 		callback: function(r){
	// 			// This will print the return of the python file. R can be anything.
	// 			frappe.msgprint(r.message)
	// 		}
	// 	})
	// }
});
