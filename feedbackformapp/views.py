from django.shortcuts import render
from .models import FeedBackData
from .forms import FeedbackForm
import datetime
date1=datetime.datetime.now()

# Create your views here.
def feedback_view(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedBackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform=FeedbackForm()
            feedbacks=FeedBackData.objects.all()
            context={'form':fform,'feedbacks':feedbacks}
            return render(request,'feedback.html',context)
    else:
        fform=FeedbackForm()
        feedbacks=FeedBackData.objects.all()
        context={'form':fform,'feedbacks':feedbacks}
        return render(request,'feedback.html',context)