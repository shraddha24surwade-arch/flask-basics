"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Shraddha',
    'title': 'Computer Engineer | Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'shraddha24surwade@gmail.com',
    'github': 'https://github.com/shraddha24surwade-arch',
    'linkedin': 'https://linkedin.com/in/shraddha-surwade-b70ab3316',
}

SKILLS = [
    {'name': 'C & C++', 'level': 90},
    {'name': 'Python', 'level': 80},
    {'name': 'HTML', 'level': 75},
    {'name': 'CSS','level':75},
    {'name': 'Java', 'level': 70},
    {'name': 'SQL', 'level': 65},
    {'name': 'Flask', 'level': 60},
]

PROJECTS = [
    {'id': 1, 'name': 'Hospital Management System', 'description': 'A system designed to manage the hospital activities.', 'tech': ['Java','HTML','AWT'], 'status': 'Completed'},
    {'id': 2, 'name': 'Portfolio Website', 'description': 'A Portfolio website describing my education, skills, projects, etc.', 'tech': ['HTML', 'CSS', 'Bootstrap'], 'status': 'Completed'},
    {'id': 3, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'In Progress'},
    {'id': 4, 'name': 'Todo App', 'description': 'A simple application for task management.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 5, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
]

BLOG_POSTS = [
    {
        'id': 1,
        'title': 'My Flask Learning Journey',
        'date': '07 Jan 2026',
        'content': 'I started learning Flask to build dynamic web applications using Python.'
    },
    {
        'id': 2,
        'title': 'Why I Love Python',
        'date': '05 Jan 2026',
        'content': 'Python is simple, powerful, and perfect for beginners as well as professionals.'
    },
    {
        'id': 3,
        'title': 'Building My First Personal Website',
        'date': '02 Jan 2026',
        'content': 'This website helped me understand routing, templates, and Flask structure.'
    }
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/blog')
def blog():
    return render_template(
        'blog.html',
        info=PERSONAL_INFO,
        blogs=BLOG_POSTS
    )


@app.route('/skill/<skill_name>')
def skill_detail(skill_name):
    matched_projects = []

    for project in PROJECTS:
        # check skill inside project tech list (case-insensitive)
        for tech in project['tech']:
            if skill_name.lower() in tech.lower():
                matched_projects.append(project)
                break

    return render_template(
        'skill.html',
        info=PERSONAL_INFO,
        skill_name=skill_name,
        projects=matched_projects
    )


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================
