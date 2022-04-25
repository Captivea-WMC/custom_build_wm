# -*- coding: utf-8 -*-


{
    'name': "Odoo Academy",
    'version': '1.0',
    'depends': ['base'],
    'author': "Walter McClure",
    'category': 'Category',
    'description': """
    Training
    """,
    # data files always loaded at installation
    'data': [
      'security/academy_security.xml',
      'security/ir.model.access.csv',
      #'views/academy_menuitems.xml',
      'views/course_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
      'demo/academy_demo.xml',
    ],
}
