from docx import Document

# Load the existing document
doc = Document("coverletter.docx")

# Replace specific placeholders in the document
for para in doc.paragraphs:
    if "[Content1234567]" in para.text:
        para.text = para.text.replace("[Content1234567]", "Oh my Allah")

# Save the modified document
doc.save("Updated_CoverLetter.docx")

print("Document updated successfully!")
