# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from secrets import choice
from django.core.mail import send_mail
from asgiref.sync import async_to_sync
from django.conf import settings
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from multiprocessing import context
from tracemalloc import stop
from turtle import position
# from types import NoneType, TracebackType
from typing import Dict
from urllib import response
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from numpy import append
import pandas as pd
import os

# from apps.api.models import Mill
from apps.api.forms import *
from apps.api.models import *
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views.decorators.http import require_http_methods
import requests
import json
from channels.layers import get_channel_layer
import requests
from datetime import date, timedelta
import numpy as np


@login_required(login_url="/login/")
def index(request):
    context = {"segment": "index", "room_name": "broadcast"}
    payload = ""
    task_req = requests.request("GET", "http://localhost:8000/api/task", data=payload)
    handover_req = requests.request(
        "GET", "http://localhost:8000/api/taskhandover", data=payload
    )
    html_template = loader.get_template("home/index.html")

    if task_req.status_code == 200 and handover_req.status_code == 200:
        tasks = task_req.json()["task"]
        tasks_df = pd.DataFrame.from_dict(tasks, orient="columns")

        tasks_df = tasks_df[tasks_df["created_date"].notnull()]
        tasks_df["created_date"] = pd.to_datetime(
            tasks_df["created_date"], format="%Y-%m-%d %H:%M:%S"
        )
        tasks_df["due_date"] = pd.to_datetime(
            tasks_df["due_date"], format="%Y-%m-%d %H:%M:%S"
        )
        my_tasks = (
            tasks_df[tasks_df["assigned_to"] == request.user.username]
            .sort_values("due_date", ascending=False)
            .head(5)
        )
        tasks_df["end_date"] = pd.to_datetime(
            tasks_df["end_date"], format="%Y-%m-%d %H:%M:%S"
        )

        cats = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        today = datetime.now()
        week_prior = today - timedelta(weeks=1)

        daily_group = tasks_df[(tasks_df["created_date"] >= week_prior)]
        completed = len(daily_group[daily_group["end_date"].notnull()])
        incomplete = len(daily_group[~daily_group["end_date"].notnull()])

        daily_group = (
            daily_group.created_date.dt.day_name().value_counts().reset_index()
        )

        daily_group["index"] = pd.Categorical(
            daily_group["index"], categories=cats, ordered=True
        )

        daily_group = daily_group.sort_values("index")["created_date"]

        ttl_complete_incomplete = {"completed": completed, "outstanding": incomplete}

        incidents = tasks_df[
            (tasks_df["type"] == "Incident")
            & (tasks_df["created_date"] >= datetime.today())
        ]
        activities = tasks_df[
            (tasks_df["type"] == "Activity")
            & (tasks_df["created_date"] >= datetime.today())
        ]

        stats = {
            "incident": len(incidents),
            "activity": len(activities),
            "handover": len(handover_req.json()["handover"]),
        }

        return HttpResponse(
            html_template.render(
                {
                    "stats": stats,
                    "daily_chrt": list(daily_group),
                    "ttl_complete": ttl_complete_incomplete,
                    "mytasks": json.loads(my_tasks.to_json(orient="records")),
                },
                request,
            )
        )
    else:
        stats = {"incident": "*", "activity": "*", "handover": "*"}
        return HttpResponse(html_template.render(stats, request))


# @login_required(login_url='/login/')
# def overall_stats(request):


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def charts(request):
    t = loader.get_template("home/charts.html")
    c = {}
    return HttpResponse(t.render(c, request))


def email(email_dict: Dict):
    subject = email_dict["subject"]
    message = email_dict["message"]
    email_from = settings.EMAIL_HOST_USER
    recipient_list = email_dict["recipient_list"]
    send_mail(subject, message, email_from, recipient_list)
    pass



