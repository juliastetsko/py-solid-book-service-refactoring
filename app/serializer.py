import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize_book(self, book: Book) -> None:
        pass


class JsonBookSerializer(BookSerializer):
    def serialize_book(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlBookSerializer(BookSerializer):
    def serialize_book(self, book: Book) -> ET:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def create_book_serializer(serialize_type: str) -> BookSerializer:
    if serialize_type == "json":
        return JsonBookSerializer()
    elif serialize_type == "xml":
        return XmlBookSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
