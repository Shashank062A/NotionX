from django.db import models

# # Create your models here.
class UploadeFiles(models.Model):
   BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics And Communication'),
        ('ME', 'Mechanical'),
        ('EE', 'Electronics'),
        ('CE', 'Civil'),
        ('FD', 'Fashion'),
    ]
   SEMESTER_CHOICES = [
        ('1', 'First SEM'),
        ('2', 'Second SEM'),
        ('3', 'Third SEM'),
        ('4', 'Fourth SEM'),
        ('5', 'Fifth SEM'),
        ('6', 'Sixth SEM'),
    ]
   CATEGORY_CHOICES = [
        ('NOTES', 'Notes'),
        ('ASSIGNMENT', 'Assignment'),
        ('PRACTICAL', 'Practical'),
    ]


 

   title = models.CharField(max_length=255)
   branch = models.CharField(max_length=10, choices=BRANCH_CHOICES, default="CSE")
   sem = models.CharField(max_length=1, choices=SEMESTER_CHOICES, default="1")
   subject = models.CharField(max_length=100, default="CO")
   category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="NOTES")
   file = models.FileField(upload_to="pdfs/")
   uploaded_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.title