import json
from odoo import http
from odoo.http import request,rpc_response
from odoo.http import JsonRequest

class OdooController(http.Controller):
    # test route
    @http.route('/api/info', auth='public', cors='*')
    def index(self, **kwargs):
        data_list = {"page": 1, "per_page": 6, "total": 12, "total_pages": 2, "data": [
            {"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth",
             "avatar": "https://reqres.in/img/faces/1-image.jpg"},
            {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver",
             "avatar": "https://reqres.in/img/faces/2-image.jpg"},
            {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong",
             "avatar": "https://reqres.in/img/faces/3-image.jpg"},
            {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt",
             "avatar": "https://reqres.in/img/faces/4-image.jpg"},
            {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris",
             "avatar": "https://reqres.in/img/faces/5-image.jpg"},
            {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos",
             "avatar": "https://reqres.in/img/faces/6-image.jpg"}],
                     "support": {"url": "https://reqres.in/#support-heading",
                                 "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}
        return json.dumps(data_list)


class WebsiteSaleController(http.Controller):
    @http.route(["/shop/checkout/"],type='http',auth='public',website=True,sitemap=False)
    def checkout(self,**kwargs):
        order =request.website.sale_get_order()
        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection
        return rpc_response()