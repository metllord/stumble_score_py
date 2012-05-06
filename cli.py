from sys import argv
from location.scoring import StumbleScore

def cli(address):
    location = StumbleScore(address)
    results = location()
    output = """
Welcome to StumbleScore!
Calculating score for {name}.
Number of locations: {bar_count}
Stumble Score: {score}
Category: {category}
--------------------
Locations:
""".format(**results)
    for place in results['locations']:
        output += place + '\n'
    return output

if __name__ == '__main__':
    print cli(argv[1])
