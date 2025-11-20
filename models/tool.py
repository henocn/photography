from odoo import models, fields



class Tool(models.Model):
    _name = 'rh.tool'
    _description = 'Tool'

    tool_type_selection = [
        ('stable', 'Lieu de travail uniquement'),
        ('mobile', 'Outil mobile'),
    ]

    image = fields.Image(string="Image de l'outil")
    name = fields.Char(string="Nom de l'outil", required=True)
    caracteristics = fields.Text(string="Caractéristiques de l'outil")
    tool_type = fields.Selection(tool_type_selection, string="Type de l'outil")
    available_quantity = fields.Integer(string="Quantité disponible", default=1)
