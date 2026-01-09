"""
Part 3: Jinja2 Variables - Passing Data from Python to HTML
============================================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    student_name = "Shraddha"
    return render_template('index.html', name=student_name)  # Pass variable to template as {{ name }}


@app.route('/profile')
def profile():
    user_data = {
        'name': 'Shraddha',
        'age': 20,
        'course': 'Deep Learning',
        'email': 'shraddha24surwade@gmail.com',
        'city': 'Nashik',
        'is_enrolled': True
    }
    return render_template('profile.html',  # Pass multiple variables to template
                           name=user_data['name'],
                           age=user_data['age'],
                           course=user_data['course'],
                           email=user_data['email'],
                           city=user_data['city'],
                           is_enrolled=user_data['is_enrolled'])


@app.route('/skills')
def skills():
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']
    return render_template('skills.html', skills=programming_skills)  # Pass list to loop through in template


@app.route('/projects')
def projects():
    project_list = [  # List of dictionaries - common pattern for database-like data
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript'},
    ]
    return render_template('projects.html', projects=project_list)

@app.route('/grades')
def grades():
    grade_list = [
        {'subject':'Mathematics-3','grade':'O'},
        {'subject':'Data Structures','grade':'O'},
        {'subject':'Software Engineering','grade':'A+'},
        {'subject':'Microprocessor','grade':'O'},
        {'subject':'Principles of Programming Lang','grade':'A'}
    ]
    return render_template('grades.html', grades=grade_list)

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# JINJA2 SYNTAX QUICK REFERENCE:
# =============================================================================
#
# {{ variable }}          - Output a variable
# {{ variable|upper }}    - Use a filter (uppercase)
# {{ variable|default('N/A') }} - Default value if variable is empty
#
# {% if condition %}      - If statement
#   ...
# {% endif %}
#
# {% for item in list %}  - For loop
#   {{ item }}
# {% endfor %}
#
# =============================================================================