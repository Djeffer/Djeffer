def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper

class UserInterface:
    @add_title('Ввод пользователем данных')
    def wait_user_answer(self):
        print("Действия со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        print("=" * 50)
        return user_answer

    @add_title('Создание статьи:')
    def add_user_articles(self):
        dict_article = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        print("=" * 50)
        return dict_article

    @add_title('Список статей:')
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        print("=" * 50)
