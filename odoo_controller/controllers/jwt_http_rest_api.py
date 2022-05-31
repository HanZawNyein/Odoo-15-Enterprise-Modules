from odoo import http
from odoo.http import request, Response


class JwtRestful:
    def __init__(self):
        self.database = request.session.db

    def login(self, username, password):
        user = request.session.authenticate(self.database, username, password)
        if user is not None:
            pass


RestAPI = staticmethod(JwtRestful.login)
