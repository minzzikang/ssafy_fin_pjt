from allauth.account.adapter import DefaultAccountAdapter


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'nickname', request.data.get('nickname'))
        user_field(user, 'mbti', request.data.get('mbti'))
        user_field(user, 'age', request.data.get('age'))
        user.save()
        return user