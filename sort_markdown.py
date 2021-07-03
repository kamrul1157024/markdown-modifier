from markdown_modifier import MarkDownContent,\
                                read_markdown,\
                                sort_markdown,\
                                write_markdown

test_markdown:MarkDownContent = read_markdown('./test.md')
sorted_test_markdown  = sort_markdown(test_markdown,reverse=False,case_sensitive=True)
write_markdown('./sorted_test.md',sorted_test_markdown)
