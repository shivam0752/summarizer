import click
from ollama import chat

# Function to call the Ollama API
def get_summary_from_ollama(text):
    messages = [
        {
            'role': 'user',
            'content': f'Please provide a summary of the following text that is between 40 and 300 words: {text}',
        },
    ]

    response = chat('qwen2:0.5b', messages=messages)
    return response['message']['content']

@click.command()
@click.option('--text', help='Text to summarize')
@click.option('--file', type=click.File('r', encoding='utf-8'), help='Text file to summarize')
def summarize(text, file):
    if text:
        summary = get_summary_from_ollama(text)
        word_count = len(summary.split())
        if 40 <= word_count <= 300:
            click.echo(f'Summary ({word_count} words): {summary}')
        else:
            click.echo(f'The summary is {word_count} words long, which is outside the desired range (40-300 words).')
    elif file:
        text = file.read()
        summary = get_summary_from_ollama(text)
        word_count = len(summary.split())
        if 40 <= word_count <= 300:
            click.echo(f'Summary ({word_count} words): {summary}')
        else:
            click.echo(f'The summary is {word_count} words long, which is outside the desired range (40-300 words).')
    else:
        click.echo('Please provide either text or a file to summarize.')

if __name__ == '__main__':
    summarize()
