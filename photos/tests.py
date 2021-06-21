from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TransactionTestCase as TestCase
from .models import Photo


def create_image(image_path: str) -> (SimpleUploadedFile, bytes):
    with open(image_path, 'rb') as image_file:
        image_file_bytes = image_file.read()
        image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_file_bytes,
            content_type='image/jpeg'
        )
    return image_file, image_file_bytes


class PhotoTestCase(TestCase):
    reset_sequences = True

    def setUp(self):
        image_path = ("C:/Users/DELL/Pictures/hela/cate"
                      "-blanchett-marvel-cinematic-universe"
                      "-smoky-eyes-marvel-comics-wallpaper-preview.jpg"
                      )
        self.image_file, self.image_file_bytes = create_image(image_path)
        self.image1 = Photo.objects.create(image=self.image_file)

    def test_create_photo(self):
        image_path = ("C:/Users/DELL/Pictures/hela/cate"
                      "-blanchett-marvel-cinematic-universe"
                      "-smoky-eyes-marvel-comics-wallpaper-preview.jpg"
                      )

        image_file, _ = create_image(image_path)
        Photo.objects.create(image=image_file)

        with Photo.objects.get(id=2).image.file as img:
            self.assertEqual(img.read(), self.image_file_bytes)

    def test_read_photo(self):
        with Photo.objects.get(id=1).image.file as img:
            self.assertEqual(img.read(), self.image_file_bytes)
        with self.assertRaises(ObjectDoesNotExist):
            Photo.objects.get(id=2)

    def test_update_photo(self):
        new_image_path = "C:\\Users\\DELL\\Pictures\\hela\\wp2063088.jpg"
        new_image_file, new_image_file_bytes = create_image(new_image_path)

        new_photo = Photo.objects.get(id=1)
        new_photo.image = new_image_file
        new_photo.save()

        with Photo.objects.get(id=1).image.file as img:
            self.assertEqual(img.read(), new_image_file_bytes)

    def test_delete_photo(self):
        Photo.objects.get(id=1).delete()

        with self.assertRaises(ObjectDoesNotExist):
            Photo.objects.get(id=1)
