from asyncio.windows_events import NULL
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import models
from django.db import connections
# from models import Coach, Players


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def teamStats(request, team_name):

    #fetching data for team stats table
    from django.core import serializers
    #data = serializers.serialize("python", models.Players.objects.filter(team=team_name))
    #coach = serializers.serialize("python", models.Coach.objects.filter(team=team_name))
    team = models.Coach.objects.raw('SELECT id, name FROM polls_team WHERE id = %s', [team_name])

    teams = ""
    for t in team:
        teams = t.name
    
    order_by1 = request.GET.get('order_by2', 'id')
    data = serializers.serialize("python", models.Players.objects.all().filter(team=team_name).order_by(order_by1))

    order_by2 = request.GET.get('order_by1', 'id')
    coach = serializers.serialize("python", models.Coach.objects.all().filter(team=team_name).order_by(order_by2))

    #make these queries prepared statements
    filter_by = request.GET.get('filter_by', '0')
    if filter_by == "1":
        coach = models.Coach.objects.all().filter(team=team_name)
        cId = request.GET.get('cId', '')
        cName = request.GET.get('cName', '')
        cAge = request.GET.get('cAge', '')
        all_time_record = request.GET.get('all_time_record', '')
        season_record = request.GET.get('season_record', '')

        if cId != "":
            coach = coach.filter(id=cId)
        if cName != '':
            coach = coach.filter(name=cName)
        if cAge != "":
            coach = coach.filter(age=cAge)
        if all_time_record != '':
            coach = coach.filter(all_time_record=all_time_record)
        if season_record != '':
            coach = coach.filter(season_record=season_record)
        coach = serializers.serialize("python", coach.order_by(order_by2))

    if filter_by == "2":
        data = models.Players.objects.all().filter(team=team_name)
        id = request.GET.get('id', '')
        name = request.GET.get('name', '')
        number = request.GET.get('number', '')
        goals = request.GET.get('goals', '')
        assists = request.GET.get('assists', '')
        position = request.GET.get('position', '')
        age = request.GET.get('age', '0')
        shots_attempted = request.GET.get('shots_attempted', '')
        yellow_cards = request.GET.get('yellow_cards', '')
        red_cards = request.GET.get('red_cards', '')
        saves = request.GET.get('saves', '')

        if id != "":
            data = data.filter(id=id)
        if name != '':
            data = data.filter(name=name)
        if number != "":
            data = data.filter(number=number)
        if goals != "":
            data = data.filter(goals=goals)
        if assists != "":
            data = data.filter(assists=assists)
        if position != '':
            data = data.filter(position=position)
        if age != "":
            data = data.filter(age=age)
        if shots_attempted != "":
            data = data.filter(shots_attempted=shots_attempted)
        if yellow_cards != "":
            data = data.filter(yellow_cards=yellow_cards)
        if red_cards != "":
            data = data.filter(red_cards=red_cards)
        if saves != "":
            data = data.filter(saves=saves)
        data = serializers.serialize("python", data.order_by(order_by1))

    context = {
        'data': data,
        'coach': coach,
        'team': teams,
        'team_name': team_name,
    }

    return render(request, 'teamstats.html', context)

def teamStatsRange(request, team_name):
    
    #fetching data for team stats table
    from django.core import serializers
    #data = serializers.serialize("python", models.Players.objects.filter(team=team_name))
    #coach = serializers.serialize("python", models.Coach.objects.filter(team=team_name))
    team = models.Coach.objects.raw('SELECT id, name FROM polls_team WHERE id = %s', [team_name])

    teams = ""
    for t in team:
        teams = t.name
    
    order_by1 = request.GET.get('order_by2', 'id')
    data = serializers.serialize("python", models.Players.objects.all().filter(team=team_name).order_by(order_by1))

    order_by2 = request.GET.get('order_by1', 'id')
    coach = serializers.serialize("python", models.Coach.objects.all().filter(team=team_name).order_by(order_by2))

    #make these queries prepared statements
    filter_by = request.GET.get('filter', '0')
    if filter_by == "1":
        coach = models.Coach.objects.all().filter(team=team_name)
        query = request.GET.get('query', '')
        qs = set()
        if query != "":
            q = 'SELECT * FROM polls_coach WHERE team_id = {team_name} AND {query}'.format(team_name=team_name, query=query)
            for c in models.Coach.objects.raw(q):
                qs.add(c)
            coach = serializers.serialize("python", qs)

    if filter_by == "2":
        data = models.Players.objects.all().filter(team=team_name)
        query = request.GET.get('query', '')
        qs = set()
        if query != "":
            q = 'SELECT * FROM polls_players WHERE team_id = {team_name} AND {query}'.format(team_name=team_name, query=query)
            for c in models.Players.objects.raw(q):
                qs.add(c)
            data = serializers.serialize("python", qs)

    context = {
        'data': data,
        'coach': coach,
        'team': teams,
        'team_name': team_name,
    }

    return render(request, 'teamstatsrange.html', context)

