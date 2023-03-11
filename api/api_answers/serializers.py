
from rest_framework import serializers
from wezacare.models import Answer,CustomUser,Question

#serializer class for our custome user model (table)
class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=CustomUser.objects.all(),slug_field='username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    user_question = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        # fields from our model
        fields = ('id','user_answer','user_question','question','user','created_at','updated_at')
        #use of password with min len of 8 enforced, make password field write only
        
    def get_user_question(self, obj):
        return obj.question.user_question