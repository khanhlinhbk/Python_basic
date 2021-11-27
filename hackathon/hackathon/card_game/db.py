'''Kết nối CSDL'''
from pymysql import connect, cursors, Error
import sys

# Tạo CSDL vs file game_log.sql, khởi chạy CSDL trước
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'game_log',
    'cursorclass': cursors.DictCursor
}

try:
    cnx = connect(**config)
    cur = cnx.cursor()
except Error as e:
    print('Lỗi kết nối đến Data, không thể khởi chạy ứng dụng')
    print(e.args[1])
    sys.exit()

def log(winner):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    sql = '''INSERT INTO games (winner) VALUES (%s)'''
    cur.execute(sql, winner)

    game_id = cur.lastrowid
    cnx.commit()
    return(game_id)
    
    
def logs(game_id, player, cards, point, biggest_card):
    sql1 = f'''
    INSERT INTO logsss (game_id, player, cards, point, biggest_card)
    VALUES (%s, %s, %s, %s, %s)
    '''
    cur.execute(sql1, (game_id, player, cards, point, biggest_card))

    cnx.commit()

def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    sql = '''
    SELECT *
    FROM games
    ORDER BY games.play_at DESC
    '''

    cur.execute(sql)
    game = cur.fetchone()

    if not game:
        raise Exception('Không có lịch sử game')

    sql = f'''
    SELECT *
    FROM logsss
    WHERE game_id = {game['game_id']}
    '''
    cur.execute(sql)
    players = cur.fetchall()

    return game, players



def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi
     (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    sql = '''
    SELECT
        winner as player,
        COUNT(*) AS game_won
    FROM games
    WHERE DATE(games.play_at) = CURDATE()
    GROUP BY player
    ORDER BY game_won DESC
    '''

    cur.execute(sql)
    records = cur.fetchall()

    if not records:
        raise Exception('Không có lịch sử game')

    total_game = sum([r['game_won'] for r in records])
    return total_game, records
