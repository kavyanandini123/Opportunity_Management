from flask import request, jsonify
from app import app
from models import db, Opportunity
from flask_login import login_required, current_user

# =========================
# ✅ CREATE OPPORTUNITY
# =========================
@app.route('/opportunities', methods=['POST'])
def create_opportunity():
    data = request.json

    print("Opportunity data:", data)

    try:
        new_op = Opportunity(
            name=data.get('name'),
            duration=data.get('duration'),
            start_date=data.get('start_date'),
            description=data.get('description'),
            skills=data.get('skills'),
            category=data.get('category'),
            future_opportunities=data.get('future_opportunities'),
            max_applicants=data.get('max_applicants'),
            admin_id=1  # temporary (since login session not used)
        )

        db.session.add(new_op)
        db.session.commit()

        return jsonify({"message": "Opportunity created successfully"}), 201

    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to create opportunity"}), 500


# =========================
# ✅ GET ALL OPPORTUNITIES
# =========================
@app.route('/opportunities', methods=['GET'])
def get_opportunities():
    ops = Opportunity.query.all()

    return jsonify([
    {
        "id": op.id,
        "name": op.name,
        "duration": op.duration,
        "start_date": op.start_date,
        "description": op.description,
        "skills": op.skills,
        "category": op.category,
        "future_opportunities": op.future_opportunities,
        "max_applicants": op.max_applicants
    } for op in ops
])

@app.route('/opportunities/<int:id>', methods=['DELETE'])
def delete_opportunity(id):
    op = Opportunity.query.get(id)

    db.session.delete(op)
    db.session.commit()

    return jsonify({"message": "Deleted"})

@app.route('/opportunities/<int:id>', methods=['PUT'])
def update_opportunity(id):
    op = Opportunity.query.get(id)

    data = request.json

    op.name = data.get('name')
    op.duration = data.get('duration')
    op.start_date = data.get('start_date')
    op.description = data.get('description')
    op.skills = data.get('skills')
    op.category = data.get('category')
    op.future_opportunities = data.get('future_opportunities')
    op.max_applicants = data.get('max_applicants')

    db.session.commit()

    return jsonify({"message": "Updated"})