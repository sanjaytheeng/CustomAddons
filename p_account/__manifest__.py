{
    'name': "p_account",
    'summary': """
        Placement Transaction Type""",

    'description': """
        This helps to add placement transaction type in payments in accounting
    """,

    'author': "Axon System",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/placement_account_inherit_view.xml',
        'views/placement_account_inherit_config_menu.xml',
    ]
}
