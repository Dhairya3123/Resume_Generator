import argparse
import requests
from fpdf import FPDF

# Function to fetch resume data from API
def fetch_resume(name):
    url = f"https://expressjs-api-resume-random.onrender.com/resume?name={name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching resume data.")
        return None

# Function to generate a PDF
def generate_pdf(data, font_size, font_color, bg_color, output_file):
    pdf = FPDF()
    pdf.add_page()

    # Set background color
    pdf.set_fill_color(int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16))
    pdf.rect(0, 0, 210, 297, style="F")

    # Set font color
    r, g, b = int(font_color[1:3], 16), int(font_color[3:5], 16), int(font_color[5:7], 16)
    pdf.set_text_color(r, g, b)

    # Add name (Bold and font_size + 2)
    pdf.set_font("Arial", style="B", size=font_size + 4)
    pdf.cell(200, 10, f"{data['name']}", ln=True)

    # Add contact details with reduced spacing
    pdf.set_font("Arial", size=font_size)
    pdf.cell(40, 10, f"{data['phone']}", border=0)
    pdf.cell(40, 10, f"{data['email']}", border=0)
    pdf.cell(40, 10, f"{data['twitter']}", ln=True)
    pdf.multi_cell(0, 10, f"{data['address']}")

    # Horizontal line
    y = pdf.get_y() + 2
    pdf.line(10, y, 200, y)
    pdf.ln(5)

    # Summary Section
    pdf.set_font("Arial", style="B", size=font_size + 2)
    pdf.cell(200, 10, "Summary:", ln=True)
    pdf.set_font("Arial", size=font_size)
    pdf.multi_cell(0, 10, data["summary"])

    # Horizontal line
    y = pdf.get_y() + 2
    pdf.line(10, y, 200, y)
    pdf.ln(5)

    # Skills Section
    pdf.set_font("Arial", style="B", size=font_size + 2)
    pdf.cell(200, 10, "Skills:", ln=True)
    pdf.set_font("Arial", size=font_size)

    skills = data["skills"]
    num_columns = 3
    column_width = 65
    row_height = 10

    for i, skill in enumerate(skills):
        pdf.cell(column_width, row_height, skill, border=0)
        if (i + 1) % num_columns == 0:
            pdf.ln(row_height)

    if len(skills) % num_columns != 0:
        pdf.ln(row_height)

    # Horizontal line
    y = pdf.get_y() + 2
    pdf.line(10, y, 200, y)
    pdf.ln(5)

    # Projects Section
    pdf.set_font("Arial", style="B", size=font_size + 2)
    pdf.cell(200, 10, "Projects:", ln=True)
    pdf.ln(2)
    
    for project in data["projects"]:
        title = project["title"]
        start_date = project["startDate"]
        end_date = project["endDate"]
        description = project["description"]

        # Project title and date range in Bold with the same font size
        pdf.set_font("Arial", style="B", size=font_size)
        pdf.cell(120, 10, title, border=0)
        pdf.cell(60, 10, f"({start_date} - {end_date})", border=0, ln=True)

        pdf.set_font("Arial", size=font_size)
        pdf.multi_cell(0, 10, description)
        pdf.ln(5)

    # Horizontal line
    y = pdf.get_y() + 2
    pdf.line(10, y, 200, y)
    pdf.ln(5)

    # Experience Section
    pdf.set_font("Arial", style="B", size=font_size + 2)
    pdf.cell(200, 10, "Experience:", ln=True)
    pdf.set_font("Arial", size=font_size)

    if "experience" in data:
        for exp in data["experience"]:
            pdf.multi_cell(0, 10, f"{exp['title']} at {exp['company']} ({exp['years']} years)")
    else:
        pdf.cell(200, 10, "No experience available.", ln=True)

    # Save PDF
    pdf.output(output_file)
    print(f"Resume saved as {output_file}")

# Command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Customizable Resume PDF Generator")
    parser.add_argument("--name", required=True, help="Name for fetching resume data")
    parser.add_argument("--font-size", type=int, default=12, help="Font size")
    parser.add_argument("--font-color", default="#000000", help="Font color in HEX")
    parser.add_argument("--background-color", default="#FFFFFF", help="Background color in HEX")
    
    args = parser.parse_args()

    resume_data = fetch_resume(args.name)
    if resume_data:
        generate_pdf(resume_data, args.font_size, args.font_color, args.background_color, "custom_resume.pdf")
