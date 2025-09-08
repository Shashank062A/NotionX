from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuestionPaper(models.Model):
    branch = models.CharField(max_length=50)
    semester = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="question_papers/")

    def __str__(self):
        return f"{self.title} ({self.subject}, Sem {self.semester})"
    
class Purchase(models.Model):
    PACKAGE_CHOICES = [
        ('single', 'Single Paper'),
        ('subject', 'All Papers of One Subject'),
        ('semester', 'All Papers of Semester'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    semester = models.CharField(max_length=10)
    subject = models.CharField(max_length=100, blank=True, null=True)
    papers = models.ManyToManyField(QuestionPaper, blank=True)
    purchased_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.package} - {self.semester}"