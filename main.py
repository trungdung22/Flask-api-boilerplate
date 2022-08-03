from app.config.server import application
import app.views.doctor
import app.views.user


@application.errorhandler(404)
def page_not_found(e):
    """ Page not found error handling """

    return {
        'status': 'error',
        'message': 'Undefined route'
    }, 404


if __name__ == '__main__':
    application.run(host='0.0.0.0')
