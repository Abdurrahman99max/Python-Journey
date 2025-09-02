# Smartphone class example

# Parent class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # battery percentage

    def make_call(self, contact):
        print(f"Calling {contact} from {self.model}...")

    def charge_phone(self):
        self.battery = 100
        print(f"{self.model} is now fully charged!")

# Child class (Inheritance)
class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery, camera_megapixels):
        super().__init__(brand, model, battery)  # Inherit attributes
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"📸 Taking a photo with {self.camera_megapixels}MP camera!")

# Testing our classes
phone1 = Smartphone("Samsung", "Galaxy S22", 50)
phone1.make_call("Alice")
phone1.charge_phone()

camera_phone = CameraPhone("Apple", "iPhone 15", 75, 48)
camera_phone.take_photo()
camera_phone.make_call("Bob")
