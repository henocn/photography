from odoo import models, fields


class PhotographyFurnitureAssociation(models.Model):
    _name = 'photography.furniture.association'
    _description = 'Association meuble <-> projet'
    _sql_constraints = [
        ('unique_furniture_project', 'unique(project_id,furniture_id)', 'This furniture is already linked to the project')
    ]

    project_id = fields.Many2one('photography.project', string="Projet associé", required=True, ondelete='cascade')
    furniture_id = fields.Many2one('photography.furniture', string="Meuble", required=True, ondelete='cascade')
    quantity = fields.Integer(string="Quantité requise", default=1)
    description = fields.Text(string="Eventuelle description")