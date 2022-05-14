from reviews.models import Comment
import csv


def run():
    with open('static/data/comments.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Comment.objects.all().delete()

        for row in reader:
            print(row)

            comments = Comment(
                id=row[0],
                review_id=row[1],
                text=row[2],
                author_id=row[3],
                pub_date=row[4]
            )
            comments.save()
