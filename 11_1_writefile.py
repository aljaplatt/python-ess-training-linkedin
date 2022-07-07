from argparse import ArgumentParser 
#* argparse provides an argument parser class. This allows you to create an obj that keeps track of all the arguments you program accepts 

#? new parser instance 
parser = ArgumentParser()

#? command line argument - called --output
parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')
parser.add_argument('--text', '-t', required=True, help='The text to write to the file')

#? This returned value args is an object that has all our arguments as attributes on it
args = parser.parse_args()

with open(args.output, 'w') as f:
    f.write(args.text+'\n')

print(f'Wrote "{args.text}" to file "{args.output}"')