# Resume_Generator
Overview

This is a Python script that generates a professional resume in PDF format using the fpdf library. The script allows customization of font size, font color, and background color.

Setup and Usage Instructions

Follow these steps to set up and run the Resume Generator on your system:

1. Download the Project
	Make sure all project files, including resume_generator.py, are in a dedicated folder on your system.

2. Install Python
	Ensure Python is installed on your system. You can check by running:
	python --version
	If Python is not installed, download and install it from python.org.
3. Install Required Dependencies
	This project uses the fpdf library to generate PDF files. Install it using:
	pip install fpdf
4. Run the Script
	Use the following command to generate a resume:
	python resume_generator.py --name "Your Name" --font-size 12 --font-color "#0000FF" --background-color "#D3D3D3"
	This will create a custom_resume.pdf file in the same directory.