from django.shortcuts import render

# Create your views here.
def about(request):
		return render(request, 'sitepages/about.html')




# return render(request, 'posts/home.html', {'posts':posts})
		# return render(request, 'posts/home.html', {'posts':posts})
