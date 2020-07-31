"""
Views that handles auth urls
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect


def handle_redirect(request):
    """
    Method that is called after google authentication (SOCIAL_AUTH_LOGIN_REDIRECT_URL)
    Handles redirect url
    """

    main_page_url = request.session.get('main_page_url')

    if main_page_url:
        response = HttpResponseRedirect(main_page_url)
        return response

        # response.set_signed_cookie('sessionid', request.COOKIES.get('sessionid'))
        # response.set_signed_cookie('csrftoken', request.COOKIES.get('csrftoken'))

    return render(request, 'social_auth_a.html', {})
