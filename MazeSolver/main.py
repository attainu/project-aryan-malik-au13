import argparse
import Maze as MazeSolver

'''calling solve_Maze function'''
res = MazeSolver.Maze()
res.solve_Maze(MazeSolver.maze)


def Main():
    pars = argparse.ArgumentParser()
    pars.add_argument("-o", "--outputfile", help="Output the result to a file", action="store_true")
    pars.add_argument("-i", "--inputfile", help="Output the result to a file", action="store_true")
    ars = pars.parse_args()
    if ars.outputfile:
        data = open("outputfile.txt", "a")
        if res.solve_Maze(MazeSolver.maze) is False:
            data.write(str("-1"))
        else:
            for i in res.solve_Maze(MazeSolver.maze):
                for result in i:
                    data.write(str(result) + " ")
                data.write('\n')
    if ars.inputfile:
        MazeSolver.Input = "inputfile.txt"


if __name__ == '__main__':
    Main()
