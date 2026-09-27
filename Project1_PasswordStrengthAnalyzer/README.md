🔐 Password Strength Analyzer
A Python-based web application that analyzes password strength using multiple security checks and provides recommendations for creating stronger passwords.

🌐 Live Demo
Try the application here:

https://thiranex-password-strength-analyzer-qrynyytatjwtuinuc6fvkh.streamlit.app/

📌 Project Overview
The Password Strength Analyzer evaluates a password based on its length, character complexity, common-password usage, repeated characters, and predictable sequences.

The application also includes a secure password generator that uses Python's secrets module to generate random passwords.

✨ Features
Password length analysis
Lowercase character detection
Uppercase character detection
Number detection
Special character detection
Common-password detection
Repeated-character detection
Predictable-sequence detection
Password strength score
Strength classification
Security recommendations
Secure password generation
Interactive Streamlit web interface
🛠️ Technologies Used
Python
Streamlit
Python secrets module
Python string module
📂 Project Structure
password-strength-analyzer/
│
├── app.py
├── analyzer.py
├── README.md
└── requirements.txt
app.py
Contains the Streamlit user interface and handles user interaction.

analyzer.py
Contains the password analysis logic and secure password generation functionality.

🔍 Password Analysis
The analyzer checks:

Password length
Lowercase letters
Uppercase letters
Numbers
Special characters
Common passwords
Repeated characters
Predictable sequences
The application calculates a score and classifies the password as:

Very Weak
Weak
Medium
Strong
Very Strong
🔐 Security Considerations
The application does not store or save the password entered by the user.

Password analysis is performed in memory.

The password generator uses Python's secrets module instead of the standard random module because secrets is designed for security-sensitive random values.

The common-password check is based on a local list of commonly used passwords and does not claim to determine whether a password has ever appeared in every known password breach.

🚀 Installation
Clone the repository:

git clone <your-github-repository-url>
Move into the project directory:

cd password-strength-analyzer
Install the required dependencies:

pip install -r requirements.txt
▶️ Running the Application
Run the following command:

streamlit run app.py
The application will open in your browser.

🧪 Testing
The application was tested using passwords with different characteristics, including:

Very short passwords
Common passwords
Passwords without uppercase characters
Passwords without numbers
Passwords without special characters
Passwords containing repeated characters
Passwords containing predictable sequences
Strong randomly generated passwords
All planned test cases produced the expected results.

🎯 Learning Outcomes
Through this project, I practiced:

Python functions
String processing
Conditional logic
Password security concepts
Secure random password generation
Streamlit application development
Software testing
Basic cybersecurity practices
⚠️ Limitations
This project is an educational password-strength analyzer and should not be considered a complete enterprise password-security solution.

The scoring system is a custom project-specific scoring model rather than an industry-standard password-strength measurement.

The common-password detection currently uses a local list and does not represent every compromised password in existence.

🔮 Future Improvements
Possible future enhancements include:

Larger common-password datasets
More advanced password-strength estimation
Password breach checking using privacy-preserving methods
Improved visualizations
More detailed security recommendations
Deployment as a public web application
👨‍💻 Project Type
Cyber Security Internship Project

Project: Password Strength Analyzer

📊 Scoring Model
The project uses a custom 8-point scoring model:

Password length of 8–11 characters: 1 point
Password length of 12 or more characters: 2 points
Lowercase letters: 1 point
Uppercase letters: 1 point
Numbers: 1 point
Special characters: 1 point
Common-password detection can reduce the score
Repeated-character patterns can reduce the score
Predictable sequences can reduce the score
This score is designed for this educational project and is not an industry-standard password-strength measurement.
