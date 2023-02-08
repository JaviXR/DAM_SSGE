# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Order(models.Model):
    _name = 'frusec.order'
    _description = 'Order template'

    order_code = fields.Char(string='Code', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New Order'))
    client_id = fields.Many2one(comodel_name='frusec.client', string='Client', required=True)
    product_ids = fields.Many2many(comodel_name='frusec.product', string='Products', required=True)
    price = fields.Float(string='Price', compute='_compute_total_price')
    datetime = fields.Date(string='Date', default=lambda self:fields.Date.today(), required=True)
    state = fields.Selection([
        ('status_0', 'Processing'),
        ('status_1', 'Canceled'),
        ('status_2', 'Sent'),
        ('status_3', 'Received'),
        ('status_4', 'Completed')
    ], string='Status', default='status_0', required=True)
    note = fields.Text(string='Note')

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'Empty Note'
        if vals.get('order_code', _('New Order')) == _('New Order'):
            vals['order_code'] = self.env['ir.sequence'].next_by_code('frusec.order') or ('New')
            
        return super(Order, self).create(vals)

    # def _compute_total_price(self):

    def action_cancel(self):
        self.state="status_1"
