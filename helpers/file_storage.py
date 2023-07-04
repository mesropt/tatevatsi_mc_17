# def movie_images_storage(instance, filename):
#     return f"movies/{instance.name}/{instance.year}/{filename}"
#
#
# def producer_images_storage(instance, filename):
#     return f"producer/{instance.first_name}_{instance.last_name}/{filename}"


def doctor_image_storage(instance, filename):
    return f"doctors/{instance.first_name}_{instance.last_name}/{filename}"
