# -*- coding: utf-8 -*-
# from odoo import http


# class odooalmacen(http.Controller):
#     @http.route('/odooalmacen/odooalmacen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odooalmacen/odooalmacen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odooalmacen.listing', {
#             'root': '/odooalmacen/odooalmacen',
#             'objects': http.request.env['odooalmacen.odooalmacen'].search([]),
#         })

#     @http.route('/odooalmacen/odooalmacen/objects/<model("odooalmacen.odooalmacen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odooalmacen.object', {
#             'object': obj
#         })
