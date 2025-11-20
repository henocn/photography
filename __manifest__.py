{
    'name': "photography",

    'summary': "Organization of photography sessions and client management",

    'description': """
        This module helps manage photography sessions, client information, and scheduling.
    """,

    'author': "Henoc N'GASAMA",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': "Henoc N'GASAMA/base",
    'version': '0.1',
    "application": True,
    'installable': True,
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', "web"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/photography_client_views.xml",
        "views/photography_equipment_views.xml",
        "views/photography_furniture_views.xml",
        "views/photography_media_views.xml",
        "views/photography_project_views.xml",

        "views/employee_views.xml",

        "views/menu/menu-actions.xml",
        "views/menu/menu.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'photography/static/src/css/photography_styles.css',
        ],
    },
}

