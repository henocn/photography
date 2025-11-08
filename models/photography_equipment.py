from odoo import fields, models


class PhotographyEquipment(models.Model):
    _name = "photography.equipment"
    _description = "Équipement photographique"

    type_selection = [
        ("audio", "AUDIO"),
        ("video", "VIDEO"),
        ("audio_video", "AUDIO&VIDEO"),
        ("lumiere", "LUMIERE"),
        ("unknown", "NON SPECIFIE")
    ]

    using_state_selection = [
        ("new", "NEUF"),
        ("on_using", "EN SERVICE"),
        ("unknown", "NON SPECIFIE"),
    ]

    image = fields.Image(string="Image")
    name = fields.Char(string="Nom de l'équipment", required=True)
    equipment_type = fields.Selection(type_selection, string="Catégorie", required=True)
    equipment_state = fields.Selection(using_state_selection, string="Etat d'utilisation", required=True)
    location = fields.Char(string="Emplacement")
    adding_date = fields.Date(string="D'ate d'acquisition")
    quantity = fields.Integer(string="Quantité", default=1)
    description = fields.Text(string="Description")