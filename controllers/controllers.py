# -*- coding: utf-8 -*-
from odoo import http

# class Demo-backend(http.Controller):
#     @http.route('/demo-backend/demo-backend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo-backend/demo-backend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo-backend.listing', {
#             'root': '/demo-backend/demo-backend',
#             'objects': http.request.env['demo-backend.demo-backend'].search([]),
#         })

#     @http.route('/demo-backend/demo-backend/objects/<model("demo-backend.demo-backend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo-backend.object', {
#             'object': obj
#         })