# from odoo import http


# class Photography(http.Controller):
#     @http.route('/photography/photography', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/photography/photography/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('photography.listing', {
#             'root': '/photography/photography',
#             'objects': http.request.env['photography.photography'].search([]),
#         })

#     @http.route('/photography/photography/objects/<model("photography.photography"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('photography.object', {
#             'object': obj
#         })

