from flask import Blueprint, current_app as app

bp = Blueprint('logs', __name__, url_prefix='/')


@bp.route('/logs')
def get_logs():
    app.logger.debug('Hello this is an debug only information !')
    app.logger.info('Hello this is an information !')
    app.logger.warn('Hello this is a warning !')
    app.logger.error('Hello this is an error !')
    return 'Regarde le terminal pour voir les logs'
