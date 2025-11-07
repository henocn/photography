from odoo import models, fields


class PhotographyFurnitureAssociation(models.Model):
    _name = "photography.furniture"
    _description = "Meuble photographique"
    _sql_constraints = [
        ('unique_furniture_association', 'unique(project_id)', 'One association')
    ]


    project_id = fields.Many2one('photography.project', string="Projet associé", required=True)
    furniture_id = fields.Selection('photography.furniture', string="Type de meuble", required=True)
    quantity = fields.Integer(string="Quantité requise", default=1)
    description = fields.Text(string="Evantuelle description")