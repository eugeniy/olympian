from olympian import create_app

app = create_app()
app.run(app.config['HOST'])
