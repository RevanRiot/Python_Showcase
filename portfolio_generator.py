# File: portfolio_generator.py

import json
from jinja2 import Environment, FileSystemLoader

def generate_portfolio(json_file, template_dir, output_file):
    """Generates a portfolio website from a JSON file and HTML template."""
    with open(json_file, 'r') as file:
        data = json.load(file)

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('portfolio_template.html')

    output = template.render(data=data)

    with open(output_file, 'w') as file:
        file.write(output)
    print(f"Portfolio generated at {output_file}")

if __name__ == '__main__':
    input_json = 'data/portfolio.json'
    templates_dir = 'templates'
    output_html = 'output/portfolio.html'
    generate_portfolio(input_json, templates_dir, output_html)
