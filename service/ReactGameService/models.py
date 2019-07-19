from django.db import models
from django.utils import timezone

class Test(models.Model):
    name =  models.TextField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name
    
    def createObject(self,name):
        return Test(name=name)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Attempt, self).save(*args, **kwargs)


class Testee(models.Model):
    react_username =  models.TextField(max_length=200)
    google_username =  models.TextField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.react_username + "|" + self.google_username

    def createObject(self,react_username,google_username):
        return Testee(react_username=react_username, google_username=google_username)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Attempt, self).save(*args, **kwargs)


class Organisation(models.Model):
    name =  models.TextField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

    def createObject(self,name):
        return Organisation(name=name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Attempt, self).save(*args, **kwargs)

class Status(models.Model):
    status_type = models.TextField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.status_type
    
    def createObject(self,status_type):
        return Status(status_type=status_type)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Attempt, self).save(*args, **kwargs)


class Attempt(models.Model):
    point_result =  models.TextField(max_length=200)
    time_result =  models.DurationField()
    test = models.ForeignKey("Test", on_delete=models.CASCADE)
    testee = models.ForeignKey("Testee", on_delete=models.CASCADE)
    organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.point_result + "|" + str(self.time_result) + "|"+ self.test.name + "|"+ self.testee.react_username + "|"+ self.organisation.name + "|"+ str(self.created_at)

    def save(self, *args, **kwargs):
         if not self.id:
             self.created_at = timezone.now()
         return super(Attempt, self).save(*args, **kwargs)

    def createObject(self,point_result,time_result,test,testee,organisation,created_at):
        return Status(point_result=point_result,time_result=time_result,test=test,testee=testee,organisation=organisation,created_at=created_at)
