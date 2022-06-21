from odoo import api, fields, models, _
from datetime import date

from odoo.exceptions import ValidationError


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
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many(comodel_name='patient.tag', string='Tags')

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not acceptable."))

    @api.model
    def create(self, vals_list):
        vals_list['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    def write(self, vals):
        if not self.ref:  # not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

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

    def name_get(self):
        # patient_list = []
        # for record in self:
        #     name = record.ref +','+ record.name
        #     patient_list.append((record.id,name))
        #
        # return patient_list
        return [(record.id, "[%s]%s" % (record.ref, record.name)) for record in self]
