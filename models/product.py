# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Product(models.Model):
    _name = 'frusec.product'
    _description = 'Product template'
    
    name = fields.Char(string='Name', required=True)
    image = fields.Image(string='Image')
    company_id = fields.Many2one(comodel_name='res.company', string='Company', 
                                default=lambda self: self.env.company)
    currency_id = fields.Many2one(comodel_name='res.currency', related='company_id.currency_id')
    price = fields.Float(string='Price', required=True, default=0.00)
    note = fields.Text(string='Description')