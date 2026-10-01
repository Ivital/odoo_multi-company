# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    company_ids = fields.Many2many(
        comodel_name="res.company",
        string="Companies",
        help="This view is specific to these companies.",
    )

    @api.model
    def _get_inheriting_views_domain(self):
        domain = list(super()._get_inheriting_views_domain() or [])
        return domain + [
            "|",
            ("company_ids", "=", False),
            ("company_ids", "in", self.env.company.ids),
        ]
