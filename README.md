# qa_python  
## Тесты
- **test_add_new_book_add_two_books** - добавление двух книг  
- **test_add_new_book_add_book_twice** - добавление одной книги дважды (негативная проверка)
- **test_set_book_rating_set_rating** - выставление рейтинга книге(позитивная проверка)
- **test_set_book_rating_negative_rating_below_one** -  выставление рейтинга книге меньше 1 (негативная проверка)
- **test_set_book_rating_negative_rating_more_ten** -  выставление рейтинга книге больше 10 (негативная проверка)
- **test_set_book_rating_unknown_book** -   выставление рейтинга неизвестной книге (негативная проверка)
- **test_add_book_in_favorites_add_two_books** -   добавление в избранное двух книг
- **test_add_book_in_favorites_unknown_book** -   добавление в избранное неизвестную книгу (негативная проверка)
- **test_book_default_rating** -   проверка рейтинга книги по умолчанию
- **test_get_book_rating** -   получение рейтинга книги по ее имени
- **test_get_books_with_specific_rating_two_books** -   вывод списка книг с определенным рейтингом
- **test_get_books_with_specific_rating_invalid_rating** -  вывод списка книг с некорректным рейтингом (негативная проверка)
- **test_delete_book_from_favorites_delete_one_book** -   удаление книги из избранного
- **test_delete_from_favorites_delete_unknown_book** -   удаление неизвестной книги из избранного (негативная проверка)
- **test_get_list_of_favorites_books_list_of_favorites** -   получение списка избранных книг
- **test_get_books_rating_dict_of_three_books** - получение списка книг