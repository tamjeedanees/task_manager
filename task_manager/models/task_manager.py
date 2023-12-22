# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _name = 'task.manager'
    _description = 'task_manager.task_manager'
    _rec_name = 'title'
    
    title = fields.Char(string="Title", index=True, readonly=False, required=True)
    description = fields.Text(string="Description", index=True, readonly=False, required=True)
    deadline = fields.Date(string="Deadline Date", description="Deadline of the task", required=True)
    task_completed = fields.Boolean(string="Task Completed", default=False)
    state = fields.Selection([
        ('progress', 'In Progress'), 
        ('completed', 'Completed')
    ], default='progress', string="State")
    
    
    def action_completed(self):
        for rec in self:
            rec.write({
                'state': 'completed',
                'completed': True
            })