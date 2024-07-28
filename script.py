from openai import OpenAI
import csv
import os


client = OpenAI()
filename = "output.csv"

with open(filename, mode='r') as file:
    csv_reader = csv.DictReader(file, delimiter='|')
    data_list = []
    for row in csv_reader:
        data_list.append(row)

resume_path = "resume.txt"
with open(resume_path, 'r', encoding = 'utf-8') as file:
    resume = file.read()

misc_path = "misc.txt"
with open(resume_path, 'r', encoding = 'utf-8') as file:
    misc = file.read()

# modulizing the entry of the output of the API calls
def insert_entry(path, filename, content):
    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

for role in data_list:
    # extract information
    company = role['Company']
    job = role['Role']
    
    company_path = company.replace(' ', '-')
    job_path = job.replace(' ', '-')
    
    role_path = os.path.join(os.getcwd(), company_path, job_path)

    responseResume = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": "You are an expert consultant on tailoring people's skills and resumes to specific jobs that they want to apply to. You will be given a file containing a resume, a file containing any other miscellaneous information that the client wants to include on their resume, and data containing what role they want to apply to and the role's description. Give your output ONLY in the format of the resume that they gave you. Do not include any other output. No 'certainly!' or anything like that. Just tweak their resume for this specific role to give them their best foot forward and don't include any other output"},
            {"role": "user", "content": str(role)},
            {"role": "user", "content": resume},
            {"role": "user", "content": misc}
        ]
    )

    responseCoverLetter = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": "You are an expert consultant on writing cover letters to people applying to roles. to specific jobs that they want to apply to. You will be given a file containing a resume, a file containing any other miscellaneous information that the client wants to include on their resume, and data containing what role they want to apply to and the role's description. Without ANY other output, write the user an excellent cover letter for this role that would highlight their interest in this role."},
            {"role": "user", "content": str(role)},
            {"role": "user", "content": resume},
            {"role": "user", "content": misc}
        ]
    )
    
    #print("resume")
    #print(type(responseResume.choices[0].message))
    #print(responseResume.choices[0].message)

    #print("cover letter")
    #print(type(responseCoverLetter.choices[0].message))
    #print(responseCoverLetter.choices[0].message)
    
    insert_entry(role_path, "resume.txt", responseResume.choices[0].message.content)
    insert_entry(role_path, "cover_letter.txt", responseCoverLetter.choices[0].message.content)

