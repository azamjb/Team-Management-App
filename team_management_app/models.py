from django.db import models

class TeamMember(models.Model):
    # Define the possible roles
    ROLE_CHOICES = (
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    )

    # Model fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    def __str__(self):
        
        return f"{self.first_name} {self.last_name} ({'Admin' if self.role == 'admin' else 'Regular'})"
