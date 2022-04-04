"""
    File: draw_maze.py
    Purpose: Read in a specification for a maze and create a graphviz data file
             that can be uploaded to http://www.webgraphviz.com/ to visualize
             the maze.
"""

def draw_maze(infile, outfile):
    outf = open(outfile, "w")
    outf.write("# Graphviz spec for the maze in {}\n".format(infile))
    outf.write("# Upload to: http://www.webgraphviz.com/\n")
    outf.write("\ngraph G {\n")

    with open(infile) as f:
        for line in f:
            words = line.split()
            outf.write("    {} -- {}\n".format(words[0], words[1]))

    outf.write("}\n")
    outf.close()

def main():
    infile = input("input file: ")
    outfile = input("output file: ")
    draw_maze(infile, outfile)

if __name__ == "__main__":
    main()
# Write your code here :-)
