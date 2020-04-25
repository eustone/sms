from django.db import models

year_level= (
    ('1', 'First Year'),
    ('2', 'second year'),
    ('3', 'Third Year'),
    ('4', 'Fourth Year'),
    ('5', 'Firth Year'),
    ('6', 'Sixth Year'),
    ('7', 'Seventh Year')

)

relationship = (
    ('father','Father'),
    ('mother','Mother'),
    ('other','Other'),


)


# Create your models here.
class Student(models.Model):
    """Class object for individual
       student personal record"""
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150,blank=True,default='')
    last_name = models.CharField(max_length=150)
    identification_number = models.CharField(max_length=30)
    student_number = models.CharField(max_length=50) #To add Auto generated Student Number
    year_level = models.CharField(max_length=6,choices=year_level)
    #course = models.ForeignKey() #Add Course Foreign key from Courses
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    telephone_number = models.CharField(max_length=12)
    birth_date = models.DateField(auto_now=True)
    current_address = models.CharField(max_length=300)
    postal_address = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=250)
    relationship = models.CharField(max_length=10,choices=relationship)
    address_of_contact = models.CharField(max_length=300)
    mobile_number_of_contact = models.CharField(max_length=12)
    telephone_number_of_contact = models.CharField(max_length=12,blank=True,default='')
    email_of_contact = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return 'f{self.name}:{self.middle_mame}: {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name}:{self.middle_name}:{self.last_name}'

    class Meta:
        ordering = ['first_name', 'middle_name', 'last_name']
        verbose_name_plural = 'student'




