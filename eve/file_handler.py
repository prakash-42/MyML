# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
# import os
#
# CLOUDINARY_CLOUD_NAME = os.environ['CLOUDINARY_CLOUD_NAME']
# CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
# CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
#
# cloudinary.config(
#   cloud_name=CLOUDINARY_CLOUD_NAME,
#   api_key=CLOUDINARY_KEY,
#   api_secret=CLOUDINARY_SECRET,
# )
#
#
def upload_to_cloudinary(file):
    # print('file passed: ', file)
    # response = cloudinary.uploader.upload_image(file, use_filename=True, folder="MyML/Eve")
    # url = response.url
    # delete_file(file.name)
    return "Final_file_url", True


# def delete_file(filename):
#     path = '/media/'
#     os.remove(os.getcwd() + path + filename)
#     return 'deleted'
