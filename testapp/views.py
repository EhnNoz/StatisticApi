import datetime
from django.conf import settings
from django.utils import timezone
from testapp.models import System, Session
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from testapp.serializers import SessionSerializer


class SessionViewSets(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                      mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

    # Authenticate vs Token
    def get_system(self, request):
        # Authorization process: Check if token is valid
        token = request.headers['authorization'].split(' ')[1]
        url = request.META['HTTP_ORIGIN']
        system = System.objects.filter(token=token, url__contains=url)
        if system.exists():
            return system[0]
        else:
            return None

    def create(self, request, *args, **kwargs):
        system = self.get_system(request)
        if not system:
            return Response(status=403)

        # Process session
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.data.get('user_id')
            ip = serializer.data.get('ip')
            user_agent = serializer.data.get('user_agent')
            referer = serializer.data.get('referer')
            xReferer = serializer.data.get('xReferer')

            # Check if session is already opened
            now = timezone.now()
            before = now - datetime.timedelta(minutes=settings.SESSION_TIMEOUT)
            session = Session.objects.filter(system=system, user_id=user_id, start_time__range=[before, now]).exclude(
                End_time=None)
            if session.exists():
                session = session[0]
                session.user_agent = user_agent
                session.referer = referer
                session.xReferer = xReferer
                session.save()
                return Response(SessionSerializer(session).data, status=200)

            session = Session.objects.create(system=system, user_id=user_id, ip=ip, user_agent=user_agent,
                                             referer=referer, xReferer=xReferer)
            return Response(SessionSerializer(session).data, status=201)
        else:
            return Response(serializer._errors, status=400)

    def update(self, request, *args, **kwargs):
        system = self.get_system(request)
        if not system:
            return Response(status=403)

        # Update session
        request.data['End_time'] = timezone.now()
        return super(SessionViewSets, self).update(request, *args, **kwargs)
