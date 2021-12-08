#!/usr/bin/env python3
from sys import stdin, stdout
from argparse import ArgumentParser, FileType, Namespace
from typing import Any
import re


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "input", nargs="?", type=FileType("r", encoding="utf-8"), default=stdin
    )
    parser.add_argument(
        "output", nargs="?", type=FileType("w", encoding="utf-8"), default=stdout
    )
    parser.add_argument("-n", type=int, default=0, help="number of spaces")
    parser.add_argument("-m", type=int, default=1, help="number of lines")
    parser.add_argument(
        "-x", action="store_false", help="do not add spaces around non-Chinese words"
    )
    return parser.parse_args()


def handle_paragraphs(article: str, n: int, m: int, skip: int = 2) -> str:
    raw_paragraphs = re.split(r"\s*\n+\s*", article.strip())
    paragraphs = raw_paragraphs[:skip]
    for raw_paragraph in raw_paragraphs[skip:]:
        paragraphs.append(" " * n + raw_paragraph)
    return ("\n" * m).join(paragraphs)


def handle_punctuations(article: str) -> str:
    trans_table = str.maketrans(",.!?()", "，。！？（）")
    return article.translate(trans_table)


def handle_words(article: str) -> str:
    return re.sub(r" *[a-zA-Z0-9_·]+ *", lambda m: f" {m[0].strip()} ", article)


def handle(args: Namespace) -> str:
    article: str = args.input.read()
    args.input.close()
    article = handle_words(article)
    article = handle_punctuations(article)
    article = handle_paragraphs(article, args.n, args.m)
    return article


def main() -> None:
    args = parse_arguments()
    article = handle(args)
    args.output.write(article)
    args.output.close()


if __name__ == "__main__":
    main()
