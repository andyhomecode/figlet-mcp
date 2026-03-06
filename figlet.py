import pyfiglet
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate ASCII art text using pyfiglet')
    parser.add_argument('text', nargs='?', default='MCP', help='Text to convert to ASCII art')
    parser.add_argument('-c', '--comment', action='store_true', help='Add Python comment prefix (#) to each line')
    parser.add_argument('-f', '--font', default='slant', help='Font to use (default: slant)')
    
    args = parser.parse_args()
    
    # Generate the ASCII art
    output = pyfiglet.figlet_format(args.text, font=args.font)
    
    # Add comment prefix to each line if requested
    if args.comment:
        lines = output.split('\n')
        commented_lines = ['#   ' + line for line in lines]
        output = '\n'.join(commented_lines)
    
    print(output)

if __name__ == '__main__':
    main()