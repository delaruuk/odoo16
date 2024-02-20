class WorkHours(models.Model):
    _name = 'procom_testing.workhours'
    _description = 'Technician Work Hours'

    technician_id = fields.Many2one('procom_testing.technician', string='Technician', required=True)
    date = fields.Date(string='Date', required=True)
    hours = fields.Float(string='Hours', required=True)