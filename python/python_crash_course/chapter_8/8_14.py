def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model name'] = model_name

    return car_info

car1 = make_car('mercedes','benz', color='white',top_speed="260km/hr")
print(car1)

car2 = make_car('mercedes','benz')
print(car2)