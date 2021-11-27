import error
from deck import Deck
from player import Player
from card import Card
import os
import db

clear = lambda: os.system('cls')
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''
    
    

    def __init__(self):
        self.is_playing = False
        self.is_dealt = False
        self.is_flipped = False
        self.players = []
        self.deck = Deck()
        self.deck.build()

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        print("Xin chào, Có bao nhiêu người chơi")
        while True:
            try: 
                number_player = int(input())
                if number_player < 2:
                            raise error.MinimumPlayerError(
                                f'Tối thiểu 2 người chơi, mời nhập lại')
                elif number_player > 17:
                            raise error.MaximumPlayerError(
                                f'Tối đa 17 người chơi, mời nhập lại')
                else: 
                    for i in range(number_player) :
                        print("Nhập tên người chơi thứ " + str(i+1))
                        player_name = input()
                        self.players.append(Player(player_name))
                    break
            except error.Error as e:
                print(e.message)
            except ValueError as e:
                print('Vui lòng nhập 1 số')

    def guide(self):
        print("1.Danh sách người chơi"+ "(" + str(len(self.players)) +")")
        print("2.thêm người chơi")
        print("3.Loại người chơi")
        print("4.chia bài")
        print("5.Lật bài")
        print("6.Xem lại game vừa chơi")
        print("7.Xem lịch sử chơi hôm nay")
        print("8.Thoát game")
    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        for player in self.players:
            print (player)

    def add_player(self):
        '''Thêm một người chơi mới'''
        print("Nhập tên người chơi thứ " + str(len(self.players)+1))
        player_name = input()
        self.players.append(Player(player_name))

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        print("Bạn muốn xóa người chơi thứ mấy")
        index_player = int(input())
        del self.players[index_player-1]

    def deal_card(self):
        '''Chia bài cho người chơi'''
        # if self.is_dealt:
        #     raise error.DealtError()
        # else:
        self.deck.shuffle_card()
        number_player = len(self.players)
        for player in self.players:
            # để ý dấu mặc chỗ index, nó là index() chứ kp là index[]
            player.add_card(self.deck.deal_card(self.players.index(player)))
            player.add_card(self.deck.deal_card(self.players.index(player)+number_player))
            player.add_card(self.deck.deal_card(self.players.index(player)+number_player*2))
        print("Đã chia bài, xuống tiền đi")
        self.is_dealt = True
        self.is_flipped = False
        self.is_playing = True

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        win_name= ""
        play_list = []
        for player in self.players:
            print("==================================================================")
            play_list.append([player.name,player.point,player.biggest_card])
            print("Các lá bài của "+ player.name+ " Là")
            for i in player.cards:
                print(i)
            print("Tổng điểm của " + player.name+ " Là " + str(player.point))
            print("Lá bài cao nhất của " + player.name+ " Là " + str(player.biggest_card))
        max_point=0 
        max_biggest="" 
        for i in play_list:
            if i[1] > max_point:
                max_point = i[1]
                max_biggest = i[2]
                win_name = i[0]
            elif i[1] == max_point:
                if max_biggest> i[2] :
                    max_point = i[1]
                    max_biggest = i[2]
                    win_name = i[0]
        print("==================================================================")
        print("Người chiến thắng là "+ win_name)
        a= db.log(win_name)
        for player in self.players:
            str1= " "
            for i in player.flip_card():
                str1 += str(i)
            db.logs(a, player.name, str1, player.point, player.biggest_card)
            # playerss.append((player.name, player.flip_card(),  player.point, player.biggest_card))
            player.remove_card()
    def last_game(self):
        print("Ván bài vừa chơi:")
        last_game, players = db.get_last_game()
        print(last_game['play_at'])
        print()

        for p in players:
            print(f'Bài của {p["player"]}')
            print(
                f'Bộ bài: {p["cards"]} Điểm: {p["point"]} Lá bài lớn nhất: {p["biggest_card"]}')
            print()

        print(f'Người chơi chiến thắng: {last_game["winner"]}') 


    def history(self):
            total_game, records = db.history()
            print(f'Hôm nay đã chơi: {total_game} ván bài')

            for r in records:
                print(f'{r["player"]:6} thắng {r["game_won"]} ván')
