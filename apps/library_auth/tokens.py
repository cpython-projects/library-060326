from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    """
    Returns a list of tokens needed to authenticate a user
    :param user:
    :return:
    """
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }


def blacklist_all_tokens(user):
    """
    Removes all tokens associated with a user to blacklist
    :param user:
    :return:
    """
    for token in OutstandingToken.objects.filter(user=user):
        BlacklistedToken.objects.get_or_create(token=token)




