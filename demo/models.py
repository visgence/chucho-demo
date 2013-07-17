from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from datetime import datetime
import time

from chucho.models import ChuchoManager, ChuchoUserManager


class ModelTimestamp(models.Model):
    created = models.IntegerField(null=True, blank=True, editable=False)
    updated = models.IntegerField(null=True, blank=True, editable=False)

    
    def save(self, *args, **kwargs):
        current_time = int(round(time.time()))

        if not self.created:
            self.created = current_time

        self.updated = current_time
        super(ModelTimestamp, self).save(*args, **kwargs)

    column_options = {
        'created': {'_type': 'timestamp'},
        'updated': {'_type': 'timestamp'}
        }

    class Meta:
        abstract = True


class DemoUserManager(BaseUserManager, ChuchoUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        user = DemoUser(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        
    def create_superuser(self, email, first_name, last_name, password):
        user = DemoUser(email=email, first_name=first_name, last_name=last_name, is_superuser=True)
        user.set_password(password)
        user.save() 


class DemoUser(AbstractBaseUser, ModelTimestamp):
    '''
    ' This is the customer user model for the application.
    ' It will behave much the same as the auth_user, but has only the fields we need.
    '''
    email = models.CharField(max_length=128, unique=True, db_index=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_superuser = models.BooleanField(default=False)

    objects = DemoUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    search_fields = ['email', 'first_name', 'last_name']
    column_options = dict(ModelTimestamp.column_options)
    column_options.update({
            'id': {'grid_column': False},
            'password': {'_type': 'password', 'grid_column': False}
            })

    class Meta:
        ordering = ['email']

    def save(self, *args, **kwargs):
        '''
        ' Overwritten save method to save a default value for last login.
        '
        '''
        if self.last_login is None:
            self.last_login = datetime(1900, 1, 1).replace(tzinfo=timezone.utc)
        super(DemoUser, self).save(*args, **kwargs)

    def get_full_name(self):
        '''
        ' This method will return the first and last name of the user.
        '''
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        '''
        ' This method will return the first name of the user.
        '''
        return self.first_name

    def can_view(self, user):
        '''
        ' Checks if a User instance is allowed to view this object instance or not.
        '
        ' Keyword Arguments:
        '   user - AuthUser to check if they have permissions.
        '
        ' Return: True if user is allowed to view and False otherwise.
        '''

        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        if user == self or user.is_superuser:
            return True

        return False

    def __unicode__(self):
        return u'%s (%s %s)' % (self.email, self.first_name, self.last_name)


class DemoInfo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    intValue = models.IntegerField(null=True, blank=True)
    floatValue = models.FloatField(null=True, blank=True)
    decimalField = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=6)
    user = models.ForeignKey(DemoUser, null=True, blank=True)
    isBoolean = models.BooleanField()
    textField = models.TextField(blank=True)
    dateTime = models.DateTimeField(default=timezone.now(), blank=True)
    

    objects = ChuchoManager()

    search_fields = ['name', 'intValue', 'user', 'floatValue', 'decimalField']

    def __unicode__(self):
        return self.name

    
    def can_view(self, user):
        '''
        ' Checks if a User instance is allowed to view this object instance or not.
        '
        ' Keyword Arguments:
        '   user - AuthUser to check if they have permissions.
        '
        ' Return: True if user is allowed to view and False otherwise.
        '''

        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        if user == self.user or user.is_superuser:
            return True

        return False


class DemoInfoTwo(models.Model):
    CHOICES = (
         ('C1', 'Choice 1')
        ,('C2', 'Choice 2')
        ,('C3', 'Choice 3')
        ,('C4', 'Choice 4')
    )

    name = models.CharField(max_length=32, unique=True)
    demoInfo = models.ForeignKey(DemoInfo, null=True, blank=True)
    choices = models.CharField(choices=CHOICES, max_length=2)

    objects = ChuchoManager()


    def __unicode__(self):
        return self.name


    def can_view(self, user):
        '''
        ' Checks if a User instance is allowed to view this object instance or not.
        '
        ' Keyword Arguments:
        '   user - AuthUser to check if they have permissions.
        '
        ' Return: True if user is allowed to view and False otherwise.
        '''

        if not isinstance(user, get_user_model()):
            raise TypeError('%s is not an auth user' % str(user))

        return True


class DemoInfoThree(models.Model):
    name = models.CharField(max_length=32, unique=True)
    demoInfoTwo = models.ForeignKey(DemoInfoTwo, null=True, blank=True)
    demoInfos = models.ManyToManyField(DemoInfo)

    objects = ChuchoManager()

