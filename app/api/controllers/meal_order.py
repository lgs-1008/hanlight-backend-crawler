import datetime

from flask import Blueprint, jsonify

from app import db
from app.api.models.meal import MealModel
from app.api.models.meal_order import FeedOrderModel


meal_order = Blueprint('meal_order', __name__, url_prefix='/meal-order/')


@meal_order.route('/update/')
def update_meal_order():
    today = datetime.datetime.now()

    if MealModel.get_lunch(month=today.month, date=today.day):
        feed_order = FeedOrderModel.latest_feed_order()
        if feed_order.count >= 5:
            FeedOrderModel.add_feed_order(order="게임-유센-해킹", count=1)
        else:
            feed_order.count += 1
        db.session.commit()

    return "meal_order_update"


@meal_order.route('/get/')
def get_meal_order():
    return jsonify({
        "success": True,
        "data": {
            "feed_order": FeedOrderModel.latest_feed_order().order
        }
    })