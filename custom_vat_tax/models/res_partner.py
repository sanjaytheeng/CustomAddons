from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_pan = fields.Char(string='Pan ID', help="Pan ID of the vendor")