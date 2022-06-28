from odoo import api, fields, models, _


class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _description = "Hospital Operation"
    _log_access = False

    doctor_id = fields.Many2one('res.users', string='Doctor')
    operation_name = fields.Char(string="Name")
    reference_record = fields.Reference(
        selection=[
            ('hospital.patient', 'Patient'),
            ('hospital.appointment', 'Appointment')],
        string='Record')

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]
