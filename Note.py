from datetime import datetime
import uuid


class Note:
    def __init__(self, id=str(uuid.uuid1())[0:3], date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")), title="текст",
                 body="текст"):
        self.id = id
        self.date = date
        self.title = title
        self.body = body

    def get_id(note):
        return note.id

    def get_date(note):
        return note.date

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date
