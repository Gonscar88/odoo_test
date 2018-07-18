# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SalesTypesData(models.Model):
    _name = 'mysales.typesofsales_products'

    name = fields.Many2one(
        'mysales.types',
        string="Type of sale",
        required=True,
        track_visibility='on_change',
    )

    stockable_products = fields.Many2many(
        'product.template',
        string="Products combo",
        required=True,
    )

    mysale_id = fields.Many2one(
        'mysales.maindata',
        string="Sale related",
    )
