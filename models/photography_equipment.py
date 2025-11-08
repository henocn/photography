from odoo import fields, models


class PhotographyEquipment(models.Model):
    _name = "photography.equipment"
    _description = "Équipement photographique"

    type_selection = [
        ("audio", "AUDIO"),
        ("video", "VIDEO"),
        ("audio_video", "AUDIO&VIDEO"),
        ("lumiere", "LUMIERE"),
    ]

    using_state_selection = [
        ("new", "NEUF"),
        ("on_using", "EN SERVICE"),
    ]

    image = fields.Image(string="Photo de l'équipement", required=True)
    name = fields.Char(string="Nom de l'équipment", required=True)
    equipment_type = fields.Selection(type_selection, string="Nom de l'équipement", required=True)
    equipment_state = fields.Selection(using_state_selection, string="Etat d'utilisation", required=True)
    quantity = fields.Integer(string="Quantité disponible", default=1)
    description = fields.Text(string="Description de l'équipement")