from django.shortcuts import render, redirect
import requests
from .models import Cidade
from .forms import CityForm
from django.contrib import messages


def homeview(request):

	cidades = Cidade.objects.all()
	form = CityForm()

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=505ae3ba084fe03f0b8071d9da4d6836'

	weather_data = []

	if request.method == 'POST':
		form = CityForm(request.POST)

		if form.is_valid():
			city = form.cleaned_data['nome']
			r = requests.get(url.format(city)).json()

			if r['cod'] == "404":
				messages.error(request, 'Esta cidade nao existe!')
				return redirect('weather:home')

			else:
				number_cities = Cidade.objects.filter(nome=city).count()

				if number_cities == 0:
					form.save()
					messages.success(request, 'Cidade adicionada com sucesso!')
				else:
					messages.error(request, 'Esta cidade ja existe!')

				return redirect('weather:home')

	for cidade in cidades:

		r = requests.get(url.format(cidade.nome)).json()

		city_weather = {
			'city': cidade.nome,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],

		}

		weather_data.append(city_weather)


	context = {
		'weather_data': weather_data,
		'form': form,
	}

	return render(request, 'weather/index.html', context)


def delete_cityview(request, city):
	city_to_delete = Cidade.objects.get(nome=city).delete()

	messages.success(request, 'Cidade removida')
	return redirect('weather:home')


