from flask import Flask, render_template, request, url_for, flash, session, redirect
from flask_bootstrap import Bootstrap
import boto3


app = Flask(__name__)
app.secret_key = "secret_key"
Bootstrap(app)

""" AWS KEY SETUP """
BUCKET = "BUCKET"
s3  = boto3.client('s3',
    aws_access_key_id = 'AWS_ACCESS_KEY_ID',
    aws_secret_access_key = 'AWS_SECRET_ACCESS_KEY')

""" HOME """
@app.route('/')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET)
    summaries = my_bucket.objects.all()
    return render_template('index.html', my_bucket=my_bucket, files=summaries)

""" UPLOAD """
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET)
    my_bucket.Object(file.filename).put(Body=file)

    flash('Upload Successful!')
    return redirect(url_for('files'))

""" DELETE """
@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET)
    my_bucket.Object(key).delete()

    flash('Delete Successful!')
    return redirect(url_for('files'))
