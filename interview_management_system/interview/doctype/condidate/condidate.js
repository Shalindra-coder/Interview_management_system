// Copyright (c) 2024, Shalindra and contributors
// For license information, please see license.txt


frappe.ui.form.on('Condidate', {
    onload: function(frm) {
        frappe.msgprint(__('Welcome to the Interview Portal, ' + frm.doc.name + '!'));
    },
});
