from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"

class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()  # Store bullet points here

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
    def get_description_as_list(self):
        return self.description.split("\n")  # Split by newline to get bullet points
    
class Education(models.Model):
    school_name = models.CharField(max_length=200)
    certificate_title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    
