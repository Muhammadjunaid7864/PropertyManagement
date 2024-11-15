import os
from flask import request, redirect, render_template, url_for, jsonify
from werkzeug.utils import secure_filename
from utilities.config import Config
from models.property import Property
from models.user import User
from app import db

# Ensure the instance folder exists
Config.ensure_instance_folder()

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def properties():
    if request.method == 'POST':
        # Get form data
        property_id = request.form.get('property_id')
        property_name = request.form.get('property_name')
        description = request.form.get('description')
        location = request.form.get('location')
        property_type = request.form.get('property_type')
        status = request.form.get('status')
        beds = request.form.get('beds')
        baths = request.form.get('baths')
        user_id = request.form.get('user_id')  # Get the selected user's ID

        # Handle file uploads
        image_paths = []
        if 'images[]' in request.files:
            files = request.files.getlist('images[]')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
                    file.save(file_path)
                    image_paths.append(file_path)  # Store the path to save to the database

        # Save property to the database
        new_property = Property(
            property_id = property_id,
            name=property_name,
            description=description,
            image_paths=",".join(image_paths),  # Join paths with a comma
            location = location,
            property_type= property_type,
            status = status,
            beds = beds,
            baths = baths,
            user_id=user_id  # Assign the property to the selected user
        )
        db.session.add(new_property)
        db.session.commit()

        # Respond with the newly created property to update the UI
        return jsonify({
        'status': 'success',
        'id': new_property.id,
        'name': new_property.name,
        'description': new_property.description,
        'images': image_paths,
        'message': 'Property added successfully!',
        'redirect_url': url_for('app_bp.properties')
    }), 200

    # Fetch all users for the dropdown
    users = User.query.all()

    # Fetch all properties
    properties = Property.query.all()

    return render_template('property.html', properties=properties, users=users)


# propert Details

def property_detail(property_id):
    property = Property.query.get_or_404(property_id)
    return render_template('property_detail.html', property=property)

# Delete Property

def delete_property():
    data = request.get_json()
    property_id = data.get('id')
    property = Property.query.get(property_id)

    if property:
        db.session.delete(property)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Property deleted successfully!','redirect_url': url_for('app_bp.properties')}),200
    else:
        return jsonify({'status': 'error', 'message': 'Property not found.'}), 404
    

def get_property(property_id):
    property = Property.query.get(property_id)

    if property is None:
        return jsonify({'status': 'error', 'message': 'Property not found'}), 404

    # Split the image paths for returning them as an array
    image_paths = property.image_paths.split(',')

    # Prepare the data to send back to the client
    property_data = {
        'property_id': property.property_id,
        'name': property.name,
        'description': property.description,
        'assigned_user': property.owner.id,  # Assuming 'owner' is a foreign key to the User model
        'image_paths': image_paths,
        'location': property.location,
        'property_type': property.property_type,
        'status': property.status,
        'beds': property.beds,
        'baths': property.baths,
    }

    return jsonify({'status': 'success', 'property': property_data})