# -*- coding: utf-8 -*-
{
    'name': "Motsoft VAT Report",

    'summary': "Mejoras al informe de impuestos.",

    'description': """
Se ofrecen las siguientes mejoras al informe de impuestos:
    * Se añade la descripción del impuesto en el informe.
    * Se fija por defecto el Detalle de Impuestos en el Wizard.
    """,

    'author': "David Sanromá",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '17.0.0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account_financial_report',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/templates/vat_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
