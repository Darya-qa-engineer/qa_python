from test_util import TestConst


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        # Act
        collector.add_new_book(TestConst.Book1)
        collector.add_new_book(TestConst.Book2)

        # Assert
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_book_twice(self, collector):
        # Act
        collector.add_new_book(TestConst.Book1)
        collector.add_new_book(TestConst.Book1)

        # Assert
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating(self, books):
        # Arrange
        rating = 7

        # Act
        books.set_book_rating(TestConst.Book1, rating)

        # Assert
        assert books.get_book_rating(TestConst.Book1) == rating

    def test_set_book_rating_negative_rating_below_one(self, books):
        # Arrange
        rating = -5

        # Act
        books.set_book_rating(TestConst.Book1, rating)

        # Assert
        assert books.get_book_rating(TestConst.Book1) == TestConst.DefaultRating

    def test_set_book_rating_negative_rating_more_ten(self, books):
        # Arrange
        rating = 14

        # Act
        books.set_book_rating(TestConst.Book1, rating)

        # Assert
        assert books.get_book_rating(TestConst.Book1) == TestConst.DefaultRating

    def test_set_book_rating_unknown_book(self, collector):
        # Arrange
        rating = 5
        unknown_book = TestConst.UnknownBook

        # Act
        collector.set_book_rating(unknown_book, rating)

        # Assert
        assert collector.get_book_rating(unknown_book) is None

    def test_add_book_in_favorites_add_two_books(self, books):
        # Act
        books.add_book_in_favorites(TestConst.Book1)
        books.add_book_in_favorites(TestConst.Book2)
        fav_list = books.get_list_of_favorites_books()

        # Assert
        assert len(fav_list) == 2
        assert TestConst.Book1 in fav_list and TestConst.Book2 in fav_list

    def test_add_book_in_favorites_unknown_book(self, collector):
        # Arrange
        unknown_book = TestConst.UnknownBook

        # Act
        collector.add_book_in_favorites(unknown_book)
        fav_list = collector.get_list_of_favorites_books()

        # Assert
        assert unknown_book not in fav_list

    def test_book_default_rating(self, books):
        # Assert
        assert books.get_book_rating(TestConst.Book1) == TestConst.DefaultRating

    def test_get_book_rating(self, books):
        # Arrange
        book = TestConst.Book1
        rating = 9

        # Act
        books.set_book_rating(book, rating)

        # Assert
        assert books.get_book_rating(book) == rating

    def test_get_books_with_specific_rating_two_books(self, books):
        # Arrange
        rating = 6

        # Act
        books.set_book_rating(TestConst.Book1, rating)
        books.set_book_rating(TestConst.Book2, rating)
        rating_list = books.get_books_with_specific_rating(rating)

        # Assert
        assert len(rating_list) == 2
        assert TestConst.Book1 in rating_list and TestConst.Book2 in rating_list

    def test_get_books_with_specific_rating_invalid_rating(self, books):
        # Arrange
        rating = -1

        # Act
        rating_list = books.get_books_with_specific_rating(rating)

        # Assert
        assert len(rating_list) == 0

    def test_delete_book_from_favorites_delete_one_book(self, books):
        # Act
        books.add_book_in_favorites(TestConst.Book1)
        books.add_book_in_favorites(TestConst.Book2)
        books.delete_book_from_favorites(TestConst.Book1)
        fav_list = books.get_list_of_favorites_books()

        # Assert
        assert len(fav_list) == 1
        assert TestConst.Book2 in fav_list

    def test_delete_from_favorites_delete_unknown_book(self, books):
        # Arrange
        unknown_book = TestConst.UnknownBook
        fav_books = [TestConst.Book1, TestConst.Book2, TestConst.Book3]

        # Act
        for book in fav_books:
            books.add_book_in_favorites(book)
        books.delete_book_from_favorites(unknown_book)
        fav_list = books.get_list_of_favorites_books()

        # Assert
        assert len(fav_list) == len(fav_books)
        assert unknown_book not in fav_list

    def test_get_list_of_favorites_books_list_of_favorites(self, books):
        # Arrange
        fav_books = [TestConst.Book1, TestConst.Book2, TestConst.Book3]

        # Act
        for book in fav_books:
            books.add_book_in_favorites(book)
        fav_list = books.get_list_of_favorites_books()

        # Assert
        assert len(fav_list) == len(fav_books)
        for item in fav_books:
            assert item in fav_list

    def test_get_books_rating_dict_of_three_books(self, books):
        # Act
        books_dict = books.get_books_rating()

        # Assert
        assert len(books_dict) == 3
