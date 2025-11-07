from odoo import fields, models



class PhotographyEquipmentAssociation(models.Model):
    _name = 'photography.equipment.association'
    _description = "Équipement photographique"
    _sql_constraints = [
        ('unique_equipment_association', 'unique(project_id)', 'One association')
    ]

    project_id = fields.Many2one('photography.project', string="Projet associé", required=True)
    equipment_id = fields.Many2one('photography.equipment', string="Nom de l'équipement", required=True)
    quantity = fields.Integer(string="Quantité requise", default=1)
    description = fields.Text(string="Evantuelle description")