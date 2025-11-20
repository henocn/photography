from odoo import models, fields 



class ToolAssociation(models.Model):
    _name = 'rh.tool.association'
    _description = 'Association between Employee and Tool'

    tool_state_selection = [
        ('new', 'Neuf'),
        ('good', 'Bon état'),
        ('used', 'Usagé'),
        ('damaged', 'Endommagé')
    ]

    employee_id = fields.Many2one('rh.employee', string='Employé', required=True)
    tool_id = fields.Many2one('rh.tool', string='Outil', required=True)
    assigned_date = fields.Date(string='Date de remise', required=True)
    image = fields.Image(related="tool_id.image", string="Image", store=False)
    tool_state = fields.Selection(tool_state_selection, string='Outil à la remise', default='good')
    quantity = fields.Integer(string='Quantité', default=1)
    additionnal_notes = fields.Text(string='Notes evantuelles')