# Om Dhakal — Personal Portfolio

A personal developer portfolio built with **Python and Django** to showcase my background, technical skills, education, projects, and contact information.

The portfolio demonstrates Django fundamentals, database-driven content, form handling, static-file management, and production deployment with Render.

## Live Demo

**[Visit Portfolio](https://omdhakal.onrender.com/)**

## Features

- Personal home and introduction section
- About section with developer profile and experience
- Database-driven skills, education, experience, projects, services, testimonials, and social links
- Resume section
- Project showcase with images and external project URLs
- Contact form with server-side Django validation
- Contact messages stored in the database
- Bootstrap-based frontend
- Static-file management with Django and WhiteNoise
- Production deployment on Render
- Environment-based Django secret key configuration

## Tech Stack

| Category | Technology |
| --- | --- |
| Backend | Python, Django 6.1 |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Database | SQLite |
| Forms | Django Forms / ModelForms |
| Static Files | Django Static Files, WhiteNoise |
| Image Handling | Pillow |
| Web Server | Gunicorn |
| Deployment | Render |
| Version Control | Git, GitHub |

## Project Structure

```text
mywebsite/
├── Blog/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── Home/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
├── staticfiles/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Database-Driven Content

The portfolio uses Django models to manage content instead of hard-coding everything into the page.

Current models include:

- `ContactMessage` — stores contact-form submissions
- `Skill` — stores skills and percentage values
- `Experience` — stores professional experience
- `Education` — stores education history
- `Project` — stores project details, images, and project URLs
- `Service` — stores services
- `Testimonial` — stores testimonials
- `SocialLink` — stores social/profile links

## Contact Form

The contact section uses a Django `ModelForm` connected to the `ContactMessage` model. Submitted data is validated before being saved to the database.

The form includes:

- Name
- Email
- Subject
- Message
- CSRF protection

## Deployment

The project is configured for production deployment with:

- **Gunicorn** as the WSGI server
- **WhiteNoise** for static-file serving
- **Render** for hosting
- Environment variables for the Django `SECRET_KEY`

Production dependencies are maintained in `requirements.txt`.

## Local Development

Clone the repository:

```bash
git clone https://github.com/OmDhakal/mywebsite.git
cd mywebsite
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set the Django secret key:

```bash
export SECRET_KEY="your-secret-key"
```

Run migrations:

```bash
python manage.py migrate
```

Collect static files:

```bash
python manage.py collectstatic
```

Start the development server:

```bash
python manage.py runserver
```

For a production-style local run:

```bash
gunicorn Blog.wsgi:application
```

## What I Practiced

- Django project and app structure
- Django models and database design
- ModelForms and server-side validation
- CSRF-protected form handling
- Django templates
- Static-file configuration
- WhiteNoise production configuration
- Gunicorn deployment
- Environment-variable configuration
- Git and GitHub workflow
- Deploying a Django application to Render

## Links

- **GitHub:** https://github.com/OmDhakal/mywebsite
- **Live Portfolio:** https://omdhakal.onrender.com/

## Credits

The frontend is based on a BootstrapMade template and has been integrated and customized for this Django portfolio project.
