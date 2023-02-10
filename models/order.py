# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Order(models.Model):
    _name = 'frusec.order'
    _description = 'Plantilla de pedido'

    order_code = fields.Char(string='Pedido', required=True, copy=False, readonly=True, 
                            default=lambda self: _('Nuevo pedido'))
    client_id = fields.Many2one(comodel_name='frusec.client', string='Cliente', required=True)
    order_lines = fields.One2many('frusec.order.line', 'order_id', string='Productos', required=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Empresa', 
                                default=lambda self: self.env.company)
    currency_id = fields.Many2one(comodel_name='res.currency', related='company_id.currency_id')
    total_price = fields.Monetary(string='Precio', compute='_compute_total_price')
    
    datetime = fields.Date(string='Fecha', default=lambda self:fields.Date.today(), required=True)
    state = fields.Selection([
        ('state_0', 'Procesando'),
        ('state_1', 'Cancelado'),
        ('state_2', 'Enviado'),
        ('state_3', 'Entregado'),
        ('state_4', 'Completado')
    ], string='Estado', default='state_0', required=True)
    note = fields.Text(string='Anotación')

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'Nota vacía'
        if vals.get('order_code', _('New Order')) == _('Nuevo pedido'):
            vals['order_code'] = self.env['ir.sequence'].next_by_code('frusec.order') or ('Nuevo pedido')
            
        return super(Order, self).create(vals)

    @api.depends('order_lines')
    def _compute_total_price(self):
        Orderline = self.env['frusec.order.line']
        for order in self:
            total = 0.00
            for subtotal in Orderline.search([('order_id', '=', 'frusec.order_id')]):
                total += subtotal.price_subtotal
            order.total_price = total
        
    def action_next_state(self):
        s = self.state
        if (s == "state_0"):
            self.state = "state_2"
        elif (s == "state_2"):
            self.state = "state_3"
        elif (s == "state_3"):
            self.state = "state_4"

    def action_cancel(self):
        self.state="state_1"