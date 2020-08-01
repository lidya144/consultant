from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Permission
from .models import (
    User,
    LanguageModel,
    TransactionModel,
    GradeModel,
    SubjectModel,
    CategoryModel,
    UnitModel,
    ExamChoiceQuestionModel,
    ExamBlankSpaceQuestionModel,
    ExamDescribeQuestionModel,
    ExamMatchQuestionModel,
    QuizeChoiceQuestionModel,
    QuizeBlankSpaceQuestionModel,
    QuizeDescribeQuestionModel,
    QuizeDescribeQuestionModel,
    QuizeMatchQuestionModel,
)

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)


admin.site.register(User)
admin.site.register(LanguageModel)
admin.site.register(TransactionModel)
admin.site.register(GradeModel)
admin.site.register(SubjectModel)
admin.site.register(CategoryModel)
admin.site.register(UnitModel)
admin.site.register(ExamChoiceQuestionModel)
admin.site.register(ExamBlankSpaceQuestionModel)
admin.site.register(ExamDescribeQuestionModel)
admin.site.register(ExamMatchQuestionModel)
admin.site.register(QuizeChoiceQuestionModel)
admin.site.register(QuizeBlankSpaceQuestionModel)
admin.site.register(QuizeDescribeQuestionModel)
admin.site.register(QuizeMatchQuestionModel)
