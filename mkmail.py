from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown_path
from premailer import transform
from argparse import ArgumentParser
import os

def md(path):
  return markdown_path(path, extras=['header-ids'])

args_parser = ArgumentParser()
args_parser.add_argument('--date', required=True)
args_parser.add_argument('--out', default=None)

jinja_env = Environment(loader=FileSystemLoader('.'))
template = jinja_env.get_template('template.html')

if __name__ == '__main__':
  args = args_parser.parse_args()
  base_path = os.path.join(os.getcwd(), 'contents', args.date)
  parts = os.listdir(base_path)
  date = ' '.join(args.date.split('-'))

  vars = dict([
    (os.path.basename(path)[:-3], markdown_path(os.path.join(base_path, path)))
    for path in parts if path.endswith('.md')
  ])
  rendered = template.render(date=date, **vars)
  inlined = transform(rendered)

  if args.out is not None:
    with open(args.out, 'w', encoding='utf8') as fp:
      print(inlined, file=fp)
  else:
    print(inlined)
