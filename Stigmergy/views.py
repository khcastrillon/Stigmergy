from django.shortcuts import  render
from django.http import HttpResponse
import datetime

TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR,"templates"),'
}

fechadehoy = datetime.datetime.now().date()
def home(request):
       return render(request,"home.html",{"fechadehoy":fechadehoy})