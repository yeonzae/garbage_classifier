from django.db import models

class ClassificationResult(models.Model):
    predicted_class = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.predicted_class
