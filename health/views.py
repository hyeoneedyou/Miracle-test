from django.shortcuts import render, get_object_or_404
from .models import Health, Certify
from datetime import datetime, timedelta

def main(request, id):
    goal = get_object_or_404(Health, pk = id)
    start_days = (datetime.now() - goal.created).days + 1
    success_days = goal.certifys.filter(achievement=True).count()
    certifys = goal.certifys.all()
    certify_dates = []
    for certify in certifys:
        certify_date = certify.created.strftime('%m/%d')
        certify_dates.append(certify_date)
    continuity_days = 0
    # for i in range(certifys.count()):
    #     date = datetime.now() - timedelta(days=i)
    #     certify = goal.certifys.filter(created=date)
    #     if certify.achievement == True:
    #         continuity_days += 1
    #         continue
    #     else:
    #         break
    context = {
        'goal': goal,
        'start_days': start_days,
        'certifys': certifys,
        'success_days': success_days,
        'certify_dates': certify_dates,
        'continuity_days': continuity_days,
    }
    return render(request, 'health/main.html', context)


def add_goal(request):
    return render(request, 'health/add_goal.html')


