class Error(Exception):
    """Base class cho các exception trong module"""
    pass

class NotInError(Error):
    """Ném ra khi giá trị đầu vào không phải số từ 0 đến 50"""

    def __init__(self, value):
        message = f"Không phải số từ 0 đến 50 {value}"
        self.value = value
        self.message = message
class LessError(Error):
    """Ném ra khi giá trị khi đoán số bé hơn số càn tìm"""

    def __init__(self, value):
        message = f"Giá trị {value} nhỏ hơn số cần tìm"
        self.value = value
        self.message = message
class MoreError(Error):
    """Ném ra khi giá trị khi đoán số lớn hơn số cần tìm"""

    def __init__(self, value):
        message = f"Giá trị {value} lớn hơn số cần tìm"
        self.value = value
        self.message = message
def choseNumber(a):
    for i in range(3):
        val = int(input('Hãy nhập vào 1 số từ 1 đến 50: ')) 
        if val<0 or val>50 :
            raise NotInError(val)
        elif val<a:
            raise LessError(val)
        elif val>a:
            raise MoreError(val)
        elif val==a:
            print("Chúc mừng bạn đoán đúng")
    # mình còn thiếu phần khi lỗi thì xử lý thế nào!!!
    #DÙng while chứ k nên dung for

choseNumber(10)