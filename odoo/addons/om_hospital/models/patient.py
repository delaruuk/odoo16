# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Records"
    
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    is_child = fields.Boolean(string='Is Child', required=True)
    notes = fields.Text(string='Notes', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
