# backend/api/models.py

from app import db



# Host model
class Host(db.Model):
    hostId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    HostName = db.Column(db.String(100), nullable=False)
    hostStatus = db.Column(db.Enum('active', 'inactive'), nullable=False)
    Location = db.Column(db.Text)
    About = db.Column(db.Text)
    HostingSince = db.Column(db.Date)

# Property model
class Property(db.Model):
    propertyId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostId = db.Column(db.Integer, db.ForeignKey('host.hostId'), nullable=False)
    Images = db.Column(db.Text)  # You can store image URLs as a comma-separated list or use a separate table for images.
    Price = db.Column(db.Numeric(10, 2))
    Location = db.Column(db.Text)
    Description = db.Column(db.Text)
    HostDetails = db.Column(db.Text)

# Guest model
class Guest(db.Model):
    guestId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    GuestName = db.Column(db.String(100), nullable=False)
    GuestGender = db.Column(db.Enum('male', 'female', 'other'))
    DateOfBirth = db.Column(db.Date)
    Bio = db.Column(db.Text)

# Booking model
class Booking(db.Model):
    bookingId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    propertyId = db.Column(db.Integer, db.ForeignKey('property.propertyId'), nullable=False)
    guestId = db.Column(db.Integer, db.ForeignKey('guest.guestId'), nullable=False)
    CheckIn = db.Column(db.Date)
    CheckOut = db.Column(db.Date)

# Property_images model (if storing images separately)
class PropertyImages(db.Model):
    imageId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    propertyId = db.Column(db.Integer, db.ForeignKey('property.propertyId'), nullable=False)
    ImageLink = db.Column(db.Text)

# Amenities model
class Amenities(db.Model):
    amenityId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Description = db.Column(db.Text)
    ImageLink = db.Column(db.Text)

# Property_Amenities model (for many-to-many relationship between Property and Amenities)
class PropertyAmenities(db.Model):
    propertyId = db.Column(db.Integer, db.ForeignKey('property.propertyId'), primary_key=True)
    amenityId = db.Column(db.Integer, db.ForeignKey('amenities.amenityId'), primary_key=True)

# Review model
class Review(db.Model):
    reviewId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reviewDescription = db.Column(db.Text)
    userId = db.Column(db.Integer, db.ForeignKey('guest.guestId'), nullable=False)
    propertyId = db.Column(db.Integer, db.ForeignKey('property.propertyId'), nullable=False)
