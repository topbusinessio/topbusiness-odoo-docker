from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    account_team_id = fields.Many2one(comodel_name="account.teams", string="Account Team")
    account_approve_line = fields.One2many(comodel_name="account.approve.route", inverse_name="invoice_id")

    @api.model
    def create(self, vals):
        res = super(AccountMove, self).create(vals)
        if res.account_team_id and res.move_type in ["out_invoice", "out_refund", "in_invoice", "in_refund"]:
            for member_id in res.account_team_id.team_member:
                self.env["account.approve.route"].create({
                    "invoice_id": res.id,
                    "partner_id": member_id.partner_id.id,
                    "role": member_id.role,
                    "state": "draft",
                })
        return res

    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        if 'account_team_id' in vals:
            for line_id in self.account_approve_line:
                line_id.sudo().unlink()
            if self.account_team_id and self.move_type in ["out_invoice", "out_refund", "in_invoice", "in_refund"]:
                for member_id in self.account_team_id.team_member:
                    self.env["account.approve.route"].create({
                        "invoice_id": self.id,
                        "partner_id": member_id.partner_id.id,
                        "role": member_id.role,
                        "state": "draft",
                    })
        return res

    def action_post(self):
        if self.account_approve_line and self.move_type in ["out_invoice", "out_refund", "in_invoice", "in_refund"]:
            if self.account_approve_line.filtered(lambda l: l.state != 'done'):
                raise ValidationError(_('%s %s is not approved') % (self.name if self.name and self.name != "/" else "", dict(self._fields['move_type'].selection).get(self.move_type)))
        return super(AccountMove, self).action_post()

    def approve_invoice(self):
        if self.account_approve_line and self.move_type in ["out_invoice", "out_refund", "in_invoice", "in_refund"]:
            if self.account_approve_line.filtered(lambda l: l.partner_id.id == self.env.user.partner_id.id):
                for line_id in self.account_approve_line.filtered(lambda l: l.partner_id.id == self.env.user.partner_id.id):
                    line_id.write({
                        "state": "done"
                    })
            else:
                raise ValidationError(_("Sorry, you don't have access for approve %s Invoice") % (self.name if self.name and self.name != "/" else ""))

    def disapprove_invoice(self):
        if self.account_approve_line and self.move_type in ["out_invoice", "out_refund", "in_invoice", "in_refund"]:
            if self.account_approve_line.filtered(lambda l: l.partner_id.id == self.env.user.partner_id.id):
                for line_id in self.account_approve_line.filtered(lambda l: l.partner_id.id == self.env.user.partner_id.id):
                    line_id.write({
                        "state": "reject"
                    })
            else:
                raise ValidationError(_("Sorry, you don't have access for Disapprove %s Invoice") % (self.name if self.name and self.name != "/" else ""))
