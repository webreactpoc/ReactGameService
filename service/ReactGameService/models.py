from django.db import models

class Test(models.Model):
    name =  models.TextField(max_length=200)

class Testee(models.Model):
    username =  models.TextField(max_length=200)
    google_username =  models.TextField(max_length=200)

class Organisation(models.Model):
    name =  models.TextField(max_length=200)

class Status(models.Model):
    type = models.TextField(max_length=200)

class Attempt(models.Model):
    point_result =  models.TextField(max_length=200)
    time_result =  models.DurationField()
    test_id = models.ForeignKey("Test", on_update=models.CASCADE)
    testee_id = models.ForeignKey("Testee", on_update=models.CASCADE)
    organisation_id = models.ForeignKey("Organisation", on_update=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

