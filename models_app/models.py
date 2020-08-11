from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    UserManager,
)
from django.db import models
from model_utils import Choices

from utilities.image_validation import validate_image

category = Choices("Lesson", "Exam", "Quize")
g_category = Choices("Lesson", "Exam")


def upload_path(instance, filename):
    """Storing an image with directory post_image with custom file name"""
    now = datetime.now()
    now_string = now.strftime("%d-%m-%Y %H:%M:%S")
    new_filename = now_string + filename
    return "/".join(["post_image", new_filename])


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


class GeneralKnowlegdyModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


class G_ChoiceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    g_knowledgy = models.ForeignKey(
        GeneralKnowlegdyModel, related_name="g_choice", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ("-created_at",)


class G_Options(models.Model):
    question = models.ForeignKey(
        G_ChoiceQuestionModel, related_name="g_option", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=128, verbose_name="Answer's text here.")
    is_correct = models.BooleanField(default=False)
    label = models.CharField(max_length=1)

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ("question", "text"), ("question", "label")
        ordering = ("label",)


class G_UnitModel(models.Model):
    unitId = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255
    )  # this is the title of unit e.g Introduction of computer science
    g_knowledy = models.ForeignKey(
        GeneralKnowlegdyModel, related_name="g_unit", on_delete=models.CASCADE
    )  # grade have many subject relationship
    name = models.CharField(
        max_length=255
    )  # this is the name of the chapter or unit e.g Chapter 9, Unit 9
    pdf = models.FileField(upload_to=upload_path, validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("name", "g_knowledy")
        ordering = ("-created_at",)


class LearnLanguageModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    is_local = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


class L_ChoiceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    g_knowledgy = models.ForeignKey(
        LearnLanguageModel, related_name="l_choice", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ("-created_at",)


class L_Options(models.Model):
    question = models.ForeignKey(
        L_ChoiceQuestionModel, related_name="l_option", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=128, verbose_name="Answer's text here.")
    is_correct = models.BooleanField(default=False)
    label = models.CharField(max_length=1)

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ("question", "text"), ("question", "label")
        ordering = ("label",)


class L_UnitModel(models.Model):
    unitId = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255
    )  # this is the title of unit e.g Introduction of computer science
    g_knowledy = models.ForeignKey(
        LearnLanguageModel, related_name="l_unit", on_delete=models.CASCADE
    )  # grade have many subject relationship
    name = models.CharField(
        max_length=255
    )  # this is the name of the chapter or unit e.g Chapter 9, Unit 9
    pdf = models.FileField(upload_to=upload_path, validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("name", "g_knowledy")
        ordering = ("-created_at",)


class LanguageModel(models.Model):
    """This is the language  that user choose to learn all subject based on their option"""

    languageId = models.AutoField(primary_key=True)
    languageName = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.languageName

    class Meta:
        ordering = ("-created_at",)


class GradeModel(models.Model):
    gradeId = models.AutoField(primary_key=True)
    gradeTitle = models.CharField(
        max_length=100
    )  # this is the title of grade e.g grade 9, grade 10
    language = models.ForeignKey(
        LanguageModel, related_name="language_grade", on_delete=models.CASCADE
    )
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
        unique_together = ("grade", "subjectName")
        ordering = ("-created_at",)


class CategoryModel(models.Model):
    categoryId = models.AutoField(primary_key=True)
    # One Category have many Category relationship
    title = models.CharField(
        max_length=255, choices=category
    )  # this is the title of sub-unit tile of a model
    subject = models.ForeignKey(
        SubjectModel, related_name="category_subejct", on_delete=models.CASCADE
    )  # grade have many subject relationship
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("title", "subject")


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
    pdf = models.FileField(upload_to=upload_path, validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("name", "subject")
        ordering = ("-created_at",)


class ExamChoiceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(
        SubjectModel, related_name="subject_choice", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ("-created_at",)


class Options(models.Model):
    question = models.ForeignKey(
        ExamChoiceQuestionModel, related_name="exam_option", on_delete=models.CASCADE
    )

    text = models.CharField(max_length=128, verbose_name="Answer's text here.")
    is_correct = models.BooleanField(default=False)
    label = models.CharField(max_length=1)

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ("question", "text"), ("question", "label")
        ordering = ("label",)


class ExamBlankSpaceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(
        SubjectModel, related_name="subject_blank", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class ExamDescribeQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)
    subject = models.ForeignKey(
        SubjectModel, related_name="subject_describe", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class MatchingInstructionModel(models.Model):
    instructionId = models.AutoField(primary_key=True)

    instructionText = models.TextField()
    subject = models.ForeignKey(
        SubjectModel, related_name="subject_instruction", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instructionText


class MatchingPosibleAnswersModels(models.Model):
    matchingId = models.AutoField(primary_key=True)
    instruction = models.ForeignKey(
        MatchingInstructionModel,
        related_name="instruction_posible",
        on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=1)
    optionText = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.optionText

    class Meta:
        unique_together = (
            ("instruction", "label"),
            ("instruction", "optionText"),
        )
        ordering = ("label",)


class MatchingQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    number = models.IntegerField()
    instruction = models.ForeignKey(
        MatchingInstructionModel,
        related_name="instruction_question",
        on_delete=models.CASCADE,
    )
    questionText = models.TextField()
    answer = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questionText

    class Meta:
        unique_together = (
            ("instruction", "answer"),
            ("instruction", "questionText"),
            ("instruction", "number"),
        )
        ordering = ("number",)


class QuizeMatchingInstructionModel(models.Model):
    """This is matching exam instruction for a quize """

    instructionId = models.AutoField(primary_key=True)
    instructionText = models.TextField()
    unit = models.ForeignKey(
        UnitModel, related_name="unit_instruction", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instructionText


class QuizeMatchingPosibleAnswersModels(models.Model):
    matchingId = models.AutoField(primary_key=True)
    instruction = models.ForeignKey(
        MatchingInstructionModel,
        related_name="quize_instruction_posible",
        on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=1)
    optionText = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.optionText

    class Meta:
        unique_together = (
            ("instruction", "label"),
            ("instruction", "optionText"),
        )
        ordering = ("label",)


class QuizeMatchingQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    number = models.IntegerField()
    instruction = models.ForeignKey(
        MatchingInstructionModel,
        related_name="quize_instruction_question",
        on_delete=models.CASCADE,
    )
    questionText = models.TextField()
    answer = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questionText

    class Meta:
        unique_together = (
            ("instruction", "answer"),
            ("instruction", "questionText"),
            ("instruction", "number"),
        )
        ordering = ("number",)


class QuizeChoiceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    unit = models.ForeignKey(
        UnitModel, related_name="unit_choice", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class QuizeOptions(models.Model):
    question = models.ForeignKey(
        QuizeChoiceQuestionModel, related_name="quize_option", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=128, verbose_name="Answer's text here.")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizeBlankSpaceQuestionModel(models.Model):
    questionId = models.AutoField(primary_key=True)
    question = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    unit = models.ForeignKey(
        UnitModel, related_name="unit_blank", on_delete=models.CASCADE
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
        UnitModel, related_name="unit_describe", on_delete=models.CASCADE
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
