from app.models import Chunk


def main():

    chunk = Chunk(
        text="Hello world",
        source="resume.pdf",
        category="resume",
        chunk_number=1
    )

    print(chunk)


if __name__ == "__main__":
    main()