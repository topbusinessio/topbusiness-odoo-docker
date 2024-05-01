
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

from odoo import fields, models, _, api


class SaleOrder(models.Model):
    _inherit = "sale.order"


    partner_amount_due = fields.Monetary(string="Amount Due",
        related='partner_id.total_due',readonly=True)
    partner_total_overdue = fields.Monetary(string="Amount Over Due",
        related='partner_id.total_overdue',readonly=True)


class AccountMove(models.Model):
    _inherit = "account.move"


    partner_amount_due = fields.Monetary(string="Amount Due",
        related='partner_id.total_due',readonly=True)
    partner_total_overdue = fields.Monetary(string="Amount Over Due",
        related='partner_id.total_overdue',readonly=True)

class AccountPayment(models.Model):
    _inherit = "account.payment"


    partner_amount_due = fields.Monetary(string="Amount Due",
        related='partner_id.total_due',readonly=True)
    partner_total_overdue = fields.Monetary(string="Amount Over Due",
        related='partner_id.total_overdue',readonly=True)
