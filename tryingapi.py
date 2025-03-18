import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv("OPENAI_API_KEY"),
)

job_descrip = f"""Spartan Controls Ltd. Logo
Spartan Controls Ltd.
4.1
Co-op/Intern Student - Data Management Specialist (16 Months)
Calgary



Apply on employer site


Apply on employer site
Spartan Controls is an employee-owned company and leading provider of data management, industrial automation, valves, measurement and control solutions for process industries in Western Canada and beyond. We are dedicated to providing exceptional sales, support and service experiences for our diverse customer base in industries such as mining, power, oil & gas, municipal, pulp & paper, and chemical.


Spartan is committed to creating a sustainable modern world with innovative automation. Our focus is Customer Outcomes. By leveraging applied automation we assist customers improving their Safety, Reliability, Operations and Productivity.


Our employee ownership model creates a unique culture of community, creativity, entrepreneurship, and a place to build your career. Spartan Controls provides an environment that not only encourages you to do your best, but also empowers you to do what it takes to create a solution, address a need, or respond to an issue.


Summary
Join our innovative Digital Foundations team based in Calgary as a Data Management Specialist Co-op/Intern Student. Reporting to the Manager of Operations, you'll contribute to the installation, data connectivity, and system integration of industrial data software applications, providing valuable support to our customer-focused initiatives.

Role and Responsibilities
As a Co-op/Intern Student, you will have the opportunity to:

Installation, data connectivity and system integration of the following software applications (AVEVA PI, Capstone DataPARC and Aspentech IP.21)
Testing of existing software applications for on-premises, virtual and cloud-based deployment
Contribute to the creation of documentation for client use.
Creation of operational displays and dashboards.
Creating of Hierarchical templates for managing customer data.
Collaborate with the broader Digital Foundations team to enhance internal processes.
The current expectation of all work being executed from the Spartan Controls office.
Qualifications and Skills
Current Engineering or Technologist student, preferably in Computer Science, Software Engineering, Electrical Engineering, Instrumentation Technology.
Students enrolled in a post-secondary Co-op/Internship program, returning to school in September 2026 are preferred.
Solid technical problem-solving skills.
Strong communication and time management skills.
Familiarity with databases and process data historians (e.g. AVEVA PI), or visualization tools (e.g. Power BI) is advantageous – training will be provided.
Understanding of industrial networks, servers, and work stations are an asset.
A working knowledge of a programming language is beneficial however not required– please highlight this in your application.
Demonstrated Customer Service in a professional environment is an asset.
Collaborative team player and strong work principles.
Proficiency in MS Office programs (Word, Power Point, Excel)
Detail oriented with an entrepreneurial work ethic.

This 16-month opportunity provides hands-on experience in a dynamic and collaborative environment, allowing you to apply yourself to real-world projects and support. Join us in shaping the future of digital solutions at Spartan Controls!


As part our recruitment process, successful candidates will be required to pass a pre-employment security background check.

Spartan recognizes that there are many ways in which candidates develop knowledge, abilities, and competencies throughout their careers. We encourage applications from candidates with a variety of backgrounds and we do consider qualifications and competencies that are equivalent to those specifically mentioned above.


Close Date: January 19, 2025 (11:59 pm MST)

Requisition ID: 1394"""

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": f"""Ahmed Elshabasi
(587)-435-9647 – Calgary, AB – ahmed.elshabasi@ucalgary.ca – LinkedIn: linkedin.com/in/ahmed-elshabasi/
Skills
•	Programming languages: Java, Python, JavaScript, C, C++, HTML, CSS, React, Node.JS, Express.JS, SQL
•	Software tools: VS Code, Git, Github, Gitlab, Unity, Unreal Engine
•	Algorithm and Data Structures: Studied different algorithms and structures in university
•	Professional Skills: Adaptability, Communication, Detail-oriented, Leadership, and Time Management
Experience
Undergraduate Research Assistant (Node, React, JS)					                           May 2024 – Sep 2024
University of Calgary,     Calgary, AB
•	Developed an automated workflow using Node and React for extracting in-depth information about the data in the corpus completing tasks within set deadlines.
•	Collected first-person videos, spoken recordings, and biometric data for a corpus of information needs for outdoor running.
•	Quickly learned new tools and technologies (Node, React, and smart capture devices) to automate data analysis workflows.
Projects
Self-Checkout Machine Software (Java)								          Sep 2023 – Dec 2023
•	Collaborated with a team of 20 to designed and develop the software for a self-checkout machine
•	Focused on user-friendly interface design and efficient transaction handling to ensure smooth customer experience.
•	Integrated functionalities that simulate real-world use cases.
Educational Assessment Web App (JS, CSS, HTML)						            Jan 2024 – Apr 2024
•	Collaborated with a team of 5 to design a web application for dynamic assessments.
•	Implemented functionality to generate random questions per session, offering immediate grading and feedback.
•	Emphasized designing a user-friendly interface to provide smooth navigation and create an engaging test experience.
Full-stack Financial Assistant| Hackathon Project (Node, React, JS)	   		     	                              Feb 2024
•	Led a team of 4 to build a full-stack prompt-based financial assistant.
•	 Used ChatGPT’s API for real-time financial insights and assistance.
•	Ensured seamless deployment within the time constraints of the hackathon (24 hours).
Education
Bachelor of Computer Science									   2022 – 2026 [Expected]
University of Calgary,  Calgary, AB									    GPA: 3.68
•	Awards:
o	PURE award
o	President’s Admission Scholarship
o	University of Calgary International Undergraduate Award
•	Certificates:
o	Google Cybersecurity Professional Certificate		
o	Ready for Research Micro credential
Volunteering
Setup Crew											          Jan 2022 – May 2022
G.N.P. Hospital,    Jeddah, Saudi Arabia
•	Assisted medical students with a staff team of 5 and documented the students’ progress.
•	Collaboratively smoothed the experience for the students by getting their feedback and answering inquiries.
•	Recorded students’ progress and managed their attendance for their hospital’s academy training.
Executive Team Member									          Dec 2021 - Apr 2022
Model United Nations (MUN) at Dar Jana International School
•	Managed and participated with the MUN executive team in the organization of documents and preparation of participants
•	Prepared the hall in which the event takes place and ensured that the event proceeded as expected.
•	As one of the spokespersons (chairmen) of the event, fulfilled my duties of planning and managing the procedures of the delegates.
Extracurricular Clubs
Event Coordinator										         Sep 2023 – May 2024
Infosec Club											
•	Coordinated hands-on security labs and ethical hacking workshops, providing practical learning experiences for members.
Member											         Sep 2023 – May 2024
Competitive Programming Club									 
•	Engaged in practical programming challenges, honing my problem-solving skills through regular workshop attendance.

