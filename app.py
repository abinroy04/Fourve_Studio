#Fourve Studio Flask Application - Abin Roy
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from supabase import create_client
from datetime import datetime
from werkzeug.utils import secure_filename

load_dotenv()

# Ensure static directories exist
img_dir = os.path.join(os.path.dirname(__file__), 'static', 'img')
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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
    response_games = supabase.table('Games').select('*').execute()
    games = response_games.data

    response_tournaments = supabase.table('Tournaments').select('*').execute()
    tournaments = response_tournaments.data

    response_scrims = supabase.table('Scrims').select('*').execute()
    scrims = response_scrims.data
    return render_template('esports/esports.html', games=games, tournaments=tournaments, scrims=scrims)


# Index page things
    #portfolio pages sorting
port_filter = {
    "photograhy": 
    [
        "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/misc-square-5.webp?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvbWlzYy1zcXVhcmUtNS53ZWJwIiwiaWF0IjoxNzQ5NDY2MDQ4LCJleHAiOjE3ODEwMDIwNDh9.f4E0ugE2eY7CAuG-Xa9_RVEL8HGK3l0GC0xgVuUP_Aw",
        "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/misc-square-16.webp?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvbWlzYy1zcXVhcmUtMTYud2VicCIsImlhdCI6MTc0OTQ2NDY2NywiZXhwIjoxNzgxMDAwNjY3fQ.Hc7Q4Ci6jR6xDSqrMzApWLBieugKVIP4b57mb-_eLJI",
        {
            "title": "Save The Date",
            "images": 
            [
                "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/temp.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvdGVtcC5wbmciLCJpYXQiOjE3NTAwNzM1MTksImV4cCI6MTc1MDY3ODMxOX0.1tRMEhVcy8nLcky2DudzXBoQKIUAB6PdHken3qdz85s",
                "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/tempo.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvdGVtcG8ucG5nIiwiaWF0IjoxNzUwMDczNTMyLCJleHAiOjE3NTA2NzgzMzJ9.UZCL3VFVmVPYEDyfzwpsfeV8mcVqJ1r1u4rSWDE2Tiw",
                "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/temp%20again.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvdGVtcCBhZ2Fpbi5wbmciLCJpYXQiOjE3NTAwNzM1NTMsImV4cCI6MTc1MDY3ODM1M30.t8bgSxs4BEDOEKOAtBis_LY2HS8ql7oZ0ma7Nrt2fDE",
                "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/temp%20again%20huh.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvdGVtcCBhZ2FpbiBodWgucG5nIiwiaWF0IjoxNzUwMDczNTYxLCJleHAiOjE3NTA2NzgzNjF9.793UQ2NSf1sq-R5F6xfiaVoQczqgPnfVJ3c6ErVqSgw"
            ]
        }
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
    ],
    "digital_marketing":
    [
        "https://mviuygatbuhwminrfoik.supabase.co/storage/v1/object/sign/potfolio-images/Rewago.png?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV8xYjc1Y2QzMy0wOTJkLTRhMTgtOGMzMi00NzhkZTA3ZGYxYzMiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJwb3Rmb2xpby1pb3Rmb2xpby1pbWFnZXMvUmV3YWdvLnBuZyIsImlhdCI6MTc1MDA3MTg4NSwiZXhwIjoyMDY1NDMxODg1fQ.Ur3vNlz4fU2UD0eaoNgtIHNHVZXsFBCpJFuVS7XYsWI"
    ],
}

