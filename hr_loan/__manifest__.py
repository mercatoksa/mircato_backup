# -*- coding: utf-8 -*-
###################################################################################
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'HR Loan Management',
    'version': '15.0.2.0.0',
    'summary': 'Manage Loan Requests',
    'description': """
        Helps you to manage Loan Requests of your company's staff.
        Note: you should duplicate loan rule in salary structure which you want
        """,
    'category': 'Human Resources',
    'author': 'ُEra Group',
    'company': 'Era Group',
    'website': "https://era.net.sa",
    'depends': [
        'base', 'hr', 'account', 'hr_payroll'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/hr_loan_seq.xml',
        'data/salary_rule_loan.xml',
        'views/hr_loan.xml',
        'views/hr_payroll.xml',
    ],
    # 'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
