def block_tag(content, _class='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class={_class}">{content}</{tag}>'


def list_tag(*itens):
    _list = ''.join(f'<li>{item}</li>' for item in itens)
    return  f'<ul>{_list}</ul>'


if __name__ == '__main__':
    print(block_tag('bloco'))
    print(block_tag('inline e classe', 'info', True))
    print(block_tag('inline', inline=True))
    print(block_tag(inline=True, content='inline'))
    print(block_tag('falhou', _class='error'))
    print(block_tag(list_tag('Item 1', 'Item 2'), _class='info'))
