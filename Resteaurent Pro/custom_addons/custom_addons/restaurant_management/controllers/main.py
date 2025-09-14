from odoo import http
from odoo.http import request

class RestaurantWebsite(http.Controller):
        
    @http.route('/restaurant/menu_list', type='http', auth="public", website=True)
    def restaurant_menu_list(self, **kw):
        menus = request.env['rsm.menu'].sudo().search([('is_available', '=', True)])
        return request.render('restaurant_management.restaurant_menu_list', {
            'menus': menus
        })
        
        
    @http.route('/restaurant/dish/<int:dish_id>', type='http', auth="public", website=True)
    def restaurant_dish_detail(self, dish_id, **kw):
        dish = request.env['rsm.menu'].sudo().browse(dish_id)
        if not dish.exists():
            return request.not_found()
        return request.render('restaurant_management.restaurant_dish_detail', {
            'dish': dish
        })
        
    @http.route('/restaurant/place_order', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def restaurant_place_order(self, **post):
        dish_id = int(post.get('dish_id'))
        quantity = int(post.get('quantity', 1))

        dish = request.env['rsm.menu'].sudo().browse(dish_id)
        if not dish.exists():
            return request.not_found()

        order = request.env['rsm.order'].sudo().create({
            'status': 'draft',
            'order_line_ids': [(0, 0, {
                'menu_id': dish.id,
                'quantity': quantity,
            })]
        })

        return request.render('restaurant_management.restaurant_order_done', {
            'order': order,
        })