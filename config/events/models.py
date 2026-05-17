from django.db import models

class EventRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=128)  
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Event Registrations"