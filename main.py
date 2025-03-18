from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor

# Create a new document
doc = Document()

# Add Name (Bold and Larger Font)
name = doc.add_paragraph()
name_run = name.add_run("Ahmed Elshabasi")
name_run.bold = True
name_run.font.size = Pt(14)
name.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

# Add Contact Info
contact_info = doc.add_paragraph("(587)-435-9647 – Calgary, AB – ahmed.elshabasi@ucalgary.ca – LinkedIn: ")
contact_info.add_run("linkedin.com/in/ahmed-elshabasi/").font.color.rgb = RGBColor(0, 0, 255)  # Blue color for link


# Add Date
doc.add_paragraph("\n15/1/2025\n")

# Add Hiring Team Info
doc.add_paragraph("Hiring Team\nSpartan Controls Ltd.\nCalgary, AB\n")

# Add Subject Line
subject = doc.add_paragraph()
subject_run = subject.add_run("\nRE: Co-op/Intern Student - Data Management Specialist")
subject_run.bold = True

# Add Greeting
doc.add_paragraph("\nDear Hiring Team,\n")

# Add Body Paragraphs
paragraphs = [
    "I am excited to apply for the Data Management Specialist Co-op/Intern position with Spartan Controls. "
    "As a computer science student at the University of Calgary, I have developed a solid foundation in data "
    "workflows, system integration, and software development, and I am eager to contribute to Spartan’s "
    "innovative Digital Foundations team.",

    "My hands-on experience includes designing and implementing automated workflows using Node.js and React "
    "as a research assistant, which enhanced my understanding of data connectivity and system integration. "
    "Additionally, my academic projects have given me exposure to data visualization tools such as Power BI "
    "and relational databases like SQL, aligning well with the role’s focus on operational displays and dashboards.",

    "What excites me most about this opportunity is the chance to work on real-world projects involving software "
    "applications. The combination of technical challenges and collaboration with Spartan’s talented team offers "
    "a unique environment for learning and growth. Furthermore, I admire Spartan’s dedication to providing customer-focused "
    "solutions and creating a sustainable, modern world through applied automation—values that align with my own aspirations.",

    "Thank you for considering my application. I would be thrilled to contribute my skills and enthusiasm to the Digital "
    "Foundations team and support Spartan’s mission to drive customer outcomes through innovative solutions. I look forward "
    "to the opportunity to discuss how I can add value to your team."
]

for para in paragraphs:
    doc.add_paragraph(para + "\n")

# Add Closing
doc.add_paragraph("Sincerely,\nAhmed Elshabasi")

# Save the document
doc.save("Ahmed_Elshabasi_CoverLetter_Generated.docx")

print("Document created successfully!")
