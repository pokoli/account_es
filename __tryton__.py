#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Account chart for Spain ',
    'name_es_ES': 'Plan general contable español ',
    'version': '1.0.0',
    'author': 'Sergi Almacellas Abellana',
    'email': 'sergi@koolpi.com',
    'website': 'http://www.tryton.org',
    'description': '''Define an account chart template for Spain.
Useful to create a Spanish account chart with the wizard in
"Financial Management>Configuration>General Account>Create Chart of Account from Template".
''',
    'description_es_ES': '''Define el plan general contable español.
Es útil para crear el plan contable español con el asistente en
"Gestión Financiera->Configuración->Cuenta General->Crear Plan Contable de una Plantilla".
''',
    'depends': [
        'account',
    ],
    'xml': [
        'account_es.xml',
        'tax_es.xml',
    ],
}
