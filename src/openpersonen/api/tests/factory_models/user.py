from django.contrib.auth import get_user_model

import factory


class UserFactory(factory.django.DjangoModelFactory):

    username = factory.Sequence(lambda n: "user-{0}".format(n))
    first_name = "Test"
    last_name = "User"
    email = factory.Sequence(lambda n: "user-{0}@maykinmedia.nl".format(n))
    password = factory.PostGenerationMethodCall("set_password", "secret")

    class Meta:
        model = get_user_model()
