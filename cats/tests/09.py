test = {
  'name': 'Problem 9',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [word_time('START', 0), word_time('What', 0.2), word_time('great', 0.4), word_time('luck', 0.8)]
          >>> p1 = [word_time('START', 0), word_time('What', 0.6), word_time('great', 0.8), word_time('luck', 1.19)]
          >>> fastest_words([p0, p1])
          8e46fe768e646201a51b6caf0ae65fdb
          # locked
          >>> fastest_words([p0, p1], 0.1)  # with a large margin, both typed "luck" the fastest
          c8f4afb99c22926d63b4937678249c68
          # locked
          >>> p2 = [word_time('START', 0), word_time('What', 0.2), word_time('great', 0.3), word_time('luck', 0.6)]
          >>> fastest_words([p0, p1, p2])
          26d9e18fe121bc000bf2abf00214a032
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 44)], [word_time('START', 44)]]
          >>> fastest_words(p, 0.020833333333333332)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 37), word_time('mennom' , 38.0)]]
          >>> fastest_words(p, 0.07692307692307693)
          [['mennom']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 40)], [word_time('START', 40)]]
          >>> fastest_words(p, 0.0625)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 24)]]
          >>> fastest_words(p, 0.25)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 46), word_time('oviferous' , 47.0)], [word_time('START', 46), word_time('oviferous' , 46.333333333333336)]]
          >>> fastest_words(p, 0.017857142857142856)
          [[], ['oviferous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 99), word_time('notchel' , 99.25), word_time('phengitical' , 100.25), word_time('dollier' , 100.75), word_time('bushlet' , 101.0), word_time('sciographic' , 101.25), word_time('vaned' , 101.45)], [word_time('START', 99), word_time('notchel' , 100.0), word_time('phengitical' , 100.2), word_time('dollier' , 101.2), word_time('bushlet' , 101.4), word_time('sciographic' , 101.9), word_time('vaned' , 102.23333333333333)]]
          >>> fastest_words(p, 0.012658227848101266)
          [['notchel', 'dollier', 'sciographic', 'vaned'], ['phengitical', 'bushlet']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 10), word_time('tylostylus' , 10.333333333333334), word_time('civil' , 11.333333333333334)]]
          >>> fastest_words(p, 0.013513513513513514)
          [['tylostylus', 'civil']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 47), word_time('delabialize' , 48.0), word_time('erythematous' , 48.333333333333336), word_time('gossipdom' , 49.333333333333336), word_time('killinite' , 50.333333333333336), word_time('osteochondropathy' , 51.333333333333336), word_time('tethydan' , 51.66666666666667)], [word_time('START', 47), word_time('delabialize' , 47.5), word_time('erythematous' , 47.833333333333336), word_time('gossipdom' , 48.03333333333334), word_time('killinite' , 48.23333333333334), word_time('osteochondropathy' , 48.48333333333334), word_time('tethydan' , 48.73333333333334)]]
          >>> fastest_words(p, 0.014492753623188406)
          [['erythematous'], ['delabialize', 'erythematous', 'gossipdom', 'killinite', 'osteochondropathy', 'tethydan']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 67), word_time('elasticness' , 68.0)], [word_time('START', 67), word_time('elasticness' , 67.25)]]
          >>> fastest_words(p, 0.011764705882352941)
          [[], ['elasticness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 92), word_time('correction' , 92.2), word_time('inadhesion' , 92.45), word_time('featherfew' , 93.45)]]
          >>> fastest_words(p, 0.01818181818181818)
          [['correction', 'inadhesion', 'featherfew']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 9), word_time('lycanthropic' , 9.2)]]
          >>> fastest_words(p, 0.0625)
          [['lycanthropic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 25), word_time('itemization' , 25.2), word_time('lecithalbumin' , 25.7), word_time('heelpiece' , 26.03333333333333)]]
          >>> fastest_words(p, 0.015625)
          [['itemization', 'lecithalbumin', 'heelpiece']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 75), word_time('choultry' , 76.0), word_time('caryopilite' , 76.5), word_time('unowed' , 76.83333333333333), word_time('overslaugh' , 77.03333333333333), word_time('unshriveled' , 77.28333333333333)], [word_time('START', 75), word_time('choultry' , 75.5), word_time('caryopilite' , 75.83333333333333), word_time('unowed' , 76.83333333333333), word_time('overslaugh' , 77.16666666666666), word_time('unshriveled' , 77.36666666666666)], [word_time('START', 75), word_time('choultry' , 75.2), word_time('caryopilite' , 75.45), word_time('unowed' , 76.45), word_time('overslaugh' , 76.95), word_time('unshriveled' , 77.2)]]
          >>> fastest_words(p, 0.03571428571428571)
          [['unowed', 'overslaugh'], ['unshriveled'], ['choultry', 'caryopilite']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 82)], [word_time('START', 82)], [word_time('START', 82)]]
          >>> fastest_words(p, 0.02040816326530612)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 88), word_time('zygostyle' , 88.33333333333333)], [word_time('START', 88), word_time('zygostyle' , 88.2)], [word_time('START', 88), word_time('zygostyle' , 88.33333333333333)]]
          >>> fastest_words(p, 0.07692307692307693)
          [[], ['zygostyle'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 72)], [word_time('START', 72)]]
          >>> fastest_words(p, 0.07692307692307693)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 41), word_time('cecidiology' , 41.2), word_time('progne' , 42.2), word_time('cosiness' , 43.2)], [word_time('START', 41), word_time('cecidiology' , 41.5), word_time('progne' , 42.5), word_time('cosiness' , 42.833333333333336)]]
          >>> fastest_words(p, 0.014285714285714285)
          [['cecidiology', 'progne'], ['progne', 'cosiness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 15), word_time('orrery' , 15.2)], [word_time('START', 15), word_time('orrery' , 15.2)], [word_time('START', 15), word_time('orrery' , 15.2)]]
          >>> fastest_words(p, 0.14285714285714285)
          [['orrery'], ['orrery'], ['orrery']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 42), word_time('careers' , 42.333333333333336), word_time('sublanceolate' , 42.833333333333336), word_time('feudist' , 43.16666666666667), word_time('vorticist' , 43.50000000000001), word_time('dup' , 43.70000000000001)]]
          >>> fastest_words(p, 0.05)
          [['careers', 'sublanceolate', 'feudist', 'vorticist', 'dup']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 93), word_time('chichipe' , 93.33333333333333), word_time('antemeridian' , 94.33333333333333), word_time('metapolitical' , 94.66666666666666)]]
          >>> fastest_words(p, 0.010101010101010102)
          [['chichipe', 'antemeridian', 'metapolitical']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 99), word_time('stratum' , 99.25), word_time('onager' , 99.58333333333333)]]
          >>> fastest_words(p, 0.01098901098901099)
          [['stratum', 'onager']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 73), word_time('hamated' , 73.33333333333333), word_time('encumberingly' , 73.83333333333333), word_time('closh' , 74.16666666666666), word_time('yugada' , 75.16666666666666)]]
          >>> fastest_words(p, 0.0125)
          [['hamated', 'encumberingly', 'closh', 'yugada']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 4), word_time('nonformation' , 5.0), word_time('yeven' , 5.2), word_time('argenteous' , 5.533333333333333), word_time('ha' , 5.733333333333333)]]
          >>> fastest_words(p, 0.022222222222222223)
          [['nonformation', 'yeven', 'argenteous', 'ha']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 83), word_time('roland' , 83.5), word_time('unfoxy' , 83.75), word_time('retrothyroid' , 84.25), word_time('haptotropic' , 84.5), word_time('anaphrodisiac' , 84.7), word_time('pupillometry' , 85.2)], [word_time('START', 83), word_time('roland' , 83.25), word_time('unfoxy' , 83.45), word_time('retrothyroid' , 83.78333333333333), word_time('haptotropic' , 84.78333333333333), word_time('anaphrodisiac' , 85.78333333333333), word_time('pupillometry' , 86.11666666666666)]]
          >>> fastest_words(p, 0.024390243902439025)
          [['haptotropic', 'anaphrodisiac'], ['roland', 'unfoxy', 'retrothyroid', 'pupillometry']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 34), word_time('titterer' , 34.5)]]
          >>> fastest_words(p, 0.25)
          [['titterer']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 4), word_time('capucine' , 5.0), word_time('scowlful' , 5.5), word_time('noration' , 5.75), word_time('tinstuff' , 5.95), word_time('arpent' , 6.95)], [word_time('START', 4), word_time('capucine' , 4.2), word_time('scowlful' , 4.4), word_time('noration' , 5.4), word_time('tinstuff' , 5.65), word_time('arpent' , 6.15)], [word_time('START', 4), word_time('capucine' , 4.2), word_time('scowlful' , 4.7), word_time('noration' , 4.95), word_time('tinstuff' , 5.45), word_time('arpent' , 6.45)]]
          >>> fastest_words(p, 0.015873015873015872)
          [['noration', 'tinstuff'], ['capucine', 'scowlful', 'arpent'], ['capucine', 'noration']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 53)], [word_time('START', 53)], [word_time('START', 53)]]
          >>> fastest_words(p, 0.015873015873015872)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 19)]]
          >>> fastest_words(p, 0.017543859649122806)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 1), word_time('perth' , 1.2), word_time('chrematistic' , 2.2), word_time('proctotomy' , 2.4000000000000004), word_time('bicetyl' , 2.6000000000000005)], [word_time('START', 1), word_time('perth' , 1.2), word_time('chrematistic' , 1.5333333333333332), word_time('proctotomy' , 2.533333333333333), word_time('bicetyl' , 2.8666666666666667)], [word_time('START', 1), word_time('perth' , 2.0), word_time('chrematistic' , 2.25), word_time('proctotomy' , 2.75), word_time('bicetyl' , 3.0)]]
          >>> fastest_words(p, 0.16666666666666666)
          [['perth', 'proctotomy', 'bicetyl'], ['perth', 'chrematistic', 'bicetyl'], ['chrematistic', 'bicetyl']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 85)]]
          >>> fastest_words(p, 0.02857142857142857)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 37), word_time('justly' , 37.25), word_time('contralto' , 37.75), word_time('erythematous' , 38.0), word_time('intromissive' , 38.333333333333336), word_time('tanglement' , 38.53333333333334)], [word_time('START', 37), word_time('justly' , 37.5), word_time('contralto' , 38.0), word_time('erythematous' , 38.333333333333336), word_time('intromissive' , 38.53333333333334), word_time('tanglement' , 38.73333333333334)]]
          >>> fastest_words(p, 0.02631578947368421)
          [['justly', 'contralto', 'erythematous', 'tanglement'], ['contralto', 'intromissive', 'tanglement']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 82), word_time('uptree' , 82.2), word_time('underlinen' , 82.53333333333333), word_time('an' , 82.86666666666666), word_time('quinqueloculine' , 83.19999999999999), word_time('demonstrativeness' , 83.53333333333332), word_time('epee' , 84.03333333333332)]]
          >>> fastest_words(p, 0.011363636363636364)
          [['uptree', 'underlinen', 'an', 'quinqueloculine', 'demonstrativeness', 'epee']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 87), word_time('draughtmanship' , 87.5), word_time('arboriform' , 87.83333333333333), word_time('oppugner' , 88.03333333333333), word_time('nucleonics' , 88.53333333333333), word_time('reducer' , 89.03333333333333), word_time('watered' , 89.28333333333333)], [word_time('START', 87), word_time('draughtmanship' , 87.25), word_time('arboriform' , 87.75), word_time('oppugner' , 88.0), word_time('nucleonics' , 88.25), word_time('reducer' , 88.58333333333333), word_time('watered' , 89.58333333333333)]]
          >>> fastest_words(p, 0.022727272727272728)
          [['arboriform', 'oppugner', 'watered'], ['draughtmanship', 'nucleonics', 'reducer']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 20), word_time('retinopapilitis' , 20.25), word_time('unabsolvedness' , 20.5)]]
          >>> fastest_words(p, 0.125)
          [['retinopapilitis', 'unabsolvedness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 33), word_time('ratiocinate' , 33.333333333333336), word_time('pasquinader' , 33.833333333333336), word_time('gamecube' , 34.833333333333336)]]
          >>> fastest_words(p, 0.011627906976744186)
          [['ratiocinate', 'pasquinader', 'gamecube']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 73), word_time('didst' , 74.0)]]
          >>> fastest_words(p, 0.0625)
          [['didst']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 5)], [word_time('START', 5)], [word_time('START', 5)]]
          >>> fastest_words(p, 0.010101010101010102)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 15), word_time('undersweep' , 16.0), word_time('sportswomanly' , 17.0), word_time('nonlocal' , 18.0), word_time('lorate' , 18.25), word_time('histopathologist' , 18.583333333333332)]]
          >>> fastest_words(p, 0.012987012987012988)
          [['undersweep', 'sportswomanly', 'nonlocal', 'lorate', 'histopathologist']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 33), word_time('undimerous' , 33.5), word_time('engrainedly' , 33.7), word_time('aschistic' , 34.03333333333334)], [word_time('START', 33), word_time('undimerous' , 33.5), word_time('engrainedly' , 34.5), word_time('aschistic' , 35.0)]]
          >>> fastest_words(p, 0.013157894736842105)
          [['undimerous', 'engrainedly', 'aschistic'], ['undimerous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 9), word_time('borscht' , 9.2), word_time('spectator' , 9.45), word_time('semiperimetry' , 9.7), word_time('decider' , 9.899999999999999)]]
          >>> fastest_words(p, 0.023809523809523808)
          [['borscht', 'spectator', 'semiperimetry', 'decider']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 70)], [word_time('START', 70)]]
          >>> fastest_words(p, 0.010869565217391304)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 64), word_time('mamelonation' , 64.5), word_time('delegable' , 64.83333333333333)]]
          >>> fastest_words(p, 0.027777777777777776)
          [['mamelonation', 'delegable']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 51), word_time('noneffervescent' , 51.2), word_time('metasaccharinic' , 51.53333333333334)], [word_time('START', 51), word_time('noneffervescent' , 51.5), word_time('metasaccharinic' , 51.833333333333336)], [word_time('START', 51), word_time('noneffervescent' , 51.333333333333336), word_time('metasaccharinic' , 51.53333333333334)]]
          >>> fastest_words(p, 0.010752688172043012)
          [['noneffervescent'], [], ['metasaccharinic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 68), word_time('overstress' , 68.33333333333333), word_time('voicelessness' , 68.58333333333333), word_time('discrepantly' , 68.83333333333333), word_time('bestsellers' , 69.33333333333333), word_time('bibliography' , 69.66666666666666)], [word_time('START', 68), word_time('overstress' , 69.0), word_time('voicelessness' , 69.33333333333333), word_time('discrepantly' , 69.58333333333333), word_time('bestsellers' , 70.08333333333333), word_time('bibliography' , 70.33333333333333)]]
          >>> fastest_words(p, 0.015384615384615385)
          [['overstress', 'voicelessness', 'discrepantly', 'bestsellers'], ['discrepantly', 'bestsellers', 'bibliography']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 20), word_time('crowkeeper' , 20.333333333333332), word_time('symphyllous' , 20.833333333333332), word_time('narratress' , 21.083333333333332), word_time('periplegmatic' , 21.28333333333333), word_time('wantonlike' , 21.78333333333333)], [word_time('START', 20), word_time('crowkeeper' , 21.0), word_time('symphyllous' , 21.25), word_time('narratress' , 21.5), word_time('periplegmatic' , 22.0), word_time('wantonlike' , 23.0)]]
          >>> fastest_words(p, 0.027777777777777776)
          [['crowkeeper', 'narratress', 'periplegmatic', 'wantonlike'], ['symphyllous', 'narratress']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 75)]]
          >>> fastest_words(p, 0.03225806451612903)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 61), word_time('heriot' , 61.2), word_time('supersalient' , 61.45), word_time('hate' , 62.45), word_time('septation' , 62.7)]]
          >>> fastest_words(p, 0.014285714285714285)
          [['heriot', 'supersalient', 'hate', 'septation']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 7)]]
          >>> fastest_words(p, 0.14285714285714285)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 0), word_time('colchicine' , 0.3333333333333333), word_time('zincographical' , 1.3333333333333333), word_time('misphrase' , 2.333333333333333), word_time('subspecifically' , 2.533333333333333)], [word_time('START', 0), word_time('colchicine' , 0.2), word_time('zincographical' , 0.4), word_time('misphrase' , 0.65), word_time('subspecifically' , 0.9833333333333334)]]
          >>> fastest_words(p, 0.019230769230769232)
          [['subspecifically'], ['colchicine', 'zincographical', 'misphrase']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 42), word_time('apodictically' , 42.2), word_time('villages' , 42.7), word_time('algebra' , 43.03333333333334), word_time('uprid' , 43.23333333333334), word_time('disadvise' , 43.433333333333344)]]
          >>> fastest_words(p, 0.021739130434782608)
          [['apodictically', 'villages', 'algebra', 'uprid', 'disadvise']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 48), word_time('dogmaticalness' , 48.2)], [word_time('START', 48), word_time('dogmaticalness' , 48.333333333333336)]]
          >>> fastest_words(p, 0.010309278350515464)
          [['dogmaticalness'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 57), word_time('saddlelike' , 57.2), word_time('postlachrymal' , 57.400000000000006), word_time('antetype' , 57.650000000000006), word_time('autocinesis' , 57.85000000000001), word_time('feces' , 58.05000000000001)], [word_time('START', 57), word_time('saddlelike' , 57.2), word_time('postlachrymal' , 57.400000000000006), word_time('antetype' , 57.650000000000006), word_time('autocinesis' , 57.98333333333334), word_time('feces' , 58.31666666666668)]]
          >>> fastest_words(p, 0.010309278350515464)
          [['saddlelike', 'postlachrymal', 'antetype', 'autocinesis', 'feces'], ['saddlelike', 'postlachrymal', 'antetype']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 28), word_time('dispensatorily' , 28.25), word_time('manganapatite' , 28.5), word_time('gatemaker' , 29.0), word_time('hydrosulphocyanic' , 29.5), word_time('drugshop' , 30.5), word_time('caracolite' , 31.5)], [word_time('START', 28), word_time('dispensatorily' , 28.333333333333332), word_time('manganapatite' , 28.583333333333332), word_time('gatemaker' , 28.833333333333332), word_time('hydrosulphocyanic' , 29.333333333333332), word_time('drugshop' , 29.583333333333332), word_time('caracolite' , 29.916666666666664)]]
          >>> fastest_words(p, 0.08333333333333333)
          [['dispensatorily', 'manganapatite', 'hydrosulphocyanic'], ['dispensatorily', 'manganapatite', 'gatemaker', 'hydrosulphocyanic', 'drugshop', 'caracolite']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 25), word_time('stirps' , 26.0), word_time('waverous' , 26.333333333333332), word_time('qualifying' , 26.833333333333332), word_time('sexuparous' , 27.166666666666664), word_time('realmless' , 27.666666666666664)], [word_time('START', 25), word_time('stirps' , 26.0), word_time('waverous' , 26.2), word_time('qualifying' , 26.53333333333333), word_time('sexuparous' , 26.866666666666664), word_time('realmless' , 27.116666666666664)]]
          >>> fastest_words(p, 0.03333333333333333)
          [['stirps', 'sexuparous'], ['stirps', 'waverous', 'qualifying', 'sexuparous', 'realmless']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 69)], [word_time('START', 69)]]
          >>> fastest_words(p, 0.3333333333333333)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 77), word_time('oxhorn' , 78.0), word_time('overskim' , 78.25), word_time('polemicist' , 78.45), word_time('injure' , 79.45), word_time('hygrophaneity' , 79.95)]]
          >>> fastest_words(p, 0.037037037037037035)
          [['oxhorn', 'overskim', 'polemicist', 'injure', 'hygrophaneity']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 85), word_time('relativeness' , 85.5), word_time('solivagant' , 85.75)]]
          >>> fastest_words(p, 0.0625)
          [['relativeness', 'solivagant']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 79), word_time('waterhorse' , 79.5), word_time('antisubstance' , 79.75), word_time('yucker' , 80.25), word_time('samely' , 80.75), word_time('dargsman' , 81.75), word_time('heterotopous' , 81.95)], [word_time('START', 79), word_time('waterhorse' , 80.0), word_time('antisubstance' , 81.0), word_time('yucker' , 81.33333333333333), word_time('samely' , 81.66666666666666), word_time('dargsman' , 82.16666666666666), word_time('heterotopous' , 82.66666666666666)]]
          >>> fastest_words(p, 0.011494252873563218)
          [['waterhorse', 'antisubstance', 'heterotopous'], ['yucker', 'samely', 'dargsman']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 35), word_time('restrainedness' , 35.2), word_time('revivement' , 35.53333333333334), word_time('tron' , 35.866666666666674), word_time('interpretably' , 36.116666666666674), word_time('runkly' , 36.31666666666668), word_time('ninebark' , 37.31666666666668)], [word_time('START', 35), word_time('restrainedness' , 35.2), word_time('revivement' , 35.400000000000006), word_time('tron' , 36.400000000000006), word_time('interpretably' , 36.650000000000006), word_time('runkly' , 36.85000000000001), word_time('ninebark' , 37.35000000000001)]]
          >>> fastest_words(p, 0.030303030303030304)
          [['restrainedness', 'tron', 'interpretably', 'runkly'], ['restrainedness', 'revivement', 'interpretably', 'runkly', 'ninebark']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 49), word_time('rangership' , 50.0), word_time('wheatstalk' , 51.0), word_time('nonprofession' , 51.5)], [word_time('START', 49), word_time('rangership' , 49.25), word_time('wheatstalk' , 49.5), word_time('nonprofession' , 50.5)]]
          >>> fastest_words(p, 0.022222222222222223)
          [['nonprofession'], ['rangership', 'wheatstalk']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 77), word_time('ripe' , 78.0), word_time('spatuliform' , 78.33333333333333)], [word_time('START', 77), word_time('ripe' , 77.5), word_time('spatuliform' , 78.0)], [word_time('START', 77), word_time('ripe' , 77.5), word_time('spatuliform' , 77.83333333333333)]]
          >>> fastest_words(p, 0.015151515151515152)
          [['spatuliform'], ['ripe'], ['ripe', 'spatuliform']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 99)], [word_time('START', 99)], [word_time('START', 99)]]
          >>> fastest_words(p, 0.05263157894736842)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 18), word_time('exampleless' , 18.25)], [word_time('START', 18), word_time('exampleless' , 18.333333333333332)]]
          >>> fastest_words(p, 0.04)
          [['exampleless'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 44)], [word_time('START', 44)], [word_time('START', 44)]]
          >>> fastest_words(p, 0.08333333333333333)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 68), word_time('overfearful' , 68.25)], [word_time('START', 68), word_time('overfearful' , 69.0)], [word_time('START', 68), word_time('overfearful' , 69.0)]]
          >>> fastest_words(p, 0.02564102564102564)
          [['overfearful'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 46), word_time('weaponshowing' , 46.5), word_time('rhombohedra' , 47.5), word_time('sparger' , 48.0), word_time('pessomancy' , 49.0), word_time('wearyingly' , 49.5)]]
          >>> fastest_words(p, 0.015625)
          [['weaponshowing', 'rhombohedra', 'sparger', 'pessomancy', 'wearyingly']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 20), word_time('phalacrocoracine' , 21.0), word_time('taxeme' , 21.333333333333332), word_time('reedless' , 21.666666666666664), word_time('winery' , 22.666666666666664), word_time('token' , 23.666666666666664)], [word_time('START', 20), word_time('phalacrocoracine' , 20.25), word_time('taxeme' , 20.583333333333332), word_time('reedless' , 20.916666666666664), word_time('winery' , 21.166666666666664), word_time('token' , 22.166666666666664)], [word_time('START', 20), word_time('phalacrocoracine' , 20.25), word_time('taxeme' , 21.25), word_time('reedless' , 21.583333333333332), word_time('winery' , 21.78333333333333), word_time('token' , 22.28333333333333)]]
          >>> fastest_words(p, 0.01639344262295082)
          [['taxeme', 'reedless'], ['phalacrocoracine', 'taxeme', 'reedless'], ['phalacrocoracine', 'reedless', 'winery', 'token']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 67), word_time('sparrowcide' , 67.5), word_time('salubrious' , 67.75), word_time('untactful' , 68.08333333333333), word_time('kava' , 68.33333333333333), word_time('japanese' , 68.83333333333333)], [word_time('START', 67), word_time('sparrowcide' , 67.25), word_time('salubrious' , 67.45), word_time('untactful' , 67.78333333333333), word_time('kava' , 68.78333333333333), word_time('japanese' , 69.03333333333333)], [word_time('START', 67), word_time('sparrowcide' , 68.0), word_time('salubrious' , 68.5), word_time('untactful' , 68.83333333333333), word_time('kava' , 69.16666666666666), word_time('japanese' , 69.49999999999999)]]
          >>> fastest_words(p, 0.018518518518518517)
          [['untactful', 'kava'], ['sparrowcide', 'salubrious', 'untactful', 'japanese'], ['untactful']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 63), word_time('galvanomagnetic' , 63.2), word_time('loir' , 64.2)]]
          >>> fastest_words(p, 0.025)
          [['galvanomagnetic', 'loir']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 54), word_time('pneumoperitonitis' , 54.5), word_time('balaenoidean' , 55.5), word_time('strawbreadth' , 56.5)], [word_time('START', 54), word_time('pneumoperitonitis' , 54.5), word_time('balaenoidean' , 55.0), word_time('strawbreadth' , 56.0)]]
          >>> fastest_words(p, 0.013157894736842105)
          [['pneumoperitonitis', 'strawbreadth'], ['pneumoperitonitis', 'balaenoidean', 'strawbreadth']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 78)], [word_time('START', 78)], [word_time('START', 78)]]
          >>> fastest_words(p, 0.011494252873563218)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 45)]]
          >>> fastest_words(p, 0.08333333333333333)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 88), word_time('wheerikins' , 88.33333333333333), word_time('uncrushed' , 89.33333333333333)], [word_time('START', 88), word_time('wheerikins' , 88.2), word_time('uncrushed' , 89.2)], [word_time('START', 88), word_time('wheerikins' , 89.0), word_time('uncrushed' , 89.2)]]
          >>> fastest_words(p, 0.05)
          [[], ['wheerikins'], ['uncrushed']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 22), word_time('sterneber' , 22.5), word_time('nonappendicular' , 22.7)], [word_time('START', 22), word_time('sterneber' , 22.333333333333332), word_time('nonappendicular' , 22.53333333333333)], [word_time('START', 22), word_time('sterneber' , 22.5), word_time('nonappendicular' , 22.75)]]
          >>> fastest_words(p, 0.05263157894736842)
          [['nonappendicular'], ['sterneber', 'nonappendicular'], ['nonappendicular']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 30), word_time('achete' , 30.2)], [word_time('START', 30), word_time('achete' , 30.5)]]
          >>> fastest_words(p, 0.010869565217391304)
          [['achete'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 19)]]
          >>> fastest_words(p, 0.012195121951219513)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 33), word_time('untriable' , 34.0), word_time('japan' , 34.2)]]
          >>> fastest_words(p, 0.125)
          [['untriable', 'japan']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 87), word_time('vortically' , 88.0), word_time('massicot' , 88.5), word_time('pinite' , 88.7), word_time('barbarian' , 88.95)]]
          >>> fastest_words(p, 0.010416666666666666)
          [['vortically', 'massicot', 'pinite', 'barbarian']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 69), word_time('longicorn' , 70.0)]]
          >>> fastest_words(p, 0.011494252873563218)
          [['longicorn']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 87), word_time('voluminously' , 88.0), word_time('hydroferrocyanate' , 88.33333333333333), word_time('canthotomy' , 88.66666666666666)], [word_time('START', 87), word_time('voluminously' , 87.5), word_time('hydroferrocyanate' , 87.75), word_time('canthotomy' , 87.95)], [word_time('START', 87), word_time('voluminously' , 87.5), word_time('hydroferrocyanate' , 87.83333333333333), word_time('canthotomy' , 88.33333333333333)]]
          >>> fastest_words(p, 0.016129032258064516)
          [[], ['voluminously', 'hydroferrocyanate', 'canthotomy'], ['voluminously']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 47), word_time('plastogamy' , 47.25), word_time('grumpily' , 47.45), word_time('tease' , 47.95)], [word_time('START', 47), word_time('plastogamy' , 47.5), word_time('grumpily' , 48.5), word_time('tease' , 48.7)], [word_time('START', 47), word_time('plastogamy' , 47.333333333333336), word_time('grumpily' , 47.833333333333336), word_time('tease' , 48.16666666666667)]]
          >>> fastest_words(p, 0.01639344262295082)
          [['plastogamy', 'grumpily'], ['tease'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 67), word_time('productivity' , 67.33333333333333), word_time('proclisis' , 67.83333333333333), word_time('expansion' , 68.08333333333333), word_time('european' , 68.58333333333333), word_time('instantly' , 68.78333333333333), word_time('draughts' , 69.03333333333333)]]
          >>> fastest_words(p, 0.015151515151515152)
          [['productivity', 'proclisis', 'expansion', 'european', 'instantly', 'draughts']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 3), word_time('nap' , 3.3333333333333335), word_time('materialistical' , 3.5333333333333337), word_time('shrag' , 3.7833333333333337), word_time('nestle' , 4.033333333333333), word_time('xanthopicrin' , 4.233333333333333)], [word_time('START', 3), word_time('nap' , 3.5), word_time('materialistical' , 4.0), word_time('shrag' , 4.25), word_time('nestle' , 4.75), word_time('xanthopicrin' , 5.75)]]
          >>> fastest_words(p, 0.014925373134328358)
          [['nap', 'materialistical', 'shrag', 'nestle', 'xanthopicrin'], ['shrag']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 82)]]
          >>> fastest_words(p, 0.041666666666666664)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 42), word_time('spondylarthritis' , 42.333333333333336), word_time('thin' , 42.66666666666667), word_time('osseous' , 42.866666666666674), word_time('controllable' , 43.366666666666674), word_time('preinvest' , 43.866666666666674)]]
          >>> fastest_words(p, 0.011111111111111112)
          [['spondylarthritis', 'thin', 'osseous', 'controllable', 'preinvest']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 32), word_time('yoicks' , 32.333333333333336), word_time('filcher' , 32.833333333333336), word_time('caddle' , 33.833333333333336)]]
          >>> fastest_words(p, 0.07142857142857142)
          [['yoicks', 'filcher', 'caddle']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 20), word_time('vibrissae' , 20.2), word_time('diplocardiac' , 20.7), word_time('enwind' , 21.2), word_time('clithral' , 21.53333333333333)]]
          >>> fastest_words(p, 0.010309278350515464)
          [['vibrissae', 'diplocardiac', 'enwind', 'clithral']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 77), word_time('warehouseful' , 77.33333333333333), word_time('intertwine' , 77.58333333333333), word_time('tickleback' , 78.58333333333333), word_time('wilsomeness' , 78.83333333333333), word_time('heptacolic' , 79.83333333333333), word_time('observedly' , 80.08333333333333)], [word_time('START', 77), word_time('warehouseful' , 78.0), word_time('intertwine' , 79.0), word_time('tickleback' , 79.25), word_time('wilsomeness' , 79.75), word_time('heptacolic' , 79.95), word_time('observedly' , 80.28333333333333)], [word_time('START', 77), word_time('warehouseful' , 77.25), word_time('intertwine' , 77.5), word_time('tickleback' , 77.83333333333333), word_time('wilsomeness' , 78.08333333333333), word_time('heptacolic' , 78.28333333333333), word_time('observedly' , 78.78333333333333)]]
          >>> fastest_words(p, 0.016666666666666666)
          [['intertwine', 'wilsomeness', 'observedly'], ['tickleback', 'heptacolic'], ['warehouseful', 'intertwine', 'wilsomeness', 'heptacolic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 88), word_time('dicrotic' , 88.5), word_time('tressured' , 88.7)], [word_time('START', 88), word_time('dicrotic' , 89.0), word_time('tressured' , 89.33333333333333)]]
          >>> fastest_words(p, 0.030303030303030304)
          [['dicrotic', 'tressured'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 19), word_time('thickbrained' , 19.333333333333332), word_time('pharyngographic' , 19.583333333333332), word_time('punch' , 20.583333333333332), word_time('rhabdomancer' , 21.583333333333332), word_time('tubemaking' , 21.78333333333333)]]
          >>> fastest_words(p, 0.03225806451612903)
          [['thickbrained', 'pharyngographic', 'punch', 'rhabdomancer', 'tubemaking']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 91), word_time('resolicit' , 91.33333333333333), word_time('gangsman' , 91.58333333333333), word_time('tailorize' , 91.91666666666666)], [word_time('START', 91), word_time('resolicit' , 91.33333333333333), word_time('gangsman' , 91.58333333333333), word_time('tailorize' , 91.91666666666666)], [word_time('START', 91), word_time('resolicit' , 92.0), word_time('gangsman' , 93.0), word_time('tailorize' , 93.5)]]
          >>> fastest_words(p, 0.03333333333333333)
          [['resolicit', 'gangsman', 'tailorize'], ['resolicit', 'gangsman', 'tailorize'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 50), word_time('rampagious' , 50.2), word_time('coralberry' , 50.53333333333334)], [word_time('START', 50), word_time('rampagious' , 50.333333333333336), word_time('coralberry' , 50.53333333333334)], [word_time('START', 50), word_time('rampagious' , 50.2), word_time('coralberry' , 50.7)]]
          >>> fastest_words(p, 0.02127659574468085)
          [['rampagious'], ['coralberry'], ['rampagious']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 42), word_time('untailorly' , 42.333333333333336), word_time('untewed' , 42.53333333333334), word_time('planoorbicular' , 42.78333333333334)], [word_time('START', 42), word_time('untailorly' , 42.333333333333336), word_time('untewed' , 42.833333333333336), word_time('planoorbicular' , 43.833333333333336)], [word_time('START', 42), word_time('untailorly' , 42.5), word_time('untewed' , 43.5), word_time('planoorbicular' , 43.833333333333336)]]
          >>> fastest_words(p, 0.014705882352941176)
          [['untailorly', 'untewed', 'planoorbicular'], ['untailorly'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 37)]]
          >>> fastest_words(p, 0.010869565217391304)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 59), word_time('sulphonalism' , 59.25), word_time('indignly' , 60.25), word_time('phylogeny' , 61.25), word_time('indicial' , 62.25), word_time('tepidarium' , 62.583333333333336)]]
          >>> fastest_words(p, 0.012048192771084338)
          [['sulphonalism', 'indignly', 'phylogeny', 'indicial', 'tepidarium']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 22), word_time('tenendum' , 22.2), word_time('slatternness' , 22.7), word_time('longsomeness' , 22.95), word_time('nutpecker' , 23.15), word_time('fatalistically' , 23.48333333333333), word_time('buccobranchial' , 24.48333333333333)], [word_time('START', 22), word_time('tenendum' , 22.333333333333332), word_time('slatternness' , 22.53333333333333), word_time('longsomeness' , 22.78333333333333), word_time('nutpecker' , 23.03333333333333), word_time('fatalistically' , 23.23333333333333), word_time('buccobranchial' , 23.43333333333333)], [word_time('START', 22), word_time('tenendum' , 23.0), word_time('slatternness' , 23.25), word_time('longsomeness' , 23.5), word_time('nutpecker' , 23.7), word_time('fatalistically' , 24.2), word_time('buccobranchial' , 24.45)]]
          >>> fastest_words(p, 0.023809523809523808)
          [['tenendum', 'longsomeness', 'nutpecker'], ['slatternness', 'longsomeness', 'fatalistically', 'buccobranchial'], ['longsomeness', 'nutpecker']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 84), word_time('racinglike' , 84.25), word_time('clavelization' , 84.45), word_time('cooing' , 84.95), word_time('pedestrian' , 85.15)], [word_time('START', 84), word_time('racinglike' , 84.5), word_time('clavelization' , 84.7), word_time('cooing' , 85.03333333333333), word_time('pedestrian' , 85.53333333333333)], [word_time('START', 84), word_time('racinglike' , 84.33333333333333), word_time('clavelization' , 84.66666666666666), word_time('cooing' , 84.91666666666666), word_time('pedestrian' , 85.41666666666666)]]
          >>> fastest_words(p, 0.01098901098901099)
          [['racinglike', 'clavelization', 'pedestrian'], ['clavelization'], ['cooing']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 90), word_time('comendite' , 90.25), word_time('communicableness' , 91.25), word_time('pullus' , 91.5)], [word_time('START', 90), word_time('comendite' , 90.2), word_time('communicableness' , 90.53333333333333), word_time('pullus' , 90.73333333333333)]]
          >>> fastest_words(p, 0.027777777777777776)
          [[], ['comendite', 'communicableness', 'pullus']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 90), word_time('unforgeability' , 90.5), word_time('antiharmonist' , 90.83333333333333), word_time('diasynthesis' , 91.16666666666666)]]
          >>> fastest_words(p, 0.023255813953488372)
          [['unforgeability', 'antiharmonist', 'diasynthesis']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 1)], [word_time('START', 1)]]
          >>> fastest_words(p, 0.027777777777777776)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import word_time, fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(typing)
          >>> p0 = [typing.word_time('START', 0), typing.word_time('What', 0.2), typing.word_time('great', 0.4), typing.word_time('luck', 0.8)]
          >>> p1 = [typing.word_time('START', 0), typing.word_time('What', 0.6), typing.word_time('great', 0.8), typing.word_time('luck', 1.19)]
          >>> typing.fastest_words([p0, p1])
          [['What', 'great'], ['great', 'luck']]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import typing
      >>> import tests.abstraction_check as test
      """,
      'teardown': r"""
      >>> test.restore_implementations(typing)
      """,
      'type': 'doctest'
    }
  ]
}
