from odoo import models, fields, api

class RestaurantOrder(models.Model):
    _name = "rsm.order"
    _description = "Restaurant Order"

    table_id = fields.Many2one("rsm.table", string="Table" , domain=[('status', '=', 'free')])
    order_line_ids = fields.One2many("rsm.order.line", "order_id", string="Order Lines")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('served', 'Served'),
        ('paid', 'Paid'),
    ], string="Status", default="draft")
    total_amount = fields.Float(string="Total", compute="_compute_total", store=True)

    def action_confirm(self):
        self.write({'status': 'confirmed'})
        if self.table_id:
            self.table_id.status = 'occupied'

    def action_serve(self):
        self.write({'status': 'served'})

    def action_paid(self):
        self.write({'status': 'paid'})
        if self.table_id:
            self.table_id.status = 'free'

    @api.depends('order_line_ids.subtotal')
    def _compute_total(self):
        for order in self:
            order.total_amount = sum(order.order_line_ids.mapped('subtotal'))


class RestaurantOrderLine(models.Model):
    _name = "rsm.order.line"
    _description = "Restaurant Order Line"

    order_id = fields.Many2one("rsm.order", string="Order", ondelete="cascade")
    menu_id = fields.Many2one("rsm.menu", string="Menu Item", required=True)
    quantity = fields.Integer(string="Quantity", default=1)
    price = fields.Float(related="menu_id.price", string="Price", store=True)
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price
