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

class AccountPaymentRegisterInherit(models.TransientModel):
    _inherit = 'account.payment.register'

    transaction_type = fields.Many2one(
        'placement.transaction.type',
        string="Transaction Type",
        domain=[],  # Ensures all records are selectable
        context={'create': False, 'edit': False},  # Disables creation & editing in selection
        required=True
    )

    def action_create_payments(self):
        res = super(AccountPaymentRegisterInherit, self).action_create_payments()

        # Get the created payments by checking payments linked to the selected invoices
        payments = self.env['account.payment'].search([('ref', '=', self.communication)])

        if payments:
            payments.write({'transaction_type': self.transaction_type.id})

        return res







