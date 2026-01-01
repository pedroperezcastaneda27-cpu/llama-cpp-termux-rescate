import queue

class JobQueue:
    def __init__(self):
        self.jobs = queue.Queue()

    def add_job(self, job):
        self.jobs.put(job)

    def get_next_job(self):
        if not self.jobs.empty():
            return self.jobs.get()
        return None
