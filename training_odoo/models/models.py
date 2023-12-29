from odoo import api, fields, models
 
class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Kursus'
     
    name = fields.Char(string='Judul', required=True)
    description = fields.Text(string='Keterangan')