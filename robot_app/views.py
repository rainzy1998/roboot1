from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'robot_app/index.html')

def upload(request):
    print(request.POST)

    file_name=request.POST['name']
    file=request.FILES['file']
    with open(file_name,'wb') as f:
        f.write(file.read())
    print(request.FILES)

    return render(request,'robot_app/index.html')