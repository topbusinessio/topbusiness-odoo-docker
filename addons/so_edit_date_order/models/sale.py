
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
from datetime import date, datetime
from odoo.exceptions import AccessError, UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def _prepare_confirmation_values(self):
        if str(self.date_order.date()) < str(date.today()):
            return {
                'state': 'sale',
            }
        else:
            return {
                'state': 'sale',
                'date_order': fields.Datetime.now()
            }
