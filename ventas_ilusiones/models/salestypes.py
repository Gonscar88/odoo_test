# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SalesTypes(models.Model):
    _name = 'mysales.types'
    _inherit = 'mail.thread'

    name = fields.Char(
        string="Type of sale",
        required=True,
        track_visibility='on_change',
    )

    realstock = fields.Integer(
        string="Real stock",
        track_visibility='on_change',
        store=True,
    )

    confirmedstock = fields.Integer(
        string="Confirmed Stock"
    )

    reservedstock = fields.Integer(
        string="Reserved Stock"
    )
