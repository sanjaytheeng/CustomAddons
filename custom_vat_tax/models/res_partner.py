from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_use_vat = fields.Boolean(string="Use VAT ID", help="Check if the user wants to use VAT ID instead of Pan ID")
    x_vat_id = fields.Char(string="VAT ID", help="VAT ID of the vendor")
    x_pan_id = fields.Char(string="PAN ID", help="PAN ID of the vendor")
