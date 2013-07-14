from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
import urllib2
from django.core import serializers
from lxml import etree
import string

def index(request):

	search=""

	if 'Name' in request.GET:
		search+=request.GET['Name']
		search+=" "
	if 'Location' in request.GET:
		search+=request.GET['Location']
		search+=" "
	if 'Email' in request.GET:
		search+=request.GET['Email']

	search=string.replace(search," ", "%20")
	print search

	url="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20boss.search%20where%20q%3D%22"+search+"%22%20and%20ck%3D%22dj0yJmk9YWF3ODdGNWZPYjg2JmQ9WVdrOWVsWlZNRk5KTldFbWNHbzlNVEEyTURFNU1qWXkmcz1jb25zdW1lcnNlY3JldCZ4PTUz%22%20and%20secret%3D%22a3d93853ba3bad8a99a175e8ffa90a702cd08cfa%22%20and%20sites%3D%22facebook.com%22%20and%20count%3D10&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"


	page = urllib2.urlopen(url)
	data=page.read()
	
	root = etree.fromstring(data)


	l=[]

	count=0
	for child in root.iter():
		if child.tag=='result':
			for i in child.iter():
				if i.tag=='url':
					url=i.text
					if url.find("public")>0 or url.find("pages")>0 or url.find("v=feed") >0 :
						break
					x=string.split(url,"facebook.com/")
					x[1]=string.replace(x[1],"?filter=1", "")
					image="http://graph.facebook.com/"+x[1]+"/picture?type=large"
#					print "id     :"+x[1]
					flag=0
					for a in l:
						if a['id']==x[1]:
							flag=1
							break
					if flag==1:
						break
					l.append({})
					l[count]['url']=url
					l[count]['image']=image
					l[count]['id']=x[1]
#					print image


				if i.tag=='title':
					title=i.text
					title=string.replace(title,"<b>", "")
					title=string.replace(title,"</b>", "")
					l[count]['title']=title
					count+=1


	url2="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20boss.search%20where%20q%3D%22"+search+"%22%20and%20ck%3D%22dj0yJmk9YWF3ODdGNWZPYjg2JmQ9WVdrOWVsWlZNRk5KTldFbWNHbzlNVEEyTURFNU1qWXkmcz1jb25zdW1lcnNlY3JldCZ4PTUz%22%20and%20secret%3D%22a3d93853ba3bad8a99a175e8ffa90a702cd08cfa%22%20and%20sites%3D%22plus.google.com%22%20and%20count%3D10&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

	page2 = urllib2.urlopen(url2)
	data2=page2.read()
	
	root2 = etree.fromstring(data2)



	for child in root2.iter():
		if child.tag=='result':
			for i in child.iter():
				if i.tag=='url':
					l.append({})
					url=i.text
					l[count]['url']=url
					x=string.split(url,"google.com/")
#					print x
					image="https://plus.google.com/s2/photos/profile/"+x[1]+"?sz=200"
					x=string.split(image,"/?")
#					print x
					if "sz=200" in x:
#						print "ETYS"
						image=x[0]+"?"+x[1]
					l[count]['image']=image
					print image
				if i.tag=='title':
					title=i.text
					title=string.replace(title,"<b>", "")
					title=string.replace(title,"</b>", "")
					l[count]['title']=title
					count+=1
					break




	
	x=len(l)
	count=0
	i=0
	j=[]
	while(1):
		j.append([])
		for k in range(0,4):
			if i>= x:
				break
			j[count].append(l[i])
			i+=1
		if i>=x:
			break
		count+=1



	return render(request,'glopss_app/basic.html',{'results':l})

