import re
import copy
from typing import *
from .MarkDownContent import MarkDownContent

def is_header(line:str)->bool:
  return True if re.search('#+\s.*', line) else False

# test
assert is_header('## this is a header') == True
assert is_header('### this is a header') == True
assert is_header('##this is not a header') == False
assert is_header('this is not a header') == False

def header_level(line:str)->int:
  match = re.search('#+\s',line) 
  return match.end()- match.start() -1

#test
assert header_level("### a level 3 header") == 3
assert header_level("# a level 1 header") == 1

def read_markdown(path:str)->MarkDownContent:
    markdown_file = open(path)
    lines = markdown_file.readlines()
    markdown_file.close()

    def serialize_content(current_header_level:int,current_line_no:int)->Tuple[int,List[MarkDownContent]]:
        if current_line_no > len(lines):
            return (current_line_no,[MarkDownContent("")])

        current_markdowncontents:List[MarkDownContent] = []
        current_markdowncontent:MarkDownContent = None
        while current_line_no<len(lines):
            if is_header(lines[current_line_no]):
                if header_level(lines[current_line_no])> current_header_level:
                    current_line_no, child_markdowncontent = serialize_content(current_header_level+1,current_line_no)
                    current_markdowncontent.add_markdowncontents(child_markdowncontent)
                elif header_level(lines[current_line_no]) == current_header_level:
                    current_markdowncontent = MarkDownContent(lines[current_line_no])
                    current_markdowncontents.append(current_markdowncontent)
                    current_line_no+=1
                else:
                    return (current_line_no,current_markdowncontents)
            else:
                current_markdowncontent.add_content(lines[current_line_no])
                current_line_no+=1 

        return (current_line_no,current_markdowncontents)

    root_markdowncontent = MarkDownContent("");
    current_line_no = 0
    while not is_header(lines[current_line_no]):
        root_markdowncontent.add_content(lines[current_line_no])
        current_line_no+=1

    _,child_markdowncontents = serialize_content(1,current_line_no)
    root_markdowncontent.add_markdowncontents(child_markdowncontents)
    
    return root_markdowncontent

def write_markdown(path:str,markdowncontent:MarkDownContent)->None:
    markdown_write_file = open(path, "w")
    markdown_write_file.write(markdowncontent.__str__())
    markdown_write_file.close()

def sort_markdown(markdowncontent:MarkDownContent,reverse=False,case_sensitive=True)->MarkDownContent:
  sorted_mark_down = copy.deepcopy(markdowncontent)

  def convert_to_lower_case(markdowncontent:MarkDownContent)->None:
    markdowncontent.header.lower()
    for current_markdowncontent in markdowncontent.markdowncontents:
      convert_to_lower_case(current_markdowncontent)
    
    if not case_sensitive:
      convert_to_lower_case(sorted_mark_down)

  def sort_by_header(markdowncontent:MarkDownContent)->None:
    markdowncontent.markdowncontents.sort(reverse=reverse)
    for current_markdowncontent in markdowncontent.markdowncontents:
      sort_by_header(current_markdowncontent)
  
  sort_by_header(sorted_mark_down)
  return sorted_mark_down
