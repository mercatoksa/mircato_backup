# -*- coding: utf-8 -*-
###################################################################################
#
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
    'name': ' Loan Accounting',
    'version': '15.0.2.0.0',
    'summary': 'Loan Accounting',
    'description': """
        Create accounting entries for loan requests.
        """,
    'category': 'Human Resources',
    'author': 'ُEra Group',
    'company': 'Era Group',
    'website': "https://era.net.sa",
    'depends': [
        'base', 'hr', 'account', 'hr_loan',
    ],
    'data': [
        'views/hr_loan_config.xml',
        'views/hr_loan_acc.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
