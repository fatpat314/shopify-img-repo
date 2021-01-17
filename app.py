from flask import Flask, render_template, request, url_for, flash
from flask_bootstrap import Bootstrap
import boto3


app = Flask(__name__)
Bootstrap(app)


BUCKET = "BUCKET_NAME"
s3  = boto3.client('s3',
    aws_access_key_id = 'AWS_ACCESS_KEY_ID',
    aws_secret_access_key = 'AWS_SECRET_ACCESS_KEY')

@app.route('/')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET)
    summaries = my_bucket.objects.all()
    # contents = list_files("shopify-img-repo")
    return render_template('index.html', my_bucket=my_bucket, files=summaries)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET)
    my_bucket.Object(file.filename).put(Body=file)

    flash('Upload Successful!')
    return redirect(url_for('files'))

@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET)
    my_bucket.Object(keu).delete()

    flash('Delete Successful!')
    return redirect(url_for('files'))
