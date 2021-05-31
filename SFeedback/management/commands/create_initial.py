from django.core.management.base import BaseCommand, CommandError
from SFeedback.models import Question


class Command(BaseCommand):
    help = 'Create ImageTutorial objects for a specific Tutorial'

    def handle(self, *args, **options):

        q = Question(question_text="What do you like to do?", question_short="Likes")
        q.save()
        q = Question(question_text="What you don't like to do but you need to?", question_short="NeedTo")
        q.save()
        q = Question(question_text="What you don't like?", question_short="NoLike")
        q.save()
        q = Question(question_text="State a reason to learn Computer Science", question_short="WhyCS")
        q.save()
        q = Question(question_text="What you want to be?", question_short="Future")
        q.save()
        q = Question(question_text="Favourite Companies", question_short="Companies")
        q.save()
        q = Question(question_text="Are you a streamer?", question_short="Streamer")
        q.save()
        q = Question(question_text="Do you use twitch.com?", question_short="Twitch")
        q.save()
        q = Question(question_text="Do you know how to code?", question_short="Code")
        q.save()
