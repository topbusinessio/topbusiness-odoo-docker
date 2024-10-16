# -*- coding: utf-8 -*-
#################################################################################
# Author      : Zero For Information Systems (<www.erpzero.com>)
# Copyright(c): 2016-Zero For Information Systems
# All Rights Reserved.
#Zerosystems #odoo #erp
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'Cancel and Reset to Draft Buttons Control',
    'version': '7.0.1',
    'category': 'Accounting',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """Cancel and Reset to Draft Buttons Control""",

    'description': """
            Sales Order Cancel and Reset to Draft Buttons Security.
            Purchase Order Cancel and Reset to Draft Buttons Security.
            Stock Picking Cancel and Reset to Draft Buttons Security.
            All Account Move Cancel and Reset to Draft Buttons Security.
            All Payments Cancel and Reset to Draft Buttons Security.
            """,
    'depends': [
        'base','purchase','sale_management','account','stock'
    ],
    'data': [
        'security/security.xml',
        'views/view.xml',
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/0W78Xozfbjs',
    'images': ['static/description/cancel_block.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 00.0,
    'currency': 'EUR',
}
