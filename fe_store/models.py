from fe_store import db


class Association(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),
                           primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'),
                             primary_key=True)
    value_id = db.Column(db.Integer, db.ForeignKey('value.id'))
    value = db.relationship("Value")

    product = db.relationship("Product", back_populates="attributes")
    attribute = db.relationship("Attribute", back_populates="products")


class ProductType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    mp_name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return "ProductType('{name}')".format(name=self.name)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False)
    image = db.Column(db.String(512), nullable=False)

    product_type_id = db.Column(
        db.Integer, db.ForeignKey("product_type.id"), nullable=False
    )
    product_type = db.relationship("ProductType")

    attributes = db.relationship('Association',  back_populates="product")

    def __repr__(self):
        return "Product('{name}'".format(name=self.name)


class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False, unique=True)
    measure_id = db.Column(db.Integer, db.ForeignKey("measure.id"))
    measure = db.relationship("Measure")
    products = db.relationship("Association", back_populates="attribute")

    def __repr__(self):
        return "Attribute('{name}'".format(name=self.name)


class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True, default='')

    def __repr__(self):
        return "Measure('{name}'".format(name=self.name)


class Value(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)

    def __repr__(self):
        return "Values('{name}'".format(name=self.name)
