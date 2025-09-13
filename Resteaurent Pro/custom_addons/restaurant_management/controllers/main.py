from odoo import http
from odoo.http import request

class RestaurantWebsite(http.Controller):

    @http.route('/restaurant/menu', type='http', auth="public", website=True)
    def restaurant_menu(self, **kw):
        menus = request.env['rsm.menu'].sudo().search([('is_available', '=', True)])
        return request.render('restaurant_management.restaurant_menu_page', {
            'menus': menus
        })

    @http.route(['/restaurant/order/<int:dish_id>'], type='http', auth="public", website=True)
    def restaurant_order(self, dish_id, **kw):
        dish = request.env['rsm.menu'].sudo().browse(dish_id)
        if not dish:
            return request.not_found()

        # Order create karo (simple flow)
        order = request.env['rsm.order'].sudo().create({
            'status': 'draft',
            'order_line_ids': [(0, 0, {
                'menu_id': dish.id,
                'quantity': 1,
            })]
        })

        return request.render('restaurant_management.restaurant_order_confirm', {
            'order': order,
            'dish': dish
        })