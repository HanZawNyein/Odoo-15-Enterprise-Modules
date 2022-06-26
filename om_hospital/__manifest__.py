{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Han Zaw Nyine',
    'sequence': -100,
    'summary': 'Hospital Management System',
    'description': """
    Hospital Management System
    """,
    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient.tag.csv',
        'data/patient_tag_data.xml',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/odoo_play_ground_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
