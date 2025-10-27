from django.db import models

# Branch Owner Model
class add(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    branch_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product_image/")
    descriptions = models.TextField()
    
    def __str__(self):
        return self.username

# Service Center Model
class add_service_center(models.Model):
    username_service = models.CharField(max_length=100)
    email_service = models.EmailField(max_length=254)
    branch_name_service = models.CharField(max_length=100)
    contact_service = models.CharField(max_length=100)
    location_service = models.CharField(max_length=100)
    image_service = models.ImageField(upload_to="product_image/")
    descriptions_service = models.TextField()
    
    def __str__(self):
        return self.username_service
    
class bookings(models.Model):
    name_booking = models.CharField(max_length=100)
    email_booking = models.EmailField( max_length=254)
    number_booking = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=100)
    service_date = models.CharField(max_length=100)
    notes_booking = models.TextField()
    service_center = models.ForeignKey(add_service_center, on_delete=models.CASCADE, null=True, blank=True)
    
      
    STATUS_CHOICES = [
        ('ok', 'OK'),
        ('pending', 'Pending'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return self.name_booking
    
class add_mechanics(models.Model):
    name_mechanic = models.CharField(max_length=100)
    contact_mechanic =models.CharField(max_length=50)
    email_mechanic = models.EmailField(max_length=254)
    specialization_mechanic = models.TextField()
    location_mechanic = models.CharField(max_length=100)
    available_from_mechanic = models.CharField(max_length=100)
    available_to_mechanic = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name_mechanic
    
class contact(models.Model):
    name_contact = models.CharField(max_length=100) 
    email_contact = models.EmailField(max_length=254) 
    message_contact = models.TextField()  
    
    def __str__(self):
        return self.name_contact
    
    
