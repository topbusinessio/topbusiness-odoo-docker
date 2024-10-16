from odoo import models, fields


class AccountTeams(models.Model):
    _name = "account.teams"
    _description = "Account Teams"

    name = fields.Char(string="Name")
    team_lead_id = fields.Many2one(comodel_name="res.partner", string="Team Lead")
    team_member = fields.One2many(comodel_name="account.team.member", inverse_name="account_team_id", string="Team Member")