# https://www.techbeamers.com/python-tutorial-step-by-step/#tutorial-list

# print((lambda isOdd: isOdd(3))(lambda x: x % 2 != 0))
#
#
# print('Interest Calculator:')
#
# amount = float(input('Principal amount ?'))
# roi = float(input('Rate of Interest ?'))
# yrs = int(input('Duration (no. of years) ?'))
#
# total = (amount * pow(1 + (roi/100), yrs))
# interest = total - amount
# print('\nInterest = %0.2f' %interest)
#
import keyword
print(keyword.kwlist)

# >> > import keyword
# >> > keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
#  'return', 'try', 'while', 'with', 'yield']
# >> >
# Back
# to
# list
#
# Python
# Identifiers.
#
# Python
# Identifiers
# are
# user - defined
# names
# to
# represent
# a
# variable, function,
#
#
# class , module or any other object.If you assign some name to a programmable entity in Python, then it is nothing but technically called an identifier.
#
#
# Python
# language
# lays
# down
# a
# set
# of
# rules
# for programmers to create meaningful identifiers.
#
# Guidelines
# for Creating Identifiers in Python.
#
# 1.
# To
# form
# an
# identifier, use
# a
# sequence
# of
# letters
# either in lowercase(a
# to
# z) or uppercase(A
# to
# Z).However, you
# can
# also
# mix
# up
# digits(0
# to
# 9) or an
# underscore(_)
# while writing an identifier.
#
# For
# example – Names
# like
# shapeClass, shape_1, and upload_shape_to_db
# are
# all
# valid
# identifiers.
#
# 2.
# You
# can’t
# use
# digits
# to
# begin
# an
# identifier
# name.It’ll
# lead
# to
# the
# syntax
# error.
#
# For
# example – The
# name, 0
# Shape is incorrect, but
# shape1 is a
# valid
# identifier.
#
# 3.
# Also, the
# Keywords
# are
# reserved, so
# you
# should
# not use
# them as identifiers.
#
# >> > for =1
# SyntaxError: invalid
# syntax
# >> > True = 1
# SyntaxError: can
# 't assign to keyword
# 4.
# Python
# Identifiers
# can
# also
# not have
# special
# characters[‘.’, ‘!’, ‘
#
# @
#
# ’, ‘  # ’, ‘$’, ‘%’] in their formation. These symbols are forbidden.
#
# >> >
#
# @index
#
# =0
# SyntaxError: invalid
# syntax
# >> > isPython?=True
# SyntaxError: invalid
# syntax
# 5.
# Python
# doc
# says
# that
# you
# can
# have
# an
# identifier
# with unlimited length.But it is just the half truth.
#
# Using a large name (more than 79 chars) would lead to the violation of a rule set by the PEP-8 standard.It says.
#
# Limit all lines to a maximum of 79 characters.
#
# Testing If an Identifier is Valid.
#
# You can test whether a Python identifier is valid or not by using the keyword.iskeyword() function.It returns “True” if the keyword is correct or “False” otherwise.
#
# Please refer the below snippet.
#
# >> > import keyword
# >> > keyword.iskeyword("techbeamers")
# False
# >> > keyword.iskeyword("try")
# True
# >> >
# Another useful method to check if an identifier is valid or not is by calling the str.isidentifier() function.But it is only available in Python 3.0 and onwards.
#
# >> > 'techbeamers'.isidentifier()
# True
# >> > '1techbeamers'.isidentifier()
# False
# >> > 'techbeamers.com'.isidentifier()
# False
# >> > 'techbemaers_com'.isidentifier()
# True
# Best Practices for Identifier Naming.
#
# Better have
#
#
# class names starting with a capital letter.All other identifiers should begin with a lowercase letter.
#
#
# Declare
# private
# identifiers
# by
# using
# the(‘_’) underscore as their
# first
# letter.
# Don’t
# use ‘_’ as the
# leading and trailing
# character in an
# identifier.As
# Python
# built - in types
# already
# use
# this
# notation.
# Avoid
# using
# names
# with only one character.Instead, make meaningful names.
# For
# example – While
# i = 1 is valid, but
# writing
# iter = 1 or index = 1
# would
# make
# more
# sense.
# You
# can
# use
# underscore
# to
# combine
# multiple
# words
# to
# form
# a
# sensible
# name.
# For
# example – count_no_of_letters.
# Back
# to
# list
#
# Python
# Variables.
#
# A
# variable in Python
# represents
# an
# entity
# whose
# value
# can
# change as and when
# required.Conceptually, it is a
# memory
# location
# which
# holds
# the
# actual
# value.And
# we
# can
# retrieve
# the
# value
# from our code
#
# by
# querying
# the
# entity.
#
# But
# it
# requires
# assigning
# a
# label
# to
# that
# memory
# location
# so
# that
# we
# can
# reference
# it.And
# we
# call
# it as a
# variable in the
# programming
# terms.
#
# Following
# are
# some
# of
# the
# key
# facts
# about
# Python
# variables.These
# will
# help
# programmers
# to
# use
# them
# efficiently.
#
# 1.
# Variables
# don’t
# require
# declaration.However, you
# must
# initialize
# them
# before
# use.
#
# For
# example –
#
# test = 10
# 2.
# The
# above
# expression
# will
# lead
# to
# the
# following
# actions.
#
# Creation
# of
# an
# object
# to
# represent
# the
# value
# 10.
# If
# the
# variable(test)
# doesn’t
# exist, then
# it’ll
# get
# created.
# Association
# of
# the
# variable
# with the object, so that it can refer the value.
# The
# variable ‘test’ is a
# reference
# to
# the
# value ’10’.Please
# refer
# to
# the
# illustration
# shown
# below.
#
# Example.
#
# | ~~~~~ | ----- ~~~~~~~~~ ------- ** **
# (test) - ---- Reference - ------ ** 10 **
# | ~~~~~ | ----- ~~~~~~~~~ ------- ** **
# Variable - ---- ~~~~~~~~~~ -------  Object
# 3.
# Whenever
# the
# expression
# changes, Python
# associates
# a
# new
# object(a
# chunk
# of
# memory) to
# the
# variable
# for referencing that value.And the old one goes to the garbage collector.
#
# Example.
#
# >> > test = 10
# >> > id(test)
# 1716585200
# >> > test = 11
# >> > id(test)
# 1716585232
# >> >
# 4.
# Also,
# for optimization, Python builds a cache and reuses some of the immutable objects, such as small integers and strings.
#
# 5.
# An
# object is just
# a
# region
# of
# memory
# which
# can
# hold
# the
# following.
#
# The
# actual
# object
# values.
# A
# type
# designator
# to
# reflect
# the
# object
# type.
# The
# reference
# counter
# which
# determines
# when
# it’s
# OK
# to
# reclaim
# the
# object.
# 6.
# It’s
# the
# object
# which
# has
# a
# type, not the
# variable.However, a
# variable
# can
# hold
# objects
# of
# different
# types as and when
# required.
#
# Example.
#
# >> > test = 10
# >> > type(test)
# <
#
# class 'int'>
#
# >> > test = 'techbeamers'
# >> > type(test)
# <
#
# class 'str'>
#
# >> > test = {'Python', 'C', 'C++'}
# >> > type(test)
# <
#
# class 'set'>
#
# >> >