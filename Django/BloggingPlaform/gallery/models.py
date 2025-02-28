from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=100)
    desscription = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def  __self__(self):
        return self.name
    
    def Edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()

    def ShortDescription(self):
        words = self.description.split()
        if(len(words) > 50):
            return ' '.join(words[:30]) + '...'
        return self.description
    