@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def incidentForm(request):
    t = loader.get_template("home/forms.html")
    # context = {'my_list': json.dumps(my_list), 'my_dict': json.dumps(my_dict)}
    context = {}

    manager_list = User.objects.all().filter(position_id=1)
    managers_email = [manager.email for manager in manager_list]

    managers_email.append("chinjunwai7@gmail.com")

    print(managers_email)
    if request.method == "POST":
        form = taskForm(request.POST, request.FILES)


        #save image
        # img = request.FILES['photo']
        # path = default_storage.save('tmp/somename.png', ContentFile(img.read()))
        # tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        # print('temp file {}'.format(tmp_file))



        if form.is_valid():
            # form.created_date = datetime.now()
            img = form.cleaned_data.get("photo")
            print(img)
            task = form.save(commit=False)
            task.created_date = datetime.now() + timedelta(hours=8)
            task.save()
            # email(
            #     {
            #         'subject': 'New {} Happended'.format(form.cleaned_data['type']),
            #         'message': 'You look so good Today keep it up',
            #         'recipient_list': managers_email,
            #     }
            # )
            print("form can besaved")

        else:
            print('error')
            print(form.errors)
    else:
        form = taskForm()

    context["taskForm"] = form
    return HttpResponse(t.render(context, request))


# @login_required(login_url="/login/")
# def assignForm(request):
#     t = loader.get_template('home/assignForm.html')
#     return HttpResponse(t.render(context, request))


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def taskUnassignedView(request):
    t = loader.get_template("home/taskUnassigned.html")
    unassignedTasks = Task.objects.all().filter(assigned_to=None)

    if request.method == "POST":
        form = assigneeForm(request.POST, request.FILES)
    # new_user.password
    context = {}
    context["unassignedTasks"] = unassignedTasks
    return HttpResponse(t.render(context, request))


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def assignFormView(request, id=None):
    print(id)
    t = loader.get_template("home/assignForm.html")
    task = Task.objects.filter(id = id)
    if request.method == "POST":
        form = assigneeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            # new_user.password
            task.update(assigned_to=form.cleaned_data['assigned_to'])
            task.update(assigned_date= datetime.now() + timedelta(hours=8))
            task.update(comment=form.cleaned_data['comment'])
            task.update(due_date=form.cleaned_data['due_date'])
            task.update(progress="In Progress")
            # task.save()
            print("form can besaved")
        else:
            print(form.errors)
    else:
        form = assigneeForm()
    all_users = User.objects.all()
    # print(all_users)
    options = [(user.name, user.name) for user in all_users]
    print(form.fields["assigned_to"])
    for option in options:
        print(option)
    form.fields["assigned_to"].choices = ("hello", "hello")
    # form['assigned_to'].choices =
    context = {}
    context["assignForm"] = form
    return HttpResponse(t.render(context, request))


@login_required(login_url="/login/")
def allTaskView(request):
    t = loader.get_template("home/allTask.html")
    all_tasks = Task.objects.all()
    context = {}
    context["allTask"] = all_tasks
    return HttpResponse(t.render(context, request))


def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {"type": "send_notification", "message": json.dumps("Notification")},
    )
    return HttpResponse("Done")


# Import these methods
# from django.core.files import File
# from django.core.files.base import ContentFile
# from django.core.files.temp import NamedTemporaryFile


# def image_upload(request):
#     context = dict()
#     if request.method == 'POST':
#         username = request.POST["username"]
#         image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
#         image = NamedTemporaryFile()
#         image.write(urlopen(path).read())
#         image.flush()
#         image = File(image)
#         name = str(image.name).split('\\')[-1]
#         name += '.jpg'  # store image in jpeg format
#         image.name = name
#         if image is not None:
#             obj = Image.objects.create(username=username, image=image)  # create a object of Image type defined in your model
#             obj.save()
#             context["path"] = obj.image.url  #url to image stored in my server/local device
#             context["username"] = obj.username
#         else :
#             return redirect('/')
#         return redirect('any_url')
#     return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_fun(subject,body,receiver_email):
    
    sender_email = 'acehackathon2022@zohomail.com'
    password = settings.EMAIL_HOST_PASSWORD
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # subject,body,receiver_email
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(settings.EMAIL_HOST,settings.EMAIL_PORT, context=context) as server:
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(settings.EMAIL_HOST_USER, receiver_email, text)
    pass
