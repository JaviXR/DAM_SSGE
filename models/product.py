# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Product(models.Model):
    _name = 'frusec.product'
    _description = 'Product template'
    
    name = fields.Text(string='Name', required=True)
    #field_name = fields.Image(string='field_name', max_width=50, max_height=50)
    price = fields.Integer(string='Price', required=True)
    note = fields.Text(string='Note')