#!/usr/bin/env python
# encoding: utf-8
"""
This is a quick and dirty algorithm test for an interesting problem.

Problem:

    Fill all the seats in a theater with groups of people, where everyone in
    the same group should sit close to other members of the group. Every
    available seat may be in use.

Algorithm:

    Each group 'eats' into the grid starting at an initial position. If the
    current seat is available occupy it. Then moves one step in the current
    direction until an expanding bounding box is reached
    (`limit_[top|right|bottom|left]`). If the limit is reached, turn clockwise
    or counter-clockwise, and expand the just hit limit by one for the next
    round.

Author:

    Chris Hager <chris@metachris.org>

Date:

    November 2011

License:

    Use this code in whichever way you want (no restrictions).
"""

import sys
import os
import math
from optparse import OptionParser

# Do not change the settings below
DIR_RIGHT = 0
DIR_BOTTOM = 1
DIR_LEFT = 2
DIR_TOP = 3
ROT_CLOCKWISE = 0
ROT_COUNTERCLOCKWISE = 1


class Pos(object):
    """Representation of a x/y position"""
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<Pos(%s, %s)>" % (self.x, self.y)

    @staticmethod
    def copy(pos):
        """Copy an existing Pos object to a new one"""
        return Pos(pos.x, pos.y)


class Grid(object):
    """Representation of the grid (theater seats)"""
    grid = []
    cols = 0
    rows = 0

    EMPTY = u" "

    def __init__(self, cols, rows):
        """Init Grid with - (empty seats)"""
        self.cols = int(cols)
        self.rows = int(rows)
        for _ in xrange(self.rows):
            self.grid.append(self.EMPTY * self.cols)

    def is_free(self, pos):
        """Returns true if position in grid is free"""
        return self.grid[pos.y][pos.x] == self.EMPTY

    def set_used(self, pos, id):
        """Mark a seat as used"""
        self.grid[pos.y] = unicode(self.grid[pos.y][:pos.x] + id + \
                self.grid[pos.y][pos.x + 1:])

    def count_free(self):
        """Returns the count of free positions"""
        cnt = 0
        for row in self.grid:
            cnt += row.count(self.EMPTY)
        return cnt

    def show(self):
        """Pretty print the grid"""
        # Add the header line with column index
        out = "     "
        for i in xrange(self.cols):
            out += "%2s " % i
        out += "\n\n"

        # Add the content lines, preceded by the line number
        cnt = 0
        for line in self.grid:
            out += "%2s   " % cnt
            cnt += 1
            for seat in line:
                out += " %s " % seat
            out += "\n"

        # Print the pretty grid representation
        print out


