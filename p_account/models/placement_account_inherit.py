from odoo import models, fields, api

class PlacementTransactionType(models.Model):
    _name = 'placement.transaction.type'

    name = fields.Char(string="Transaction Type", required=True)

class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'

    transaction_type = fields.Many2one(
        'placement.transaction.type',
        string="Transaction Type",
        domain=[],  # Ensures all records are selectable
        context={'create': False, 'edit': False},  # Disables creation & editing in selection
        required=True
    )








