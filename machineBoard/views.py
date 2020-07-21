from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


from .models import MaintainerTeam, Machine, Defaillance, InfoIntervention

# Create your views here.



def index(request):
    context = {
        'machineAll': Machine.objects.all(),
        'teamList': MaintainerTeam.objects.all()

    }

    return render(request, "index.html", context)


def maintenanceBoard(request):
    try:
        teamName_enter = request.POST["teamName"]
        team = MaintainerTeam.objects.get(nameTeam=teamName_enter)

    except KeyError:
        return render(request, "error.html")
    except MaintainerTeam.DoesNotExist:
        return render(request, "error.html")

    if(team.passwordTeam != request.POST["password"]):
        return render(request, "error.html")

    context = {
        'machineAll': Machine.objects.all(),
        'teamName': teamName_enter
    }

    return render(request, "maintenance_board.html", context)


def saveAgain(request):
    try:
        machineName_enter = request.POST["machineName"]

        maintainerTeam = MaintainerTeam.objects.get(
            nameTeam=request.POST["maintainerTeam"])

        defaillanceList = Defaillance(
            cause=request.POST["codeA"], origine=request.POST["codeB"], gravite=request.POST["codeC"])

        defaillanceList.save()

        infoIntervention = InfoIntervention.objects.create(dateDefaillance=request.POST["dateDefaillance"],
                                                           dateIntervention=request.POST["dateIntervention"],
                                                           durationIntervention=request.POST["durationIntervention"],
                                                           dateServiceOn=request.POST["dateServiceOn"],
                                                           defaillanceList=defaillanceList,
                                                           maintainerTeam=maintainerTeam)
        infoIntervention.save()

    except KeyError:
        return render(request, "error.html", {'error': 'keyEroor'})

    except MaintainerTeam.DoesNotExist:
        return render(request, "error.html", {'error': 'Maintainer existe pas'})

    try:
        machine = Machine.objects.get(machineName=machineName_enter)

    except Machine.DoesNotExist:
        machine = Machine.objects.create(machineName=machineName_enter)

        machine.infoInterventionAll.add(infoIntervention)
        machine.save()

        context = {
            'machineAll': Machine.objects.all(),
            'teamName': request.POST["maintainerTeam"]
        }
        return render(request, "maintenance_board.html", context)

    machine.infoInterventionAll.add(infoIntervention)

    context = {
        'machineAll': Machine.objects.all(),
        'teamName': request.POST["maintainerTeam"]
    }

    return render(request, "maintenance_board.html", context)
