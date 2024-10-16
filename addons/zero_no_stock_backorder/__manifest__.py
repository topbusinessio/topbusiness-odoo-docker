# -*- coding: utf-8 -*-
#################################################################################
# Author      : Zero For Information Systems (<www.erpzero.com>)
# Copyright(c): 2016-Zero For Information Systems
# All Rights Reserved.
#zerosystems #erp #odoo
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'User Restrict Backorder During Picking',
    'version': '7.0.1',
    'category': 'Warehouse',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """New Security Groups to control stock picking backorder allowed or not allowed""",

    'description': """
            In Odoo as a standard the in picking Transfers when Product Demand Qty is More than Done Qty then Backorder wizard form pop to user to select between creating Backorder or No Backorder.
            but with this Module in case user hasn't any of the following security groups the user error message will pop instead of backorder wizard form.
            1- Allow Create Stock Delivery BackOrder.

            2- Allow Create Stock Receipt BackOrder.

            3- Allow Create Stock Internal BackOrder.
            """,
    'depends': [
        'base','stock'
    ],
    'data': [
        'security/security.xml',
        'views/view.xml',
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/kMUPGwlidpE',
    'images': ['static/description/zero_no_stock_backorder.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 00.0,
    'currency': 'EUR',
}
