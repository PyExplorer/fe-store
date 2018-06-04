from flask import render_template
from fe_store import app
from fe_store.models import Product


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home page")


@app.route("/products")
def products_list():
    return render_template(
        "products.html",
        products=Product.query.all(),
        title="Products list"
    )


@app.route("/products/<int:product_id>")
def product(product_id):
    return render_template(
        "product.html",
        product=Product.query.filter_by(id=product_id).first_or_404(),
        title="product {}".format(product_id)
    )
