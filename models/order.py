# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Order(models.Model):
    _name = 'frusec.order'
    _description = 'Order template'

    order_code = fields.Char(string='Order', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New Order'))
    client_id = fields.Many2one(comodel_name='frusec.client', string='Client', required=True)
    order_lines = fields.One2many('frusec.order.line', 'order_id', string='Products', required=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', 
                                default=lambda self: self.env.company)
    currency_id = fields.Many2one(comodel_name='res.currency', related='company_id.currency_id')
    total_price = fields.Float(string='Total', compute='_compute_total_price')
    
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
            vals['order_code'] = self.env['ir.sequence'].next_by_code('frusec.order') or ('New Order')
            
        return super(Order, self).create(vals)

    @api.depends('order_lines')
    def _compute_total_price(self):
        Orderline = self.env['frusec.order.line']
        for order in self:
            total = 0.00
            for subtotal in Orderline.search([('order_id', '=', 'frusec.order_id')]):
                total += subtotal.price_subtotal
            order.total_price = total
        
    def action_cancel(self):
        self.state="status_1"