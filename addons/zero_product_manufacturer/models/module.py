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

import base64
import datetime
import re
from lxml import etree
import io
import math
import os
from collections import defaultdict
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError, UserError
from odoo.osv import expression
from PIL import Image
from odoo.tools.misc import formatLang, format_date, get_lang
from odoo.osv.expression import AND
from odoo.http import request

from odoo.tests.common import Form
from itertools import groupby

import logging
import psycopg2
import pytz

_logger = logging.getLogger(__name__)



class ProductManufacturer(models.Model):
    _name = 'product.manufacturer'
    _description = 'Product Manufacturer'
    _inherit = ['image.mixin','portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _check_company_auto = True

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    logo = fields.Binary(string="Manufacturer Logo", readonly=False, store=True)
    company_id = fields.Many2one('res.company', string='Company',index=True, default=lambda self: self.env.company)
    product_ids = fields.Many2many(string='Products', comodel_name="product.template", relation="manufacturer_rel", column1="manufacturer_id", column2="product_id",readonly=False)

   
    products_count = fields.Integer(
        '# Products', compute='_compute_branch_count',
        help="The number of Products under this Manufacturer")

    @api.depends('product_ids')
    def _compute_branch_count(self):
        for rec in self:
            rec.products_count = len(rec.product_ids)

    def redirect_products(self,context=None):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'view_mode': 'tree,form',
            'res_model': 'product.product',
            'domain': [('manufacturere_ids','=',self.id)],
            'target': 'current',
            'context': context,
        }
    def redirect_product_variants(self,context=None):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products Variants',
            'view_mode': 'tree,form',
            'res_model': 'product.template',
            'domain': [('manufacturere_ids','=',self.id)],
            'target': 'current',
            'context': context,
        }

            ###########           Redirect Branches Tags      ####################

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    def _manufactureres_count(self):
        return self.env['product.manufacturer'].sudo().search_count([])

    manufactureres_count = fields.Integer(compute='_compute_manufactureres_count', string="Number of manufacturer", default=_manufactureres_count)


    def _compute_manufactureres_count(self):
        manufactureres_count = self._manufactureres_count()
        for Product in self:
            Product.branches_count = branches_count



    manufacturere_ids = fields.Many2many(comodel_name="product.manufacturer", relation="manufacturer_rel", column1="product_id", column2="manufacturer_id",string='Manufacturers', readonly=False)

    
