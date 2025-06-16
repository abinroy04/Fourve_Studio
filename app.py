#Fourve Studio Flask Application - Abin Roy
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key-for-flashing')

@app.route('/')
def home():
    return render_template('index.html', port_filter=port_filter)

@app.route('/team')
def team():
    return render_template('team.html', team_members=team_members)

@app.route('/service/livestreaming')
def livestreaming():
    return render_template('service/livestreaming.html')

@app.route('/service/media-production')
def media_production():
    return render_template('service/media-production.html')

@app.route('/service/digital-marketing')    
def digital_marketing():
    return render_template('service/digital-marketing.html')

@app.route('/service/event-management')
def event_management():
    return render_template('service/event-management.html')

@app.route('/fourve-e-sports')
def e_sports():
    return render_template('esports.html')



# Index page things
    #portfolio pages sorting
port_filter = {
    "photograhy": 
    [
        "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/misc-square-5.webp?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pbWFnZXMvbWlzYy1zcXVhcmUtNS53ZWJwIiwiaWF0IjoxNzQ5NDY2MDQ4LCJleHAiOjE3ODEwMDIwNDh9.f4E0ugE2eY7CAuG-Xa9_RVEL8HGK3l0GC0xgVuUP_Aw",
        "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/misc-square-16.webp?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvbWlzYy1zcXVhcmUtMTYud2VicCIsImlhdCI6MTc0OTQ2NDY2NywiZXhwIjoxNzgxMDAwNjY3fQ.Hc7Q4Ci6jR6xDSqrMzApWLBieugKVIP4b57mb-_eLJI"
    ],
    "videography":
    [
        "https://www.instagram.com/p/C6y0NHYSLVQ/",
        "https://www.instagram.com/p/C_YYqc-SeI8/",
        "https://drive.google.com/file/d/1Rtzpx2axoRKfm32Se6uzSKZU5lUxfC5R/preview"
    ],
    "live_streaming":
    [
        "https://www.youtube.com/watch?v=iOgc_cjoILk&t=2s"
    ]
}

# Team page things
team_members = [
    {
        "name": "Alen T Koshy",
        "role": "Cheif Executive Officer",
        "image": "img/team/Alen_T_Koshy.webp",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec.",
        "instagram": "https://www.instagram.com/alen.tkoshy/",
        "linkedin": "https://www.linkedin.com/in/alen-t-koshy-71535821b/"
    },
    {
        "name": "Danie Joseph Augustine",
        "role": "Chief Financial Officer",
        "image": "img/team/Danie.webp",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec.",
        "instagram": "https://www.instagram.com/dani.e_j/",
        "linkedin": "https://www.linkedin.com/in/alen-t-koshy-71535821b/"
    },
    {
        "name": "Shalom Saji John",
        "role": "Chief Marketing Officer",
        "image": "img/team/Shalom.webp",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec.",
        "instagram": "https://www.instagram.com/shalomsjohn/",
        "linkedin": "https://www.linkedin.com/in/shalom-saji-john-4a9691275/"
    },
    {
        "name": "Cyril Luke Anish",
        "role": "Chief Content Officer",
        "image": "img/team/Cyril.webp",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec.",
        "instagram": "https://www.instagram.com/ft._cyril/",
        "linkedin": "https://www.linkedin.com/in/cyril-luke-anish-089819271/"
    },
    {
        "name": "Abin Roy",
        "role": "Lead Developer",
        "image": "img/team/AbinR.webp",
        "description": "Dedicated Developer with experience in full-stack development, API integration, and database design. Passionate about creating impactful digital solutions.",
        "instagram": "https://www.instagram.com/alen.tkoshy/",
        "linkedin": "https://www.linkedin.com/in/abin-roy-750783293/"
    },
    {
        "name": "Designer Chechi",
        "role": "Lead Designer",
        "image": "img/team/chechi.webp",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec.",
        "instagram": "https://www.instagram.com/alen.tkoshy/",
        "linkedin": "https://www.linkedin.com/in/alen-t-koshy-71535821b/"
    }
]

# Contact form handling
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        sender_email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Validate form data
        if not all([name, sender_email, subject, message]):
            return jsonify({
                'success': False,
                'message': 'All fields are required!'
            })
        
        try:
            receiver_email = os.environ.get('EMAIL_ID')
            sender_account_email = os.environ.get('EMAIL_ID')
            sender_account_password = os.environ.get('APP_PASSWORD')
            
            # Check if credentials exist
            if not all([receiver_email, sender_account_email, sender_account_password]):
                print("Email credentials not found in environment variables")
                return jsonify({
                    'success': False,
                    'message': 'Server configuration error. Please try again later.'
                })
            
            # Create email message
            email_message = f"""
            Name: {name}
            Email: {sender_email}
            Subject: {subject}
            
            Message:
            {message}
            """
            
            msg = MIMEText(email_message)
            msg['Subject'] = f'New Contact Form: {subject}'
            msg['From'] = sender_account_email
            msg['To'] = receiver_email
            msg['Reply-To'] = sender_email
            
            # Send email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_account_email, sender_account_password)
                server.send_message(msg)
            
            response = jsonify({
                'success': True,
                'message': 'Thank you for contacting us! We will get back to you soon.'
            })
            # Set content type explicitly for AJAX requests
            response.headers['Content-Type'] = 'application/json'
            return response
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return jsonify({
                'success': False,
                'message': 'We are unable to receive your message at the moment. Please try contacting us via phone.'
            })


if __name__ == '__main__':
    app.run(debug=False)
