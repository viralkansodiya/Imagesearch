// Copyright (c) 2025, test and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product Search", {
	search(frm) {
        frappe.call({
            method: "find_your_product",
            args : {
                product_name: frm.doc.product_name,
            }
        })
	},
});
