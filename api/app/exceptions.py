import uuid


class TaskNotFoundError(Exception):
    def __init__(self, task_id: uuid.UUID):
        self.task_id = task_id
