{
    'name': "Test App",
    'summary': """TESTING PURPOSE""",

    'description': """TESTING""",

    'author': "TEST",
    'website': "https://www.test.com/",
    'category': 'Uncategorized',
    'version': '17.0',
    "currency": "USD",
    'price': 1.0,

    'category': 'Productivity',

    'images': ['static/description/banner.jpg'],

    'depends': ['base', 'hr', 'account', 'om_account_accountant', 'accounting_pdf_reports', 'web'],
    'data': [
        # data files
        'data/sequence.xml',
        'data/mail_template_data.xml',
        'data/loan_type_init_data.xml',
        'data/update_quick_loan_amount_payroll.xml',
        'data/ir_attachment.xml',

        # record rules and access rights
        'security/employee_loan_security.xml',
        'security/ir.model.access.csv',

        # wizard
        'wizard/quick_loan_general_wizard.xml',

        # views
        'views/employee_quick_loan_request.xml',
        'views/employee_loan_types.xml',
        'views/employee_loan_return.xml',
        'views/employee_manage_request.xml',
        'views/set_loan_amount.xml',
        'views/reject_reason_popup_view.xml',

        'views/hr_contract_view.xml',

        # reports
        'reports/quick_loan_general_report.xml',
        'reports/employee_loan_report.xml',
        'reports/general_loan_report.xml',

        # config_settings
        'views/res_config_settings_views.xml',

    ],
    'qweb': [
        'static/src/xml/change_button_text_add_funds.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'aalogics_employee_loan/static/src/**/*',
            'aalogics_employee_loan/static/src/css/custom_styles.css',
        ],
        'web.assets_frontend': [
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
# -*- coding: utf-8 -*-
