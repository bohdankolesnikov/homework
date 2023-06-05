# 16.32

def foo(x, y):       # pos(x, y)
        # next pos
        #   (x + 2, y + 1)
        #   (x + 2, y - 1)
        #   (x - 2, y + 1)
        #   (x - 2, y - 1)

    moves = [[(x, y)]];     # list of sequences of moves

    while (True):

        tmoves = [];

        for pos in moves:

            x, y = pos[-1];			# current position
            tpos = pos;

            pmvs_x2 = [x + 2, x - 2];       	# possible moves
            pmvs_x1 = [x + 1, x - 1];
            pmvs_y2 = [y + 2, y - 2];
            pmvs_y1 = [y + 1, y - 1];

            for x in pmvs_x2:
                for y in pmvs_y1:
                    if ( (x >= 1) and (x <= 8) and (y >= 1) and (y <= 8) ):
                        tmoves = tmoves + [tpos + [(x, y)]];

            for x in pmvs_x1:
                for y in pmvs_y2:
                    if ( (x >= 1) and (x <= 8) and (y >= 1) and (y <= 8) ):
                        tmoves = tmoves + [tpos + [(x, y)]];

        moves = tmoves;

        yield tmoves;


def convert_to_chess_notation(x, y):
    return (ord(x) - ord('a') + 1, int(y));

def convert_from_chess_notation(pos):
    return (chr(ord('a') + pos[0] - 1), pos[1]);

s1x, s1y = input("Enter s1 position (x: (a-h), y: (1-8)) separated by comma: ").replace(" ", "").split(",");
s2x, s2y = input("Enter s2 position (x: (a-h), y: (1-8)) separated by comma: ").replace(" ", "").split(",");

x1, y1 = convert_to_chess_notation(s1x, s1y);
x2, y2 = convert_to_chess_notation(s2x, s2y);

gen = foo(x1, y1);

condition = True;

while (condition):

    for seq in next(gen):
        if ( seq[-1] == (x2, y2) ):
            res = seq;
            condition = False;

print(f"result: {list(map(convert_from_chess_notation, res))}");