# Team page things
team_members = [
    {
        "name": "Alen T Koshy",
        "role": "Cheif Executive Officer",
        "image": "img/team/Alen_T_Koshy.webp",
        "description": "Team lead at Fourve, blending digital marketing, video editing, drones, esports, and storytelling with impact.",
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
        "description": "Shaping business strategies, building strong client relationships, and unlocking new market opportunities to ensure continuous growth and competitive advantage.",
        "instagram": "https://www.instagram.com/shalomsjohn/",
        "linkedin": "https://www.linkedin.com/in/shalom-saji-john-4a9691275/"
    },
    {
        "name": "Cyril Luke Anish",
        "role": "Chief Content Officer",
        "image": "img/team/Cyril.webp",
        "description": "I'm a graphic designer, cameraman, and editor who loves turning moments into meaningful visuals. At Fourve, I focus on clean, detailed storytelling that brings out the soul in every frame.",
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

#Esports page things
@app.route('/fourve-e-sports/game/<game_id>')
def game_detail(game_id):
    try:
        # Fetch specific game by ID
        response = supabase.table('Games').select('*').eq('Game-id', game_id).execute()
        
        if not response.data:
            # Game not found
            flash('Game not found', 'error')
            return redirect(url_for('e_sports'))
            
        game = response.data[0]
        print(f"Game found: {game['Game']}")
          
        # Fetch tournaments for this game
        tournaments_response = supabase.table('Tournaments').select('*').eq('Game-id', game_id).execute()
        tournaments = tournaments_response.data
        print(f"Found {len(tournaments)} tournaments")
        
        # Fetch scrims for this game
        scrims_response = supabase.table('Scrims').select('*').eq('Game-id', game_id).execute()
        scrims = scrims_response.data
        print(f"Found {len(scrims)} scrims")
        
        # Debug: Check if each tournament has Tournament-id
        for i, tournament in enumerate(tournaments):
            print(f"Tournament {i}: has Tournament-id: {'Tournament-id' in tournament}")
            
        # Debug: Check if each scrim has Scrims-id
        for i, scrim in enumerate(scrims):
            print(f"Scrim {i}: has Scrims-id: {'Scrims-id' in scrim}")
        
        return render_template('esports/game_detail.html', 
                              game=game,
                              tournaments=tournaments,
                              scrims=scrims)
    except Exception as e:
        import traceback
        print(f"Error fetching game details: {e}")
        print(traceback.format_exc())  # Print full stack trace
        flash('Error loading game details', 'error')
        return redirect(url_for('e_sports'))


@app.route('/register/<registration_type>/<int:id>')
def register(registration_type, id):
    try:
        if registration_type not in ['tournament', 'scrim']:
            flash('Invalid registration type', 'error')
            return redirect(url_for('e_sports'))
        
        # Get game_id based on the tournament or scrim
        if registration_type == 'tournament':
            # Get tournament data, including game info
            response = supabase.table('Tournaments').select('*,Games:Game-id(Game)').execute()
            print(f"Looking for tournament with id {id}")
            
            # Find the tournament with matching id
            matching_items = []
            for item in response.data:
                tournament_id = item.get('Tournament-id') 
                if tournament_id and str(tournament_id) == str(id):
                    matching_items.append(item)
            
            if not matching_items:
                flash(f'Tournament with ID {id} not found', 'error')
                return redirect(url_for('e_sports'))                
            item = matching_items[0]
            game_id = item['Game-id']
            game_name = item['Games']['Game']
            item_name = item['name']
            item_fee = item.get('entry_fee', 0)
            
            return render_template('esports/e_registration.html',
                                registration_type=registration_type,
                                game_id=game_id,
                                game_name=game_name,
                                tournament_id=id,
                                tournament_name=item_name,
                                tournament_fee=item_fee)
        else:
            # Handle scrim registration
            response = supabase.table('Scrims').select('*,Games:Game-id(Game)').execute()
            print(f"Looking for scrim with id {id}")
            
            # Find the scrim with matching id
            matching_items = []
            for item in response.data:
                scrim_id = item.get('Scrims-id')
                if scrim_id and str(scrim_id) == str(id):
                    matching_items.append(item)
            
            if not matching_items:
                flash(f'Scrim with ID {id} not found', 'error')
                return redirect(url_for('e_sports'))
                
            item = matching_items[0]
            game_id = item['Game-id']
            game_name = item['Games']['Game']
            item_title = item['title']
            item_fee = item.get('fee', 0)
            
            return render_template('esports/e_registration.html',
                                registration_type=registration_type,
                                game_id=game_id,
                                game_name=game_name,
                                scrim_id=id,
                                scrim_title=item_title,
                                scrim_fee=item_fee)
                                
    except Exception as e:
        print(f"Error loading registration page: {e}")
        flash('Error loading registration page', 'error')
        return redirect(url_for('e_sports'))

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    if request.method != 'POST':
        return jsonify({'success': False, 'message': 'Invalid request method'})
        
    try:
        # Get form data
        registration_type = request.form.get('registration_type')
        game_id = request.form.get('game_id')
        
        # Basic player info
        player_name = request.form.get('player_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        game_handle = request.form.get('game_handle')
        
        # Check if payment proof file exists
        if 'payment_proof' not in request.files:
            return jsonify({'success': False, 'message': 'Payment proof is required'})
            
        payment_file = request.files['payment_proof']
        if not payment_file or payment_file.filename == '':
            return jsonify({'success': False, 'message': 'No payment proof selected'})
        
        # Check file extension
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if not payment_file.filename.split('.')[-1].lower() in allowed_extensions:
            return jsonify({'success': False, 'message': 'Only image files are allowed for payment proof'})
            
        # Upload payment proof to Supabase storage
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"payment_{registration_type}_{timestamp}_{secure_filename(payment_file.filename)}"
        storage_path = f"payment_proofs/{filename}"
        
        # Read file content and upload to Supabase storage
        file_content = payment_file.read()
        supabase.storage.from_('esports').upload(storage_path, file_content)
          # Get payment proof URL
        payment_proof_url = supabase.storage.from_('esports').get_public_url(storage_path)
        
        # Prepare data for database based on actual table schema
        registration_data = {
            'Game-id': game_id,
            'Player-name': player_name,
            'Email': email,
            'Game-handle': game_handle,
            'Payment-proof': payment_proof_url,  # Store as varchar
            'Reg-date': datetime.now().isoformat()
        }
        
        # Add tournament/scrim specific data
        if registration_type == 'tournament':
            tournament_id = request.form.get('tournament_id')
            team_name = request.form.get('team_name')
            
            # Team members
            members = []
            for i in range(1, 4):  # 3 additional members
                member = {
                    'name': request.form.get(f'member{i}_name'),
                    'handle': request.form.get(f'member{i}_handle')
                }
                members.append(member)
                
            # Substitutes (optional)
            substitutes = []
            for i in range(1, 3):  # 2 substitutes
                sub_name = request.form.get(f'sub{i}_name')
                sub_handle = request.form.get(f'sub{i}_handle')
                
                if sub_name and sub_handle:
                    substitutes.append({
                        'name': sub_name,
                        'handle': sub_handle
                    })
              # Update registration data with tournament specific fields using correct column names
            registration_data.update({
                'Tournament-id': tournament_id,
                'Team-name': team_name,
                'Team-members': members,            # Already in JSON format
                'Substitures': substitutes         # Note: "Substitures" matches your schema (not "Substitutes")
            })
              # Insert into Tournament_Registrations table
            supabase.table('Tournament_Registrations').insert(registration_data).execute()
            
        elif registration_type == 'scrim':
            scrim_id = request.form.get('scrim_id')
            registration_data['Scrim-id'] = scrim_id
            
            # Insert into Scrim_Registrations table
            supabase.table('Scrim_Registrations').insert(registration_data).execute()
        
        # Send email notification to admin
        try:
            receiver_email = os.environ.get('EMAIL_ID')
            sender_account_email = os.environ.get('EMAIL_ID')
            sender_account_password = os.environ.get('APP_PASSWORD')
            
            subject = f"New {registration_type.capitalize()} Registration"
            
            # Customize email body based on registration type
            if registration_type == 'tournament':
                body = f"""
                New Tournament Registration:
                
                Player: {player_name}
                Email: {email}
                Phone: {phone}
                Game Handle: {game_handle}
                Team Name: {team_name}
                
                Registration needs to be verified in the admin dashboard.
                """
            else:
                body = f"""
                New Scrim Registration:
                
                Player: {player_name}
                Email: {email}
                Phone: {phone}
                Game Handle: {game_handle}
                
                Registration needs to be verified in the admin dashboard.
                """
                
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender_account_email
            msg['To'] = receiver_email
            
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_account_email, sender_account_password)
                server.send_message(msg)
        except Exception as e:
            print(f"Email notification failed: {e}")
            # Continue with success response even if email fails
            
        return jsonify({
            'success': True,
            'message': 'Registration submitted successfully! We will verify your payment and confirm your registration.'
        })
            
    except Exception as e:
        print(f"Error processing registration: {e}")
        return jsonify({
            'success': False,
            'message': 'An error occurred while processing your registration. Please try again.'
        })


if __name__ == '__main__':
    app.run(debug=False)
