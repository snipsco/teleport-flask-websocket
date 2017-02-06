from flask import render_template

def routes_with_app(app):
    INDEX_HTML_NAME = '_index.html' if app.config['TYPE'] == 'localhost' else '_index_prod.html'

    context = {
        "SITE_NAME": app.config["SITE_NAME"],
        "teleport": app.config["teleport"],
        "URL": app.config["URL"]
    }

    @app.route('/')
    def get_home():
    	return render_template(INDEX_HTML_NAME, **context)

    @app.route('/ping')
    def get_ping():
        return 'ping'

    # serve index for all paths, so a client side router can take over
    @app.route('/<path:path>')
    def get_home_redirect(path):
    	return get_home()
