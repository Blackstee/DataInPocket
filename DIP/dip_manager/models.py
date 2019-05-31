from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


class ProjectManager(models.Manager):


    def create_project(self, project_name, description):

        project = self.create(project_name=project_name, description = description)

        return project





class User(AbstractUser):

    photo = models.ImageField(null=True, blank=True)

    user_position = models.TextField(max_length=30, blank=False, null=True)

    user_type = models.IntegerField(blank=False, null=True)

    user_telegram = models.TextField(max_length=30, blank=True, null=True)

    send_email = models.BooleanField(blank=False, null=True)

    send_telegram = models.BooleanField(blank=False, null=True)



class Project(models.Model):

    project_name = models.TextField(blank=False, max_length=100, null=True)

    description = models.TextField(max_length=10000, blank=True, null=True)

    objects = ProjectManager()


class TaskManager(models.Manager):


    def create_task(self, task_name, description, date_start, date_end,
                    date_update, updated,  creator, doer,
                    project):

        task = self.create(task_name=task_name, description = description, date_start=date_start,
                              date_end=date_end, date_update=date_update, updated=updated,creator=creator,
                              doer=doer,project=project)

        return task



class Task(models.Model):

    task_name = models.TextField(blank=False, max_length=100, null=True)

    description = models.TextField(max_length=10000, blank=True, null=True)

    date_start = models.DateTimeField(default=datetime.datetime.utcnow, null=True)

    date_end = models.DateTimeField(blank=False, null=True)

    date_update = models.DateTimeField(default=datetime.datetime.utcnow, null=True)

    updated = models.IntegerField(blank=True, default=0, null=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_of_task")

    doer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doer_of_task")

    followers = models.ManyToManyField(User)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    objects = TaskManager()


class Comment(models.Model):

    text = models.TextField(max_length=1000, blank=False, null=True)

    сreator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_of_comment")

    date_post = models.DateTimeField(default=datetime.datetime.utcnow, null=True)

    date_update = models.DateTimeField(default=datetime.datetime.utcnow, null=True)

    updated = models.IntegerField(blank=True, default=0, null=True)

    followers = models.ManyToManyField(User)

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="related_task")



class Suggestion(models.Model):


    date_post = models.DateTimeField(default=datetime.datetime.utcnow, null=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_of_suggestion")

    text = models.TextField(max_length= 10000, blank=False, null=True)

    followers = models.ManyToManyField(User)



class Change (models.Model):

    date_post = models.DateTimeField(default=datetime.datetime.utcnow, null=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_of_change")

    act_type = models.TextField(blank=False, null=True)

    before = models.TextField(blank=True, null=True)

    after = models.TextField(blank=True, null=True)




class Pic_comm (models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to = 'pic_folder/comments/', default = 'pic_folder/None/no-img.jpg')



class Pic_Task(models.Model):

    comment = models.ForeignKey(Task, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='pic_folder/tasks/', default='pic_folder/None/no-img.jpg')



class Pic_User(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='pic_folder/users/', default='pic_folder/None/no-img.jpg')


class Link_users(models.Model):

    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boss")

    doer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doer")


class Task_check (models.Model):

    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checks_task")

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_being_checked")

    level = models.IntegerField(blank=False, null = 0)