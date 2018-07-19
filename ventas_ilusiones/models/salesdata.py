# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SalesData(models.Model):
    _name = 'mysales.maindata'
    _inherit = 'mail.thread'

    name = fields.Char(
        string="Sale Number",
        default=lambda self: 'MS000X',
        required=True,
    )

    customer = fields.Many2one(
        'res.partner',
        string="Customer",
        required=True,
    )

    sales_lines_ids = fields.One2many(
        'mysales.typesofsales_products',
        'mysale_id',
        string="Sale lines",
        required=True,
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('quotation', 'Quotation'),
            ('confirm', 'Confirmed'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
        string="State",
        default='draft',
        required=True
    )

    @api.multi
    def setnewstockproducts(self):
        # Update quantity on hand for all the sold products
        stock_discount = 0
        for lineas in self.sales_lines_ids:
            if lineas.stockable_products:
                for producto in lineas.stockable_products:
                    stock_discount += 1
                    product_obj = producto.product_id
                    product_stock = product_obj.qty_available
                    # Search the current stock of the product
                    stock_qnt_obj = producto.env['stock.quant'].sudo().search(
                        [
                            ('product_id.id', '=', product_obj.id)
                        ]
                    )
                    if stock_qnt_obj:
                        stock_qnt_obj = stock_qnt_obj[-1]
                        """ Ask for the stock and 
                        confirm that is enough to sell all the products """
                        if product_stock > 0 and product_stock > stock_discount:
                            new_stock = int(product_stock) - stock_discount
                            stock_qnt_obj.sudo().write(
                                {
                                    'quantity': new_stock,
                                }
                            )
                        else:
                            raise UserError(
                                _(
                                    'You cant set to done this sale,'
                                    'there is not enough stock'
                                )
                            )

    @api.multi
    def settoquotation(self):
        self.state = 'quotation'

    @api.multi
    def settoconfirm(self):
        self.state = 'confirm'

    @api.multi
    def settodone(self):
        self.setnewstockproducts()
        self.state = 'done'

    @api.multi
    def settocancell(self):
        self.state = 'cancel'


    @api.model
    def create(self, vals):
        if vals.get('name', 'MS000X') == 'MS000X':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'mysales_maindata'
            ) or 'MS000X'
        return super(SalesData, self).create(vals)
