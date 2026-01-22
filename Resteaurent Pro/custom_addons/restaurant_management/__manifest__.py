{
    'name':'Food Restaurant Management',
    'version':'18.0',
    'author':'Vishal',
    'category': 'Restaurant',
    'summary': 'Manage Food Menu, Tables, and Orders in a Restaurant',
    'description': """
                Restaurant Management System:
                This module helps to manage a food restaurant:
                - Menu Management (foods, drinks, categories, prices)
                - Table Management (tables, capacity, status)
                - Order Management (create orders, assign tables, track status)
                    """,
    'depends': ['base', 'sale', 'account','website'],
    'data': [
         'security/ir.model.access.csv',
        'views/restaurant_menu_views.xml',
        'views/restaurant_order_views.xml',
        'views/restaurant_table_views.xml',
        'views/reservation_views.xml',
        'views/restaurant_templates.xml',
    ],
    'assets': {
    'web.assets_frontend': [
        'restaurant_management/static/src/js/quantity.js',
    ],
},
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
