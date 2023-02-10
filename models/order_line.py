# -*- coding: utf-8 -*-
from odoo import models, fields, api

class OrderLine(models.Model):
    _name = 'frusec.order.line'
    _description = 'Order lines template'

    product_id = fields.Many2one('frusec.product', string='Product', required=True)
    product_price = fields.Float('Price', related='product_id.price')
    product_name = fields.Char('Product', related='product_id.name')

    order_id = fields.Many2one('frusec.order', string='Order')
    currency_id = fields.Many2one(comodel_name='res.currency', related='order_id.currency_id')

    product_qty = fields.Integer(string='Quantity', required=True, default=1)
    price_subtotal = fields.Float('Subtotal', compute='_compute_price_subtotal')

    @api.depends('product_price', 'product_qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.product_price * rec.product_qty