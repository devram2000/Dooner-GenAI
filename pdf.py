from fpdf import FPDF
from unidecode import unidecode
import re

class PDF(FPDF):
    def header(self):
        # Logo with increased padding (adjust the x, y values and width as needed)
        self.image('sju_logo.jpeg', 10, 0, 33)
        self.set_font('Arial', 'B', 15)
        # Move to the right (adjust the value to change padding)
        self.cell(100)
        # Title
        self.cell(30, 10, 'SJU Sustainability Plan', 0, 1, 'C') # Line break changed from 0 to 1
        # Add more padding (adjust the padding value as needed)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        # Process the body to format bold text and remove non-readable text
        body = self.format_body_text(body)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_chapter(self, title, body):
        # No longer adding a new page for each chapter
        self.chapter_title(title)
        self.chapter_body(body)

    def format_body_text(self, text):
        # Remove non-readable characters like '------'
        text = re.sub(r'-{2,}', '', text)
        # Convert body text to closest latin-1 representation
        text = unidecode(text)
        # Replace **bold** with FPDF bold formatting
        def replace_bold(match):
            return self.set_text_mode('B') + match.group(1) + self.set_text_mode('')
        text = re.sub(r'\*\*(.*?)\*\*', replace_bold, text)
        return text

    def set_text_mode(self, mode=''):
        # Helper method to switch to bold mode and back.
        if mode == 'B':
            self.set_font('Arial', 'B', 11)
        else:
            self.set_font('Arial', '', 11)
        return ''

# Create a PDF object
pdf = PDF()

# Add the first page to the PDF
pdf.add_page()  # <-- This line was added.

# Read the text from the file
with open('sju_sustainability_plan_draft.txt', 'r', encoding='utf-8') as file:
    text = unidecode(file.read())

# Split the text into sections
sections = text.split('## ')
introduction = sections[0]
chapters = sections[1:]

# Add other chapters
for chapter in chapters:
    title, body = chapter.split('\n', 1)
    pdf.add_chapter(title, body)

# Number of pages
pdf.alias_nb_pages()

# Save the PDF with name
pdf.output('SJU_Sustainability_Plan.pdf')
