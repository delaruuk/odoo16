class TechnicianReport(models.TransientModel):
    _name = 'procom_testing.technician_report'
    _description = 'Technician Report'

    technician_ids = fields.Many2many('procom_testing.technician', string='Technicians')

    def generate_csv(self):
        technicians_data = []
        for technician in self.technician_ids:
            total_hours = sum(technician.work_hours_ids.mapped('hours'))
            technicians_data.append({
                'Technician Name': technician.name,
                'Total Hours': total_hours
            })

        output = io.StringIO()
        fieldnames = ['Technician Name', 'Total Hours']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(technicians_data)

        return {
            'type': 'ir.actions.act_url',
            'url': 'data:text/csv;charset=utf-8,' + output.getvalue(),
            'target': 'new',
            'filename': 'technician_hours_report.csv'
        }