from odoo import models, fields


class AccountApproveRoute(models.Model):
    _name = "account.approve.route"
    _description = "Account Approve Route"

    invoice_id = fields.Many2one(comodel_name="account.move", string="Invoice")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Approver")
    role = fields.Char(string="Role")
    state = fields.Selection(selection=[('draft', 'Pending'), ('done', 'To Approve'), ('reject', 'Disapprove')],
                             string='Status', default='draft')
