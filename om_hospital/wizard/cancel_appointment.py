import datetime

from dateutil import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment',
                                     domain=['|', ('state', '=', 'draft'), ('priority', 'in', ('0', '1'))])
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancellation Date")

    @api.model
    def default_get(self, fields_list):
        res = super(CancelAppointmentWizard, self).default_get(fields_list)
        res['reason'] = 'Odoo Mates'
        res['date_cancel'] = datetime.date.today()
        return res

    def action_cancel(self):
        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_day')
        allowed_date = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_day))
        if allowed_date < datetime.date.today():
            raise ValidationError(_("Sorry, cancellation is not allowed for this booking !"))
        # if self.appointment_id.booking_date == fields.Date.today():
        #     raise ValidationError(_("Sorry, cancellation is not allowed on the same day of booking !"))
        self.appointment_id.state = 'cancel'