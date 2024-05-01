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
    'name': 'Create Account Move Restrict',
    'version': '7.1.0',
    'category': 'Accounting',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/q2iUCSC6Ick',
    'summary': 'Invoice, Bill and Journal Entry Manual Creation Restricted',
    "description": 'Invoice, Bill and Journal Entry Manual Creation Restricted',
    'depends': ['base','account'],
    'data': [
        'security/security.xml',

    ],
    "price": 00.00,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/not_allwoed.png'],
}

