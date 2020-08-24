from rest_framework.generics import CreateAPIView
from Main.api.serializers import SubscriberSerializer
from rest_framework.authentication import BasicAuthentication
from Main.api.utils import CsrfExemptSessionAuthentication


class SubscriberCreateAPIView(CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
    serializer_class = SubscriberSerializer
