# -*- coding: utf-8 -*-

#   Documentación usada
#   https://www.odoo.com/documentation/12.0/developer/reference/orm.html#common-orm-methods
{
    'name': "Frusec",

    'version': '1.14',

    'author': "Javier, Jose & Pedro",

    'website': "http://www.fruseconline.com",

    'license': "AGPL-3",

    'sequence': -100,

    'complexity': 'easy',

    # Descripción corta (1 línea) del propósito del módulo, usado como subtítulo 
    # en el listado de módulos o en apps.openerp.com
    'summary': "Compañía minorista de venta de frutos secos.",

    # Descripción extendida del propósito del módulo
    'description': """Módulo encargado de gestionar la empresa Frusec,
            concretamente el apartado de pedidos y facturas.""",

    # Las categorías se pueden usar para filtrar el módulo en el listado de módulos.
    # Lista completa en https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    'category': 'Sale Management',

    # Icono del módulo
    'images': ['static/description/icon.png'],

    # Módulos necesarios para que éste módulo funcione
    'depends': ['base'],

    # Datos cargados por el módulo
    'data': [
        'security/ir.model.access.csv',
        'views/data.xml',
        'views/vista_order.xml',
        'views/vista_order_line.xml',
        'views/vista_product.xml',
        'views/vista_client.xml',
    ],
    # Datos cargados solamente en modo de demostración
    #'demo': [
    #    'demo/demo.xml',
    #],

    # Convierte el módulo en aplicación.
    'application': True,
}
