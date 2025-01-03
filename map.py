from position import Position

def setUpMap():
    initial_pos = Position(0, "Start",'You are at the initial position.')
    pos1 = Position(1, 'Rocks', 'A rocky area with uneven terrain.', item = ['rocks'])
    pos2 = Position(2, 'Cave', 'A dark and quiet cave.', item = ['iron-ore'])
    pos3 = Position(3, 'Tree', 'A tall tree with thick branches.', item = ['wood'])
    pos4 = Position(4, 'Dead Animals', 'The remains of dried, lifeless animals are scattered here.', item = ['leather'])
    pos5 = Position(5, 'Shop', 'A small shop with useful supplies.', item = ['sword','cross-guard','helmet'])
    pos6 = Position(6, 'Trees', 'A cluster of dense trees.', item = ['wood'])
    pos7 = Position(7, 'River', 'A calm river flows gently.', item = ['water'])
    pos8 = Position(8, 'Cave', 'Another dark cave looms ahead.', item = ['iron-ore'])
    pos9 = Position(9, 'Dried Carcasses', 'The bones and dried remains of animals lie here.', item = ['leather'])
    pos10 = Position(10, 'Cave', 'A small, cramped cave.', item = ['iron-ore'])
    pos11 = Position(11, 'Trees', 'A cluster of dense trees.', item = ['wood'])
    final_pos = Position(11, 'War', 'You have reached your destination.')

    initial_pos.possible_positions = {
       'forward': pos1,
    }
    pos1.possible_positions =  {
       'forward': pos4,
       'backward': initial_pos,
       'left': pos2, 
       'right': pos3,
    }
    pos2.possible_positions = {
       'forward': pos6,
       'right': pos1,
    }
    pos3.possible_positions = {
        'forward':pos5,
        'left': pos1
    }
    pos4.possible_positions = {
       'forward': pos7,
       'backward': pos1,
       'left': pos6,
       'right': pos5
    }
    pos5.possible_positions = {
       'backward':pos3,
       'left':pos4,
       'forward':pos11
    }
    
    pos6.possible_positions = {
       'right': pos4,
       'backward': pos2
    }

    pos7.possible_positions = {
       'forward':pos8,
       'backward':pos4,
       'right':pos11
    }
    pos8.possible_positions = {
       'forward':pos9,
       'backward':pos7
    }
    pos9.possible_positions = {
       'forward': final_pos,
       'left': pos10,
       'backward': pos8,
    }
    pos10.possible_positions = {
       'right': pos9
    }
    pos11.possible_positions = {
       'left': pos7,
       'backward':pos5
    }
    return initial_pos
