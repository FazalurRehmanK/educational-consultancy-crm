from django.db import models

class StudentLead(models.Model):
    STATUS_CHOICES = [
        ('LEAD', 'New Lead'),
        ('PREP', 'IELTS/GRE Prep'),
        ('APPLY', 'University Applied'),
        ('VISA', 'Visa Processing'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    target_country = models.CharField(max_length=50, default='Germany')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='LEAD')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.target_country}"



class TestScore(models.Model):
    # This creates a One-to-One relational link to the student
    student = models.OneToOneField(StudentLead, on_delete=models.CASCADE, related_name='test_scores')

    # Tracking August-October prep targets
    ielts_band = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="IELTS Overall Band")
    gre_score = models.IntegerField(null=True, blank=True, verbose_name="GRE Total Score")

    def __str__(self):
        return f"Test Scores for {self.student.first_name}"

class ApplicationDocument(models.Model):
    # Another One-to-One relational link
    student = models.OneToOneField(StudentLead, on_delete=models.CASCADE, related_name='documents')

    # The Document Checklist
    has_passport = models.BooleanField(default=False, verbose_name="Valid Passport")
    has_transcripts = models.BooleanField(default=False, verbose_name="Attested Transcripts")
    has_sop = models.BooleanField(default=False, verbose_name="Statement of Purpose (SOP)")
    has_lor = models.BooleanField(default=False, verbose_name="Letters of Recommendation")

    def __str__(self):
        return f"Documents for {self.student.first_name}"