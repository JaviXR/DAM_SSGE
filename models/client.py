# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Order(models.Model):
    _name = 'frusec.client'
    _description = 'Client template'

    name = fields.Char(string='Name', required=True)
    phone = fields.Text(string='Phone', default='+34 123444555')
    contact = fields.Html(string='Contact', default='mailto:aaaaa@bbbb.ccc')
    note = fields.Text(string='Note')
