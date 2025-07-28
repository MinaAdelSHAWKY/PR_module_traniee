{
    'name': 'Purchasee Requisition',
    'version': '1.0.0',
    'category': 'Purchases',
    'summary': 'Internal Purchase Requisition Workflow',
    'depends': ['base', 'hr', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/purchase_requisition_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': '-100'
}
