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

from odoo import api, fields, models, _
from odoo.exceptions import UserError



class Company(models.Model):
    _inherit = 'res.company'

    remove_sale_advance = fields.Boolean("Remove Sales Order Advance Payments",default=True)
  

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    remove_sale_advance = fields.Boolean(string="Remove Sales Order Advance Payments",related='company_id.remove_sale_advance', readonly=False)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
   

    remove_sale_advance = fields.Boolean(string="Remove Sales Order Advance Payments",related='company_id.remove_sale_advance')

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
   


    remove_sale_advance = fields.Boolean(string="Remove Sales Order Advance Payments",related='company_id.remove_sale_advance')

