from django.conf import settings
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class ConfigView(APIView):
    """GET /api/v1/config - bootstrap payload the client fetches before login.

    Extend this with whatever the app needs at startup: feature flags, a
    minimum supported build, maintenance state, support links.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({
            'app_name': 'Flutter Boilerplate',
            'api_version': 'v1',
            'min_supported_version': '1.0.0',
            'maintenance_mode': False,
            'features': {
                'registration_enabled': True,
                'social_login_enabled': False,
            },
            'support_email': 'support@example.com',
            'debug': settings.DEBUG,
        })
