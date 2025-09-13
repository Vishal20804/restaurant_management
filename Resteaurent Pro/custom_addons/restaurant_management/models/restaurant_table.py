from odoo import models, fields

class RestaurantTable(models.Model):
    _name = "rsm.table"
    _description = "Restaurant Table"

    name = fields.Char(string="Table Number/Name", required=True)
    capacity = fields.Integer(string="Capacity", default=2)
    status = fields.Selection([
        ('free', 'Free'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
    ], string="Status", default="free")
