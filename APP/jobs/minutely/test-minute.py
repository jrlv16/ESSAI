from django_extensions.management.jobs import MinutelyJob


class Job(MinutelyJob):
    help = "My sample job."

    def execute(self):
        # executing empty sample job
        print("This is my first job")
