import textwrap

text = '''The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.'''

def print_wrap_text(text, width):
	print textwrap.fill(text, width = width)
	print '\n'
	print textwrap.wrap(text, width = width)
	print '\n'

# width = 30
print_wrap_text(text, 30)

# width = 75
print_wrap_text(text, 75)