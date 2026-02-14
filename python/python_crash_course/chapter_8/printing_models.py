def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model name'] = model_name

    return car_info

def collect_items_in_sandwich(*items):
    for item in items:
        print(f"I am adding {item} to your sandwich.")


if __name__ == '__main__':
    car1 = make_car('mercedes','benz', color='white',top_speed="260km/hr")
    print(car1)

    car2 = make_car('mercedes','benz')
    print(car2)

    user_profile = build_profile('aarya', 'sarfare',
                            location='mumbai',
                            field='Full Stack Development',
                            favorite_number=34,
                            )

    print(user_profile)