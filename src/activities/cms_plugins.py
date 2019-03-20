from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .forms import LatestActivitiesPluginForm
from .models import LatestActivityPlugin


@plugin_pool.register_plugin
class LatestActivityPublisher(CMSPluginBase):
    model = LatestActivityPlugin
    form = LatestActivitiesPluginForm
    name = _('Latest Activities')
    render_template = 'activities/plugins/latest.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['activity_list'] = instance.get_activities()
        return context
