from odoo import models, fields

class RestaurantMenu(models.Model):
    _name = "rsm.menu"
    _description = "Restaurant Menu"

    name = fields.Char(string="Dish Name", required=True)
    category = fields.Selection([
        ('starter', 'Starter'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drinks', 'Drinks'),
    ], string="Category", required=True)
    price = fields.Float(string="Price", required=True)
    is_available = fields.Boolean(string="Available", default=True)
    dish_image = fields.Binary(string = "Dish Image")
    description = fields.Text(string = 'Description')