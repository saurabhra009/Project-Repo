from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, URLField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, Email

class ItemForm(FlaskForm): #SP2943 December 15, 2022
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("description", validators=[DataRequired()])
    category = TextAreaField("category", validators=[DataRequired()])
    stock = IntegerField("stock", validators=[NumberRange(min=0)])
    unit_price = IntegerField("unit_price", validators=[NumberRange(min=0)])
    image = URLField("image", validators=[Optional()])
    visibility = BooleanField("visibility")
    submit = SubmitField("Save")

class PaymentForm(FlaskForm): #SP2943 December 15, 2022
    id = HiddenField("id", validators=[Optional()])
    username = StringField("username", validators=[DataRequired(), Length(2, 30)])
    email = EmailField("email", validators=[DataRequired(), Email()])
    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("last_name", validators=[DataRequired()])
    address = TextAreaField("address", validators=[DataRequired()])
    apartment = IntegerField("apartment", validators=[DataRequired()])
    city = StringField("city", validators=[DataRequired()])
    state = StringField("state", validators=[DataRequired()])
    country = StringField("country", validators=[DataRequired()])
    zipcode = IntegerField("zipcode", validators=[DataRequired(), Length(5)])
    payment_method = TextAreaField("payment_method", validators=[DataRequired()])
    total_amount = IntegerField("total_amount", validators=[DataRequired()])
    submit = SubmitField("Save")