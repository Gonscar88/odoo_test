# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductStockableSaleTypeRelation(models.Model):
    _name = 'mysales.product_saletype_relation'

    name = fields.Char(
        string="Product",
        related='product_id.name'
    )

    product_id = fields.Many2one(
        'product.product',
        string="Products",
        domain="[('type', '=', 'product'), ('qty_available', '>', 0)]",
        required=True,
    )

    serial_number = fields.Char(
        string="Serial Number",
        required=True,
    )

    saletype_id = fields.Many2one(
        'mysales.typesofsales_products',
        string="Type of sale related",
    )


class ServicesSaleTypeRelation(models.Model):
    _name = 'mysales.services_saletype_relation'

    name = fields.Char(
        string="Product",
        related='service_id.name',
    )

    service_id = fields.Many2one(
        'product.product',
        string="Services",
        domain="[('type', '=', 'service')]",
        required=True,
    )

    saletype_id = fields.Many2one(
        'mysales.typesofsales_products',
        string="Type of sale related",
    )
