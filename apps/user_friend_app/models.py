# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    print 'woohoo'


class User(models.Model):
    name = models.CharField(max_length=45)
    friendships = models.ManyToManyField('self', related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def add_friendship(self,person2):
        self.friendships.add(person2)
        return
    
    def get_friends(self):
        if not self:
            return None
        return self.friendships.all()
    
    def __repr__(self):
        return "<\tName: {}>".format(self.name)



'''
RELATIONSHIP_FRIENDS = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FRIENDS, 'Friends'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


class Friendship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_people')
    to_person = models.ForeignKey(Person, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Person(models.Model):
    name = models.CharField(max_length=100)
    relationships = models.ManyToManyField('self', through='Relationship', symmetrical=False,  related_name='related_to')

    def __unicode__(self):
        return self.name

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Relationship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_people')
    to_person = models.ForeignKey(Person, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

'''