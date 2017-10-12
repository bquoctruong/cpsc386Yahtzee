
import Player
import Rules

p = Player.Player()

p.rollDices()

p.keepDices([0, 1, 0, 0, 1])

r = Rules.Rules(p.keptDices)

r.runSections()
