# -*- coding: utf-8 -*-
{
    'name': "Frusec",

    'version': '1.0',

    'author': "Javier, Jose & Pedro",

    'website': "http://www.fruseconline.com",

    'license': "AGPL-3",

    'sequence': -100,

    #'complexity': 'easy',

    # Short (1 phrase/line) summary of the module's purpose, used as subtitle on 
    # modules listing or apps.openerp.com
    'summary': "Compañía minorista de venta de frutos secos.",

    # Long description of module's purpose
    'description': """Módulo encargado de gestionar la empresa Frusec,
            concretamente el apartado de pedidos y facturas.""",

    # Categories can be used to filter modules in modules listing.
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale Management',

    # Icon for the module
    'images': ['static/description/icon.png'],

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vista_order.xml',
        'views/vista_product.xml',
        'views/vista_client.xml',
        #'views/vista_product.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],

    # to make your module an application.
    'application': True,
}
