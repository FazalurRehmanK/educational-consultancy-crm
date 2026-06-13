from django.contrib import admin
from .models import StudentLead, TestScore, ApplicationDocument

# These classes tell Django to embed the tables inside another page
class TestScoreInline(admin.StackedInline):
    model = TestScore
    can_delete = False

class ApplicationDocumentInline(admin.StackedInline):
    model = ApplicationDocument
    can_delete = False

# This registers the StudentLead, but attaches the two inlines above to it
@admin.register(StudentLead)
class StudentLeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'target_country', 'status')
    inlines = [TestScoreInline, ApplicationDocumentInline]