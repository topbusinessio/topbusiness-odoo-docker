# -*- coding: utf-8 -*-
{
    'name': 'Customer Amount Due Enterprise',
    'version': '6.0.1',
    'category': 'Accounting',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """Show Customer Amount Due and Amount Over Due""",

    'description': """
            Show Customer Amount Due and Amount Over Due in sale Order, Invoice, Credit Note and payments""",
    'depends': [
        'base','sale_management','account_followup'
    ],
    'data': [
        'security/security.xml',
        'views/due.xml',
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/RCq8pTnsgMw',
    'images': ['static/description/due_over.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 00.0,
    'currency': 'EUR',
}
