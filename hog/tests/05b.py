test = {
  'name': 'Question 5b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # example 1
          >>> def strat0(s0, s1):
          ...     if s0 == 0: return 3
          ...     if s0 == 7: return 5
          ...     return 8
          >>> def strat1(s0, s1):
          ...     if s0 == 0: return 1
          ...     if s0 == 4: return 2
          ...     return 6
          >>> s0, s1 = hog.play(
          ...   strat0, strat1, score0=0, score1=0, goal=21,
          ...   dice=hog.make_test_dice(2, 2, 3, 4, 2, 2, 2, 2, 2, 3, 5, 2, 2, 2, 2, 2, 2, 2, 6, 1))
          >>> s0
          43
          >>> s1
          15
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # example 2
          >>> s0, s1 = hog.play(always(2), always(1), score0=0, score1=0, goal=5, dice=hog.make_test_dice(2, 2))
          >>> s0
          7
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # swap after feral hogs
          >>> s0, s1 = hog.play(always(2), always(1), score0=17, score1=6, goal=21, dice=hog.make_test_dice(1, 2))
          >>> s0
          6
          >>> s1
          21
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=45891, score0=47, score1=53, goal=54, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (47, 53).
          Player 0 rolls 9 dice and gets outcomes [5, 1, 1, 2, 6, 1, 1, 1, 5].
          End scores = (48, 53)
          >>> print(turns[1])
          Start scores = (48, 53).
          Player 1 rolls 7 dice and gets outcomes [3, 2, 6, 2, 3, 2, 5].
          End scores = (76, 48)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5192, score0=43, score1=12, goal=47, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (43, 12).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 5, 1, 3, 3, 2, 3].
          End scores = (44, 12)
          >>> print(turns[1])
          Start scores = (44, 12).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 5, 3, 5, 4, 2, 1].
          End scores = (44, 13)
          >>> print(turns[2])
          Start scores = (44, 13).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 1, 1, 6, 1].
          End scores = (45, 13)
          >>> print(turns[3])
          Start scores = (45, 13).
          Player 1 rolls 3 dice and gets outcomes [4, 6, 5].
          End scores = (31, 45)
          >>> print(turns[4])
          Start scores = (31, 45).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (45, 35)
          >>> print(turns[5])
          Start scores = (45, 35).
          Player 1 rolls 10 dice and gets outcomes [5, 2, 6, 1, 1, 3, 6, 6, 6, 2].
          End scores = (45, 36)
          >>> print(turns[6])
          Start scores = (45, 36).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 2, 6, 6, 2, 3, 1, 5, 2].
          End scores = (46, 36)
          >>> print(turns[7])
          Start scores = (46, 36).
          Player 1 rolls 6 dice and gets outcomes [4, 2, 2, 5, 2, 4].
          End scores = (46, 55)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=95816, score0=15, score1=45, goal=50, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 45).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 6, 5, 1, 5, 6].
          End scores = (16, 45)
          >>> print(turns[1])
          Start scores = (16, 45).
          Player 1 rolls 10 dice and gets outcomes [5, 2, 4, 3, 6, 3, 4, 5, 1, 2].
          End scores = (16, 46)
          >>> print(turns[2])
          Start scores = (16, 46).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (26, 46)
          >>> print(turns[3])
          Start scores = (26, 46).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (26, 48)
          >>> print(turns[4])
          Start scores = (26, 48).
          Player 0 rolls 6 dice and gets outcomes [2, 1, 4, 2, 6, 6].
          End scores = (27, 48)
          >>> print(turns[5])
          Start scores = (27, 48).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (27, 56)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25365, score0=3, score1=8, goal=34, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 8).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 4, 6, 5, 1].
          End scores = (4, 8)
          >>> print(turns[1])
          Start scores = (4, 8).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (4, 11)
          >>> print(turns[2])
          Start scores = (4, 11).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (6, 11)
          >>> print(turns[3])
          Start scores = (6, 11).
          Player 1 rolls 5 dice and gets outcomes [2, 3, 1, 1, 6].
          End scores = (6, 15)
          >>> print(turns[4])
          Start scores = (6, 15).
          Player 0 rolls 7 dice and gets outcomes [2, 6, 5, 5, 2, 4, 1].
          End scores = (7, 15)
          >>> print(turns[5])
          Start scores = (7, 15).
          Player 1 rolls 5 dice and gets outcomes [4, 6, 6, 6, 6].
          End scores = (7, 43)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11863, score0=55, score1=5, goal=56, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (55, 5).
          Player 0 rolls 6 dice and gets outcomes [5, 1, 2, 1, 3, 5].
          End scores = (56, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59465, score0=61, score1=16, goal=88, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (61, 16).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 3, 4].
          End scores = (72, 16)
          >>> print(turns[1])
          Start scores = (72, 16).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (72, 21)
          >>> print(turns[2])
          Start scores = (72, 21).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 3, 6, 2, 1, 5, 1, 3].
          End scores = (73, 21)
          >>> print(turns[3])
          Start scores = (73, 21).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 2, 2, 2, 1].
          End scores = (73, 22)
          >>> print(turns[4])
          Start scores = (73, 22).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (74, 22)
          >>> print(turns[5])
          Start scores = (74, 22).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 1, 5, 5, 3, 1, 2].
          End scores = (74, 23)
          >>> print(turns[6])
          Start scores = (74, 23).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 3, 4, 4, 4, 5, 4, 4].
          End scores = (110, 23)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=4714, score0=9, score1=3, goal=20, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (9, 3).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (17, 3)
          >>> print(turns[1])
          Start scores = (17, 3).
          Player 1 rolls 2 dice and gets outcomes [2, 6].
          End scores = (17, 14)
          >>> print(turns[2])
          Start scores = (17, 14).
          Player 0 rolls 6 dice and gets outcomes [4, 4, 6, 3, 2, 3].
          End scores = (39, 14)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=10742, score0=4, score1=25, goal=57, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 25).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 3, 6, 4, 3, 6].
          End scores = (5, 25)
          >>> print(turns[1])
          Start scores = (5, 25).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 5, 6, 4].
          End scores = (5, 48)
          >>> print(turns[2])
          Start scores = (5, 48).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 3, 2, 6, 6].
          End scores = (6, 48)
          >>> print(turns[3])
          Start scores = (6, 48).
          Player 1 rolls 9 dice and gets outcomes [4, 3, 5, 6, 1, 1, 3, 4, 2].
          End scores = (6, 49)
          >>> print(turns[4])
          Start scores = (6, 49).
          Player 0 rolls 9 dice and gets outcomes [5, 6, 2, 4, 5, 1, 2, 1, 2].
          End scores = (7, 49)
          >>> print(turns[5])
          Start scores = (7, 49).
          Player 1 rolls 6 dice and gets outcomes [6, 1, 3, 6, 4, 2].
          End scores = (7, 50)
          >>> print(turns[6])
          Start scores = (7, 50).
          Player 0 rolls 7 dice and gets outcomes [5, 1, 6, 1, 4, 1, 6].
          End scores = (8, 50)
          >>> print(turns[7])
          Start scores = (8, 50).
          Player 1 rolls 4 dice and gets outcomes [4, 6, 2, 3].
          End scores = (8, 65)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5480, score0=5, score1=8, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (5, 8).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 4, 4, 6].
          End scores = (34, 8)
          >>> print(turns[1])
          Start scores = (34, 8).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (34, 12)
          >>> print(turns[2])
          Start scores = (34, 12).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 4, 4].
          End scores = (49, 12)
          >>> print(turns[3])
          Start scores = (49, 12).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 5, 1, 1, 2, 4, 5, 5, 4].
          End scores = (49, 13)
          >>> print(turns[4])
          Start scores = (49, 13).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 1, 1, 2, 1, 3, 1, 4].
          End scores = (50, 13)
          >>> print(turns[5])
          Start scores = (50, 13).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (50, 16)
          >>> print(turns[6])
          Start scores = (50, 16).
          Player 0 rolls 5 dice and gets outcomes [6, 1, 5, 2, 4].
          End scores = (51, 16)
          >>> print(turns[7])
          Start scores = (51, 16).
          Player 1 rolls 9 dice and gets outcomes [4, 6, 4, 5, 6, 5, 2, 2, 3].
          End scores = (51, 53)
          >>> print(turns[8])
          Start scores = (51, 53).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 2].
          End scores = (66, 53)
          >>> print(turns[9])
          Start scores = (66, 53).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 1, 1, 4, 6].
          End scores = (54, 66)
          >>> print(turns[10])
          Start scores = (54, 66).
          Player 0 rolls 3 dice and gets outcomes [6, 2, 2].
          End scores = (64, 66)
          >>> print(turns[11])
          Start scores = (64, 66).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 4, 2, 4, 2, 2].
          End scores = (64, 88)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5014, score0=56, score1=59, goal=64, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (56, 59).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 1, 4, 5, 1].
          End scores = (57, 59)
          >>> print(turns[1])
          Start scores = (57, 59).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (63, 57)
          >>> print(turns[2])
          Start scores = (63, 57).
          Player 0 rolls 4 dice and gets outcomes [5, 6, 5, 4].
          End scores = (83, 57)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=50496, score0=4, score1=15, goal=19, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 15).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 2, 6, 1, 5, 5, 2, 6].
          End scores = (5, 15)
          >>> print(turns[1])
          Start scores = (5, 15).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 1, 4, 5, 1, 1, 6, 4].
          End scores = (5, 16)
          >>> print(turns[2])
          Start scores = (5, 16).
          Player 0 rolls 2 dice and gets outcomes [1, 6].
          End scores = (6, 16)
          >>> print(turns[3])
          Start scores = (6, 16).
          Player 1 rolls 9 dice and gets outcomes [6, 4, 1, 2, 5, 6, 1, 5, 6].
          End scores = (6, 17)
          >>> print(turns[4])
          Start scores = (6, 17).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (7, 17)
          >>> print(turns[5])
          Start scores = (7, 17).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (7, 27)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=97617, score0=16, score1=27, goal=35, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (16, 27).
          Player 0 rolls 6 dice and gets outcomes [4, 3, 5, 1, 5, 2].
          End scores = (17, 27)
          >>> print(turns[1])
          Start scores = (17, 27).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (17, 38)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=19709, score0=27, score1=6, goal=85, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (27, 6).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (6, 35)
          >>> print(turns[1])
          Start scores = (6, 35).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 4, 1, 3, 6, 2, 4, 4, 6].
          End scores = (6, 36)
          >>> print(turns[2])
          Start scores = (6, 36).
          Player 0 rolls 2 dice and gets outcomes [3, 1].
          End scores = (7, 36)
          >>> print(turns[3])
          Start scores = (7, 36).
          Player 1 rolls 3 dice and gets outcomes [6, 2, 3].
          End scores = (7, 50)
          >>> print(turns[4])
          Start scores = (7, 50).
          Player 0 rolls 8 dice and gets outcomes [4, 2, 4, 5, 6, 1, 1, 3].
          End scores = (8, 50)
          >>> print(turns[5])
          Start scores = (8, 50).
          Player 1 rolls 8 dice and gets outcomes [4, 5, 2, 2, 2, 2, 2, 4].
          End scores = (8, 73)
          >>> print(turns[6])
          Start scores = (8, 73).
          Player 0 rolls 6 dice and gets outcomes [2, 1, 2, 5, 3, 4].
          End scores = (9, 73)
          >>> print(turns[7])
          Start scores = (9, 73).
          Player 1 rolls 4 dice and gets outcomes [2, 4, 5, 4].
          End scores = (9, 88)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=33634, score0=48, score1=74, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (48, 74).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 1, 3, 3, 4, 3, 1].
          End scores = (49, 74)
          >>> print(turns[1])
          Start scores = (49, 74).
          Player 1 rolls 8 dice and gets outcomes [3, 6, 3, 3, 4, 6, 6, 2].
          End scores = (49, 107)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22855, score0=12, score1=22, goal=98, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (12, 22).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 5, 3, 3, 2, 5, 3].
          End scores = (42, 22)
          >>> print(turns[1])
          Start scores = (42, 22).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 2, 6, 4, 6].
          End scores = (42, 48)
          >>> print(turns[2])
          Start scores = (42, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 3, 1, 4].
          End scores = (43, 48)
          >>> print(turns[3])
          Start scores = (43, 48).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 4, 5, 5, 3, 1, 2].
          End scores = (43, 49)
          >>> print(turns[4])
          Start scores = (43, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (48, 49)
          >>> print(turns[5])
          Start scores = (48, 49).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (48, 61)
          >>> print(turns[6])
          Start scores = (48, 61).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (53, 61)
          >>> print(turns[7])
          Start scores = (53, 61).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (53, 65)
          >>> print(turns[8])
          Start scores = (53, 65).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 3, 4, 1, 3].
          End scores = (54, 65)
          >>> print(turns[9])
          Start scores = (54, 65).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (66, 54)
          >>> print(turns[10])
          Start scores = (66, 54).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 5, 3, 2, 4, 5].
          End scores = (89, 54)
          >>> print(turns[11])
          Start scores = (89, 54).
          Player 1 rolls 9 dice and gets outcomes [4, 6, 6, 3, 5, 4, 3, 1, 5].
          End scores = (89, 55)
          >>> print(turns[12])
          Start scores = (89, 55).
          Player 0 rolls 8 dice and gets outcomes [2, 2, 6, 4, 2, 6, 5, 6].
          End scores = (122, 55)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=49015, score0=12, score1=5, goal=82, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (12, 5).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 1, 5, 1, 4, 1].
          End scores = (13, 5)
          >>> print(turns[1])
          Start scores = (13, 5).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 2, 5, 5, 6, 5, 4, 1, 2].
          End scores = (13, 6)
          >>> print(turns[2])
          Start scores = (13, 6).
          Player 0 rolls 6 dice and gets outcomes [2, 4, 2, 4, 2, 5].
          End scores = (32, 6)
          >>> print(turns[3])
          Start scores = (32, 6).
          Player 1 rolls 4 dice and gets outcomes [3, 5, 6, 6].
          End scores = (32, 26)
          >>> print(turns[4])
          Start scores = (32, 26).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 4, 5, 3, 2, 1].
          End scores = (33, 26)
          >>> print(turns[5])
          Start scores = (33, 26).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 1, 4, 1].
          End scores = (33, 27)
          >>> print(turns[6])
          Start scores = (33, 27).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 6, 2, 2, 4].
          End scores = (27, 57)
          >>> print(turns[7])
          Start scores = (27, 57).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 4, 6, 2, 6, 2].
          End scores = (27, 86)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=50497, score0=46, score1=5, goal=51, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (46, 5).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 1, 2, 5, 2].
          End scores = (47, 5)
          >>> print(turns[1])
          Start scores = (47, 5).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 6].
          End scores = (47, 20)
          >>> print(turns[2])
          Start scores = (47, 20).
          Player 0 rolls 8 dice and gets outcomes [6, 2, 3, 3, 3, 4, 2, 6].
          End scores = (76, 20)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=42297, score0=6, score1=22, goal=25, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (6, 22).
          Player 0 rolls 2 dice and gets outcomes [6, 1].
          End scores = (7, 22)
          >>> print(turns[1])
          Start scores = (7, 22).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 5, 1, 2, 2, 3, 4].
          End scores = (7, 23)
          >>> print(turns[2])
          Start scores = (7, 23).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 4, 2, 1, 5, 2, 1, 2, 1].
          End scores = (8, 23)
          >>> print(turns[3])
          Start scores = (8, 23).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 2, 5, 6, 5, 6, 4, 6, 4].
          End scores = (24, 8)
          >>> print(turns[4])
          Start scores = (24, 8).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 6].
          End scores = (25, 8)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=1726, score0=19, score1=5, goal=52, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (19, 5).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 3, 4, 3, 1, 5, 1, 5, 3].
          End scores = (20, 5)
          >>> print(turns[1])
          Start scores = (20, 5).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (7, 20)
          >>> print(turns[2])
          Start scores = (7, 20).
          Player 0 rolls 2 dice and gets outcomes [2, 3].
          End scores = (20, 12)
          >>> print(turns[3])
          Start scores = (20, 12).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (20, 15)
          >>> print(turns[4])
          Start scores = (20, 15).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 2, 6, 4, 6, 6, 4, 4, 4].
          End scores = (67, 15)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=17218, score0=19, score1=10, goal=50, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (19, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (21, 10)
          >>> print(turns[1])
          Start scores = (21, 10).
          Player 1 rolls 8 dice and gets outcomes [3, 1, 5, 2, 3, 3, 5, 1].
          End scores = (11, 21)
          >>> print(turns[2])
          Start scores = (11, 21).
          Player 0 rolls 4 dice and gets outcomes [1, 4, 6, 3].
          End scores = (12, 21)
          >>> print(turns[3])
          Start scores = (12, 21).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 2, 2, 5].
          End scores = (12, 38)
          >>> print(turns[4])
          Start scores = (12, 38).
          Player 0 rolls 6 dice and gets outcomes [3, 2, 5, 3, 5, 6].
          End scores = (36, 38)
          >>> print(turns[5])
          Start scores = (36, 38).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 6, 6].
          End scores = (36, 39)
          >>> print(turns[6])
          Start scores = (36, 39).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (39, 41)
          >>> print(turns[7])
          Start scores = (39, 41).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (39, 49)
          >>> print(turns[8])
          Start scores = (39, 49).
          Player 0 rolls 6 dice and gets outcomes [3, 4, 6, 1, 5, 2].
          End scores = (40, 49)
          >>> print(turns[9])
          Start scores = (40, 49).
          Player 1 rolls 8 dice and gets outcomes [2, 3, 3, 2, 2, 5, 5, 5].
          End scores = (40, 76)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=88988, score0=15, score1=95, goal=100, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 95).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 2, 4, 2, 1, 3, 2, 5].
          End scores = (16, 95)
          >>> print(turns[1])
          Start scores = (16, 95).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 3, 2, 6, 4, 6, 1, 2, 1].
          End scores = (16, 96)
          >>> print(turns[2])
          Start scores = (16, 96).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (22, 96)
          >>> print(turns[3])
          Start scores = (22, 96).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 3, 1, 5, 6, 2].
          End scores = (22, 97)
          >>> print(turns[4])
          Start scores = (22, 97).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 2, 3, 6, 1].
          End scores = (97, 23)
          >>> print(turns[5])
          Start scores = (97, 23).
          Player 1 rolls 8 dice and gets outcomes [4, 4, 1, 2, 3, 1, 4, 5].
          End scores = (97, 24)
          >>> print(turns[6])
          Start scores = (97, 24).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (103, 24)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8964, score0=79, score1=56, goal=83, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (79, 56).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 6, 6, 1, 6].
          End scores = (80, 56)
          >>> print(turns[1])
          Start scores = (80, 56).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 5, 1].
          End scores = (80, 57)
          >>> print(turns[2])
          Start scores = (80, 57).
          Player 0 rolls 9 dice and gets outcomes [2, 5, 6, 3, 5, 6, 6, 1, 4].
          End scores = (81, 57)
          >>> print(turns[3])
          Start scores = (81, 57).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 3, 3, 3, 2, 6, 3].
          End scores = (81, 86)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=24932, score0=12, score1=0, goal=14, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (12, 0).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 1, 3, 3, 2].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 5, 4, 3, 3, 5, 1].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 0 rolls 4 dice and gets outcomes [5, 3, 2, 3].
          End scores = (1, 26)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76726, score0=40, score1=73, goal=93, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (40, 73).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 1, 2, 5].
          End scores = (41, 73)
          >>> print(turns[1])
          Start scores = (41, 73).
          Player 1 rolls 3 dice and gets outcomes [6, 1, 4].
          End scores = (74, 41)
          >>> print(turns[2])
          Start scores = (74, 41).
          Player 0 rolls 3 dice and gets outcomes [2, 1, 6].
          End scores = (75, 41)
          >>> print(turns[3])
          Start scores = (75, 41).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (45, 75)
          >>> print(turns[4])
          Start scores = (45, 75).
          Player 0 rolls 9 dice and gets outcomes [1, 6, 4, 2, 5, 4, 1, 6, 2].
          End scores = (46, 75)
          >>> print(turns[5])
          Start scores = (46, 75).
          Player 1 rolls 5 dice and gets outcomes [5, 5, 3, 6, 1].
          End scores = (46, 76)
          >>> print(turns[6])
          Start scores = (46, 76).
          Player 0 rolls 10 dice and gets outcomes [2, 2, 5, 2, 4, 5, 6, 2, 5, 4].
          End scores = (76, 83)
          >>> print(turns[7])
          Start scores = (76, 83).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 3].
          End scores = (76, 91)
          >>> print(turns[8])
          Start scores = (76, 91).
          Player 0 rolls 2 dice and gets outcomes [6, 3].
          End scores = (85, 91)
          >>> print(turns[9])
          Start scores = (85, 91).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 3, 3, 3, 1, 5, 1].
          End scores = (85, 92)
          >>> print(turns[10])
          Start scores = (85, 92).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 5, 1, 4, 1, 2, 5, 3, 1].
          End scores = (86, 92)
          >>> print(turns[11])
          Start scores = (86, 92).
          Player 1 rolls 5 dice and gets outcomes [3, 4, 4, 6, 1].
          End scores = (86, 93)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85393, score0=3, score1=0, goal=44, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 0).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 3, 2, 6, 5].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (16, 1)
          >>> print(turns[3])
          Start scores = (16, 1).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 4, 6, 3, 2, 1, 1, 2, 3].
          End scores = (16, 2)
          >>> print(turns[4])
          Start scores = (16, 2).
          Player 0 rolls 2 dice and gets outcomes [4, 3].
          End scores = (23, 2)
          >>> print(turns[5])
          Start scores = (23, 2).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (4, 23)
          >>> print(turns[6])
          Start scores = (4, 23).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 1].
          End scores = (5, 23)
          >>> print(turns[7])
          Start scores = (5, 23).
          Player 1 rolls 8 dice and gets outcomes [6, 1, 1, 1, 1, 6, 4, 4].
          End scores = (5, 24)
          >>> print(turns[8])
          Start scores = (5, 24).
          Player 0 rolls 9 dice and gets outcomes [3, 4, 4, 1, 6, 2, 3, 5, 1].
          End scores = (6, 24)
          >>> print(turns[9])
          Start scores = (6, 24).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (6, 25)
          >>> print(turns[10])
          Start scores = (6, 25).
          Player 0 rolls 4 dice and gets outcomes [4, 6, 1, 3].
          End scores = (25, 7)
          >>> print(turns[11])
          Start scores = (25, 7).
          Player 1 rolls 9 dice and gets outcomes [4, 6, 5, 3, 1, 1, 2, 6, 3].
          End scores = (25, 8)
          >>> print(turns[12])
          Start scores = (25, 8).
          Player 0 rolls 7 dice and gets outcomes [2, 4, 1, 5, 4, 2, 1].
          End scores = (26, 8)
          >>> print(turns[13])
          Start scores = (26, 8).
          Player 1 rolls 9 dice and gets outcomes [1, 1, 4, 6, 2, 5, 6, 4, 6].
          End scores = (26, 9)
          >>> print(turns[14])
          Start scores = (26, 9).
          Player 0 rolls 2 dice and gets outcomes [2, 6].
          End scores = (34, 9)
          >>> print(turns[15])
          Start scores = (34, 9).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 1, 3, 3, 6, 2, 6].
          End scores = (34, 10)
          >>> print(turns[16])
          Start scores = (34, 10).
          Player 0 rolls 3 dice and gets outcomes [2, 3, 3].
          End scores = (42, 10)
          >>> print(turns[17])
          Start scores = (42, 10).
          Player 1 rolls 4 dice and gets outcomes [5, 2, 3, 1].
          End scores = (42, 11)
          >>> print(turns[18])
          Start scores = (42, 11).
          Player 0 rolls 2 dice and gets outcomes [1, 5].
          End scores = (43, 11)
          >>> print(turns[19])
          Start scores = (43, 11).
          Player 1 rolls 10 dice and gets outcomes [3, 5, 6, 3, 6, 2, 5, 5, 5, 2].
          End scores = (43, 53)
          >>> print(turns[20])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=35702, score0=10, score1=13, goal=14, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (10, 13).
          Player 0 rolls 4 dice and gets outcomes [5, 4, 6, 2].
          End scores = (13, 27)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=75713, score0=62, score1=6, goal=63, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (62, 6).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 2, 6, 4, 4, 6].
          End scores = (63, 6)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=14879, score0=24, score1=8, goal=29, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (24, 8).
          Player 0 rolls 4 dice and gets outcomes [1, 1, 6, 6].
          End scores = (25, 8)
          >>> print(turns[1])
          Start scores = (25, 8).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 5, 1, 4, 6, 3, 4].
          End scores = (25, 9)
          >>> print(turns[2])
          Start scores = (25, 9).
          Player 0 rolls 3 dice and gets outcomes [6, 3, 3].
          End scores = (37, 9)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=62742, score0=9, score1=5, goal=11, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 5).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 4].
          End scores = (18, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=99168, score0=34, score1=40, goal=95, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (34, 40).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (35, 40)
          >>> print(turns[1])
          Start scores = (35, 40).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 5].
          End scores = (35, 52)
          >>> print(turns[2])
          Start scores = (35, 52).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 5, 2, 6, 4, 4, 3, 1].
          End scores = (36, 52)
          >>> print(turns[3])
          Start scores = (36, 52).
          Player 1 rolls 5 dice and gets outcomes [4, 1, 5, 4, 4].
          End scores = (36, 53)
          >>> print(turns[4])
          Start scores = (36, 53).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (42, 53)
          >>> print(turns[5])
          Start scores = (42, 53).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 5, 5, 2, 1, 5, 1, 2, 2].
          End scores = (42, 54)
          >>> print(turns[6])
          Start scores = (42, 54).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (44, 54)
          >>> print(turns[7])
          Start scores = (44, 54).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 2].
          End scores = (44, 68)
          >>> print(turns[8])
          Start scores = (44, 68).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 2].
          End scores = (45, 68)
          >>> print(turns[9])
          Start scores = (45, 68).
          Player 1 rolls 9 dice and gets outcomes [6, 1, 6, 1, 1, 5, 1, 1, 5].
          End scores = (45, 72)
          >>> print(turns[10])
          Start scores = (45, 72).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (53, 72)
          >>> print(turns[11])
          Start scores = (53, 72).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 3, 6].
          End scores = (53, 90)
          >>> print(turns[12])
          Start scores = (53, 90).
          Player 0 rolls 10 dice and gets outcomes [1, 3, 2, 2, 3, 2, 4, 6, 2, 4].
          End scores = (57, 90)
          >>> print(turns[13])
          Start scores = (57, 90).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 2, 3, 3, 3, 5, 2, 3, 1].
          End scores = (57, 91)
          >>> print(turns[14])
          Start scores = (57, 91).
          Player 0 rolls 10 dice and gets outcomes [3, 1, 1, 1, 6, 5, 3, 2, 1, 1].
          End scores = (58, 91)
          >>> print(turns[15])
          Start scores = (58, 91).
          Player 1 rolls 6 dice and gets outcomes [1, 2, 4, 1, 5, 1].
          End scores = (58, 92)
          >>> print(turns[16])
          Start scores = (58, 92).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (64, 92)
          >>> print(turns[17])
          Start scores = (64, 92).
          Player 1 rolls 2 dice and gets outcomes [1, 5].
          End scores = (64, 93)
          >>> print(turns[18])
          Start scores = (64, 93).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 2, 2, 4, 3, 6, 5, 1, 5].
          End scores = (65, 93)
          >>> print(turns[19])
          Start scores = (65, 93).
          Player 1 rolls 9 dice and gets outcomes [6, 5, 1, 2, 5, 2, 3, 6, 4].
          End scores = (94, 65)
          >>> print(turns[20])
          Start scores = (94, 65).
          Player 0 rolls 8 dice and gets outcomes [4, 5, 3, 5, 2, 4, 2, 6].
          End scores = (125, 65)
          >>> print(turns[21])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=98804, score0=37, score1=45, goal=47, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (37, 45).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 3, 2].
          End scores = (38, 45)
          >>> print(turns[1])
          Start scores = (38, 45).
          Player 1 rolls 8 dice and gets outcomes [6, 5, 5, 3, 5, 5, 4, 3].
          End scores = (38, 81)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27518, score0=87, score1=16, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (87, 16).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 6, 6, 1, 5, 2].
          End scores = (88, 16)
          >>> print(turns[1])
          Start scores = (88, 16).
          Player 1 rolls 2 dice and gets outcomes [6, 1].
          End scores = (88, 17)
          >>> print(turns[2])
          Start scores = (88, 17).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 4, 2, 4, 5, 5, 4, 2, 1].
          End scores = (89, 17)
          >>> print(turns[3])
          Start scores = (89, 17).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 6, 2, 2, 2, 2, 3, 2, 2].
          End scores = (89, 18)
          >>> print(turns[4])
          Start scores = (89, 18).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 1, 2].
          End scores = (90, 18)
          >>> print(turns[5])
          Start scores = (90, 18).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 2, 2, 1, 3, 1].
          End scores = (90, 19)
          >>> print(turns[6])
          Start scores = (90, 19).
          Player 0 rolls 6 dice and gets outcomes [3, 5, 4, 2, 6, 1].
          End scores = (91, 19)
          >>> print(turns[7])
          Start scores = (91, 19).
          Player 1 rolls 6 dice and gets outcomes [6, 4, 1, 4, 5, 6].
          End scores = (91, 20)
          >>> print(turns[8])
          Start scores = (91, 20).
          Player 0 rolls 9 dice and gets outcomes [6, 3, 5, 5, 5, 5, 6, 1, 5].
          End scores = (92, 20)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=75062, score0=43, score1=5, goal=97, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (43, 5).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 4, 5, 6, 6, 5, 3].
          End scores = (44, 5)
          >>> print(turns[1])
          Start scores = (44, 5).
          Player 1 rolls 4 dice and gets outcomes [5, 5, 2, 4].
          End scores = (44, 21)
          >>> print(turns[2])
          Start scores = (44, 21).
          Player 0 rolls 3 dice and gets outcomes [6, 2, 1].
          End scores = (45, 21)
          >>> print(turns[3])
          Start scores = (45, 21).
          Player 1 rolls 9 dice and gets outcomes [1, 5, 3, 3, 4, 5, 5, 4, 6].
          End scores = (45, 22)
          >>> print(turns[4])
          Start scores = (45, 22).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 6, 6, 5, 3].
          End scores = (46, 22)
          >>> print(turns[5])
          Start scores = (46, 22).
          Player 1 rolls 3 dice and gets outcomes [2, 5, 2].
          End scores = (46, 31)
          >>> print(turns[6])
          Start scores = (46, 31).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 2, 6, 1, 1].
          End scores = (47, 31)
          >>> print(turns[7])
          Start scores = (47, 31).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 4, 6, 5, 5, 1, 1, 4].
          End scores = (47, 32)
          >>> print(turns[8])
          Start scores = (47, 32).
          Player 0 rolls 9 dice and gets outcomes [1, 2, 5, 6, 6, 3, 6, 2, 2].
          End scores = (32, 48)
          >>> print(turns[9])
          Start scores = (32, 48).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (32, 59)
          >>> print(turns[10])
          Start scores = (32, 59).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 4, 5, 4, 5, 5, 2, 1, 6].
          End scores = (33, 59)
          >>> print(turns[11])
          Start scores = (33, 59).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (33, 64)
          >>> print(turns[12])
          Start scores = (33, 64).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (34, 64)
          >>> print(turns[13])
          Start scores = (34, 64).
          Player 1 rolls 9 dice and gets outcomes [2, 4, 5, 6, 2, 2, 5, 3, 6].
          End scores = (34, 99)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=578, score0=7, score1=24, goal=30, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 24).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 3, 2, 5, 2, 5, 6, 6, 2].
          End scores = (24, 8)
          >>> print(turns[1])
          Start scores = (24, 8).
          Player 1 rolls 4 dice and gets outcomes [6, 3, 6, 2].
          End scores = (24, 25)
          >>> print(turns[2])
          Start scores = (24, 25).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (29, 25)
          >>> print(turns[3])
          Start scores = (29, 25).
          Player 1 rolls 4 dice and gets outcomes [5, 5, 1, 1].
          End scores = (29, 26)
          >>> print(turns[4])
          Start scores = (29, 26).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 3, 6, 2, 5, 1, 2].
          End scores = (30, 26)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=93942, score0=42, score1=41, goal=43, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (42, 41).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 2, 6, 1].
          End scores = (41, 43)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=48161, score0=15, score1=55, goal=83, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (55, 16)
          >>> print(turns[1])
          Start scores = (55, 16).
          Player 1 rolls 6 dice and gets outcomes [1, 4, 5, 6, 3, 6].
          End scores = (55, 17)
          >>> print(turns[2])
          Start scores = (55, 17).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 2, 5, 3, 1, 3, 4, 3].
          End scores = (56, 17)
          >>> print(turns[3])
          Start scores = (56, 17).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (56, 30)
          >>> print(turns[4])
          Start scores = (56, 30).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (62, 30)
          >>> print(turns[5])
          Start scores = (62, 30).
          Player 1 rolls 3 dice and gets outcomes [1, 6, 6].
          End scores = (62, 31)
          >>> print(turns[6])
          Start scores = (62, 31).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 2, 2, 5, 3].
          End scores = (63, 31)
          >>> print(turns[7])
          Start scores = (63, 31).
          Player 1 rolls 10 dice and gets outcomes [6, 1, 3, 1, 2, 5, 4, 5, 4, 5].
          End scores = (63, 32)
          >>> print(turns[8])
          Start scores = (63, 32).
          Player 0 rolls 6 dice and gets outcomes [4, 4, 2, 1, 3, 3].
          End scores = (64, 32)
          >>> print(turns[9])
          Start scores = (64, 32).
          Player 1 rolls 6 dice and gets outcomes [3, 3, 6, 3, 2, 2].
          End scores = (51, 64)
          >>> print(turns[10])
          Start scores = (51, 64).
          Player 0 rolls 5 dice and gets outcomes [6, 4, 3, 2, 1].
          End scores = (52, 64)
          >>> print(turns[11])
          Start scores = (52, 64).
          Player 1 rolls 4 dice and gets outcomes [5, 4, 1, 1].
          End scores = (52, 65)
          >>> print(turns[12])
          Start scores = (52, 65).
          Player 0 rolls 7 dice and gets outcomes [6, 3, 4, 3, 1, 6, 4].
          End scores = (53, 65)
          >>> print(turns[13])
          Start scores = (53, 65).
          Player 1 rolls 5 dice and gets outcomes [2, 3, 1, 6, 2].
          End scores = (53, 66)
          >>> print(turns[14])
          Start scores = (53, 66).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (66, 54)
          >>> print(turns[15])
          Start scores = (66, 54).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (66, 55)
          >>> print(turns[16])
          Start scores = (66, 55).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 2, 2].
          End scores = (67, 55)
          >>> print(turns[17])
          Start scores = (67, 55).
          Player 1 rolls 7 dice and gets outcomes [6, 5, 2, 1, 5, 3, 1].
          End scores = (67, 56)
          >>> print(turns[18])
          Start scores = (67, 56).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (80, 56)
          >>> print(turns[19])
          Start scores = (80, 56).
          Player 1 rolls 7 dice and gets outcomes [4, 2, 2, 2, 4, 4, 5].
          End scores = (79, 80)
          >>> print(turns[20])
          Start scores = (79, 80).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (86, 80)
          >>> print(turns[21])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=52136, score0=2, score1=14, goal=15, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 14).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 1, 5].
          End scores = (3, 14)
          >>> print(turns[1])
          Start scores = (3, 14).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (3, 15)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=30971, score0=11, score1=12, goal=25, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 12).
          Player 0 rolls 9 dice and gets outcomes [2, 2, 1, 2, 6, 5, 4, 6, 3].
          End scores = (12, 12)
          >>> print(turns[1])
          Start scores = (12, 12).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 4, 1].
          End scores = (12, 13)
          >>> print(turns[2])
          Start scores = (12, 13).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 6, 5, 3, 5].
          End scores = (37, 13)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=69948, score0=11, score1=19, goal=43, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 19).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 6, 6, 2, 6, 1, 6, 4].
          End scores = (12, 19)
          >>> print(turns[1])
          Start scores = (12, 19).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 5, 6, 1, 3].
          End scores = (20, 12)
          >>> print(turns[2])
          Start scores = (20, 12).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (21, 12)
          >>> print(turns[3])
          Start scores = (21, 12).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 5, 6, 6, 5, 6, 2, 3, 5].
          End scores = (21, 60)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=33856, score0=9, score1=9, goal=19, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 9).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 3 dice and gets outcomes [5, 5, 6].
          End scores = (12, 25)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=93176, score0=7, score1=37, goal=80, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 37).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (17, 37)
          >>> print(turns[1])
          Start scores = (17, 37).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (17, 45)
          >>> print(turns[2])
          Start scores = (17, 45).
          Player 0 rolls 6 dice and gets outcomes [6, 6, 6, 6, 3, 6].
          End scores = (50, 45)
          >>> print(turns[3])
          Start scores = (50, 45).
          Player 1 rolls 5 dice and gets outcomes [4, 6, 4, 1, 3].
          End scores = (50, 46)
          >>> print(turns[4])
          Start scores = (50, 46).
          Player 0 rolls 8 dice and gets outcomes [2, 6, 4, 6, 1, 4, 4, 5].
          End scores = (51, 46)
          >>> print(turns[5])
          Start scores = (51, 46).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (51, 49)
          >>> print(turns[6])
          Start scores = (51, 49).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 1, 5, 1, 2].
          End scores = (52, 49)
          >>> print(turns[7])
          Start scores = (52, 49).
          Player 1 rolls 10 dice and gets outcomes [1, 2, 3, 6, 1, 4, 5, 4, 4, 4].
          End scores = (52, 50)
          >>> print(turns[8])
          Start scores = (52, 50).
          Player 0 rolls 10 dice and gets outcomes [6, 4, 1, 1, 1, 5, 5, 3, 1, 2].
          End scores = (53, 50)
          >>> print(turns[9])
          Start scores = (53, 50).
          Player 1 rolls 4 dice and gets outcomes [4, 2, 1, 5].
          End scores = (53, 51)
          >>> print(turns[10])
          Start scores = (53, 51).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 5, 2, 6, 4, 5, 2].
          End scores = (84, 51)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85986, score0=35, score1=12, goal=74, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (35, 12).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 3, 4, 3, 3, 6, 5, 1, 2].
          End scores = (36, 12)
          >>> print(turns[1])
          Start scores = (36, 12).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 6, 1].
          End scores = (36, 13)
          >>> print(turns[2])
          Start scores = (36, 13).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 3, 6, 4].
          End scores = (54, 13)
          >>> print(turns[3])
          Start scores = (54, 13).
          Player 1 rolls 10 dice and gets outcomes [2, 5, 1, 6, 3, 6, 4, 3, 3, 5].
          End scores = (54, 14)
          >>> print(turns[4])
          Start scores = (54, 14).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 3].
          End scores = (61, 14)
          >>> print(turns[5])
          Start scores = (61, 14).
          Player 1 rolls 2 dice and gets outcomes [4, 5].
          End scores = (23, 61)
          >>> print(turns[6])
          Start scores = (23, 61).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (28, 61)
          >>> print(turns[7])
          Start scores = (28, 61).
          Player 1 rolls 4 dice and gets outcomes [6, 3, 6, 5].
          End scores = (28, 81)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76820, score0=28, score1=14, goal=61, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (28, 14).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 1].
          End scores = (29, 14)
          >>> print(turns[1])
          Start scores = (29, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (29, 17)
          >>> print(turns[2])
          Start scores = (29, 17).
          Player 0 rolls 5 dice and gets outcomes [1, 1, 1, 3, 3].
          End scores = (30, 17)
          >>> print(turns[3])
          Start scores = (30, 17).
          Player 1 rolls 9 dice and gets outcomes [6, 6, 6, 4, 2, 5, 4, 1, 5].
          End scores = (30, 18)
          >>> print(turns[4])
          Start scores = (30, 18).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 6, 5, 4, 4, 5, 3, 5].
          End scores = (70, 18)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=83984, score0=64, score1=49, goal=78, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (64, 49).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 3, 5, 6, 3, 4].
          End scores = (93, 49)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25773, score0=3, score1=17, goal=30, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 17).
          Player 0 rolls 5 dice and gets outcomes [3, 4, 5, 4, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 4].
          End scores = (25, 18)
          >>> print(turns[2])
          Start scores = (25, 18).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 5, 3].
          End scores = (26, 18)
          >>> print(turns[3])
          Start scores = (26, 18).
          Player 1 rolls 8 dice and gets outcomes [1, 4, 3, 2, 1, 5, 6, 2].
          End scores = (26, 19)
          >>> print(turns[4])
          Start scores = (26, 19).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 6, 2, 1, 5, 2, 1, 1].
          End scores = (27, 19)
          >>> print(turns[5])
          Start scores = (27, 19).
          Player 1 rolls 10 dice and gets outcomes [5, 6, 6, 4, 2, 5, 3, 3, 2, 4].
          End scores = (27, 59)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=6012, score0=30, score1=3, goal=85, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (30, 3).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (36, 3)
          >>> print(turns[1])
          Start scores = (36, 3).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (4, 36)
          >>> print(turns[2])
          Start scores = (4, 36).
          Player 0 rolls 4 dice and gets outcomes [4, 6, 2, 4].
          End scores = (20, 36)
          >>> print(turns[3])
          Start scores = (20, 36).
          Player 1 rolls 6 dice and gets outcomes [2, 4, 2, 4, 3, 3].
          End scores = (20, 54)
          >>> print(turns[4])
          Start scores = (20, 54).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (54, 30)
          >>> print(turns[5])
          Start scores = (54, 30).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (54, 34)
          >>> print(turns[6])
          Start scores = (54, 34).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 6, 6, 5].
          End scores = (34, 81)
          >>> print(turns[7])
          Start scores = (34, 81).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (34, 83)
          >>> print(turns[8])
          Start scores = (34, 83).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (42, 83)
          >>> print(turns[9])
          Start scores = (42, 83).
          Player 1 rolls 2 dice and gets outcomes [5, 1].
          End scores = (42, 84)
          >>> print(turns[10])
          Start scores = (42, 84).
          Player 0 rolls 4 dice and gets outcomes [1, 4, 2, 4].
          End scores = (43, 84)
          >>> print(turns[11])
          Start scores = (43, 84).
          Player 1 rolls 10 dice and gets outcomes [5, 3, 3, 4, 1, 1, 5, 6, 1, 1].
          End scores = (85, 43)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=56692, score0=69, score1=40, goal=71, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (69, 40).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 6, 4, 4, 1].
          End scores = (70, 40)
          >>> print(turns[1])
          Start scores = (70, 40).
          Player 1 rolls 3 dice and gets outcomes [3, 3, 4].
          End scores = (50, 70)
          >>> print(turns[2])
          Start scores = (50, 70).
          Player 0 rolls 2 dice and gets outcomes [5, 5].
          End scores = (60, 70)
          >>> print(turns[3])
          Start scores = (60, 70).
          Player 1 rolls 3 dice and gets outcomes [6, 2, 5].
          End scores = (60, 83)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11528, score0=6, score1=7, goal=17, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (6, 7).
          Player 0 rolls 3 dice and gets outcomes [2, 6, 2].
          End scores = (16, 7)
          >>> print(turns[1])
          Start scores = (16, 7).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 1, 5, 2, 6, 5, 5].
          End scores = (16, 8)
          >>> print(turns[2])
          Start scores = (16, 8).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 2, 1].
          End scores = (17, 8)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=95684, score0=3, score1=1, goal=10, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 1).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (6, 1)
          >>> print(turns[1])
          Start scores = (6, 1).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 3, 5, 1, 6, 2, 6].
          End scores = (6, 2)
          >>> print(turns[2])
          Start scores = (6, 2).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 5, 5, 4].
          End scores = (10, 2)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=81397, score0=45, score1=40, goal=52, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (45, 40).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 3].
          End scores = (59, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22637, score0=32, score1=11, goal=58, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (32, 11).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 5, 5, 5].
          End scores = (59, 11)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11998, score0=16, score1=21, goal=67, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (16, 21).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (21, 20)
          >>> print(turns[1])
          Start scores = (21, 20).
          Player 1 rolls 10 dice and gets outcomes [2, 3, 5, 6, 3, 3, 6, 2, 1, 6].
          End scores = (21, 21)
          >>> print(turns[2])
          Start scores = (21, 21).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (25, 21)
          >>> print(turns[3])
          Start scores = (25, 21).
          Player 1 rolls 3 dice and gets outcomes [5, 3, 4].
          End scores = (25, 33)
          >>> print(turns[4])
          Start scores = (25, 33).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 3, 4, 2, 3, 4, 3, 6, 2].
          End scores = (60, 33)
          >>> print(turns[5])
          Start scores = (60, 33).
          Player 1 rolls 4 dice and gets outcomes [5, 6, 4, 6].
          End scores = (60, 54)
          >>> print(turns[6])
          Start scores = (60, 54).
          Player 0 rolls 5 dice and gets outcomes [2, 6, 3, 2, 1].
          End scores = (54, 61)
          >>> print(turns[7])
          Start scores = (54, 61).
          Player 1 rolls 2 dice and gets outcomes [3, 6].
          End scores = (70, 54)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=69783, score0=11, score1=13, goal=38, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 13).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (21, 13)
          >>> print(turns[1])
          Start scores = (21, 13).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (19, 21)
          >>> print(turns[2])
          Start scores = (19, 21).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 5, 6, 4, 3, 5, 1, 1].
          End scores = (21, 20)
          >>> print(turns[3])
          Start scores = (21, 20).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (21, 21)
          >>> print(turns[4])
          Start scores = (21, 21).
          Player 0 rolls 3 dice and gets outcomes [6, 6, 3].
          End scores = (36, 21)
          >>> print(turns[5])
          Start scores = (36, 21).
          Player 1 rolls 5 dice and gets outcomes [6, 5, 5, 4, 3].
          End scores = (44, 36)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=37364, score0=29, score1=22, goal=35, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (29, 22).
          Player 0 rolls 4 dice and gets outcomes [1, 6, 1, 6].
          End scores = (30, 22)
          >>> print(turns[1])
          Start scores = (30, 22).
          Player 1 rolls 3 dice and gets outcomes [5, 6, 6].
          End scores = (30, 39)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5143, score0=2, score1=15, goal=79, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 15).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 6, 6, 4].
          End scores = (28, 15)
          >>> print(turns[1])
          Start scores = (28, 15).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (28, 19)
          >>> print(turns[2])
          Start scores = (28, 19).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 2, 3, 4].
          End scores = (43, 19)
          >>> print(turns[3])
          Start scores = (43, 19).
          Player 1 rolls 6 dice and gets outcomes [6, 2, 2, 2, 4, 3].
          End scores = (41, 43)
          >>> print(turns[4])
          Start scores = (41, 43).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 6, 1, 4, 5, 1, 5, 5, 3].
          End scores = (43, 42)
          >>> print(turns[5])
          Start scores = (43, 42).
          Player 1 rolls 7 dice and gets outcomes [2, 1, 2, 6, 2, 1, 5].
          End scores = (43, 43)
          >>> print(turns[6])
          Start scores = (43, 43).
          Player 0 rolls 8 dice and gets outcomes [2, 5, 3, 3, 2, 4, 4, 4].
          End scores = (70, 43)
          >>> print(turns[7])
          Start scores = (70, 43).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 6, 2, 5, 6, 4].
          End scores = (70, 72)
          >>> print(turns[8])
          Start scores = (70, 72).
          Player 0 rolls 2 dice and gets outcomes [1, 5].
          End scores = (71, 72)
          >>> print(turns[9])
          Start scores = (71, 72).
          Player 1 rolls 5 dice and gets outcomes [2, 2, 4, 2, 3].
          End scores = (71, 85)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=82888, score0=26, score1=39, goal=87, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (26, 39).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 3, 4, 3, 6, 5, 2, 6].
          End scores = (63, 39)
          >>> print(turns[1])
          Start scores = (63, 39).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (63, 54)
          >>> print(turns[2])
          Start scores = (63, 54).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 2, 4].
          End scores = (64, 54)
          >>> print(turns[3])
          Start scores = (64, 54).
          Player 1 rolls 4 dice and gets outcomes [4, 5, 5, 4].
          End scores = (64, 72)
          >>> print(turns[4])
          Start scores = (64, 72).
          Player 0 rolls 3 dice and gets outcomes [4, 2, 2].
          End scores = (75, 72)
          >>> print(turns[5])
          Start scores = (75, 72).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 3, 4, 1].
          End scores = (75, 73)
          >>> print(turns[6])
          Start scores = (75, 73).
          Player 0 rolls 8 dice and gets outcomes [2, 6, 1, 6, 2, 1, 4, 3].
          End scores = (76, 73)
          >>> print(turns[7])
          Start scores = (76, 73).
          Player 1 rolls 3 dice and gets outcomes [1, 4, 1].
          End scores = (76, 77)
          >>> print(turns[8])
          Start scores = (76, 77).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 3, 2, 5, 5, 2].
          End scores = (77, 77)
          >>> print(turns[9])
          Start scores = (77, 77).
          Player 1 rolls 2 dice and gets outcomes [1, 2].
          End scores = (77, 78)
          >>> print(turns[10])
          Start scores = (77, 78).
          Player 0 rolls 3 dice and gets outcomes [4, 2, 3].
          End scores = (89, 78)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25835, score0=15, score1=64, goal=95, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 64).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (19, 64)
          >>> print(turns[1])
          Start scores = (19, 64).
          Player 1 rolls 10 dice and gets outcomes [3, 2, 3, 4, 3, 1, 2, 1, 3, 1].
          End scores = (65, 19)
          >>> print(turns[2])
          Start scores = (65, 19).
          Player 0 rolls 9 dice and gets outcomes [6, 6, 4, 4, 2, 3, 4, 2, 5].
          End scores = (19, 101)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85071, score0=86, score1=5, goal=89, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (86, 5).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 2, 6, 4, 5, 6].
          End scores = (87, 5)
          >>> print(turns[1])
          Start scores = (87, 5).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (87, 7)
          >>> print(turns[2])
          Start scores = (87, 7).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 1, 3, 5].
          End scores = (88, 7)
          >>> print(turns[3])
          Start scores = (88, 7).
          Player 1 rolls 6 dice and gets outcomes [6, 6, 5, 5, 3, 4].
          End scores = (36, 88)
          >>> print(turns[4])
          Start scores = (36, 88).
          Player 0 rolls 2 dice and gets outcomes [4, 2].
          End scores = (42, 88)
          >>> print(turns[5])
          Start scores = (42, 88).
          Player 1 rolls 3 dice and gets outcomes [5, 5, 4].
          End scores = (42, 102)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=23577, score0=32, score1=23, goal=45, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (32, 23).
          Player 0 rolls 7 dice and gets outcomes [1, 4, 6, 5, 3, 6, 4].
          End scores = (33, 23)
          >>> print(turns[1])
          Start scores = (33, 23).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 3, 5, 3, 6, 6, 5].
          End scores = (33, 24)
          >>> print(turns[2])
          Start scores = (33, 24).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (34, 24)
          >>> print(turns[3])
          Start scores = (34, 24).
          Player 1 rolls 7 dice and gets outcomes [4, 4, 5, 2, 6, 4, 2].
          End scores = (51, 34)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=663, score0=44, score1=13, goal=59, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (44, 13).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (48, 13)
          >>> print(turns[1])
          Start scores = (48, 13).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (48, 18)
          >>> print(turns[2])
          Start scores = (48, 18).
          Player 0 rolls 7 dice and gets outcomes [6, 6, 4, 5, 3, 5, 5].
          End scores = (82, 18)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=6543, score0=65, score1=70, goal=87, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (65, 70).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (68, 70)
          >>> print(turns[1])
          Start scores = (68, 70).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 3, 3, 2, 3, 6, 6, 2].
          End scores = (68, 103)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=31919, score0=2, score1=16, goal=28, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (2, 16).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (10, 16)
          >>> print(turns[1])
          Start scores = (10, 16).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (10, 21)
          >>> print(turns[2])
          Start scores = (10, 21).
          Player 0 rolls 2 dice and gets outcomes [6, 2].
          End scores = (18, 21)
          >>> print(turns[3])
          Start scores = (18, 21).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 2, 5, 2, 4, 1].
          End scores = (22, 18)
          >>> print(turns[4])
          Start scores = (22, 18).
          Player 0 rolls 10 dice and gets outcomes [3, 2, 2, 5, 4, 1, 2, 2, 3, 5].
          End scores = (18, 23)
          >>> print(turns[5])
          Start scores = (18, 23).
          Player 1 rolls 3 dice and gets outcomes [3, 5, 4].
          End scores = (18, 35)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=67699, score0=24, score1=17, goal=28, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (24, 17).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 3, 6, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 2 dice and gets outcomes [4, 3].
          End scores = (25, 27)
          >>> print(turns[2])
          Start scores = (25, 27).
          Player 0 rolls 6 dice and gets outcomes [5, 4, 3, 4, 4, 5].
          End scores = (50, 27)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25815, score0=52, score1=11, goal=54, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (52, 11).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 5, 4, 2, 4, 3, 1, 5].
          End scores = (53, 11)
          >>> print(turns[1])
          Start scores = (53, 11).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 1, 2, 6].
          End scores = (53, 12)
          >>> print(turns[2])
          Start scores = (53, 12).
          Player 0 rolls 6 dice and gets outcomes [4, 5, 6, 3, 1, 4].
          End scores = (54, 12)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=41969, score0=38, score1=54, goal=78, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (38, 54).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (39, 54)
          >>> print(turns[1])
          Start scores = (39, 54).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 5, 6].
          End scores = (39, 55)
          >>> print(turns[2])
          Start scores = (39, 55).
          Player 0 rolls 3 dice and gets outcomes [2, 4, 1].
          End scores = (40, 55)
          >>> print(turns[3])
          Start scores = (40, 55).
          Player 1 rolls 8 dice and gets outcomes [4, 5, 6, 4, 2, 2, 5, 2].
          End scores = (40, 85)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=68309, score0=53, score1=40, goal=56, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (53, 40).
          Player 0 rolls 7 dice and gets outcomes [2, 4, 3, 5, 6, 2, 2].
          End scores = (77, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8243, score0=28, score1=23, goal=30, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (28, 23).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 5, 2, 6, 5].
          End scores = (52, 23)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=43015, score0=53, score1=74, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (53, 74).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 6, 6, 1, 4, 3, 5, 3, 2].
          End scores = (74, 54)
          >>> print(turns[1])
          Start scores = (74, 54).
          Player 1 rolls 2 dice and gets outcomes [1, 6].
          End scores = (74, 58)
          >>> print(turns[2])
          Start scores = (74, 58).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (80, 58)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76012, score0=39, score1=36, goal=73, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (39, 36).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (36, 40)
          >>> print(turns[1])
          Start scores = (36, 40).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 6].
          End scores = (36, 58)
          >>> print(turns[2])
          Start scores = (36, 58).
          Player 0 rolls 9 dice and gets outcomes [6, 6, 2, 1, 3, 3, 2, 3, 5].
          End scores = (37, 58)
          >>> print(turns[3])
          Start scores = (37, 58).
          Player 1 rolls 3 dice and gets outcomes [3, 6, 2].
          End scores = (37, 69)
          >>> print(turns[4])
          Start scores = (37, 69).
          Player 0 rolls 4 dice and gets outcomes [6, 3, 5, 1].
          End scores = (38, 69)
          >>> print(turns[5])
          Start scores = (38, 69).
          Player 1 rolls 6 dice and gets outcomes [1, 5, 1, 6, 6, 6].
          End scores = (38, 70)
          >>> print(turns[6])
          Start scores = (38, 70).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 2, 4, 4, 4, 5, 5].
          End scores = (39, 70)
          >>> print(turns[7])
          Start scores = (39, 70).
          Player 1 rolls 2 dice and gets outcomes [5, 1].
          End scores = (39, 71)
          >>> print(turns[8])
          Start scores = (39, 71).
          Player 0 rolls 8 dice and gets outcomes [4, 3, 4, 1, 4, 3, 1, 1].
          End scores = (40, 71)
          >>> print(turns[9])
          Start scores = (40, 71).
          Player 1 rolls 2 dice and gets outcomes [4, 2].
          End scores = (40, 77)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=9818, score0=11, score1=9, goal=64, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (11, 9).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 3, 6, 6, 4, 1, 1, 2].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 2, 6].
          End scores = (12, 10)
          >>> print(turns[2])
          Start scores = (12, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (14, 10)
          >>> print(turns[3])
          Start scores = (14, 10).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (13, 14)
          >>> print(turns[4])
          Start scores = (13, 14).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 6, 5].
          End scores = (33, 14)
          >>> print(turns[5])
          Start scores = (33, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (33, 26)
          >>> print(turns[6])
          Start scores = (33, 26).
          Player 0 rolls 4 dice and gets outcomes [5, 4, 2, 3].
          End scores = (47, 26)
          >>> print(turns[7])
          Start scores = (47, 26).
          Player 1 rolls 5 dice and gets outcomes [3, 6, 6, 3, 1].
          End scores = (47, 27)
          >>> print(turns[8])
          Start scores = (47, 27).
          Player 0 rolls 4 dice and gets outcomes [5, 3, 3, 3].
          End scores = (61, 27)
          >>> print(turns[9])
          Start scores = (61, 27).
          Player 1 rolls 10 dice and gets outcomes [2, 6, 3, 2, 5, 4, 4, 4, 5, 4].
          End scores = (61, 66)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25916, score0=86, score1=24, goal=88, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (86, 24).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 5, 5, 1].
          End scores = (87, 24)
          >>> print(turns[1])
          Start scores = (87, 24).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 4, 2, 5, 2, 2, 2].
          End scores = (87, 50)
          >>> print(turns[2])
          Start scores = (87, 50).
          Player 0 rolls 7 dice and gets outcomes [1, 2, 4, 1, 6, 4, 2].
          End scores = (88, 50)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=15583, score0=11, score1=40, goal=55, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (11, 40).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (14, 40)
          >>> print(turns[1])
          Start scores = (14, 40).
          Player 1 rolls 2 dice and gets outcomes [1, 2].
          End scores = (14, 44)
          >>> print(turns[2])
          Start scores = (14, 44).
          Player 0 rolls 10 dice and gets outcomes [3, 5, 4, 4, 2, 5, 1, 2, 1, 2].
          End scores = (15, 44)
          >>> print(turns[3])
          Start scores = (15, 44).
          Player 1 rolls 6 dice and gets outcomes [1, 4, 6, 4, 2, 1].
          End scores = (15, 45)
          >>> print(turns[4])
          Start scores = (15, 45).
          Player 0 rolls 7 dice and gets outcomes [3, 3, 5, 4, 3, 4, 1].
          End scores = (16, 45)
          >>> print(turns[5])
          Start scores = (16, 45).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 2, 2, 2, 5].
          End scores = (64, 16)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=7242, score0=19, score1=46, goal=98, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (19, 46).
          Player 0 rolls 8 dice and gets outcomes [2, 2, 3, 5, 4, 1, 1, 3].
          End scores = (20, 46)
          >>> print(turns[1])
          Start scores = (20, 46).
          Player 1 rolls 8 dice and gets outcomes [1, 1, 6, 6, 5, 3, 1, 4].
          End scores = (20, 47)
          >>> print(turns[2])
          Start scores = (20, 47).
          Player 0 rolls 10 dice and gets outcomes [4, 5, 4, 6, 1, 1, 6, 2, 3, 1].
          End scores = (21, 47)
          >>> print(turns[3])
          Start scores = (21, 47).
          Player 1 rolls 7 dice and gets outcomes [1, 5, 4, 4, 5, 3, 2].
          End scores = (21, 48)
          >>> print(turns[4])
          Start scores = (21, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 1, 1, 1].
          End scores = (22, 48)
          >>> print(turns[5])
          Start scores = (22, 48).
          Player 1 rolls 5 dice and gets outcomes [1, 1, 6, 6, 3].
          End scores = (49, 22)
          >>> print(turns[6])
          Start scores = (49, 22).
          Player 0 rolls 3 dice and gets outcomes [5, 3, 2].
          End scores = (22, 62)
          >>> print(turns[7])
          Start scores = (22, 62).
          Player 1 rolls 9 dice and gets outcomes [2, 3, 4, 5, 3, 1, 6, 1, 6].
          End scores = (63, 22)
          >>> print(turns[8])
          Start scores = (63, 22).
          Player 0 rolls 6 dice and gets outcomes [6, 3, 2, 1, 1, 3].
          End scores = (64, 22)
          >>> print(turns[9])
          Start scores = (64, 22).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (64, 28)
          >>> print(turns[10])
          Start scores = (64, 28).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 6].
          End scores = (68, 28)
          >>> print(turns[11])
          Start scores = (68, 28).
          Player 1 rolls 9 dice and gets outcomes [3, 2, 2, 5, 6, 2, 6, 3, 3].
          End scores = (60, 68)
          >>> print(turns[12])
          Start scores = (60, 68).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 4, 4, 1, 4, 2].
          End scores = (68, 61)
          >>> print(turns[13])
          Start scores = (68, 61).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (68, 65)
          >>> print(turns[14])
          Start scores = (68, 65).
          Player 0 rolls 5 dice and gets outcomes [5, 5, 1, 3, 4].
          End scores = (69, 65)
          >>> print(turns[15])
          Start scores = (69, 65).
          Player 1 rolls 6 dice and gets outcomes [1, 2, 1, 5, 3, 1].
          End scores = (69, 69)
          >>> print(turns[16])
          Start scores = (69, 69).
          Player 0 rolls 3 dice and gets outcomes [2, 3, 3].
          End scores = (80, 69)
          >>> print(turns[17])
          Start scores = (80, 69).
          Player 1 rolls 7 dice and gets outcomes [1, 5, 4, 3, 2, 1, 6].
          End scores = (80, 70)
          >>> print(turns[18])
          Start scores = (80, 70).
          Player 0 rolls 3 dice and gets outcomes [3, 6, 5].
          End scores = (70, 94)
          >>> print(turns[19])
          Start scores = (70, 94).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 2, 4, 5, 6, 3].
          End scores = (70, 125)
          >>> print(turns[20])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=74122, score0=18, score1=14, goal=32, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (18, 14).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 5, 2, 2, 6, 1].
          End scores = (19, 14)
          >>> print(turns[1])
          Start scores = (19, 14).
          Player 1 rolls 3 dice and gets outcomes [1, 3, 3].
          End scores = (19, 15)
          >>> print(turns[2])
          Start scores = (19, 15).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 4, 3, 6, 3, 2, 5, 6].
          End scores = (15, 56)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59593, score0=27, score1=9, goal=40, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (27, 9).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (9, 32)
          >>> print(turns[1])
          Start scores = (9, 32).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 2, 2].
          End scores = (9, 44)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8128, score0=17, score1=8, goal=29, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (17, 8).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 4, 5].
          End scores = (8, 32)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22810, score0=7, score1=0, goal=43, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 0).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (15, 0)
          >>> print(turns[1])
          Start scores = (15, 0).
          Player 1 rolls 2 dice and gets outcomes [2, 1].
          End scores = (15, 1)
          >>> print(turns[2])
          Start scores = (15, 1).
          Player 0 rolls 8 dice and gets outcomes [4, 1, 1, 3, 1, 4, 3, 5].
          End scores = (16, 1)
          >>> print(turns[3])
          Start scores = (16, 1).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (16, 4)
          >>> print(turns[4])
          Start scores = (16, 4).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 6, 3, 1, 5, 4, 3, 1, 2].
          End scores = (17, 4)
          >>> print(turns[5])
          Start scores = (17, 4).
          Player 1 rolls 2 dice and gets outcomes [6, 5].
          End scores = (15, 17)
          >>> print(turns[6])
          Start scores = (15, 17).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 6, 6, 6, 2, 1, 5, 2, 4].
          End scores = (16, 17)
          >>> print(turns[7])
          Start scores = (16, 17).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 5].
          End scores = (16, 31)
          >>> print(turns[8])
          Start scores = (16, 31).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 3, 5].
          End scores = (36, 31)
          >>> print(turns[9])
          Start scores = (36, 31).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 5, 6].
          End scores = (36, 32)
          >>> print(turns[10])
          Start scores = (36, 32).
          Player 0 rolls 8 dice and gets outcomes [5, 2, 3, 6, 4, 3, 5, 3].
          End scores = (67, 32)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59348, score0=95, score1=84, goal=97, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (95, 84).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (97, 84)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=88169, score0=23, score1=40, goal=79, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (23, 40).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 6].
          End scores = (24, 40)
          >>> print(turns[1])
          Start scores = (24, 40).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 6, 6, 2, 3, 3].
          End scores = (24, 68)
          >>> print(turns[2])
          Start scores = (24, 68).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 4].
          End scores = (39, 68)
          >>> print(turns[3])
          Start scores = (39, 68).
          Player 1 rolls 5 dice and gets outcomes [2, 3, 5, 1, 6].
          End scores = (39, 69)
          >>> print(turns[4])
          Start scores = (39, 69).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (49, 69)
          >>> print(turns[5])
          Start scores = (49, 69).
          Player 1 rolls 5 dice and gets outcomes [6, 6, 4, 5, 3].
          End scores = (49, 93)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=70467, score0=61, score1=74, goal=97, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (61, 74).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (69, 74)
          >>> print(turns[1])
          Start scores = (69, 74).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 3, 1, 5, 1, 5, 6].
          End scores = (69, 75)
          >>> print(turns[2])
          Start scores = (69, 75).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 4, 1, 5, 6].
          End scores = (70, 75)
          >>> print(turns[3])
          Start scores = (70, 75).
          Player 1 rolls 6 dice and gets outcomes [6, 4, 6, 1, 5, 3].
          End scores = (70, 76)
          >>> print(turns[4])
          Start scores = (70, 76).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 1, 3, 3, 6, 1].
          End scores = (71, 76)
          >>> print(turns[5])
          Start scores = (71, 76).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 6, 4, 5, 3, 1].
          End scores = (71, 77)
          >>> print(turns[6])
          Start scores = (71, 77).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 4].
          End scores = (77, 87)
          >>> print(turns[7])
          Start scores = (77, 87).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (77, 88)
          >>> print(turns[8])
          Start scores = (77, 88).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 3, 3].
          End scores = (91, 88)
          >>> print(turns[9])
          Start scores = (91, 88).
          Player 1 rolls 3 dice and gets outcomes [4, 1, 2].
          End scores = (91, 89)
          >>> print(turns[10])
          Start scores = (91, 89).
          Player 0 rolls 10 dice and gets outcomes [4, 2, 2, 6, 4, 2, 3, 5, 4, 6].
          End scores = (129, 89)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8714, score0=38, score1=19, goal=57, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (38, 19).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (45, 19)
          >>> print(turns[1])
          Start scores = (45, 19).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 1, 1, 4, 5, 5, 4, 6].
          End scores = (45, 20)
          >>> print(turns[2])
          Start scores = (45, 20).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 3, 4, 3, 5, 1, 5].
          End scores = (46, 20)
          >>> print(turns[3])
          Start scores = (46, 20).
          Player 1 rolls 4 dice and gets outcomes [4, 2, 5, 5].
          End scores = (46, 36)
          >>> print(turns[4])
          Start scores = (46, 36).
          Player 0 rolls 8 dice and gets outcomes [5, 4, 2, 1, 5, 4, 3, 6].
          End scores = (47, 36)
          >>> print(turns[5])
          Start scores = (47, 36).
          Player 1 rolls 6 dice and gets outcomes [1, 5, 1, 3, 3, 4].
          End scores = (37, 47)
          >>> print(turns[6])
          Start scores = (37, 47).
          Player 0 rolls 5 dice and gets outcomes [6, 5, 4, 2, 6].
          End scores = (60, 47)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=13230, score0=65, score1=56, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (65, 56).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 2, 1, 3, 4].
          End scores = (66, 56)
          >>> print(turns[1])
          Start scores = (66, 56).
          Player 1 rolls 2 dice and gets outcomes [2, 5].
          End scores = (66, 66)
          >>> print(turns[2])
          Start scores = (66, 66).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 1, 5, 3, 6, 1, 3, 5].
          End scores = (67, 66)
          >>> print(turns[3])
          Start scores = (67, 66).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 6, 6, 3, 6, 1].
          End scores = (67, 67)
          >>> print(turns[4])
          Start scores = (67, 67).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 1, 4, 3, 4, 1, 3, 2].
          End scores = (68, 67)
          >>> print(turns[5])
          Start scores = (68, 67).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 6].
          End scores = (68, 81)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=96667, score0=2, score1=3, goal=13, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 3).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 3, 5, 3, 6, 6, 4, 1].
          End scores = (3, 3)
          >>> print(turns[1])
          Start scores = (3, 3).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 5].
          End scores = (3, 13)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27904, score0=23, score1=39, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (23, 39).
          Player 0 rolls 9 dice and gets outcomes [6, 6, 2, 6, 1, 4, 3, 4, 3].
          End scores = (24, 39)
          >>> print(turns[1])
          Start scores = (24, 39).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (24, 43)
          >>> print(turns[2])
          Start scores = (24, 43).
          Player 0 rolls 2 dice and gets outcomes [3, 3].
          End scores = (30, 43)
          >>> print(turns[3])
          Start scores = (30, 43).
          Player 1 rolls 9 dice and gets outcomes [4, 5, 5, 6, 2, 4, 1, 3, 5].
          End scores = (30, 44)
          >>> print(turns[4])
          Start scores = (30, 44).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 2, 2, 4, 1, 1].
          End scores = (31, 44)
          >>> print(turns[5])
          Start scores = (31, 44).
          Player 1 rolls 7 dice and gets outcomes [5, 5, 6, 1, 6, 1, 1].
          End scores = (45, 31)
          >>> print(turns[6])
          Start scores = (45, 31).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 2, 2].
          End scores = (56, 31)
          >>> print(turns[7])
          Start scores = (56, 31).
          Player 1 rolls 10 dice and gets outcomes [5, 2, 6, 6, 2, 3, 5, 3, 4, 5].
          End scores = (72, 56)
          >>> print(turns[8])
          Start scores = (72, 56).
          Player 0 rolls 2 dice and gets outcomes [2, 1].
          End scores = (56, 73)
          >>> print(turns[9])
          Start scores = (56, 73).
          Player 1 rolls 6 dice and gets outcomes [5, 5, 3, 6, 6, 2].
          End scores = (56, 100)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36152, score0=49, score1=25, goal=52, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (49, 25).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 6, 1, 3].
          End scores = (50, 25)
          >>> print(turns[1])
          Start scores = (50, 25).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 2, 2, 2].
          End scores = (26, 50)
          >>> print(turns[2])
          Start scores = (26, 50).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (28, 50)
          >>> print(turns[3])
          Start scores = (28, 50).
          Player 1 rolls 6 dice and gets outcomes [3, 1, 5, 5, 3, 2].
          End scores = (28, 51)
          >>> print(turns[4])
          Start scores = (28, 51).
          Player 0 rolls 4 dice and gets outcomes [2, 3, 1, 5].
          End scores = (32, 51)
          >>> print(turns[5])
          Start scores = (32, 51).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (32, 54)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=97165, score0=13, score1=4, goal=42, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (13, 4).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 1, 4].
          End scores = (14, 4)
          >>> print(turns[1])
          Start scores = (14, 4).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 5, 3, 3, 5].
          End scores = (14, 29)
          >>> print(turns[2])
          Start scores = (14, 29).
          Player 0 rolls 7 dice and gets outcomes [4, 6, 1, 2, 4, 1, 5].
          End scores = (15, 29)
          >>> print(turns[3])
          Start scores = (15, 29).
          Player 1 rolls 8 dice and gets outcomes [5, 6, 1, 1, 3, 3, 3, 6].
          End scores = (15, 30)
          >>> print(turns[4])
          Start scores = (15, 30).
          Player 0 rolls 6 dice and gets outcomes [3, 4, 4, 5, 2, 6].
          End scores = (39, 30)
          >>> print(turns[5])
          Start scores = (39, 30).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (39, 38)
          >>> print(turns[6])
          Start scores = (39, 38).
          Player 0 rolls 6 dice and gets outcomes [4, 6, 1, 3, 6, 6].
          End scores = (40, 38)
          >>> print(turns[7])
          Start scores = (40, 38).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 5, 4, 2, 3, 2, 6].
          End scores = (40, 70)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=7964, score0=0, score1=12, goal=30, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (0, 12).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (13, 12)
          >>> print(turns[1])
          Start scores = (13, 12).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (13, 16)
          >>> print(turns[2])
          Start scores = (13, 16).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 5].
          End scores = (16, 25)
          >>> print(turns[3])
          Start scores = (16, 25).
          Player 1 rolls 10 dice and gets outcomes [4, 6, 3, 3, 2, 4, 2, 2, 1, 1].
          End scores = (16, 26)
          >>> print(turns[4])
          Start scores = (16, 26).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (19, 26)
          >>> print(turns[5])
          Start scores = (19, 26).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (19, 28)
          >>> print(turns[6])
          Start scores = (19, 28).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 2].
          End scores = (20, 28)
          >>> print(turns[7])
          Start scores = (20, 28).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (20, 33)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=87291, score0=59, score1=15, goal=87, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (59, 15).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 1].
          End scores = (60, 15)
          >>> print(turns[1])
          Start scores = (60, 15).
          Player 1 rolls 9 dice and gets outcomes [6, 2, 4, 4, 4, 3, 5, 2, 3].
          End scores = (60, 48)
          >>> print(turns[2])
          Start scores = (60, 48).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 1, 6, 6, 2, 3, 4].
          End scores = (61, 48)
          >>> print(turns[3])
          Start scores = (61, 48).
          Player 1 rolls 5 dice and gets outcomes [6, 2, 5, 6, 3].
          End scores = (61, 70)
          >>> print(turns[4])
          Start scores = (61, 70).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 4, 4].
          End scores = (76, 70)
          >>> print(turns[5])
          Start scores = (76, 70).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 4, 1, 6, 1, 2, 4].
          End scores = (76, 71)
          >>> print(turns[6])
          Start scores = (76, 71).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 2, 1].
          End scores = (77, 71)
          >>> print(turns[7])
          Start scores = (77, 71).
          Player 1 rolls 4 dice and gets outcomes [1, 3, 3, 6].
          End scores = (77, 72)
          >>> print(turns[8])
          Start scores = (77, 72).
          Player 0 rolls 4 dice and gets outcomes [6, 2, 6, 2].
          End scores = (93, 72)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=2481, score0=32, score1=79, goal=98, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (32, 79).
          Player 0 rolls 10 dice and gets outcomes [2, 4, 4, 5, 2, 5, 3, 1, 2, 5].
          End scores = (33, 79)
          >>> print(turns[1])
          Start scores = (33, 79).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 5, 5, 1, 6].
          End scores = (33, 80)
          >>> print(turns[2])
          Start scores = (33, 80).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (80, 40)
          >>> print(turns[3])
          Start scores = (80, 40).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (80, 47)
          >>> print(turns[4])
          Start scores = (80, 47).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (86, 47)
          >>> print(turns[5])
          Start scores = (86, 47).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 2, 4, 6].
          End scores = (86, 48)
          >>> print(turns[6])
          Start scores = (86, 48).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (88, 48)
          >>> print(turns[7])
          Start scores = (88, 48).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (88, 50)
          >>> print(turns[8])
          Start scores = (88, 50).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 1, 3, 6, 4, 2, 3, 6, 1].
          End scores = (89, 50)
          >>> print(turns[9])
          Start scores = (89, 50).
          Player 1 rolls 6 dice and gets outcomes [4, 2, 2, 3, 2, 1].
          End scores = (89, 51)
          >>> print(turns[10])
          Start scores = (89, 51).
          Player 0 rolls 9 dice and gets outcomes [1, 4, 6, 3, 1, 6, 5, 4, 3].
          End scores = (90, 51)
          >>> print(turns[11])
          Start scores = (90, 51).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 5, 2].
          End scores = (90, 66)
          >>> print(turns[12])
          Start scores = (90, 66).
          Player 0 rolls 10 dice and gets outcomes [1, 5, 3, 6, 1, 2, 4, 2, 6, 2].
          End scores = (91, 66)
          >>> print(turns[13])
          Start scores = (91, 66).
          Player 1 rolls 9 dice and gets outcomes [1, 4, 1, 3, 1, 3, 4, 4, 5].
          End scores = (91, 67)
          >>> print(turns[14])
          Start scores = (91, 67).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (94, 67)
          >>> print(turns[15])
          Start scores = (94, 67).
          Player 1 rolls 4 dice and gets outcomes [6, 5, 4, 2].
          End scores = (94, 84)
          >>> print(turns[16])
          Start scores = (94, 84).
          Player 0 rolls 7 dice and gets outcomes [4, 3, 4, 2, 4, 5, 5].
          End scores = (121, 84)
          >>> print(turns[17])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=57878, score0=4, score1=13, goal=29, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 13).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 1, 6, 3].
          End scores = (5, 13)
          >>> print(turns[1])
          Start scores = (5, 13).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 2, 3, 3, 4, 1, 4, 3].
          End scores = (5, 14)
          >>> print(turns[2])
          Start scores = (5, 14).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 2, 3, 1].
          End scores = (6, 14)
          >>> print(turns[3])
          Start scores = (6, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (6, 22)
          >>> print(turns[4])
          Start scores = (6, 22).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 3, 6, 6, 1, 1, 6, 4, 5].
          End scores = (7, 22)
          >>> print(turns[5])
          Start scores = (7, 22).
          Player 1 rolls 10 dice and gets outcomes [3, 4, 4, 2, 2, 3, 2, 1, 6, 3].
          End scores = (7, 26)
          >>> print(turns[6])
          Start scores = (7, 26).
          Player 0 rolls 8 dice and gets outcomes [1, 4, 4, 3, 6, 4, 3, 5].
          End scores = (8, 26)
          >>> print(turns[7])
          Start scores = (8, 26).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 2, 5, 2, 3, 1, 3, 6, 6].
          End scores = (8, 27)
          >>> print(turns[8])
          Start scores = (8, 27).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 3, 4].
          End scores = (19, 27)
          >>> print(turns[9])
          Start scores = (19, 27).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 2, 3].
          End scores = (19, 40)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27303, score0=31, score1=3, goal=39, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (31, 3).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 6, 1, 6, 2, 2, 2, 6].
          End scores = (32, 3)
          >>> print(turns[1])
          Start scores = (32, 3).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 1, 1, 5, 5, 2, 1, 6].
          End scores = (4, 32)
          >>> print(turns[2])
          Start scores = (4, 32).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 6, 6, 6, 3, 3, 5, 5].
          End scores = (47, 32)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=98514, score0=46, score1=42, goal=60, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (46, 42).
          Player 0 rolls 5 dice and gets outcomes [5, 1, 3, 3, 5].
          End scores = (47, 42)
          >>> print(turns[1])
          Start scores = (47, 42).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (47, 48)
          >>> print(turns[2])
          Start scores = (47, 48).
          Player 0 rolls 10 dice and gets outcomes [6, 3, 4, 4, 5, 1, 4, 6, 4, 5].
          End scores = (48, 48)
          >>> print(turns[3])
          Start scores = (48, 48).
          Player 1 rolls 6 dice and gets outcomes [6, 3, 2, 2, 6, 5].
          End scores = (72, 48)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=64395, score0=3, score1=18, goal=52, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (3, 18).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 6, 3, 2, 6, 3, 3, 2].
          End scores = (36, 18)
          >>> print(turns[1])
          Start scores = (36, 18).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 2].
          End scores = (36, 19)
          >>> print(turns[2])
          Start scores = (36, 19).
          Player 0 rolls 8 dice and gets outcomes [6, 5, 6, 3, 3, 2, 6, 4].
          End scores = (71, 19)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=13464, score0=27, score1=4, goal=47, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (27, 4).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 5, 4].
          End scores = (4, 28)
          >>> print(turns[1])
          Start scores = (4, 28).
          Player 1 rolls 3 dice and gets outcomes [5, 3, 2].
          End scores = (4, 38)
          >>> print(turns[2])
          Start scores = (4, 38).
          Player 0 rolls 3 dice and gets outcomes [5, 4, 5].
          End scores = (21, 38)
          >>> print(turns[3])
          Start scores = (21, 38).
          Player 1 rolls 5 dice and gets outcomes [3, 6, 4, 1, 2].
          End scores = (21, 39)
          >>> print(turns[4])
          Start scores = (21, 39).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 3, 4, 5, 3, 3].
          End scores = (47, 39)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=92338, score0=64, score1=67, goal=69, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (64, 67).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 4, 4, 6, 4, 4, 6, 3, 4].
          End scores = (107, 67)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=55414, score0=9, score1=19, goal=32, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 19).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 6, 1, 2, 5, 3].
          End scores = (10, 19)
          >>> print(turns[1])
          Start scores = (10, 19).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 4, 6, 1, 5, 1, 3, 2, 1].
          End scores = (10, 20)
          >>> print(turns[2])
          Start scores = (10, 20).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 2].
          End scores = (19, 20)
          >>> print(turns[3])
          Start scores = (19, 20).
          Player 1 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (19, 40)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=2412, score0=90, score1=38, goal=94, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (90, 38).
          Player 0 rolls 7 dice and gets outcomes [5, 3, 2, 6, 4, 1, 5].
          End scores = (38, 91)
          >>> print(turns[1])
          Start scores = (38, 91).
          Player 1 rolls 10 dice and gets outcomes [2, 3, 3, 5, 1, 6, 1, 1, 5, 1].
          End scores = (38, 92)
          >>> print(turns[2])
          Start scores = (38, 92).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (40, 92)
          >>> print(turns[3])
          Start scores = (40, 92).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (40, 95)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=43957, score0=35, score1=51, goal=100, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (35, 51).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 4, 6, 3, 2].
          End scores = (55, 51)
          >>> print(turns[1])
          Start scores = (55, 51).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 1, 1].
          End scores = (55, 52)
          >>> print(turns[2])
          Start scores = (55, 52).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (58, 52)
          >>> print(turns[3])
          Start scores = (58, 52).
          Player 1 rolls 4 dice and gets outcomes [5, 1, 1, 4].
          End scores = (58, 53)
          >>> print(turns[4])
          Start scores = (58, 53).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 3, 4, 5, 5, 3, 6, 6].
          End scores = (100, 53)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36287, score0=42, score1=52, goal=100, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (42, 52).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 1, 5, 6, 4, 2, 3, 4, 4].
          End scores = (43, 52)
          >>> print(turns[1])
          Start scores = (43, 52).
          Player 1 rolls 10 dice and gets outcomes [3, 4, 6, 2, 4, 2, 4, 6, 4, 3].
          End scores = (43, 90)
          >>> print(turns[2])
          Start scores = (43, 90).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 4, 6, 6, 4, 4].
          End scores = (77, 90)
          >>> print(turns[3])
          Start scores = (77, 90).
          Player 1 rolls 5 dice and gets outcomes [4, 4, 1, 6, 1].
          End scores = (91, 77)
          >>> print(turns[4])
          Start scores = (91, 77).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 6, 5, 4, 1, 3].
          End scores = (92, 77)
          >>> print(turns[5])
          Start scores = (92, 77).
          Player 1 rolls 4 dice and gets outcomes [1, 3, 1, 1].
          End scores = (92, 78)
          >>> print(turns[6])
          Start scores = (92, 78).
          Player 0 rolls 9 dice and gets outcomes [2, 2, 2, 2, 2, 1, 5, 4, 5].
          End scores = (93, 78)
          >>> print(turns[7])
          Start scores = (93, 78).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 4].
          End scores = (93, 90)
          >>> print(turns[8])
          Start scores = (93, 90).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 4].
          End scores = (97, 90)
          >>> print(turns[9])
          Start scores = (97, 90).
          Player 1 rolls 5 dice and gets outcomes [6, 6, 5, 3, 5].
          End scores = (115, 97)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36008, score0=3, score1=9, goal=11, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 9).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 4, 3, 2, 1, 6, 5, 6, 5].
          End scores = (4, 9)
          >>> print(turns[1])
          Start scores = (4, 9).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 5, 1, 3, 1, 3, 5, 6, 6].
          End scores = (4, 10)
          >>> print(turns[2])
          Start scores = (4, 10).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (5, 10)
          >>> print(turns[3])
          Start scores = (5, 10).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 3, 1, 6, 4, 4, 5].
          End scores = (5, 11)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib, hog_gui
      >>> # importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
