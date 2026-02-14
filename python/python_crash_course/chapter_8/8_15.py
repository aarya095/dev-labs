from chapter_8.printing_models import make_car

car = make_car('BMW','M5')

for key, value in car.items():
    print(f"{key} : {value}")