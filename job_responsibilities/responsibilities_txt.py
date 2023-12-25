import docx

# Define the path to your Word document
file_path = "./Center and Institute Director Duties and Responsibilities with Blurb.docx"

# Open the document using the variable
doc = docx.Document(file_path)
text = ""

# Access text from paragraphs
for paragraph in doc.paragraphs:
    text += paragraph.text

schools = []
current_school = []
i = 0
for section in text.split("***"):
    if section:
        if i < 6:
            current_school.append(section.replace("*", "").replace("[", "").replace("]", "").strip())
            i += 1
        else:
            schools.append(current_school)
            current_school = [section]
            i = 1
schools.append(current_school)

schools_nolinks = []
for s in schools:
    s_new = []
    for t in s:
        if "http" not in t:
            s_new.append(t)
    schools_nolinks.append(s_new)

# Adjust the size of each sublist
for i in range(len(schools_nolinks)):
    if len(schools_nolinks[i]) != 4:
        schools_nolinks[i].append("")

# Save the data to a text file
with open('school_responsibilities.txt', 'w', encoding='utf-8') as file:
    file.write("[")
    for school in schools_nolinks:
        file.write("[")
        for s in school:
            file.write(s +', ')
        file.write("]")
    file.write("]")


print("All Schools processed. Corpus saved to 'school_responsibilities.txt'.")
