from app.allImports import *

def redirect_url(default='deadlineDisplay'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)