from odoo import models, fields, api


class PhotographyFurniture(models.Model):
    _name = "photography.furniture"
    _description = "Meuble photographique"

    type_selection = [
        ('mobilier', 'MOBILIER'),
        ('decor', 'DECORATIF'),
        ('plant', 'PLANTE'),
        ('other', 'AUTRE'),
    ]

    using_state_selection = [
        ("new", "NEUF"),
        ("on_using", "EN SERVICE"),
        ("unknown", "NON SPECIFIE"),
    ]
    

    image = fields.Image(string="Photo du meuble", required=True)
    name = fields.Char(string="Nom du meuble", required=True)
    furniture_type = fields.Selection(type_selection, string="Type de meuble", required=True)
    furniture_state = fields.Selection(using_state_selection, string="Etat d'utilisation")
    location = fields.Char(string="Emplacement")
    quantity = fields.Integer(string="Quantité", default=1)
    description = fields.Text(string="Description")
    
    
    
    @api.multi
    def name_get(self):
        result = []
        for record in self:
            display_value = record.name
            if record.description:
                display_value = f"{display_value}, {record.description}"
            
            result.append((record.id, display_value))
        return result