# -*- coding: utf-8 -*-
#################################################################################
# Author      : Zero For Information Systems (<www.erpzero.com>)
# Copyright(c): 2016-Zero For Information Systems
# All Rights Reserved.
#zerosystems #odoo #erp
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': 'Create Manual Stock Picking Restricted',
    'version': '7.1.0',
    'category': 'Warehouse',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/zvtd_wkRdqg',
    'summary': 'Receipt, Delivery and Internal Picking Transfers Manual Creation Restricted',
    "description": 'Receipt, Delivery and Internal Picking Transfers Manual Creation Restricted',
    'depends': ['base','stock'],
    'data': [
        'security/security.xml',

    ],
    "price": 0.00,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/stock_picking.png'],
}

