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
