# recruiting-pipeline

A quick script I wrote to help people who are recruiting now use AI to tailor their resumes/cover letters for roles. You'll need the following:

- An OpenAI api key. Create a .env file in the same directory as the python script and put into the file `OPENAI_API_KEY=` followed by your key, no spaces
- A csv file (change this to be delimited by the |, not a comma. Also title it "jobs.csv") containing all of the jobs you are applying to. Keep the columns titled "Company", "Role", and "Description
- Two files: resume.txt and misc.txt. Resume.txt should be explanatory, but misc.txt should contain any information that is not found on your resume that you would like to be included when writing the tailored resumes and cover letters. Keep them in the same directory as the script.

The script will create folders for companies and roles that you are applying to, and store resume.txt and coverletter.txt files accordingly. Format the content to your liking in your desired format.

> Keep in mind that this is just a starting point for some inspiration. Reword and further tailor it yourself to put your best foot forward.