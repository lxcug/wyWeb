from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# Create your views here.


def index(request):
    return render(request, 'index.html')


def getPlotData(request):
    return render(request, 'plot.html')


def getScatterData(request):
    return render(request, 'scatter.html')


def getPolyFitData(request):
    return render(request, 'polyfit.html')


def plot(request):
    if request.POST:
        x = request.POST['x'].split(' ')
        y = request.POST['y'].split(' ')
        title = request.POST['title']
        label = request.POST['label']
        x = [float(_) for _ in x if _ != '']
        y = [float(_) for _ in y if _ != '']
        if len(x) != len(y):
            return HttpResponse('x的长度为{}，y的长度为{}'.format(len(x), len(y)))
        plt.figure()
        plt.plot(x, y, label=label)
        plt.scatter(x, y)
        if label:
            plt.legend()
        for i in range(len(x)):
            plt.text(x[i], y[i] * 1.01, '{}'.format(y[i]))
        plt.title(title)
        plt.savefig('temp1.png')
        with open('temp1.png', 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
    else:
        return HttpResponse("Please post!")


def scatter(request):
    if request.POST:
        x = request.POST['x'].split(' ')
        y = request.POST['y'].split(' ')
        title = request.POST['title']
        label = request.POST['label']
        x = [float(_) for _ in x if _ != '']
        y = [float(_) for _ in y if _ != '']
        if len(x) != len(y):
            return HttpResponse('x的长度为{}，y的长度为{}'.format(len(x), len(y)))
        plt.figure()
        plt.scatter(x, y, label=label)
        if label:
            plt.legend()
        for i in range(len(x)):
            plt.text(x[i], y[i] * 1.01, '{}'.format(y[i]))
        plt.title(title)
        plt.savefig('temp2.png')
        with open('temp2.png', 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
    else:
        return HttpResponse("Please post!")


def polyFit(request):
    if request.POST:
        x = request.POST['x'].split(' ')
        y = request.POST['y'].split(' ')
        title = request.POST['title']
        label = request.POST['label']
        n = int(request.POST['n'])
        x = [float(_) for _ in x if _ != '']
        y = [float(_) for _ in y if _ != '']
        if len(x) != len(y):
            return HttpResponse('x的长度为{}，y的长度为{}'.format(len(x), len(y)))
        plt.figure()
        plt.scatter(x, y)
        for i in range(len(x)):
            plt.text(x[i], y[i] * 1.01, '{}'.format(y[i]))
        z1 = np.polyfit(x, y, n)
        p1 = np.poly1d(z1)
        y_new = p1(x)
        plt.plot(x, y_new, label=label)
        if label:
            plt.legend()
        plt.title(title)
        plt.savefig('temp3.png')
        with open('temp3.png', 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
    else:
        return HttpResponse("Please post!")