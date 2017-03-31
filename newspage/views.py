# Create your views here.

# -*- coding: utf-8 -*-

from django.http import HttpResponse
from newspage.models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.shortcuts import render


def content(request):
    title_qs = News.objects.values_list("title")
    url_qs = News.objects.values_list("url")

    # count = News.objects.count()
    # page_number = count/100
    # page_obj = []

    # for i in range(page_number):
    title_link_str = []
    for j in range(100):
        title_link_str.append('<a href=\"' + str(url_qs[j][0]) + '\">'+ str(title_qs[j][0]) + '<br></p>\n')
    #     page_obj.append(title_link_str)
    #
    # p = Paginator(page_obj, page_number)
    #
    # page = request.GET.get('page')
    #
    # try:
    #     contacts = p.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     contacts = p.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     contacts = p.page(p.num_pages)
    #
    # return render_to_response('list.html', {"contacts": contacts})

    html_struct = "<!DOCTYPE html>\n<html>\n<head>\n<title>News List</title>\n</head>\n<body> "

    return HttpResponse(html_struct + "<article>" + ' '.join(title_link_str) + "</body>\n</html>")

    # return HttpResponse(' '.join(title_link_str))
