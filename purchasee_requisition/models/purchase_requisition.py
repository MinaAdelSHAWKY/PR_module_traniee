from odoo import api, fields, models


class PurchaseRequisition(models.Model):
    _name = "purchasee.requisition"
    _description = "Purchasee Requisition"

    name = fields.Char(string='Requisition Reference',required=True,copy=False,index=True)
    employee_id = fields.Many2one('hr.employee', string='Requested By', required=True)
    responsible_id = fields.Many2one('res.users', string='Responsible')
    department_id = fields.Many2one('hr.department', string='Department')
    requisition_date = fields.Date(string='Requisition Date', default=fields.Date.today)
    requisition_deadline = fields.Date(string='Deadline')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('inventory_approval', 'Inventory Approval'),
        ('purchase_approval', 'Purchase Approval'),
        ('confirmed', 'Confirmed'),
        ('received', 'Received')
    ], string='Status', default='draft', tracking=True)

    #       to link it to the purchasee.requisition.line model.
    line_ids = fields.One2many('purchasee.requisition.line', 'requisition_id', string='Lines')

    #      Methods for buttons
    def action_submit_inventory(self):
        for rec in self:
            rec.state = 'inventory_approval'

    def action_submit_purchase(self):
        for rec in self:
            rec.state = 'purchase_approval'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_mark_received(self):
        for rec in self:
            rec.state = 'received'