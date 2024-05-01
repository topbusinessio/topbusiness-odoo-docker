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


class StockPicking(models.Model):
    _inherit = 'stock.picking'
   
    @api.onchange('origin','picking_type_id')
    def onchange_source_id(self):
        for picking in self:
            user_internal = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_stock_picking_restricted.create_internal_picking_restrict').id)])
            user_receipt = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_stock_picking_restricted.create_receipt_picking_restrict').id)])
            user_deliver = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_stock_picking_restricted.create_deliver_picking_restrict').id)])
            if not user_internal and not picking.origin and picking.picking_type_id.code =='internal':
                raise UserError(_('Not Allowed To Create Manual Stock Internal Transfers!'))
            if not user_receipt and not picking.origin and picking.picking_type_id.code =='incoming':
                raise UserError(_('Not Allowed To Create Manual Stock Receipt Transfers!'))

            if not user_deliver and not picking.origin and picking.picking_type_id.code =='outgoing':
                raise UserError(_('Not Allowed To Create Manual Stock Delivery Transfers!'))

