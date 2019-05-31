from typing import List

import datetime

import bson
import mongoengine

from dip_manager.data.Change import Change
from dip_manager.data.Comment import Comment
from dip_manager.data.Suggestion import Suggestion
from dip_manager.data.Task import Task
from dip_manager.data.User import User


mongoengine.register_connection(alias='core', name='dip_project_db')

bob = User(full_name="Bob Jones", user_name = "bob", password = "vgjhb", email = "bob@gmail.com", user_type = "manager", user_telegram = 'bob').save()

change = Change (date_post = "2018-01-01 12:00:00", creator = bob.id, act_type = "hj", before = ['vgh'], after = ['vgjh'] ).save()

comment = Comment(date_post = "2018-01-01 12:00:00", date_update = "2018-01-01 12:00:00", creator = bob.id, text="vbjnk", updated = 0, followers = [bob.id]).save()

suggestion = Suggestion(date_post = "2018-01-01 12:00:00",  creator = bob.id, text="vbjnk", photos = [], followers = [bob.id]).save()

task = Task(task_name = "cfgvh",  photos = ["bhj"], description = "cvbnm",  date_start = "2018-01-01 12:00:00", date_end = "2018-01-01 12:00:00",
            date_update = "2018-01-01 12:00:00", updated = 0, creator = bob.id, doer = bob.id, comments =[comment.id], followers = [bob.id] ).save()
