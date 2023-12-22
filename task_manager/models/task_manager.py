# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime

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
    days_remaining = fields.Integer(string="Days Remaining", compute='_compute_days_remaining', store=True)

    @api.onchange('deadline')
    def onchange_deadline(self):
        if self.deadline and fields.Date.from_string(self.deadline) < datetime.now().date():
            raise UserError("Deadline date cannot be less than the current date.")
    
    @api.depends('deadline')
    def _compute_days_remaining(self):
        for rec in self:
            if rec.deadline:
                deadline_date = fields.Date.from_string(rec.deadline)
                today_date = datetime.now().date()
                remaining_days = (deadline_date - today_date).days
                rec.days_remaining = remaining_days if remaining_days > 0 else 0
                
    def action_completed(self):
        for rec in self:
            rec.write({
                'state': 'completed',
                'task_completed': True
            })