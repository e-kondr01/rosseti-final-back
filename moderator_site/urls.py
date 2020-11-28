from django.urls import path
from . import views


urlpatterns = [
    path('proposals', views.ProposalList.as_view(), name='proposal_list'),
    path('proposals/<int:pk>', views.ProposalDetail.as_view(),
         name='proposal_detail'),
    path('proposals/<int:pk>/edit', views.UpdateProposal.as_view(),
         name='update_proposal'),
]
