from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown_path
from premailer import transform
from argparse import ArgumentParser
import os

def md(path):
  return markdown_path(path, extras=['header-ids'])

args_parser = ArgumentParser(description='''
This tool compiles a set of markdown documents into a .html document that can
be send as newsletter.

The compiler assumes that the --date option is a directory in ./contents. It
will take the three files intro.md, contents.md, and content.md, compile them,
and merge them with the template file.
The compiler will also use date argument to set the date of the newsletter. For
that, the compiler will capitalize every string and replace dashes with spaces.
''')
args_parser.add_argument('--date', required=True, help='''
Date of the newsletter. Must be a valid directory within ./contents.
''')
args_parser.add_argument('--out', default=None, help='''
File to write the rendered document to. If omitted, will be written to stdout.
''')

jinja_env = Environment(loader=FileSystemLoader('.'))
template = jinja_env.get_template('template.html')

if __name__ == '__main__':
  args = args_parser.parse_args()
  base_path = os.path.join(os.getcwd(), 'contents', args.date)
  parts = os.listdir(base_path)
  date = ' '.join(map(lambda datePart: datePart.capitalize(), args.date.split('-')))

  vars = dict([
    # [:-3] to skip the file extension
    (os.path.basename(path)[:-3], md(os.path.join(base_path, path)))
    for path in parts if path.endswith('.md')
  ])
  rendered = template.render(date=date, **vars)
  inlined = transform(rendered)

  if args.out is not None:
    with open(args.out, 'w', encoding='utf8') as fp:
      print(inlined, file=fp)
  else:
    print(inlined)