def teamStatsAdd(request, team_name):

    #fetching data for team stats table
    from django.core import serializers
    #data = serializers.serialize("python", models.Players.objects.filter(team=team_name))
    #coach = serializers.serialize("python", models.Coach.objects.filter(team=team_name))
    team = models.Coach.objects.raw('SELECT id, name FROM polls_team WHERE id = %s', [team_name])

    teams = ""
    for t in team:
        teams = t.name
    context = {
        'team': teams,
        'team_name': team_name,
    }

    add = request.GET.get('add', '0')
    if add == "1":
        cName = request.GET.get('cName', '')
        cAge = request.GET.get('cAge', '')
        all_time_record = request.GET.get('all_time_record', '')
        season_record = request.GET.get('season_record', '')

        cursor = connections['default'].cursor()

        query = "INSERT INTO polls_coach (name, age, all_time_record, season_record, team_id) VALUES (\"{name}\", {age}, \"{all_time_record}\", \"{season_record}\", {team_id})".format(name=cName, age=cAge, all_time_record=all_time_record, season_record=season_record, team_id=team_name)
        cursor.execute(query)
    if add == "2":
        name = request.GET.get('name', '')
        number = request.GET.get('number', '')
        goals = request.GET.get('goals', '')
        assists = request.GET.get('assists', '')
        position = request.GET.get('position', '')
        age = request.GET.get('age', '0')
        shots_attempted = request.GET.get('shots_attempted', '')
        yellow_cards = request.GET.get('yellow_cards', '')
        red_cards = request.GET.get('red_cards', '')
        saves = request.GET.get('saves', '')

        cursor = connections['default'].cursor()

        query = "INSERT INTO polls_players (name, age, number, goals, assists, position, shots_attempted, yellow_cards, red_cards, saves, team_id) VALUES (\"{name}\", {age}, {number}, {goals}, {assists}, \"{position}\", {shots_attempted}, {yellow_cards}, {red_cards}, {saves}, {team_id})".format(name=name, age=age, number=number, goals=goals, assists=assists, position=position, shots_attempted=shots_attempted, yellow_cards=yellow_cards, red_cards=red_cards, saves=saves, team_id=team_name)
        cursor.execute(query)
    return render(request, 'teamstatsadd.html', context)

def teamList(request):

    #fetching data for team stats table
    from django.core import serializers
    #data = serializers.serialize("python", models.Players.objects.filter(team=team_name))
    #coach = serializers.serialize("python", models.Coach.objects.filter(team=team_name))
    #team = models.Coach.objects.raw('SELECT id, name FROM polls_team WHERE id = %s', [team_name])

    #teams = ""
    #for t in team:
    #    teams = t.name
    
    order_by1 = request.GET.get('order_by2', 'id')
    order_by2 = request.GET.get('order_by1', 'id')

    data = serializers.serialize("python", models.Team.objects.all().order_by(order_by1))

    #make these queries prepared statements
    filter_by = request.GET.get('filter_by', '0')
    if filter_by == "1":

        data = models.Team.objects.all()
        id = request.GET.get('id', '')
        name = request.GET.get('name', '')
        points = request.GET.get('points', '')
        league_position = request.GET.get('league_position', '')
        salary = request.GET.get('salary', '')
        record = request.GET.get('record', '')
        stadium = request.GET.get('stadium', '')

        if id != "":
            data = data.filter(id=id)
        if name != '':
            data = data.filter(name=name)
        if points != "":
            data = data.filter(points=points)
        if league_position != "":
            data = data.filter(league_position=league_position)
        if salary != "":
            data = data.filter(salary=salary)
        if record != '':
            data = data.filter(record=record)
        if stadium != "":
            data = data.filter(stadium=stadium)
        
        data = serializers.serialize("python", data.order_by(order_by1))

    context = {
        'data': data
    }

    return render(request, 'teamlist.html', context)

def teamListRange(request):
    
    #fetching data for team stats table
    from django.core import serializers
    #data = serializers.serialize("python", models.Players.objects.filter(team=team_name))
    #coach = serializers.serialize("python", models.Coach.objects.filter(team=team_name))
    
    order_by1 = request.GET.get('order_by2', 'id')
    order_by2 = request.GET.get('order_by1', 'id')
    data = serializers.serialize("python", models.Team.objects.all().order_by(order_by1))
    query = request.GET.get('query', '')
    qs = set()
    if query != "":
        q = 'SELECT * FROM polls_team WHERE {query}'.format(query=query)
        for c in models.Team.objects.raw(q):
            qs.add(c)
        data = serializers.serialize("python", qs)

    context = {
        'data': data,
    }

    return render(request, 'teamlistrange.html', context)

def teamListAdd(request):

    #fetching data for team stats table
    from django.core import serializers
    #data = serializers.serialize("python", models.Players.objects.filter(team=team_name))
    #coach = serializers.serialize("python", models.Coach.objects.filter(team=team_name))
    context = {
    }
    add = request.GET.get('add', '0')
    if add == "1":

        name = request.GET.get('name', '')
        points = request.GET.get('points', '')
        league_position = request.GET.get('league_position', '')
        salary = request.GET.get('salary', '')
        record = request.GET.get('record', '')
        stadium = request.GET.get('stadium', '')

        cursor = connections['default'].cursor()

        query = "INSERT INTO polls_team (name, points, league_position, salary, record, stadium) VALUES \
            (\"{name}\", {points}, {league_position}, {salary}, \"{record}\", \"{stadium}\")"\
                .format(name=name, points=points, league_position=league_position, salary=salary, record=record, stadium=stadium)
        cursor.execute(query)
    return render(request, 'teamlistadd.html', context)
