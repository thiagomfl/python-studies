def block_tag(text, _class='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class={_class}">{text}</{tag}>'


if __name__ == '__main__':
    print(block_tag('bloco'))
    print(block_tag('inline e classe', 'info', True))
    print(block_tag('inline', inline=True))
    print(block_tag(inline=True, text='inline'))
    print(block_tag('falhou', _class='error'))
