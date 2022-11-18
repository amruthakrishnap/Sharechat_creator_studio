# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Teampandavas
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    # id = models.
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    post = models.CharField(max_length=50000)

    def __str__(self):
        return self.name
    
# INSERTING Data
Default_Data = [ 
    (56, "shareadmin", "tester@gmail.com", "367238", 
    "{'overall': {'New Viewers': '17K', 'Views': '9.5M', 'followers': '131k','New Viewer SC' : '5K','Views SC' :'3M','followers SC' : '30K', 'New Views pct': '80', 'Views Pct': '92', 'follow pct': '89'}, 'Analytics':{'TP': '5301', 'TWH': '203.2', 'WL': [888, 270, 998, 501, 423, 608, 400, 3, 8, 0]}}"),
    
    (25, "Tester", "tester@gmail.com", "367238", 
    "{'overall':{'New Viewers': '700', 'Views': '3.6k', 'followers': '14', 'New Views pct': '60', 'Views Pct': '92', 'follow pct': '45'}, 'Analytics':{'TP': '68', 'TWH': '0.36', 'WL': [8, 2, 9, 5, 4, 6, 4, 3, 8, 0]}}"),

    (895, "banker", "baker@gmail.com", "367238", 
    "{'overall':{'New Viewers': '7K', 'Views': '204k', 'followers': '23.3K', 'New Views pct': '65', 'Views Pct': '78', 'follow pct': '67'}, 'Analytics':{'TP': '190', 'TWH': '2.3', 'WL': [1, 9, 10, 8, 10, 2, 4, 3, 8, 0]}}"),

    (35, "Easeter", "easter@gmail.com", "989137827", 
    "{'overall':{'New Viewers': '12K', 'Views': '9.8M', 'followers': '58909'}, 'New Views pct': '60', 'Views Pct': '92', 'follow pct': '89'},'Analytics':{'TP': '6800', 'TWH': '6.7', 'WL': [8, 2, 9, 5, 4, 6, 4, 3, 8, 0]}}"),

    (165, "Broker", "broker@gmail.com", "112337827", 
    "{'overall':{'New Viewers': '28K', 'Views': '3.6M', 'followers': '14K'}, 'New Views pct': '60', 'Views Pct': '92', 'follow pct': '80'},'Analytics':{'TP': '2022', 'TWH': '9.8', 'WL': [8, 2, 9, 5, 4, 6, 4, 3, 8, 0]}}"),
]

for row in Default_Data:
    UserDetails_db = UserDetails(id=row[0], name=row[1], email=row[2], phone=row[3], post=row[4])
    UserDetails_db.save()