from reviews.models import Genre_Title
import csv


def run():
    with open('static/data/genre_title.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Genre_Title.objects.all().delete()

        for row in reader:
            print(row)

            genre_title = Genre_Title(
                id=row[0],
                title_id=row[1],
                genre_id=row[2],
            )
            genre_title.save()
