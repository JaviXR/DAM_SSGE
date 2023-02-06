# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Order(models.Model):
    _name = 'frusec.order'
    _description = 'Order template'

    order_code = fields.Char(string='Code', required=True)
    client = fields.Char(string='Client', required=True)
    datetime = fields.Date(string='Date', default=lambda self:fields.Date.today(), required=True)
    status = fields.Selection([
        ('status_1', 'Processing'),
        ('status_2', 'Sent'),
        ('status_3', 'Received'),
        ('status_4', 'Completed'),
    ], string='Status', default='status_1', required=True)
    note = fields.Text(string='Note')

