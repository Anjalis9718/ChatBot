from django.shortcuts import render
from first_app.models import Listing
from django.http import HttpResponse
from . import forms
import MySQLdb
import xlrd
# Create your views here.
def button(request):

    return render(request,'first.html')

def button1(request):
    form=forms.PostForm()
    if request.method=='POST':
        form=forms.PostForm(request.POST)
        if form.is_valid():
                    # process form data
            obj = Listing() #gets new object
            obj.text = form.cleaned_data['text']

                    #finally save the object in db
            obj.save()
            return render(request,'status.html',{'form':form})


    return render(request,'status.html',{'form':form})

def button2(request):
    form=forms.PostForm()
    if request.method=='POST':
        form=forms.PostForm(request.POST)
        if form.is_valid():
                    # process form data
            obj = Listing() #gets new object
            obj.text = form.cleaned_data['text']

                    #finally save the object in db
            obj.save()
            return render(request,'Ticket_confirm.html',{'form':form})


    return render(request,'Ticket_confirm.html',{'form':form})

def button3(request):
    form=forms.PostForm()
    if request.method=='POST':
        form=forms.PostForm(request.POST)
        if form.is_valid():
                    # process form data
            obj = Listing() #gets new object
            obj.text = form.cleaned_data['text']

                    #finally save the object in db
            obj.save()
            return render(request,'check-in-timing.html',{'form':form})


    return render(request,'check-in-timing.html',{'form':form})

def button4(request):
    form=forms.PostForm()
    if request.method=='POST':
        form=forms.PostForm(request.POST)
        if form.is_valid():
                    # process form data
            obj = Listing() #gets new object
            obj.text = form.cleaned_data['text']

                    #finally save the object in db
            obj.save()
            return render(request,'other.html',{'form':form})


    return render(request,'other.html',{'form':form})






def form_view(request):
    form=forms.PostForm()
    import mysql.connector

    #mydb = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #passwd="",
    #database="Air_India"
    #)
    if request.method=='POST':
        if request.is_ajax():
            data = request.POST.get('mydata')
            mydb = MySQLdb.connect(user='root', db='AirIndia', passwd='', host='localhost')
            cursor = mydb.cursor()
            if(data=='ok' or data=='Ok'):
                astr="<html><b></br>CHATBOT:Thanks !!</html>"
            #cursor.execute("SELECT Date FROM Flight_Info where Flight_No=%s"%data)
            #cursor.execute("SELECT case when Flight_No=%s then 'YES' else 'NO' end as result from Flight_Info" %data)
            else:
                #cursor.execute("SELECT case when Flight_No='%s' then 'YES' else 'NO' end as result from flight_info" %data)
                cursor.execute("select count(*) from flight_info where Flight_No='%s'"%data)
                name=cursor.fetchall()
                print(name)

                import re
                import string
                names=str(name)
                names=names.replace(",","")
                names=names.replace("[","")
                names=names.replace("]","")
                names=names.replace(")","")
                names=names.replace("(","")
                names=names.replace("''","")
                names=names.replace("'","")
                print(names)

                if (names == '0'):

                    astr = "<html><b></br>Sorry, this isn't a valid PNR number. TRY AGAIN!!</html>"
                else:
                    cursor.execute('SELECT Date_of_Dept FROM flight_info where Flight_No="%s"'%data)
                    info=cursor.fetchall()
                    astr = "<html><b></br>The date of flight is %s</html>" % info

                mydb.close()
            return HttpResponse(astr)
    return render(request)




def input(request):
    form=forms.message()
    if request.method=='POST':
        form=forms.message(request.POST)
        if form.is_valid():
            data=form.cleaned_data['text']

            print(post_text)
            print(data)


    return render(request,'status.html',{'form':form})

def ticket_confirm(request):
    form=forms.PostForm()
    import mysql.connector
    if request.method=='POST':
        if request.is_ajax():
            data = request.POST.get('mydata')
            mydb = MySQLdb.connect(user='root', db='AirIndia', passwd='', host='localhost')
            cursor = mydb.cursor()
            if(data=='ok' or data=='Ok'):
                astr="<html><b></br>CHATBOT:Thanks !!</html>"
            else:
                cursor.execute("select count(*) from customer_info where Booking_No='%s'"%data)
                name=cursor.fetchall()
                import re
                import string
                names=str(name)
                names=names.replace(",","")
                names=names.replace("[","")
                names=names.replace("]","")
                names=names.replace(")","")
                names=names.replace("(","")
                names=names.replace("''","")
                names=names.replace("'","")
                print(names)

                if (names == '0'):

                    astr = "<html><b></br>Sorry, this isn't a valid Booking number. TRY AGAIN!!</html>"
                else:
                    cursor.execute('SELECT Booking_status FROM customer_info where Booking_No="%s"'%data)
                    info=cursor.fetchall()
                    astr = "<html><b></br>The reservation status is %s</html>" % info

                mydb.close()
            return HttpResponse(astr)
    return render(request)




def input1(request):
    form=forms.message()
    if request.method=='POST':
        form=forms.message(request.POST)
        if form.is_valid():
            data=form.cleaned_data['text']

            print(post_text)
            print(data)


    return render(request,'Ticket_confirm.html',{'form':form})

def checkintime(request):
    form=forms.PostForm()
    import mysql.connector
    if request.method=='POST':
        if request.is_ajax():
            data = request.POST.get('mydata')
            mydb = MySQLdb.connect(user='root', db='AirIndia', passwd='', host='localhost')
            cursor = mydb.cursor()
            if(data=='ok' or data=='Ok'):
                astr="<html><b></br>CHATBOT:Thanks !!</html>"
            else:
                cursor.execute("select count(*) from flight_info where Flight_No='%s'"%data)
                name=cursor.fetchall()
                import re
                import string
                names=str(name)
                names=names.replace(",","")
                names=names.replace("[","")
                names=names.replace("]","")
                names=names.replace(")","")
                names=names.replace("(","")
                names=names.replace("''","")
                names=names.replace("'","")
                print(names)

                if (names == '0'):

                    astr = "<html><b></br>CHATBOT:Sorry, this isn't a valid Flight number. TRY AGAIN!!</html>"
                else:
                    cursor.execute('SELECT Time_of_Dept FROM flight_info where Flight_No="%s"'%data)
                    info=cursor.fetchall()
                    astr = "<html><b></br>The time of departture is %s</html>" % info

                mydb.close()
            return HttpResponse(astr)
    return render(request)




def input2(request):
    form=forms.message()
    if request.method=='POST':
        form=forms.message(request.POST)
        if form.is_valid():
            data=form.cleaned_data['text']

            print(post_text)
            print(data)


    return render(request,'check-in-timing.html',{'form':form})
from first_app import nlp
def otherquery(request):
    form=forms.PostForm()
    if request.method=='POST':
        if request.is_ajax():
            user_response= request.POST.get('mydata')

            reply3=nlp.reply(user_response)
            astr="<html><b></br> %s</html>" % reply3
            return HttpResponse(astr)
    return render(request)

def input3(request):
    form=forms.message()
    if request.method=='POST':
        form=forms.message(request.POST)
        if form.is_valid():
            data=form.cleaned_data['text']

            print(post_text)
            print(data)


    return render(request,'other.html',{'form':form})
