# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockProductInherited(models.Model):
    _inherit = 'product.template'

    type_sale_product_id = fields.Many2one(
        'mysales.typesofsales_products',
        string="Type of sale related"
    )
