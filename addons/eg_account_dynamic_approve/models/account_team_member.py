from odoo import models, fields


class AccountTeamMember(models.Model):
    _name = "account.team.member"
    _description = "Account Team Member"

    account_team_id = fields.Many2one(comodel_name="account.teams", string="Account Team")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Team Lead")
    role = fields.Char(string="Role")
    min_amount = fields.Float(string="Minimum Amount")
    max_amount = fields.Float(string="Maximum Amount")