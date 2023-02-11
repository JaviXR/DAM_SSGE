# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Order(models.Model):
    _name = 'frusec.client'
    _description = 'Plantilla de cliente'

    name = fields.Char(string='Nombre', required=True)
    phone = fields.Char(string='Teléfono')
    contact = fields.Char(string='Email')
    website = fields.Char(string='Web de contacto')
    note = fields.Text(string='Anotación')
