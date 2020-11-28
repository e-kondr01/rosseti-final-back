from django.views.generic import ListView, UpdateView, DetailView
from api.models import Proposal


class ProposalList(ListView):
    model = Proposal
    template_name = 'moderator_site/proposal_list.html'


class ProposalDetail(DetailView):
    model = Proposal
    template_name = 'moderator_site/proposal_detail.html'


class UpdateProposal(UpdateView):
    model = Proposal
    template_name = 'moderator_site/proposal_form.html'
    fields = [
        'title', 'description', 'status', 'category',
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['draft_description'] = self.object.draft.description
        return context
