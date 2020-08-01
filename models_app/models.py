from django.db import models
from model_utils import Choices
from datetime import datetime
from django.contrib.auth.models import (
    UserManager,
    BaseUserManager,
    PermissionsMixin,
    AbstractBaseUser,
)

answer = Choices(
    (1, "optionOne"),
    (2, "optionTwo"),
    (3, "optionThree"),
    (4, "optionFour"),
    (5, "optionFive"),
    (6, "optionSix"),
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and Save a new User"""
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Creates and save a new superuser"""
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instade of the default username"""

    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.name


class LanguageModel(models.Model):
    languageId = models.AutoField(primary_key=True)
    languageName = models.CharField(
        max_length=100, unique=True
    )  # this is the title of grade e.g grade 9, grade 10
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.languageName

    class Meta:
        ordering = ("-created_at",)


# Create your models here.
class GradeModel(models.Model):
    gradeId = models.AutoField(primary_key=True)
    gradeTitle = models.CharField(
        max_length=100
    )  # this is the title of grade e.g grade 9, grade 10
    language = models.ForeignKey(
        LanguageModel, related_name="language_subejct", on_delete=models.CASCADE
    )  # grade have many subject relationship
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gradeTitle

    class Meta:
        unique_together = ("language", "gradeTitle")
        ordering = ("-created_at",)


class SubjectModel(models.Model):
    subjectId = models.AutoField(primary_key=True)
    grade = models.ForeignKey(
        GradeModel, related_name="grade_subejct", on_delete=models.CASCADE
    )  # grade have many subject relationship
    subjectName = models.CharField(
        max_length=255
    )  # this is the name of the subject e.g biology, physics
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subjectName

    class Meta:
        ordering = ("-created_at",)


class CategoryModel(models.Model):
    categorytId = models.AutoField(primary_key=True)
    grade = models.ForeignKey(
        GradeModel, related_name="grade_category", on_delete=models.CASCADE
    )  # One grade have many Category relationship
    title = models.CharField(
        max_length=255
    )  # this is the title of sub-unit tile of a model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


def upload_path(instance, filename):
    """Storing an image with directory post_image with custom file name"""
    now = datetime.now()
    now_string = now.strftime("%d-%m-%Y %H:%M:%S")
    new_filename = now_string + filename
    return "/".join(["post_image", new_filename])


# Create your models here.
class UnitModel(models.Model):
    unitId = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255
    )  # this is the title of unit e.g Introduction of computer science
    subject = models.ForeignKey(
        SubjectModel, related_name="subject_unit", on_delete=models.CASCADE
    )  # grade have many subject relationship
    name = models.CharField(
        max_length=255
    )  # this is the name of the chapter or unit e.g Chapter 9, Unit 9
    pdf = models.FileField(upload_to=upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


class ExamChoiceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    optionOne = models.TextField(max_length=1000)
    optionTwo = models.TextField(max_length=1000)
    optionThree = models.TextField(max_length=1000)
    optionFour = models.TextField(max_length=1000, null=True, blank=True)
    optionFive = models.TextField(max_length=1000, null=True, blank=True)
    optionSix = models.TextField(max_length=1000, null=True, blank=True)
    answer = models.CharField(max_length=100, choices=answer)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(
        SubjectModel, related_name="choice_subject", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ("-created_at",)


class ExamBlankSpaceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(
        SubjectModel, related_name="blank_subject", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class ExamDescribeQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(
        SubjectModel, related_name="describe_subject", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class ExamMatchQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(
        SubjectModel, related_name="match_subject", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


# Create your models here.
class QuizeChoiceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    optionOne = models.TextField(max_length=1000)
    optionTwo = models.TextField(max_length=1000)
    optionThree = models.TextField(max_length=1000)
    optionFour = models.TextField(max_length=1000, null=True, blank=True)
    optionFive = models.TextField(max_length=1000, null=True, blank=True)
    optionSix = models.TextField(max_length=1000, null=True, blank=True)
    answer = models.CharField(max_length=100, choices=answer)
    description = models.TextField(max_length=1000)
    unit = models.ForeignKey(
        UnitModel, related_name="choice_unit", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ("-created_at",)


class QuizeBlankSpaceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    unit = models.ForeignKey(
        UnitModel, related_name="blank_unit", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class QuizeDescribeQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    unit = models.ForeignKey(
        UnitModel, related_name="describe_unit", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class QuizeMatchQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)

    unit = models.ForeignKey(
        UnitModel, related_name="dmatch_unit", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class TransactionModel(models.Model):
    transactionId = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name="user_transaction", on_delete=models.CASCADE
    )
    grade = models.ForeignKey(
        GradeModel, related_name="grade_transaction", on_delete=models.CASCADE
    )
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

