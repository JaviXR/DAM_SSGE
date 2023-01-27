# -*- coding: utf-8 -*-
# from odoo import http


# class Main(http.Controller):
#     @http.route('/main/main/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/main/main/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('main.listing', {
#             'root': '/main/main',
#             'objects': http.request.env['main.main'].search([]),
#         })

#     @http.route('/main/main/objects/<model("main.main"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('main.object', {
#             'object': obj
#         })
