from odoo import models, fields 



class Employee(models.Model):
    _name = 'employee.employee'
    _description = 'Employee'

    day_off_selection = [
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi')
    ]

    name = fields.Char(string="Nom de l'employé", required=True)
    email = fields.Char(string='Email', required=True)
    birth_date = fields.Date(string='Date de naissance')
    gender = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string='Genre', default='homme')
    enrollment_date = fields.Date(string="Date d'embauche")
    day_off = fields.Selection(day_off_selection, string='Jour de répos', default='samedi')
    position = fields.Char(string='Position')
    specialization = fields.Char(string='Spécialité')
    tools = fields.One2many('employee.tool', 'employee_id', string='Outils')
    active = fields.Boolean(string='Active', default=True)