# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Job Order - Material Planning Integration with Material Requisition',
    'version': '1.6',
    'price': 11.0,
    'depends': [
        'material_purchase_requisitions',
        'odoo_job_costing_management',
            ],
    'category' : 'Projects/Projects',
    'license': 'Other proprietary',
    'currency': 'EUR',
    'summary': """This app allow your project users to create Material Requisition from job order.""",
    'description': """
job order
work order
Material Requisition
purchase Material Requisition
internal Material Requisition
internal Requisition
job Requisition
employee Requisition
Requisition job
Requisition material
Material Planning Integration
Material Planning
job Material Planning


""",
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/img.jpg'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/job_order_material_requisition/719',#'https://youtu.be/-mOkZg5kFEQ',
    'data':[
            'security/ir.model.access.csv',
            'wizard/material_requisition.xml',
            'views/project_task.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

