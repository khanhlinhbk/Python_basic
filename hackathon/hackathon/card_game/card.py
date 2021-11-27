
class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    ranks=[ 2, 3, 4, 5, 6, 7, 8, 9,1]
    suits=['♠', '♣', '♦', '♥']
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return (str(self.rank)+ self.suit)

    def __gt__(self, other):
         return Card.ranks.index(self.rank)==Card.ranks.index(other.rank) if Card.suits.index(self.suit)>Card.suits.index(other.suit) else Card.ranks.index(self.rank)>Card.ranks.index(other.rank)
       
