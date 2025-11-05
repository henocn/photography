from odoo import fields, models


class PhotographyEquipment(models.Model):
    _name = "photography.equipment"
    _description = "Équipement photographique"

    type_selection = [
        ('camera', 'Appareil photo'),
        ('lens', 'Objectif'),
        ('tripod', 'Trépied'),
        ('lighting', 'Éclairage'),
        ('reflector', 'Réflecteur'),
        ('microphone', 'Microphone'),
        ('microcravate', 'Micro-cravate'),
        ('other', 'Autre'),
    ]

    project_id = fields.Many2one('project.project', string="Projet associé", required=True)
    equipment_type = fields.Selection(type_selection, string="Nom de l'équipement", required=True)
    quantity = fields.Integer(string="Quantité", default=1)
    description = fields.Text(string="Description de l'équipement")