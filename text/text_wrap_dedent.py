import textwrap

text_indented_with_tab = '''
	The textwrap module can be used to format text for output in
	situations where pretty-printing is desired. It offers
	programmatic functionality similar to the paragraph wrapping
	or filling features found in many text editors.'''


text_indented_with_space = '''
  The textwrap module can be used to format text for output in
  situations where pretty-printing is desired. It offers
  programmatic functionality similar to the paragraph wrapping
  or filling features found in many text editors.'''

text_dedent_not_work = '''
	The textwrap module can be used to format text for output in
	situations where pretty-printing is desired. It offers
	programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.'''

def print_text_after_remove_indent(text):
	print textwrap.dedent(text)
	print '\n'


print_text_after_remove_indent(text_indented_with_tab)
print_text_after_remove_indent(text_indented_with_space)
print_text_after_remove_indent(text_dedent_not_work)




