from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from music.models import Song
from music.models import album
from music.models import podcast
from music.models import Singer
# from django_sp import sp_loader     Singer._meta.get_fields()   
# Create your views here. 
global SP_loader
SP_loader =''
@login_required(login_url='login')
def HomePage(request):
    song = Song.objects.all()
    main = Song.objects.filter(song_id=6) 
    singer = "Sid Sriram"
    sid = Song.objects.filter(singer=2) 
    return render(request,'index.html',{'song':song,'main':main,'sid':sid})
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('your password and conform passwod are not matching!!')
        else:
            my_user=User.objects.create_user(uname,email,pass1) 
            my_user.save() 
            return redirect('login') 


    return render(request,'signup.html')
def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is INCORRECT!!!")
        
    return render(request,'login.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')
def play(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'play.html',{'song':song})
def albums(request):
    playlist = album.objects.all()
    return render(request,'albums-store.html',{'playlist':playlist})
def Channel(request):
    return render(request,'Channel.html')
def album_play(request,name):
    pylist = album.objects.filter(album_name=name).first()
    return render(request,'album_play.html',{'pylist':pylist})
def podcasts(request):
    pod = podcast.objects.all()
    return render(request,'podcast.html',{'pod':pod})
def podcast_upload(request):
        n='not yet registered!!'
        if request.method=='POST':
            name = request.POST.get('name')
            podcaster = request.POST.get('podcaster')
            tags = request.POST.get('tags')
            audio = request.FILES.get('audio')
            img= request.FILES.get('img')
            new_podcast = podcast(name=name,podcaster=podcaster,tags=tags,audio=audio,image=img)
            
            new_podcast.save()
            n = '      details ulpoaded successfully'
        return render(request,'podcast_upload.html',{'n':n})
def music_upload_singer(request):
    n='not Registered!'
    if request.method=="POST":
        Singer_name= request.POST.get('Singer_name')
        Singer_image= request.FILES['Singer_image']
        singer_list = Singer.objects.all()
        new_singer=Singer(name=Singer_name,image=Singer_image)
        for i in singer_list:
            if i.name==Singer_name:
              return HttpResponse("Singer already exits")
            else:
                new_singer.save()
                n = 'Registered Successfully'
            
    return render(request,'music_upload_singer.html',{'n':n})
def music_upload_song(request):
    n = ' not yet uploaded!!'
    singer_list = Singer.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')
        singer= request.POST.get('singer')
        tags = request.POST.get('tags')
        img= request.FILES.get('image')
        audio = request.FILES.get('audio')
        s_name = Singer.objects.get(name=singer)
        new_song = Song(name=name,
        singer=s_name,
        tags=tags,
        image=img,
        song=audio)
        song_list = Song.objects.all()
        for i in song_list:
            if i.name==name:
                return HttpResponse("Song already exits")
            else:
                new_song.save()
                n = '      details ulpoaded successfully'



    return render(request,'music_upload_song.html',{'singer_list':singer_list,'n':n})
def search(request):
    n=''
    if request.method=="POST":
        q_name=request.POST.get('name')
        name = request.POST.get('name')
        if Song.objects.filter(name__contains=name)!=q_name:
            n ='not found'
        if q_name:
            results = Song.objects.filter(name__contains=q_name)
            return render(request, 'search.html', {"results":results})
        else:
            n="RESULT NOT FOUND"
            return render(request, 'search.html', {"n":n})
    else:
        n="RESULT NOT FOUND"
        return render(request, 'search.html',{'n':n})
    n="RESULT NOT FOUND"   
    return render(request, 'search.html',{'n':n})

