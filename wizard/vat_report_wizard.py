from odoo import fields, models


class MotsoftVATReportWizard(models.TransientModel):
    _inherit = "vat.report.wizard"

    tax_detail = fields.Boolean(default=True)
