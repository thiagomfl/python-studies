block_attrs = ('block_accesskey', 'block_id')
ul_attrs = ('ul_id', 'ul_style')


def get_attrs(informeds, supporteds):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informeds.items()
                    if k in supporteds)


def block_tag(content, *args, _class='success', inline=False, **new_attrs):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args, **new_attrs)
    atributes = get_attrs(new_attrs, block_attrs)

    return f'<{tag} {atributes} class={_class}">{html}</{tag}>'


def list_tag(*itens, **new_attrs):
    _list = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {get_attrs(new_attrs, ul_attrs)}>{_list}</ul>'


if __name__ == '__main__':
    print(block_tag('bloco'))
    print(block_tag('inline e classe', 'info', True))
    print(block_tag('inline', inline=True))
    print(block_tag(inline=True, content='inline'))
    print(block_tag('falhou', _class='error'))
    print(block_tag(list_tag('Item 1', 'Item 2'), _class='info'))
    print(block_tag(list_tag, 'Sabado', 'Domingo', _class='info'))

    print(block_tag(list_tag, 'Item 1', 'Item 2', _class='info',
          block_accesskey='m', block_id='content', ul_id='list'))
