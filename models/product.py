# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Product(models.Model):
    _name = 'frusec.product'
    _description = 'Plantilla de producto'
    
    name = fields.Char(string='Nombre', required=True)
    image = fields.Image(string='Imagen')
    company_id = fields.Many2one(comodel_name='res.company', string='Empresa', 
                                default=lambda self: self.env.company)
    currency_id = fields.Many2one(comodel_name='res.currency', string='Divisa', related='company_id.currency_id')
    price = fields.Float(string='Precio', required=True, default=0.00)
    note = fields.Text(string='Descripción')