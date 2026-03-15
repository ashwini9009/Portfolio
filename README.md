# Ashwini Rukare Portfolio & Resume

Welcome to my personal portfolio! This repository contains all information about my skills, projects, and contact form, along with instructions to run the portfolio locally.

---

## 👤 About Me

- **Name:** Ashwini Kailas Rukare  
- **Course:** MCA, K.B. Joshi Institute of Information Technology  
- **Email:** rukareashwini@gmail.com  
  

I am passionate about **Java, Spring Boot, Frontend Development (HTML, CSS, Angular), and Databases (MySQL)**. This portfolio demonstrates my work and skills in **web development** and **full-stack projects**.

---

## 💻 Project Overview

This portfolio project includes:

1. **Frontend**  
   - Responsive pages built with HTML, CSS, JavaScript, and Angular.  
   - Hero section, project showcase, and contact form.  
   - Images and static assets stored in `/static/images`.  

2. **Backend**  
   - Flask backend handles contact form submissions.  
   - Saves messages to **MySQL database** and sends email notifications.  
   - Uses Python libraries: `pymysql`, `flask`, `flask-cors`, `smtplib`, `email.message`.  

3. **Database**  
   - MySQL database named `portfolio`  
   - Table `contacts` stores messages: `name`, `email`, `message`.  

---

## Project Structure
portfolio/
├── app.py # Flask backend
├── README.md # Project overview
├── index.html
├── css/ # CSS files
├── js/ # JavaScript files


---

##  Features

- Responsive **portfolio website**  
- Contact form saves messages in **MySQL**  
- Sends **email notifications** when a new message is received  
- Mobile-friendly design  
- Integrated **Flask backend** with frontend  

---

##  Technologies Used

- **Frontend:** HTML, CSS, JavaScript, 
- **Backend:** Python, Flask  
- **Database:** MySQL  
- **Libraries:** PyMySQL, Flask-CORS, EmailMessage (Python)  

---

##  How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/portfolio.git
cd portfolio

Create a .env file (never push your real passwords!):
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
DB_USER=root
DB_PASSWORD=root
DB_NAME=portfolio

Run Flask app:
python app.py
