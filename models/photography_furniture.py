from odoo import models, fields


class PhotographyFurniture(models.Model):
    _name = "photography.furniture"
    _description = "Meuble photographique"

    type_selection = [
        ('chair', 'Chaise'),
        ('desk', 'Banc'),
        ('table', 'Table'),
        ('sofa', 'Canapé'),
        ('shelf', 'Étagère'),
        ('plant', 'Plante'),
        ('other', 'Autre'),
    ]

    project_id = fields.Many2one('photography.project', string="Projet associé", required=True)
    furniture_type = fields.Selection(type_selection, string="Type de meuble", required=True)
    quantity = fields.Integer(string="Quantité", default=1)
    description = fields.Text(string="description du meuble")