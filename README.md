# Text-Extraction-using-Doctr

![Screenshot 1](./Images/Screenshot%20from%202023-07-21%2011-23-33.png)

This project is a straightforward text extraction tool from documents, leveraging the powerful doctr library. doctr is a robust, efficient, and accessible OCR (Optical Character Recognition) library, based on cutting-edge Deep Learning techniques. The project's repository can be found at https://github.com/mindee/doctr.

In addition to the OCR capabilities, the project also includes a user-friendly interface created using Selenium. This interface enables users to interact with the tool seamlessly.

![Screenshot 2](./Images/Screenshot%20from%202023-07-21%2011-23-54.png)

To run the project, Docker is used along with the provided Dockerfile and requirements.txt file. Follow these steps:

1. Build the Docker image using: docker build -t <image_name> .
2. Run the container using: docker run <image_name>

To further enhance the project, there are several To-Do items:

1. Improve the user interface to enhance the navigation of document pages.
2. Implement summarization or contextual analysis of the document, utilizing a Deep Learning library for more advanced insights.
