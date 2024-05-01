# -*- coding: utf-8 -*-
{
    'name': 'Stock Picking View internal Locations Only',
    'version': '7.0.1',
    'category': 'Warehouse',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """Show only Stock Locations with Internal Type Only during create Stock Picking""",

    'description': """
            Show only Stock Locations with Internal Type Only during create Stock Picking.
            """,
    'depends': [
        'stock'
    ],
    'data': [
        'views/view.xml',
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/Q28C65VF5V0',
    'images': ['static/description/stock_locations.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 00.0,
    'currency': 'EUR',
}
