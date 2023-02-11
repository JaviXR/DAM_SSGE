# -*- coding: utf-8 -*-
from odoo import models, fields, api

class OrderLine(models.Model):
    _name = 'frusec.order.line'
    _description = 'Plantilla de linea de pedido'

    product_id = fields.Many2one('frusec.product', string='Producto', required=True)
    product_price = fields.Float('Precio', related='product_id.price')
    product_name = fields.Char('Producto', related='product_id.name')

    order_id = fields.Many2one('frusec.order', string='Pedido')
    currency_id = fields.Many2one(comodel_name='res.currency', related='order_id.currency_id')
    
    product_qty = fields.Integer(string='Cantidad', required=True, default=1)
    price_subtotal = fields.Float('Subtotal', compute='_compute_price_subtotal')

    @api.depends('product_price', 'product_qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.product_price * rec.product_qty