class Group(object):
    """Representation of one group"""
    id = None
    count = 0
    seats = []

    # Current position and direction
    cur_pos = None
    cur_dir = None
    rotation = None

    # If reaching one of the limits, turn clockwise and expand limit
    limit_left = None
    limit_top = None
    limit_right = None
    limit_bottom = None

    def __init__(self, id, count, start_pos=None, start_dir=DIR_LEFT,
            rotation=ROT_CLOCKWISE):
        self.seats = []
        self.count = count
        self.cur_pos = start_pos
        self.cur_dir = start_dir
        self.rotation = rotation

        # Only accept a valid id (single-digit)
        if id is None or len(unicode(id)) != 1:
            raise TypeError("Group id needs to be one digit, not '%s'" % id)
        self.id = unicode(id)

    def __str__(self):
        return "<Group-%s(%s)>" % (self.id, self.count)

    def find_initial_pos(self):
        """
        Find an initial position in the grid, start at the bottom right and
        move left and up if too far left.
        """
        # Start at bottom right (and work left and up)
        pos = Pos(self.grid.cols - 2, self.grid.rows - 2)

        # Search until found or out of space
        found = False
        backup_pos = None
        while not found:
            if self.grid.is_free(pos):
                backup_pos = pos
                # Only use spot if column to the left is also free
                if pos.x > 0 and self.grid.is_free(Pos(pos.x - 1, pos.y)):
                    return pos

            # Step 1 to the lefts
            pos.x -= 1

            # Step up if necessary
            if pos.x < 0:
                pos.x = self.grid.cols - 1
                pos.y -= 1
                if pos.y < 0:
                    if backup_pos:
                        return backup_pos
                    else:
                        raise IndexError("Could not find an initial position")

    def occupy(self, grid):
        """Start occupying this groups part in the grid"""
        self.grid = grid

        # Error out if there are not enough seats
        count_free = self.grid.count_free()
        if self.count > count_free:
            raise IndexError("Not enough available positions in the grid " + \
                    "(%s available, %s required)" % (count_free, self.count))

        if not self.cur_pos:
            self.cur_pos = self.find_initial_pos()

        # Set initial limits (1 in each direction)
        self.limit_left = self.cur_pos.x - 2 if self.cur_pos.x - 2 >= 0 else 0
        self.limit_right = self.cur_pos.x + 1 if self.cur_pos.x + 1 < \
                grid.cols else grid.cols - 1
        self.limit_top = self.cur_pos.y - 1 if self.cur_pos.y - 1 >= 0 else 0
        self.limit_bottom = self.cur_pos.y + 1 if self.cur_pos.y + 1 < \
                grid.rows else grid.rows - 1

        # Occupy seats until we have enough
        while len(self.seats) < self.count:
            if self.grid.is_free(self.cur_pos):
                self.grid.set_used(self.cur_pos, self.id)
                self.seats.append(Pos.copy(self.cur_pos))

            # Update the current position, and change direction if necessary
            self.move()

    def move(self):
        """
        Move in current direction by 1. If outside of limit, update direction
        and expand the limit.
        """
        if self.cur_dir == DIR_RIGHT:
            if self.cur_pos.x + 1 > self.limit_right:
                self.turn()
            else:
                self.cur_pos.x = self.cur_pos.x + 1

        elif self.cur_dir == DIR_BOTTOM:
            if self.cur_pos.y + 1 > self.limit_bottom:
                self.turn()
            else:
                self.cur_pos.y = self.cur_pos.y + 1

        elif self.cur_dir == DIR_LEFT:
            if self.cur_pos.x - 1 < self.limit_left:
                self.turn()
            else:
                self.cur_pos.x = self.cur_pos.x - 1

        elif self.cur_dir == DIR_TOP:
            if self.cur_pos.y - 1 < self.limit_top:
                self.turn()
            else:
                self.cur_pos.y = self.cur_pos.y - 1

    def turn(self):
        """
        Expands the limit in the current direction by one and updates
        self.cur_dir with a 90 degree turn either cw or ccw.
        """
        self.expand_limit()
        if self.rotation == ROT_CLOCKWISE:
            # Turn clockwise
            self.cur_dir = (self.cur_dir + 1) % 4
        else:
            # Turn counter-clockwise
            self.cur_dir = (self.cur_dir - 1) % 4

    def expand_limit(self):
        """Expands the limit in the current direction by 1, if enough space"""
        if self.cur_dir == DIR_RIGHT:
            if self.limit_right + 1 < self.grid.cols:
                self.limit_right += 1

        elif self.cur_dir == DIR_BOTTOM:
            if self.limit_bottom + 1 < self.grid.rows:
                self.limit_bottom += 1

        elif self.cur_dir == DIR_LEFT:
            if self.limit_left - 1 >= 0:
                self.limit_left -= 1

        elif self.cur_dir == DIR_TOP:
            if self.limit_top - 1 >= 0:
                self.limit_top -= 1

    def show_seats(self, delim="; "):
        """Prints the seats of this group in csv like format"""
        print "group-%s%s" % (self.id, delim) + \
                delim.join(["%s,%s" % (pos.x, pos.y) for pos in self.seats])


def build_groups(groups):
    """Build the initial list of groups based on a list of sizes"""
    # Symbols (id/representations) to use for the groups
    #symbols = [u"♥", u"☼", u"♪", u"✌", u"☺", u"x", u"/", u"#", u"@", u"o"]
    symbols = [u"-", u"O", u"+", u"*", u"X", u"x", u"/", u"#", u"@", u"0"]
    if not len(groups):
        # If no command-line specified group sizes, use default ones
        groups = [3, 8, 150, 2, 10]
    # Build the groups and return them in a list
    return [Group(symbols[i], int(groups[i])) for i in xrange(len(groups))]


def build_grid(grid_size, group_sizes):
    # Instantiate the grid
    cols, rows = grid_size.split("x") if grid_size else (15, 10)
    grid = Grid(cols=cols, rows=rows)

    # Build the list of groups, based on the supplied sizes
    groups = build_groups(group_sizes)

    # Have the groups eat into the grid, one by one
    for group in groups:
        group.occupy(grid)

    return grid, groups

def main(grid_size, group_sizes, output_format):
    grid, groups = build_grid(grid_size, group_sizes)

    # Output either the final grid or the seats in csv
    if output_format == "grid":
        grid.show()
    elif output_format == "csv":
        for group in groups:
            group.show_seats()


if __name__ == '__main__':
    usage = """usage: %prog [options] size-group1 size-group2 ...

    Example: %prog -s 10x15 20 30 10 14"""
    parser = OptionParser(usage=usage)
    parser.add_option("-s", "--size", dest="size",
            help="Specify grid columns and rows (eg 15x10)", metavar="SIZE")
    parser.add_option("-o", "--ouput", dest="output", choices=["grid", "csv"],
            default="grid", help="Type of output ('grid' or 'csv')",
            metavar="FORMAT")

    (options, args) = parser.parse_args()
    main(options.size, args, options.output)
