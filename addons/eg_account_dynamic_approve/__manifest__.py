{
    'name': 'Dynamic Approve in Account',
    'version': '17.0',
    'category': 'Accounting/Accounting',
    'summary': 'Accounting Invoice-Bill Dynamic Approval Workflow Odoo Apps',
    'author': 'INKERP',
    'website': 'https://www.inkerp.com/',
    'depends': ['base', 'account', 'payment'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/account_teams_views.xml',
        'views/account_move_view.xml',
    ],
    
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
