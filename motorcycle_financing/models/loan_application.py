# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class LoanApplication(models.Model):
    _name = 'loan.application'
    _description = 'Loan Application'

    name = fields.Char(
        string='Application Number',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New')
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    date_application = fields.Date(
        string='Application Date',
        default=fields.Date.context_today
    )
    date_approval = fields.Date(
        string='Approval Date'
    )
    date_rejection = fields.Date(
        string='Rejection Date'
    )
    date_signed = fields.Date(
        string='Signed Date'
    )
    down_payment = fields.Monetary(
        string='Down Payment',
        currency_field='currency_id',
        required=True,
    )
    interest_rate = fields.Float(
        string='Interest Rate (%)',
        digits=(5, 4),
        default=0.0
    )
    loan_amount = fields.Monetary(
        string='Loan Amount',
        currency_field='currency_id',
    )
    loan_term = fields.Integer(
        string='Loan Term (Months)',
        required=True,
        default=36
    )
    rejection_reason = fields.Text(
        string='Rejection Reason'
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('sent', 'Sent'),
            ('review', 'Credit Check'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('signed', 'Signed'),
            ('cancel', 'Canceled')
        ], string='Status',
        default='draft',
        required=True,
        readonly=True,
    )
    notes = fields.Html(
        string='Notes',
    )

