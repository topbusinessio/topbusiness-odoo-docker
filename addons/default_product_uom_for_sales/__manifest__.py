{
    "name": "Default Product UOM for Sales",
    "version": "7.1.0",
    "category": "Sales",
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    "summary": """ default Unit value of a product in sales and Purchase UoM for Bill """,
    'description': """In Odoo, as a standard, there are two fields in the item data to define the units
        First field:(Unit of Measure)
        is unfortunately used as a default unit for inventory and also as a default unit for sale,
        but sometimes you may need to define an independent unit for sale that is different from the storage unit,
        such as the liter unit, but in selling you want another unit, such as a barrel, and the barrel unit is the default unit for sale, 
        so with In this system, you can define (Default Sale UoM) to be an independent default unit for the item in the sales screens (Sales Orders - Sales Invoice - Credit Note.) 
        If the (Default Sale UoM) unit is not specified, the default unit of sale will be (Unit of Measure).
        Second field:(Purchase UoM)
        In this field, the default unit for purchase orders is defined, 
        but it does not work when creating a manual invoice or creating a manual refund, and the default unit in this case is (Unit of Measure). 
        But with this program we corrected this error and made the default unit (Purchase UoM).

      """,
    "depends": ["sale_management","account"],
    "data": [
        "views/view.xml",
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/HrpWNfNoywg',
    'images': ['static/description/default_product_uom_for_sales.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 00.0,
    'currency': 'EUR',
}
