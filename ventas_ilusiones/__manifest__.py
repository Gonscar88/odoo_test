# -*- coding: utf-8 -*-
{
    'name': "Practica Odoo Ventas",

    'summary':
        """
            * Desarrollar entorno de ventas de x compañia.
        """,

    'description':
        """
            * Desarrollar una aplicación de ventas 
                capaz de capturar los 3 tipos de ventas de la empresa
                Ilusiones S.A. de C.V. solicitando los campos mencionados c/u
                y mostrar cada tipo de venta en una sola línea de venta.
        """,

    'author': "Oscar González",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'backend_theme_v11',
        'mail',
        'stock',
    ],

    'demo': [],

    'data': [
        'security/mysales_grouops.xml',
        'security/ir.model.access.csv',
        'data/mysales_typeofsales_data.xml',
        'data/mysalesmaindata_consecutive.xml',
        'views/menu.xml',
        'views/mysales_types_views.xml',
        'views/mysales_types_products_views.xml',
        'views/mysales_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
