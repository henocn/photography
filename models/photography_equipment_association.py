from odoo import fields, models



class PhotographyEquipmentAssociation(models.Model):
    _name = 'photography.equipment.association'
    _description = 'Association équipement <-> projet'
    _sql_constraints = [
        ('unique_equipment_project', 'unique(project_id,equipment_id)', 'This equipment is already linked to the project')
    ]

    project_id = fields.Many2one('photography.project', string="Projet associé", required=True, ondelete='cascade')
    equipment_id = fields.Many2one('photography.equipment', string="Équipement", required=True, ondelete='cascade')
    quantity = fields.Integer(string="Quantité requise", default=1)
    description = fields.Text(string="Eventuelle description")