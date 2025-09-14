from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RestaurantReservation(models.Model):
    _name = "rsm.reservation"
    _description = "Table Reservation"

    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    table_id = fields.Many2one("rsm.table", string="Table", required=True)
    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", required=True)
    state = fields.Selection([
        ("draft", "Draft"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("done", "Done"),
    ], default="draft")

    @api.constrains("start_time", "end_time", "table_id")
    def _check_overlap(self):
        for rec in self:
            if rec.start_time >= rec.end_time:
                raise ValidationError("End time must be after start time.")

            overlapping = self.search([
                ("id", "!=", rec.id),
                ("table_id", "=", rec.table_id.id),
                ("state", "=", "confirmed"),
                ("start_time", "<", rec.end_time),
                ("end_time", ">", rec.start_time),
            ])
            if overlapping:
                raise ValidationError("This table is already reserved for this time slot.")

    def action_confirm(self):
        for rec in self:
            rec.state = "confirmed"
    def action_create_order(self):
        for rec in self:
            if rec.state != "confirmed":
                continue
            order = self.env["rsm.order"].create({
                "table_id": rec.table_id.id,
            })
            return {
                "type": "ir.actions.act_window",
                "res_model": "rsm.order",
                "view_mode": "form",
                "res_id": order.id,
            }
    def action_cancel(self):
        for rec in self:
            rec.state = "cancelled"

    def action_done(self):
        for rec in self:
            rec.state = "done"