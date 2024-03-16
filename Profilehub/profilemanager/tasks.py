from celery import shared_task
import os


@shared_task(bind=True, queue="count_words")
def count_words_in_file(self, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        return word_count

# count_words_in_file.delay('path/to/your/file.txt')