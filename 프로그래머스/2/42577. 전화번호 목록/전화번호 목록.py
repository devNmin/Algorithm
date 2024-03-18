def solution(phone_book):
    phone_book.sort()


    phone_book_length = len(phone_book)
    for i in range(phone_book_length-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False

    return True