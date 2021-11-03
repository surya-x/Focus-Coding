from main import load_urls


def test_load_urls():
    path = r""
    list = load_urls(path)
    print(list)


if __name__ == '__main__':
    test_load_urls()
