# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Order(models.Model):
    _name = 'frusec.order'
    _description = 'Order template'

    order_code = fields.Char(string='Code', required=True)
    client_id = fields.Char(string='Client', required=True)
    datetime = fields.Date(string='Date', default=lambda self:fields.Date.today(), required=True)
    state = fields.Selection([
        ('status_0', 'Processing'),
        ('status_1', 'Canceled'),
        ('status_2', 'Sent'),
        ('status_3', 'Received'),
        ('status_4', 'Completed')
    ], string='Status', default='status_0', required=True)
    note = fields.Text(string='Note')

    def action_cancel(self):
        self.state="status_1"
