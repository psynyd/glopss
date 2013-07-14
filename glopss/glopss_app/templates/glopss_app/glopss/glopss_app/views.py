from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
import urllib2
from django.core import serializers
from lxml import etree

def index(request):

	




	url="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20boss.search%20where%20q%3D%22akash%20agarwal%20iiit%22%20and%20ck%3D%22dj0yJmk9YWF3ODdGNWZPYjg2JmQ9WVdrOWVsWlZNRk5KTldFbWNHbzlNVEEyTURFNU1qWXkmcz1jb25zdW1lcnNlY3JldCZ4PTUz%22%20and%20secret%3D%22a3d93853ba3bad8a99a175e8ffa90a702cd08cfa%22%20and%20sites%3D%22facebook.com%22%20and%20count%3D10&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"



	page = urllib2.urlopen(url)
	data=page.read()
	
	root = etree.fromstring(data)


	l=[]

	count=0
	for child in root.iter():
		if child.tag=='result':
			for i in child.iter():
				if i.tag=='url':
					l.append({})
					l[count]['url']=i.text
				if i.tag=='title':
					l[count]['title']=i.text
					count+=1


	url2="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20boss.search%20where%20q%3D%22akash%20agarwal%22%20and%20ck%3D%22dj0yJmk9YWF3ODdGNWZPYjg2JmQ9WVdrOWVsWlZNRk5KTldFbWNHbzlNVEEyTURFNU1qWXkmcz1jb25zdW1lcnNlY3JldCZ4PTUz%22%20and%20secret%3D%22a3d93853ba3bad8a99a175e8ffa90a702cd08cfa%22%20and%20sites%3D%22plus.google.com%22%20and%20count%3D10&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

	page2 = urllib2.urlopen(url2)
	data2=page2.read()
	
	root2 = etree.fromstring(data2)



	for child in root2.iter():
		if child.tag=='result':
			for i in child.iter():
				if i.tag=='url':
					l.append({})
					l[count]['url']=i.text
				if i.tag=='title':
					l[count]['title']=i.text
					count+=1





	url3="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20boss.search%20where%20q%3D%22akash%20agarwal%22%20and%20ck%3D%22dj0yJmk9YWF3ODdGNWZPYjg2JmQ9WVdrOWVsWlZNRk5KTldFbWNHbzlNVEEyTURFNU1qWXkmcz1jb25zdW1lcnNlY3JldCZ4PTUz%22%20and%20secret%3D%22a3d93853ba3bad8a99a175e8ffa90a702cd08cfa%22%20and%20sites%3D%22plus.google.com%22%20and%20count%3D10&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

	page3 = urllib2.urlopen(url3)
	data3=page3.read()
	
	root3 = etree.fromstring(data3)



	for child in root3.iter():
		if child.tag=='result':
			for i in child.iter():
				if i.tag=='url':
					l.append({})
					l[count]['url']=i.text
				if i.tag=='title':
					l[count]['title']=i.text
					count+=1





	url4="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20boss.search%20where%20q%3D%22akash%20agarwal%22%20and%20ck%3D%22dj0yJmk9YWF3ODdGNWZPYjg2JmQ9WVdrOWVsWlZNRk5KTldFbWNHbzlNVEEyTURFNU1qWXkmcz1jb25zdW1lcnNlY3JldCZ4PTUz%22%20and%20secret%3D%22a3d93853ba3bad8a99a175e8ffa90a702cd08cfa%22%20and%20sites%3D%22plus.google.com%22%20and%20count%3D10&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

	page4 = urllib2.urlopen(url4)
	data4=page4.read()
	
	root4 = etree.fromstring(data4)



	for child in root4.iter():
		if child.tag=='result':
			for i in child.iter():
				if i.tag=='url':
					l.append({})
					l[count]['url']=i.text
				if i.tag=='title':
					l[count]['title']=i.text
					count+=1


	return render(request,'glopss_app/index.html',{'results':l})

