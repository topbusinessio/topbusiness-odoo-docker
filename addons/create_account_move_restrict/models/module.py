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


class AccountMove(models.Model):
    _inherit = 'account.move'
   
    @api.onchange('invoice_origin','move_type')
    def onchange_invoice_origin(self):
        for move in self:
            user_invoice = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_account_move_restrict.create_invoice_restrict').id)])
            user_bill = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_account_move_restrict.create_bill_restrict').id)])
            user_entry = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_account_move_restrict.create_entry_restrict').id)])
            if not user_invoice and not move.invoice_origin and move.move_type =='out_invoice':
                raise UserError(_('Not Allowed To Create Manual Invoice'))
            if not user_bill and not move.invoice_origin and move.move_type =='in_invoice':
                raise UserError(_('Not Allowed To Create Manual Bill'))
            if not user_entry and not move.invoice_origin and move.move_type =='entry':
                raise UserError(_('Not Allowed To Create Manual Journal Entry'))

