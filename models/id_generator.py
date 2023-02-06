# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ID_Generator(models.Model):
    _name = 'frusec.id_generator'

    next_available_order_id = fields.Char('Next Order ID', default='/')

    # on create method
    @api.model
    def create(self, vals):
        obj = super(frusec_id_generator, self).create(vals)
        if obj.next_available_order_id == '/':
            number = self.env['ir.sequence'].get('your.sequence.code') or '/'
            obj.write({'next_available_order_id': number})
        return obj