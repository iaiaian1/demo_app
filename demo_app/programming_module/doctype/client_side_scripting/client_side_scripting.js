// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	

	refresh: function(frm) {
		// if document is not saved, this will run. after saving it will be false.
		if(frm.is_new()){
			frm.set_intro("This doc is new")
		}

		// Custom button
		// frm.add_custom_button('Clickity', () => {
		// 	frappe.msgprint("clackity")
		// })

		// Useful for drop-down buttons, parent is button called click me as the 3rd parameter.
		frm.add_custom_button('Click me 1', () => {
			frappe.msgprint('Click me 1 is clicked')
		}, 'click me')

		frm.add_custom_button('Click me 2', () => {
			frappe.msgprint('Click me 2 is clicked')
		}, 'click me')
	},

	// onload: function(frm){
		
	// },

	first_name: function(frm) {
		// frm.set_value({
		// 	full_name : `${frm.doc.first_name} ${frm.doc.last_name}`
		// })
		frm.add_child('family_members', {
			name1: 'Tennis Racke',
			relation: "Father",
			age: 56,
		});

		frm.refresh_field('family_members');
		console.log("Validate")
	},

	// before_save: function(frm){
	// 	frappe.msgprint("Before save")
	// },

	//Fired after save button but before saving to the database
	// before_save: function(frm){
	// 	// For accessing the form objects. :)
	// 	console.log(frm.doc.first_name)
	// },

	//Fired after save button and saving to the database
	// after_save: function(frm){
	// 	// For accessing the form objects. :)
	// 	console.log(frm.doc.first_name)
	// },

	//Field based and will fire on any changes, theres a slight time for the function to fire though.
	enable: function(frm){
		frappe.msgprint("Enable is changed")

		// These can be done on the site itself during doctype editing
		// But if for some reason you cant edit those, these methods can be used
	
		// frm.set_df_property('first_name', 'reqd', 1)
		// frm.refresh_field('first_name');

		// frm.set_df_property('middle_name', 'read_only', 1)
		// frm.refresh_field('first_name');

		// frm.toggle_reqd('age', true)
		// frm.refresh_field('age')
	},

	// middle_name: function(frm) {
	// 	console.log(frm.doc.middle_name)
	// 	frappe.msgprint(frm.doc.middle_name)
	// }
	
	// Important for accessing child table
	family_members_on_form_rendered: function(frm){
		console.log(frm.doc.family_members[0].relation)
	},

	// after submit. before submit is fast.
	on_submit: function(frm) {
		frappe.msgprint("baz")
	}

	// before_submit, on_submit, before_cancel, after_cancel

	
});

frappe.ui.form.on('Family Members', {
	//cdt is child doctype name i.e Family Members (Family Members)
	//cdn is the row name (new-family-members-1)

	// name1: function(frm){
	// 	console.log(frm.doc.family_members[0].name1)
	// },

	// relation: function (frm, cdt, cdn) {
	// 	// frappe.msgprint(`You are the ${frm.doc.family_members[0].relation}`)
	// 	frm.doc.family_members.map((element, index) => {
	// 		// console.log(family_members[index].relation)
	// 		frappe.msgprint(element.relation)
	// 	})
	// 	console.log(`Full name: ${frm.doc.first_name}`)
	// }
})