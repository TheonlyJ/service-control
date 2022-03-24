from app import views


def setup(app):
    app.router.add_get('/', views.mainpage)
    app.router.add_get('/start', views.start_button)
    app.router.add_get('/stop', views.stop_button)
    app.router.add_get('/restart', views.restart_button)
    app.router.add_get('/status', views.status_button)
    app.router.add_get('/checkbox', views.checkbox_status)
    app.router.add_get('/checkbox_save', views.checkbox_save)
