from django.shortcuts import  render
from django.http import HttpResponse
import datetime

TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR,"templates"),'
}

fechadehoy = datetime.datetime.now().date()
def interfazManejador(request):
       return render(request,"manejador_ordenes.html",{"fechadehoy":fechadehoy})
