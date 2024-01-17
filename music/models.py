from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images')
    def __str__ (self):
         return self.name

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer= models.ForeignKey(Singer, on_delete=models.CASCADE)
    tags = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='audio_files')
    def __str__ (self):
         return self.name

class album(models.Model):
    album_id = models.IntegerField()
    album_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images')
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,primary_key=True)
    song11 = models.ForeignKey(Song, on_delete=models.CASCADE)
    song22= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song2')
    song33= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song3')
    song44= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song4')
    song55= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song5')
    song66= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song6')
    song77= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song7')
    song88= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song8')
    song99= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song9')
    song100= models.ForeignKey(Song, on_delete=models.CASCADE,related_name='Song_song10')

    def __str__ (self):
         return self.album_name
class podcast(models.Model):
    name = models.CharField(max_length=1000)
    podcaster = models.CharField(max_length=1000)
    tags = models.CharField(max_length=10000)
    audio = models.FileField(upload_to='audio_files')
    image=models.ImageField(upload_to='images')
    def __str__ (self):
         return self.name
