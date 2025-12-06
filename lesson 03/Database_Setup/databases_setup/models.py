from django.db import models

class Student(models.Model):
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_address = models.CharField(max_length=255)
    student_birthday = models.DateField()
    student_gpa = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Name: {self.student_first_name} {self.student_last_name} | "
            f"Age: {self.student_age} | "
            f"GPA: {self.student_gpa}"
        )

    class Meta:
        ordering = ["student_first_name"]
