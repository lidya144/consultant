from django.urls import include, path
from transaction import views

urlpatterns = [
    path("transactions/",views.TransactionList.as_view()),
    path("transactions/<int:transactionId>/",views.TransactionRUD.as_view())
    
]