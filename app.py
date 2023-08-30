from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app_name = os.getenv("APP_NAME")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://db_user:db_password@db_host/db_name'
db = SQLAlchemy(app)
CORS(app)

class Sentences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String(255))
    read = db.Column(db.Integer)
    content = db.Column(db.Integer)
    category = db.Column(db.Integer)

@app.route('/sentences', methods=['POST', 'GET'])
def cr_sentences():
    if request.method == 'POST':
        data = request.json
        new_sentence = Sentences(sentence=data['sentence'], read=data['read'], content=data['content'], category=data['category'])
        db.session.add(new_sentence)
        db.session.commit()
        return jsonify({'message': 'Sentence created successfully'})

    if request.method == 'GET':
        read_no = Sentences.query.filter_by(read=0)
        read_yes = Sentences.query.filter_by(read=1)
        content_no = Sentences.query.filter_by(content=0)
        content_yes = Sentences.query.filter_by(content=1)
        category_no = Sentences.query.filter_by(category=0)
        category_yes = Sentences.query.filter_by(category=1)
        return jsonify({
                'reads':[
                    {'0': [rn.sentence for rn in read_no]},
                    {'1': [ry.sentence for ry in read_yes]}
                ],
                'contents':[
                    {'0': [con.sentence for con in content_no]},
                    {'1': [coy.sentence for coy in content_yes]}
                ],
                'categories':[
                    {'0': [can.sentence for can in category_no]},
                    {'1': [cay.sentence for cay in category_yes]}
                ],})
    
@app.route('/sentences/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def ud_sentences(id):
    sentence = Sentences.query.get(id)
    if request.method == 'GET':
        if sentence:
            return jsonify({'sentence': sentence.sentence, 'read': sentence.read, 'content': sentence.content, 'category': sentence.category })
        else:
            return jsonify({'message': 'Sentence not found'}), 404
    
    if request.method == 'PUT':
        data = request.json
        if sentence:
            sentence.sentence = data['sentence']
            sentence.read = data['read']
            sentence.content = data['content']
            sentence.category = data['category']
            db.session.commit()
            return jsonify({'message': 'Sentence updated successfully'})
        else:
            return jsonify({'message': 'Sentence not found'}), 404
    
    if request.method == 'DELETE':
        if sentence:
            db.session.delete(sentence)
            db.session.commit()
            return jsonify({'message': 'Sentence deleted successfully'})
        else:
            return jsonify({'message': 'Sentence not found'}), 404

@app.route('/')
def hello():
    return "API Server " + app_name

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
