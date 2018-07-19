# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductStockableSaleTypeRelation(models.Model):
    _name = 'mysales.product_saletype_relation'

    name = fields.Char(
        string="Product",
        related='product_id.name'
    )

    product_id = fields.Many2one(
        'product.template',
        string="Products",
        domain="[('type', '=', 'product')]",
        required=True,
    )

    saletype_id = fields.Many2one(
        'mysales.typesofsales_products',
        string="Type of sale related",
        required=True,
    )


class ServicesSaleTypeRelation(models.Model):
    _name = 'mysales.services_saletype_relation'

    name = fields.Char(
        string="Product",
        related='service_id.name',
    )

    service_id = fields.Many2one(
        'product.template',
        string="Services",
        domain="[('type', '=', 'service')]",
        required=True,
    )

    saletype_id = fields.Many2one(
        'mysales.typesofsales_products',
        string="Type of sale related",
        required=True,
    )