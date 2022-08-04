from django.shortcuts import render
from .models import PlayerModel
from django.http import HttpResponseRedirect
from .forms import ChartForm

# Create your views here.
class PlayerChartView:


    def get_chart(request):
        
        chart_request = request.POST or None
        form = ChartForm(chart_request)
        context = {}

        if form.is_valid():
            form.save()

        context['form'] = form
        return render(request, '../templates/chartbase/index.html', context)

# Cannot render more that one data view in the same page
    def get_player_stats(request):
        player_stats = PlayerModel.objects.all()
        return render(request, '../templates/chartbase/player_index.html', {'player_stats': player_stats})


    def delete_player(request, player):
        player = PlayerModel.objects.get(id = player)
        player.delete()
        player_stats = PlayerModel.objects.all()
        return HttpResponseRedirect('/playercreation/playerindex/')
