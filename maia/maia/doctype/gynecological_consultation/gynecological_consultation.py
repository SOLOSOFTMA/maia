# -*- coding: utf-8 -*-
# Copyright (c) 2017, DOKOS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from maia.maia.invoicing import create_and_submit_invoice, get_customer_name

class GynecologicalConsultation(Document):

        def on_submit(self):
                get_customer_name(self)
                create_and_submit_invoice(self)
