import textwrap

text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
print 'original text :\n'
print text


text_removed_indented = textwrap.dedent(text).strip()
print 'text after rem:\n'
print text_removed_indented
print '\n\n'


# use textwrap to format width = 30
print 'format text width = 30 \n'
print textwrap.fill(text_removed_indented, width = 30)
print '\n\n'

# use textwrap to format width = 70
print 'format text width = 70 \n'
print textwrap.fill(text_removed_indented, width = 70)
print '\n\n'