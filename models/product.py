# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Product(models.Model):
    _name = 'frusec.product'
    _description = 'Product template'
    
    name = fields.Text(string='Name', required=True)
    image = fields.Image(string='Image')
    price = fields.Integer(string='Price', required=True)
    note = fields.Text(string='Note')