from flask import Blueprint, render_template, request, redirect, url_for, send_file
from .models import UserProfile
from .forms import UserProfileForm
from .utils import generate_pdf, generate_recommendations
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        user = UserProfile(
            name=form.name.data,
            age=form.age.data,
            profession=form.profession.data,
            goals=form.goals.data,
            interests=form.interests.data,
            time_frame=form.time_frame.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.recommendations', user_id=user.id))
    return render_template('profile.html', form=form)

@main.route('/recommendations/<int:user_id>')
def recommendations(user_id):
    user = UserProfile.query.get_or_404(user_id)
    recommendations = generate_recommendations(user)
    return render_template('recommendations.html', user=user, recommendations=recommendations)

@main.route('/generate_pdf/<int:user_id>')
def generate_pdf_route(user_id):
    user = UserProfile.query.get_or_404(user_id)
    recommendations = generate_recommendations(user)
    pdf_path = generate_pdf(user, recommendations)
    return send_file(pdf_path, as_attachment=True)
