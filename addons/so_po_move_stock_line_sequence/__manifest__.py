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
    "name": "Line Sequence Sales,Purchase,Invoices,Stock",
    'version': '0.7.2',
    'category': 'Sales',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/kPHsGoxUsNM',
    "summary": "sales order, Purchase order , Stock Piking , Invoice and Bill line sequence .",
    "data": [
        "views/view.xml",
         "views/report.xml"
         ],
    "depends": ['sale_stock','purchase','account'],
    "price": 0.0,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/sequence.png'],
}
