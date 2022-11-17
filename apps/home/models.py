# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
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
    "{'overall': {'New Viewers': '178', 'Views': '9.5M', 'followers': '131k', 'New Views pct': '60', 'Views Pct': '92', 'follow pct': '89'}, 'Analytics':{'TP': '15', 'TWH': '0.20', 'WL': [8, 2, 9, 5, 4, 6, 4, 3, 8, 0]}}"),
    
    (25, "Tester", "tester@gmail.com", "367238", 
    "{'overall':{'New Viewers': '10', 'Views': '3.6k', 'followers': '14', 'New Views pct': '60', 'Views Pct': '92', 'follow pct': '89'}, 'Analytics':{'TP': '15', 'TWH': '0.20', 'WL': [8, 2, 9, 5, 4, 6, 4, 3, 8, 0]}}"),

    (895, "banker", "baker@gmail.com", "367238", 
    "{'overall':{'New Viewers': '25', 'Views': '2.1k', 'followers': '67', 'New Views pct': '29', 'Views Pct': '38', 'follow pct': '67'}, 'Analytics':{'TP': '190', 'TWH': '20', 'WL': [1, 9, 10, 8, 10, 2, 4, 3, 8, 0]}}"),

    (35, "Easeter", "easter@gmail.com", "989137827", 
    "{'overall':{'New Viewers': '1230', 'Views': '9.8M', 'followers': '58909'}, 'New Views pct': '60', 'Views Pct': '92', 'follow pct': '89'},'Analytics':{'TP': '15', 'TWH': '0.20', 'WL': [8, 2, 9, 5, 4, 6, 4, 3, 8, 0]}}"),

    (165, "Broker", "broker@gmail.com", "112337827", 
    "{'overall':{'New Viewers': '120', 'Views': '3.6M', 'followers': '1400'}, 'New Views pct': '60', 'Views Pct': '92', 'follow pct': '89'},'Analytics':{'TP': '15', 'TWH': '0.20', 'WL': [8, 2, 9, 5, 4, 6, 4, 3, 8, 0]}}"),
]

for row in Default_Data:
    UserDetails_db = UserDetails(id=row[0], name=row[1], email=row[2], phone=row[3], post=row[4])
    UserDetails_db.save()