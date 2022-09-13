# Project Statement

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

## Tasks
 - Write a script to process supplier images 
 - Upload update images to web server 
 - Upload text descripitons to website
 - Generate a PDF using Python
 - Automatically send a PDF by email
 - Write a script to check the health status of the system

### Write a Script to Process Supplier Images
In this section, you will write a Python script named `changeImage.py` to process the supplier images within `./supplier-data/images` directory to the following specifications:

  - **Size**: Change image resolution from `3000x2000` to `600x400` pixel
  - **Format**: Change image format from `.TIFF` to `.JPEG`

### Upload Images to Web Server
You have modified the fruit images through `changeImage.py` script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the [linux-instance-IP-Address]/upload URL

### Upload Descriptions to Website
Write a Python script named `run.py` to process the text files `(001.txt, 003.txt ...)` from the `supplier-data/descriptions` directory. 
Example of the input text (001.txt):
     `Apple`
     `500 lbs`
     `Apple is one of the most nutritious and healthiest fruits. It is very rich in antioxidants and dietary fiber. Moderate consumption can not only increase satiety, but also help promote bowel movements. Apple also contains minerals such as calcium and magnesium, which can help prevent and delay bone loss and maintain bone health. It is good for young and old. `

The data model in the Django application fruit has the following fields: name, weight, description and image_name. The weight field is defined as an integer field. The final JSON object should be similar to:
    `{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}`


 ### Generate a PDF Report and Send it through email

Once the `images` and `descriptions` have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed.
The content of the report should look like this:

        #### Processed Update on <Today's date>

        [blank line]

        name: Apple

        weight: 500 lbs

        [blank line]

        name: Avocado

        weight: 200 lbs

        [blank line]

        ...

### Health check
Write a Python script named `health_check.py` that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

  - Report an error if CPU usage is over 80%
  - Report an error if available disk space is lower than 20%
  - Report an error if available memory is less than 500MB
  - Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"