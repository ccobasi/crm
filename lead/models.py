from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICE_PRIORITY = (
        (LOW, 'LOW'),
        (MEDIUM, 'MEDIUM'),
        (HIGH, 'HIGH'),
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICE_STATUS = (
        (NEW, 'new'),
        (CONTACTED, 'contacted'),
        (WON, 'won'),
        (LOST, 'lost')
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICE_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICE_STATUS, default=NEW)
    converted_to_client = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
