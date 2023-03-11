
from rest_framework import serializers
from wezacare.models import Question,CustomUser

#serializer class for our custome user model (table)
class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=CustomUser.objects.all(),slug_field='username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    class Meta:
        model = Question
        # fields from our model
        fields = ('id','user_question','user','created_at','updated_at')
        #use of password with min len of 8 enforced, make password field write only