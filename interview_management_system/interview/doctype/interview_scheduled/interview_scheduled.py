# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.exceptions import ValidationError  # Import the ValidationError for custom exceptions
from frappe import _  # Import the _ function for translation

class InterviewScheduled(Document):
    def validate(self):
        # Get the selected interview date and today's date
        selected_date = self.interview_date
        current_date = frappe.utils.nowdate()  # Get today's date

        # Check if the selected date is in the past
        if selected_date < current_date:
            # Throw an error if the selected date is in the past
            frappe.throw(_("Please select a future date. This date is in the past."))
