# Animal Info Web Generator 🐾

This project is a simple web generator that fetches animal data from an external API and displays the information in a clean HTML layout.

## 🔍 What is it about?

The application allows users to enter the name of an animal and fetch detailed information about it (such as diet, habitat, and type) using the [API Ninjas Animals API](https://api-ninjas.com/api/animals). It’s perfect for learning purposes or small educational projects about animals.

## 🎯 Problem it Solves

It simplifies the process of looking up and displaying structured animal data without needing to manually browse databases or APIs. It’s ideal for students, educators, or anyone curious about animal facts.

## 👥 Intended Audience

- Programming beginners  
- Educators and students  
- Anyone interested in animal data

---

## 🚀 How to Use

1. **Install the requirements:**

   ```bash
   pip install -r requirements.txt
   

2. Create a .env file in the project root and add your API key:
    API_KEY=your_api_key_here


3. Run the script:
    -Mac/Linux user
    python3 animals_web_generator.py

    - Windows user
    python animals_web_generator.py


4. Enter the name of the animal you want to search (e.g., lion).


5. Open the generatet animals.html file from the statig/ folder in your browser.


Example:

Enter an animal: elephant

Then open static/animals.html in your browser to view the information.

If the animal not found you'll see a message like:

The animal "xyz" doesn't exist!

