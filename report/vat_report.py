import operator

from odoo import api, models


class MotsoftVATReport(models.AbstractModel):
    _inherit = "report.account_financial_report.vat_report"

    def _get_tax_data(self, tax_ids):
        tax_data = super(MotsoftVATReport, self)._get_tax_data(tax_ids)
        taxes = self.env["account.tax"].browse(tax_ids)

        for tax in taxes:
            if tax.id in tax_data:
                tax_data[tax.id].update({
                    "description": tax.description or "",  # Añadimos descripción
                })

        return tax_data
