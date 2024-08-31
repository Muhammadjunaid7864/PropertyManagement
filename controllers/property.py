from flask import request, redirect, render_template, url_for

def properties():
    return render_template('property.html')
