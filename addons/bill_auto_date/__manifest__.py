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
    'name': 'Bill Date today Date',
    'version': '7.0.1',
    'category': 'Accounting',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """Bill Date field will be equal to today's date automatically """,


    'description': """
        The standard situation of the Odoo system, when confirming the Bill,
        the Bill Date field is empty and must be filled in manually,
        but with this modification, the date field will be equal to today's date automatically ” ,


        """,
    'depends': [
        'account',
    ],
    'data': [
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/fzxzoRlrabA',
    'images': ['static/description/bill_date_today.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 0.00,
    'currency': 'EUR',
}
