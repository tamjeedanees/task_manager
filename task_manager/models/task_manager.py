# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _name = 'task.manager'
    _description = 'task_manager.task_manager'
    
    title = fields.Char(string="Title", index=True, readonly=False)
    description = fields.Text(string="Description", index=True, readonly=False)
    deadline = fields.Date(string="Deadline Date", description="Deadline of the task")
    completed = fields.Boolean(string="Task Completed", default=False)
    state = fields.Selection([
        ('progress', 'In Progress'), 
        ('completed', 'Completed')
    ], default='progress', string="State")
    
    