
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

    _inherit = "stock.picking"

    product_uom_qty = fields.Float(
        'Total Qty Demand',digits='Product Unit of Measure',compute='_quantity_picking_compute')

    quantity = fields.Float(
        'Total Quantity Done',digits='Product Unit of Measure', compute='_quantity_picking_compute')


    @api.onchange("move_ids_without_package","move_ids_without_package.product_uom_qty", "move_ids_without_package.quantity")
    def _quantity_picking_compute(self):
        for order in self:
            uom_qty = 0.0
            done_qty = 0.0
            for line in order.move_ids_without_package:
                uom_qty += (line.product_uom_qty)
                done_qty += (line.quantity)
            order.product_uom_qty = uom_qty
            order.quantity = done_qty

  

    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        for move in self:
            user_delivery = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('zero_no_stock_backorder.zero_no_stock_backorder_delivery').id)])
            user_receipt = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('zero_no_stock_backorder.zero_no_stock_backorder_receipt').id)])
            user_internal = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('zero_no_stock_backorder.zero_no_stock_backorder_internal').id)])
            if not user_delivery and not move.origin and move.picking_type_id.code =='outgoing':
                if move.product_uom_qty != move.quantity:
                    raise UserError(_('Total Qty Demand Not Equal Total Quantity Done'))
            if not user_receipt and not move.origin and move.picking_type_id.code =='incoming':
                if move.product_uom_qty != move.quantity:
                    raise UserError(_('Total Qty Demand Not Equal Total Quantity Done'))
            if not user_internal and not move.origin and move.picking_type_id.code =='internal':
                if move.product_uom_qty != move.quantity:
                    raise UserError(_('Total Qty Demand Not Equal Total Quantity Done'))

        return res
