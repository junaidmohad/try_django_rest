from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

class Role(models.Model):  # first step from the flowchart
    STUDENT = 1
    FACULTY = 2
    STAFF = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (STUDENT, "student"),
        (FACULTY, "faculty"),
        (STAFF, "staff"),
        (ADMIN, "admin"),
        # more user types can be added
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()
    
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"


# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email: 
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,            
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom user model
class CustomUser(AbstractBaseUser):
    roles = models.ManyToManyField(
        Role
    )  # the last thing of the first step from the flowchart

    # Use the custom user manager
    
   

    email = models.EmailField(verbose_name='email', unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    #for authentication and permissions
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Use the custom user manager
    objects = CustomUserManager()

    USERNAME_FIELD = "email"                    #these are the important fields in order to create users
    REQUIRED_FIELDS = ["username"]

    

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_Label):
        return True

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Branch(models.Model):
    branch_choices = [
        ("Comps", "Computer Science"),
        ("IT", "Information Technology"),
        ("EXTC", "Electronics and Telecommunication"),
        ("ETRX", "Electronics"),
        ("MECH", "Mechanical"),
    ]

    branch_name = models.CharField(max_length=50, choices=branch_choices, unique=True)

    def __str__(self):
        return str(self.branch_name)
    
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class Admin(models.Model):
    """
    #the second step form the flowchart is to have onetoonefield in all of our individual profile models in relationship to our customuser model
    """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, to_field="email")

    def __str__(
        self,
    ):  # this is like a constructor to return something whenever this objects is being called
        return str(self.user)
    
    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"


class Faculty(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, to_field="email")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    dept = models.CharField(max_length=100)  # do we need dept?
    employee_code = models.PositiveIntegerField()
    faculty_name = models.CharField(max_length=100)
    employee_abbreviation = models.CharField(max_length=20, primary_key=True)
    faculty_email = models.EmailField(max_length=100)
    experience = models.PositiveIntegerField()
    post = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, to_field="email")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    dept = models.CharField(max_length=100)  # do we need dept?
    employee_code = models.PositiveIntegerField()
    staff_name = models.CharField(max_length=100)
    employee_abbreviation = models.CharField(max_length=20, primary_key=True)
    staff_email = models.EmailField(max_length=100)
    experience = models.PositiveIntegerField()
    post = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"



class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, to_field="email")
    student_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    roll_number = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=100)
    proctor_Abbreviation = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, to_field="employee_abbreviation"
    )
    student_contact_no = models.CharField(max_length=20)
    parents_contact_no = models.CharField(max_length=20)
    parent_email_id = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

class Proctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, to_field="email")

    def __str__(self):
        return str(self.course_code)
    
    class Meta:
        verbose_name = "Proctor"
        verbose_name_plural = "Proctors"

class Course(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, to_field="branch_name")
    course_code = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)  # do we need dept?
    sem = models.IntegerField()
    scheme_name = models.CharField(max_length=100)
    credit = models.IntegerField()
    hours = models.IntegerField()

    def __str__(self):
        return str(self.course_code)
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Year(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    faculty_name = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, to_field="employee_abbreviation"
    )
    staff_name = models.ForeignKey(
        Staff, on_delete=models.CASCADE, to_field="employee_abbreviation"
    )
    course_code = models.ForeignKey(
        Course, on_delete=models.CASCADE, to_field="course_code"
    )

    def __str__(self):
        return str(self.year)
    
    class Meta:
        verbose_name = "Year"
        verbose_name_plural = "Year"


# Register your models here.


# Create your models here.
