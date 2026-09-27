🔐 Password Strength Analyzer
_____________________________________

A Python-based web application that analyzes password strength using multiple security checks and provides recommendations for creating stronger passwords.

🌐 Live Demo
____________________________
Try the application here:

https://thiranex-password-strength-analyzer-qrynyytatjwtuinuc6fvkh.streamlit.app/

📌 Project Overview
________________________

The Password Strength Analyzer evaluates a password based on its length, character complexity, common-password usage, repeated characters, and predictable sequences.

The application also includes a secure password generator that uses Python's secrets module to generate random passwords.

✨ Features
_________________

1.Password length analysis
2.Lowercase character detection
3.Uppercase character detection
4.Number detection
5.Special character detection
6.Common-password detection
7.Repeated-character detection
8.Predictable-sequence detection
9.Password strength score
10.Strength classification
11.Security recommendations
12.Secure password generation
13.Interactive Streamlit web interface

🛠️ Technologies Used
______________________

1.Python
2.Streamlit
3.Python secrets module
4.Python string module

📂 Project Structure
_______________________

password-strength-analyzer/
│
├── app.py
├── analyzer.py
├── README.md
└── requirements.txt

1. app.py

-> Contains the Streamlit user interface and handles user interaction.

2. analyzer.py

-> Contains the password analysis logic and secure password generation functionality.

🔍 Password Analysis
_________________________

The analyzer checks:

1. Password length
2. Lowercase letters
3. Uppercase letters
4. Numbers
5. Special characters
6. Common passwords
7. Repeated characters
8. Predictable sequences

-> The application calculates a score and classifies the password as:

1. Very Weak
2. Weak
3. Medium
4. Strong
5. Very Strong

🔐 Security Considerations
________________________________


-> The application does not store or save the password entered by the user.

-> Password analysis is performed in memory.

-> The password generator uses Python's secrets module instead of the standard random module because secrets is     designed for security-sensitive random values.

-> The common-password check is based on a local list of commonly used passwords and does not claim to determine    whether a password has ever appeared in every known password breach.

🚀 Installation
__________________

1. Clone the repository:

git clone <your-github-repository-url>

2. Move into the Project directory:

cd password-strength-analyzer

3.Install the required dependencies:

pip install -r requirements.txt

▶️ Running the Application
____________________________

Run the following command

streamlit run app.py

The application will open in your browser.

🧪 Testing
_______________

The Application was tested using passwords with different characteristics,including

1. Very Short Passwords
2. Common Passwords
3. Passwords Without Uppercase Characters
4. Passwords Without Numbers
5. passwords Without Special Characters
6. Passwords Containing Repeated Characters
7. Passwords Containing Predictable Sequences
8. Strong Randomly Generated Passwords

All planned test cases produced the expected results.

🎯 Learning Outcomes
__________________________

Through this project, I practiced:

-> Python Functions

-> String Processing 

-> Conditional Logic

-> Password Security Concepts

-> Secure Random Password Generation

-> Streamlit Application Development 

-> Software Testing

-> Basic CyberSecurity Practices


⚠️ Limitations
___________________

-> This project is an educational password-strength analyzer and should not be considered a complete enterprise password-security solution.

-> The scoring system is a custom project-specific scoring model rather than an industry-standard password-strength measurement.

-> The common-password detection currently uses a local list and does not represent every compromised password in existence.


🔮 Future Improvements
_________________________________

Possible future enhancements include:

1. Larger common-password datasets
2. More advanced password-strength estimation
3. Password breach checking using privacy-     preserving methods
4. Improved visualizations
5. More detailed security recommendations
6. Deployment as a public web application

👨‍💻 Project Type:
_______________________


Cyber Security Internship Project

Project: Password Strength Analyzer

📊 Scoring Model:
_______________________

The project uses a custom 8-point scoring model:

1. Password length of 8–11 characters: 1 point
2. Password length of 12 or more characters: 2 points
3. Lowercase letters: 1 point
4. Uppercase letters: 1 point
5. Numbers: 1 point
6. Special characters: 1 point
7. Common-password detection can reduce the score
8. Repeated-character patterns can reduce the score
9. Predictable sequences can reduce the score


This score is designed for this educational project and is not an industry-standard password-strength measurement.