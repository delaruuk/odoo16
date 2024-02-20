from odoo import models, fields, api
import csv
import io

class Technician(models.Model):
    _name = 'procom_testing.technician'
    _department = 'Company Department'
    _employment = 'Employment'

    name = fields.Char(string='Name', required=True)