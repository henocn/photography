from odoo import models, fields


class PhotographyFurniture(models.Model):
    _name = "photography.furniture"
    _description = "Meuble photographique"

    type_selection = [
        ('category1', 'Categorie 1'),
        ('category2', 'Categorie 2'),
        ('category3', 'Categorie 3'),
        ('other', 'Autre'),
    ]

    image = fields.Image(string="Photo du meuble", required=True)
    name = fields.Char(string="Nom du meuble", required=True)
    furniture_type = fields.Selection(type_selection, string="Type de meuble", required=True)
    location = fields.Char(string="Emplacement")
    quantity = fields.Integer(string="Quantité disponible", default=1)
    description = fields.Text(string="description du meuble")