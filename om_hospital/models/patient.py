from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', )
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)

    ref = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string="Appointments")
    active = fields.Boolean(string='Active', default=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1
        # self.age = today.year - self.date_of_birth.year - (
        #             (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
