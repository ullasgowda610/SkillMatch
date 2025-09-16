import streamlit as st
from pdfextractor import text_extractor
import google.generativeai as genai
import os

# Congigure the model
key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

resume_text=job_desc=None

#Upload resume
st.sidebar.title(':blue[UPLOAD YOUR RESUME (PDF Only)]')
file=st.sidebar.file_uploader('Resume',type=['pdf'])
if file:
    resume_text = text_extractor(file)
    

# Lets define the main page

st.title(':orange[SKILL MATCH]: :blue[AI Assistant skill Matching Tool]')
st.markdown('#### This application will match your resume and the job decription.It will create a detailed report on the match')
tips='''Follow these steps to proceed
* Upload your resume in the sidebar(PDF Only)
* Copy and paste the job description below for which you are applying for.
* click the button and see the magic'''

st.write(tips)

job_desc=st.text_area('copy and paste the job description here(press ctrl+enter to run):',max_chars=10000)

prompt=f'''Assume you are a expert in skill matching and creating profiles.
Match the following resumes with job decription provided by the user.
resume={resume_text}
job description={job_desc}


Your output should be as follows:
* Give a brief description of the applicant in 3 to 5 lines.
* Give a range expected ATS score along with the matching and non matching keywords.
* Give the chances of getting shortlisted for this position in  percentage.
* Perform SWOT analysis and discuss each and everything in bullet points
* Suggest what all improvements can be made in resume in order to get better ATS and increase          percentage  og getting shortlisted.
* Also create two customized resumes as per the job description provided.
* prepare one page resume in such a format that can be copied and pasted in word and converted to pdf.
* Use bullet points and tables wherever necessary.
* Keep the language professional and easy to understand.'''


if job_desc:
    if resume_text:
        response=model.generate_content(prompt)
        st.write(response.text)
    else:
        st.error('Please upload your resume and job description')