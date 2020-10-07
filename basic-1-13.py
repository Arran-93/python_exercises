sample='a string that you "don\'t" have to escape\nThis\nis a ....... multi-line\nheredoc string --------> example'
print(sample)
#was curious if you can do it without \n 's, below one is how to do it
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
#usefull, make's printing long strings easier :)
sample2 ="""
that is test for
saving text
in variable first
then printing
"""
print(sample2)
