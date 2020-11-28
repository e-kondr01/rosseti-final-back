from django.urls import path
from . import views


urlpatterns = [
    path('proposal-drafts', views.ProposalDraftView.as_view()),
    path('proposals', views.ProposalListView.as_view()),
    path('proposals/<int:pk>', views.ProposalView.as_view()),
    path('proposals/latest-success', views.latest_successful_proposal),
    path('proposals/collection', views.proposal_collection),
]
