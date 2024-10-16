
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

from operator import mod
from odoo import fields, models, _, api

from datetime import date, timedelta, datetime


class AccountMove(models.Model):
    _inherit = "account.move"

    def _post(self, soft=False):
        for move in self:
            if move.is_purchase_document(include_receipts=True) and not move.invoice_date:
                move.invoice_date = fields.Date.context_today(self)
        res = super(AccountMove, self)._post(soft=False)
        return res

