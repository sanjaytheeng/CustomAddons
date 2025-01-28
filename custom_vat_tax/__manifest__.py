{
    'name': 'Vendor VAT ID',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Add VAT ID field to Vendor',
    'author': 'Sanjay Tamang',
    'depends': ['base', 'account'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
