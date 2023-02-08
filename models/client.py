# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Order(models.Model):
    _name = 'frusec.client'
    _description = 'Client template'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    contact = fields.Char(string='Email')
    website = fields.Char(string='Website')
    note = fields.Text(string='Note')
