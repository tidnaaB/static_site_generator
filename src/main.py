from textnode import TextNode, text_type_bold


def main():
    node = TextNode(
        "Example Text Node", text_type_bold, "https://www.github.com/tidnaaB"
    )
    print(node)


if __name__ == "__main__":
    main()
