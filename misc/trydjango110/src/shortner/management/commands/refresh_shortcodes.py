from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from shortner.models import KirrURL

# class Command(BaseCommand):
#     help = 'Refreshing available shortcodes'

#     def add_arguments(self, parser):
#         parser.add_argument('--these are like command line arguments which can be accessed via options variable', type=int)

#     def handle(self, *args, **options):
#         # for poll_id in options['poll_id']:
#         #     try:
#         #         poll = Poll.objects.get(pk=poll_id)
#         #     except Poll.DoesNotExist:
#         #         raise CommandError('Poll "%s" does not exist' % poll_id)

#         #     poll.opened = False
#         #     poll.save()

#         #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
#         print(options)
#         return KirrURL.objects.refresh_shortcodes()


class Command(BaseCommand):
    help = 'Refreshing available shortcodes'
    def add_arguments(self, parser):
        # parser.add_argument('Last X Ids', type=int) # Better to use single word
        parser.add_argument('last_X_ids', type=int) # Adding -- make this parameter as options & in  that case we need to pass this key as well so ' '(space) in between will create error  ('--Last X Ids' wouldn't work)
    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(lastX = options['last_X_ids'])