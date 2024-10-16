# -*- coding: utf-8 -*-
#################################################################################
# Author      : Zero For Information Systems (<www.erpzero.com>)
# Copyright(c): 2016-Zero For Information Systems
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################


from odoo import api, Command, fields, models, _
from odoo.exceptions import ValidationError, UserError,RedirectWarning

class Company(models.Model):
    _inherit = 'res.company'

    sale_unique_product = fields.Boolean(string="Activate Unique Sale order products")
    purchase_unique_product = fields.Boolean(string="Activate Unique purchase order products")
    invoice_unique_product = fields.Boolean(string="Activate Unique Invoice products")
    bill_unique_product = fields.Boolean(string="Activate Unique Bill products")

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def _compute_sale_unique_product(self):
        company = self.env.company
        if company.sale_unique_product:
            self.sale_unique_product = True
        else:
            self.sale_unique_product = False

    sale_unique_product = fields.Boolean(default='_compute_sale_unique_product',store=True,string="Activate Unique Sale order products",readonly=False)

    @api.constrains('order_line','sale_unique_product')
    def _check_product_id_unique(self):
        for move in self:
            user_so = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('unique_product_name.group_sales_uniqe_product').id)])
            if not user_so:
                if move.sale_unique_product and  len(move.order_line) > 0:
                    for line in move.order_line.filtered(lambda x: x.display_type not in ('line_section', 'line_note')):
                        results1 = line.search_count([('product_id', '=', line.product_id.id), ('order_id', '=', line.order_id.id)])
                        if results1 > 1:
                            raise ValidationError(_('product number already exists!. (Product Name: %s)', line.product_id.name))



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    def _compute_purchase_unique_product(self):
        company = self.env.company
        if company.purchase_unique_product:
            self.purchase_unique_product = True
        else:
            self.purchase_unique_product = False

    purchase_unique_product = fields.Boolean(default='_compute_purchase_unique_product',store=True,string="Activate Unique Purchase order products",readonly=False)

    @api.constrains('order_line','purchase_unique_product')
    def _check_product_id_unique(self):
        for move in self:
            user_po = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('unique_product_name.group_purchase_uniqe_product').id)])
            if not user_po:
                if move.purchase_unique_product and  len(move.order_line) > 0:
                    for line in move.order_line.filtered(lambda x: x.display_type not in ('line_section', 'line_note')):
                        results1 = line.search_count([('product_id', '=', line.product_id.id), ('order_id', '=', line.order_id.id)])
                        if results1 > 1:
                            raise ValidationError(_('product number already exists!. (Product Name: %s)', line.product_id.name))

class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def compute_bill_unique_product(self):
        return self.env.company.bill_unique_product


    @api.model
    def compute_invoice_unique_product(self):
        return self.env.company.invoice_unique_product



    invoice_unique_product = fields.Boolean(default=compute_invoice_unique_product,store=True,string="Activate Unique Invoice products",readonly=False)


    bill_unique_product = fields.Boolean(default=compute_bill_unique_product,store=True,string="Activate Unique Bill products",readonly=False)


    @api.constrains('invoice_line_ids','invoice_unique_product','bill_unique_product','move_type')
    def _check_product_id_unique(self):
        for move in self:
            user_inv = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('unique_product_name.group_invoice_uniqe_product').id)])
            user_bill = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('unique_product_name.group_bill_uniqe_product').id)])
            if not user_inv and move.move_type in ('out_invoice','out_refund'):
                if move.invoice_unique_product and  len(move.invoice_line_ids) > 0:
                    for line in move.invoice_line_ids.filtered(lambda x: x.display_type not in ('line_section', 'line_note')):
                        results1 = line.search_count([('product_id', '=', line.product_id.id), ('move_id', '=', line.move_id.id)])
                        if results1 > 1:
                            raise ValidationError(_('product number already exists!. (Product Name: %s)', line.product_id.name))
            if not user_bill and move.move_type in ('in_invoice','in_refund'):
                if move.bill_unique_product and  len(move.invoice_line_ids) > 0:
                    for line in move.invoice_line_ids.filtered(lambda x: x.display_type not in ('line_section', 'line_note')):
                        results2 = line.search_count([('product_id', '=', line.product_id.id), ('move_id', '=', line.move_id.id)])
                        if results2 > 1:
                            raise ValidationError(_('product number already exists!. (Product Name: %s)', line.product_id.name))
                 
