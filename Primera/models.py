from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        
from django.db import models

class Disco(models.Model):
    nombre = models.CharField(max_length=200) 
    artista = models.CharField(max_length=200) 
    año = models.PositiveIntegerField()  
    duracion = models.DurationField()  
    canciones = models.IntegerField()  
    genero = models.CharField(max_length=100)  
    imagen = models.ImageField(upload_to='discos_imagenes/', blank=True, null=True) 
    sello = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.nombre} - {self.artista}"
    

    



   

    
    