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

{
    'name': 'Unique Product Name',
    'version': '7.0.0',
    'category': 'Sales',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/t_0NAmEnKvU',
    'summary': """Unique Product Name in Sales Order,Purchase Order,Invoice and Bill""",
    'description': """
        In Odoo, as a standard, the name of the product can be repeated in the sale order,
        purchase order, sales invoice, purchase invoice, as well as debit and credit notes,
        but with this module you can activate the conditions not to repeat the name of the product in the right of the previous documents
        or all of them. Also, the system can be activated in a specific company or all companies defined In the same database
        and also you can allow one or more users to bypass these conditions""",
    'depends': ['account','purchase','sale_management'],
    'data': [
        'views/view.xml',
    ],
    'images': ['static/description/unique_product_name.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    "price": 00.0,
    "currency": 'EUR',
}
