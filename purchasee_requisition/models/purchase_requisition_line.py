from odoo import api, fields, models


class PurchaseRequisitionLine(models.Model):
    _name = 'purchasee.requisition.line'
    _description = 'Purchase Requisition Line'

    requisition_id = fields.Many2one('purchasee.requisition', string='Requisition')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    description = fields.Text(string='Description')
    quantity = fields.Float(string='Quantity', default=1.0)
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
