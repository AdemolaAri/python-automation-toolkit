import unittest
import os
from PIL import Image

from scripts.image_processing import resize_images, convert_format


class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and add some test images
        self.test_dir = "test_images/"
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, "test_image1.png"), "w") as f:
            f.write("Test image 1")
        with open(os.path.join(self.test_dir, "test_image2.png"), "w") as f:
            f.write("Test image 2")
        with open(os.path.join(self.test_dir, "test_image3.jpg"), "w") as f:
            f.write("Test image 3")

    def tearDown(self):
        # Remove the temporary directory and its contents
        os.rmdir(self.test_dir)

    def test_resize_images(self):
        # Test resizing images
        img_size = (50, 50)
        resize_images(self.test_dir, img_size)

        # Check if the resized images exist
        resized_image_paths = [
            os.path.join(self.test_dir, "test_image1.png"),
            os.path.join(self.test_dir, "test_image2.png"),
            os.path.join(self.test_dir, "test_image3.jpg"),
        ]

        for path in resized_image_paths:
            with self.subTest(path=path):
                self.assertTrue(os.path.exists(path))
                with Image.open(path) as img:
                    self.assertEqual(img.size, img_size)

    def test_convert_format(self):
        # Test converting image formats
        from_extension = "png"
        to_extension = "jpg"
        convert_format(self.test_dir, from_extension, to_extension)

        # Check if the converted images exist
        converted_image_paths = [
            os.path.join(self.test_dir, "test_image1.jpg"),
            os.path.join(self.test_dir, "test_image2.jpg"),
            os.path.join(self.test_dir, "test_image3.jpg"),
        ]

        for path in converted_image_paths:
            with self.subTest(path=path):
                self.assertTrue(os.path.exists(path))
                with Image.open(path) as img:
                    self.assertEqual(img.format.lower(), to_extension.lower())


if __name__ == "__main__":
    unittest.main()
