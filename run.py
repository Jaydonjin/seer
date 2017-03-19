"""deimos entry point

"""

if __name__ == '__main__':
    import os

    from app import create_app

    ENV_NAME = 'ENV'

    app = create_app(os.environ.get(ENV_NAME, 'development'))

    app.logger.info('demo listening %s:%s', app.config['HTTP_HOST'], app.config['HTTP_PORT'])

    if app.config.get('DEBUG', False):
        app.run(app.config['HTTP_HOST'], app.config['HTTP_PORT'], debug=False)

