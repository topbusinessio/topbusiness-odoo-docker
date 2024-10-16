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
    'name': 'Remove Sale Order Advance Payment Options',
    'version': '7.1.0',
    'category': 'Sales',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/vw_2EQAv9nU',
    'summary': 'Sale Order Advance Payment Options By company setting',
    "description": 'Sale Order Advance Payment Options By company setting',
    'depends': ['sale','sale_management'],
    'data': [
        'views/view.xml',

    ],
    "price": 00.00,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/no_sale_adv.png'],
}

