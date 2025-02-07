"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
from cgi import print_exception
import os
from app import app,form,db
from flask import render_template, request, redirect, url_for,flash
from .form import PropertyForm
from .models import Properties_db
from flask_migrate import Migrate
from werkzeug.utils import secure_filename


migrate = Migrate(app, db)
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET','POST'])
def create():
    """Render the properties create page."""
    myform = PropertyForm()
    if request.method == "POST" and myform.validate_on_submit():
        property_name = request.form['property_name']
        description = request.form['description']
        rooms_num = request.form['rooms_num']
        bathrooms_num = request.form['bathrooms_num']
        price = request.form['price']
        property_type = request.form['property_type']
        location = request.form['location']
        photo = request.files['photo']
        filename=secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        property_form = Properties_db(property_name,description,rooms_num,bathrooms_num,price,property_type,location,'/uploads/'+filename)
        db.session.add(property_form)
        db.session.commit()
        return redirect('/properties')
    return render_template('create.html', form=myform)

@app.route('/properties')
def properties():
    """Render the list of properties"""
    properti = Properties_db.query.all()
    return render_template('properties.html',propertis=properti)

@app.route('/properties/<propertyid>')
def property_desisplay(propertyid):
    property_dis = Properties_db.query.get(propertyid)
    if property_dis is not None:
        title = property_dis.property_name
        description = property_dis.description
        rooms_num = property_dis.rooms_num
        bathroom_num = property_dis.bathrooms_num
        price = property_dis.price
        property_type = property_dis.property_type
        location = property_dis.location
        photo = property_dis.photo
        return render_template('property.html',property_name=title,description=description,rooms_num=rooms_num,bathrooms_num=bathroom_num,price=price,property_type=property_type,location=location,photo=photo)
    flash("No property found")
    return render_template('404.html')
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