Ahmed Elshabasi
(587)-435-9647
ahmed.elshabasi@ucalgary.ca
Calgary, AB

[Hiring Manager]
Dear [Hiring Manager at [company]],
I am writing to express my interest in the [job position] at [your company]. I am a highly dedicated and resourceful individual with a passion for achieving goals under tight deadlines. With strong skills in various programming languages and project management, I am confident that I can contribute to your team’s success.
Throughout my academic and professional journey, I have developed a solid foundation in programming and software development. I pride myself on being adaptable and quick to learn new technologies, as well as my ability to handle complex tasks while managing multiple projects simultaneously. My approach to problem-solving is both creative and analytical, allowing me to navigate challenges and deliver results effectively.
I am particularly excited about the opportunity to bring my skills in leadership, time management, and teamwork to [your company]. I am driven by the desire to meet deadlines without compromising on quality, and I believe my strong work ethic and ability to think on my feet would be valuable to your team.
I welcome the opportunity to further discuss how my dedication, technical skills, and resourcefulness align with the needs of your organization. Thank you for considering my application. I am available at your convenience for an interview and look forward to the possibility of contributing to [your company].
Sincerely,
Ahmed Elshabasi



this is my resume and bs coverletter keep that in mind cause i am about to ask you to do stuff

Here is the job description: {job_descrip}

Write me a cover letter but i want it in a very strict format

the format should look like this:
[Date123]:[[[the actual date of today and i need you to write it as dd/mm/yyyy]]]
[Company123]:[[[the actual company name]]]
[Location123]:[[[the address of the company]]]
[Subject123]:[[[the actual subject of the cover letter]]]
[Content123]:[[[this is what follows exactly right after "dear hiring manager," and right before "sincerely, Ahmed Elshabasi"]]]
"""
        }
    ]
)

print(completion.choices[0].message.content)