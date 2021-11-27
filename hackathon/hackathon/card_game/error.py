
class Error(Exception):
    '''Base class cho game error'''
    pass


class MaximumPlayerError(Error):
    '''Số lượng người chơi vượt quá mức quy định'''

    message = 'Số lượng người chơi quá đông và nguy hiểm rồi :)\n'

    def __init__(self, message=message):
        self.message = message


class MinimumPlayerError(Error):
    '''Số lượng người chơi nhỏ hơn mức quy định'''

    message = 'Còn quá ít người chơi, rủ thêm đi cho vui :)\n'

    def __init__(self, message=message):
        self.message = message


class PlayerDoesNotExistsError(Error):
    '''Người chơi không tồn tại'''

    message = '''ID người chơi không tồn tại\n'''

    def __init__(self, message=message):
        self.message = message


class PlayingError(Error):
    '''Lỗi thao tác khi game đang chơi, ví dụ định chuồn =]]'''

    message = 'Game đang chơi, kết thúc ván đã nhé :)\n'

    def __init__(self, message=message):
        self.message = message


class DealtError(Error):
    '''Lỗi thực hiện thao tác chia bài nhiều lần'''
    message = 'Bài đã được chia rồi'

    # def __init__(self, message=message):
    #     self.message = message


class NotDealtError(Error):
    '''Lỗi thực hiện thao tác lật bài khi chưa chia'''

    message = 'Chưa chia bài mà :)\nGọi thêm người chơi cho vui :)\n'

    def __init__(self, message=message):
        self.message = message


class FlippedError(Error):
    '''Lỗi khi lật bài nhiều lần'''

    message = 'Bài đã lật rồi mà :)\nCay cú thì làm ván mới gỡ x2 nhé :)\n'

    def __init__(self, message=message):
        self.message = message


class FunctionDoesNotExists(Error):
    '''Lỗi khi chọn chức năng không tồn tại'''

    message = 'Chức năng không tồn tại\n'

    def __init__(self, message=message):
        self.message = message


class CancelError(Error):
    '''Lỗi khi hủy chức năng, ví dụ hủy thêm người chơi, hay xóa người chơi'''

    def __init__(self, message=''):
        self.message = message