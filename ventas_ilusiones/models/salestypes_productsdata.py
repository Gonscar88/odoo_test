# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SalesTypesData(models.Model):
    _name = 'mysales.typesofsales_products'

    name = fields.Char(
        string="Name",
        related='type.name',
        store=True,
    )

    type = fields.Many2one(
        'mysales.types',
        string="Type of sale",
        required=True,
        track_visibility='on_change',
    )

    stockable_products = fields.One2many(
        'mysales.product_saletype_relation',
        'saletype_id',
        string="Products combo",
    )

    services_ids = fields.One2many(
        'mysales.services_saletype_relation',
        'saletype_id',
        string="Services combo",
    )

    mysale_id = fields.Many2one(
        'mysales.maindata',
        string="Sale related",
    )

    serial_number = fields.Char(
        string="Serial number"
    )

    contract_number = fields.Char(
        string="Contract number",
    )

    suggested_price = fields.Float(
        string="Suggested price",
        compute='getsuggestedprice',
        help="This is 15% above the total of the  list price of the products"
    )

    price = fields.Float(
        string="Price",
    )

    @api.multi
    @api.depends('stockable_products')
    def getsuggestedprice(self):
        sum_products = 0
        for record in self:
            for product in record.stockable_products:
                sum_products += product.product_id.list_price
                sug_price = sum_products * 1.15
                record.suggested_price = sug_price
