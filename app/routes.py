from app import views


def setup(app):
    app.router.add_get('/', views.mainpage)
